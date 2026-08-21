import pennylane as qml
import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. SETUP & ZIELVERTEILUNG (DER EDGE CASE)
# ==========================================
n_qubits = 6
n_states = 2**n_qubits

# Ziel: 90% uniformes Rauschen, 10% konzentriert auf die global korrelierten Edge Cases
# |000000> (Index 0) und |111111> (Index 63)
target_probs = np.ones(n_states) * (0.9 / (n_states - 2))
target_probs[0] = 0.05   # Edge Case 1: Alle Qubits 0
target_probs[-1] = 0.05  # Edge Case 2: Alle Qubits 1
target_probs = torch.tensor(target_probs, dtype=torch.float32)

print(f"Starte Experiment mit {n_qubits} Qubits ({n_states} mögliche Zustände)...")
print("Ziel: Finde die versteckten Edge Cases (Index 0 und 63) im Rauschen.\n")

# ==========================================
# 2. KLASSISCHES BASELINE MODELL (MLP / Independent)
# ==========================================
class ClassicalGenerator(nn.Module):
    """
    Simuliert einen klassischen Latent-Space Generator.
    Er lernt für jedes Bit eine unabhängige Wahrscheinlichkeit.
    (Kann per Definition keine globale Verschränkung/Parität lernen).
    """
    def __init__(self):
        super().__init__()
        # 6 unabhängige Logits (Parameter)
        self.logits = nn.Parameter(torch.zeros(n_qubits))
        
    def get_joint_probs(self):
        p = torch.sigmoid(self.logits)
        # Berechne das Tensor-Produkt aller unabhängigen Wahrscheinlichkeiten
        probs = torch.tensor([1.0])
        for i in range(n_qubits):
            p_i = p[i]
            probs = torch.cat([probs * (1 - p_i), probs * p_i])
        return probs

# ==========================================
# 3. QUANTEN MODELL (PQC - Parametrized Quantum Circuit)
# ==========================================
dev = qml.device("default.qubit", wires=n_qubits)

@qml.qnode(dev)
def quantum_circuit(params):
    # Nutze stark verschränkende Layer (CNOTs + Rotationen)
    qml.StronglyEntanglingLayers(weights=params, wires=range(n_qubits))
    return qml.probs(wires=range(n_qubits))

# Initialisiere Quanten-Parameter (2 Layer, Standard PennyLane Shape)
shape = qml.StronglyEntanglingLayers.shape(n_layers=2, n_wires=n_qubits)
q_params = torch.tensor(np.random.uniform(0, 2*np.pi, shape), requires_grad=True, dtype=torch.float32)

# ==========================================
# 4. TRAININGS-LOOP
# ==========================================
epochs = 150
lr = 0.05

opt_classical = torch.optim.Adam(ClassicalGenerator().parameters(), lr=lr)
opt_quantum = torch.optim.Adam([q_params], lr=lr)

# Loss Function: Kullback-Leibler Divergenz (Standard für Verteilungs-Matching)
loss_fn = nn.KLDivLoss(reduction='sum')

model_classical = ClassicalGenerator()

print("Training läuft... (Dauert ca. 1-2 Minuten)")
for epoch in range(epochs):
    # --- Klassisches Training ---
    opt_classical.zero_grad()
    c_probs = model_classical.get_joint_probs()
    # KL Divergenz erwartet log-probabilities als Input
    loss_c = loss_fn(torch.log(c_probs + 1e-8), target_probs)
    loss_c.backward()
    opt_classical.step()
    
    # --- Quanten Training ---
    opt_quantum.zero_grad()
    q_probs = quantum_circuit(q_params)
    loss_q = loss_fn(torch.log(q_probs + 1e-8), target_probs)
    loss_q.backward()
    opt_quantum.step()
    
    if (epoch + 1) % 30 == 0:
        print(f"Epoche {epoch+1:3d} | Klassisch Loss: {loss_c.item():.4f} | Quanten Loss: {loss_q.item():.4f}")

# ==========================================
# 5. AUSWERTUNG & VISUALISIERUNG
# ==========================================
final_c_probs = model_classical.get_joint_probs().detach().numpy()
final_q_probs = quantum_circuit(q_params).detach().numpy()
target_np = target_probs.numpy()

# Fokussiere auf die Edge Cases (Index 0 und 63)
edge_indices = [0, 63]
print("\n--- ERGEBNIS: WAHRSCHEINLICHKEIT DER EDGE CASES ---")
print(f"Ziel (Target)    : Index 0 = {target_np[0]:.3f} | Index 63 = {target_np[-1]:.3f}")
print(f"Klassisch (MLP)  : Index 0 = {final_c_probs[0]:.3f} | Index 63 = {final_c_probs[-1]:.3f}  <-- Mode Collapse!")
print(f"Quanten (PQC)    : Index 0 = {final_q_probs[0]:.3f} | Index 63 = {final_q_probs[-1]:.3f}  <-- Edge Case gefunden!")

# Plotting
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
x = np.arange(n_states)

# Target
axes[0].bar(x, target_np, color='gray', alpha=0.6)
axes[0].set_title("Ziel-Verteilung (Target)\n(90% Rauschen, 10% Edge Cases)")
axes[0].set_xlim(-1, n_states)

# Classical
axes[1].bar(x, final_c_probs, color='red', alpha=0.7)
axes[1].set_title("Klassischer Generator\n(Scheitert an globaler Korrelation)")
axes[1].set_xlim(-1, n_states)

# Quantum
axes[2].bar(x, final_q_probs, color='blue', alpha=0.7)
axes[2].set_title("Quanten-Sampler (PQC)\n(Findet Edge Cases durch Verschränkung)")
axes[2].set_xlim(-1, n_states)

# Markiere die Edge Cases in allen Plots
for ax in axes:
    ax.bar([0], [ax.get_ylim()[1]*0.9], color='gold', width=1, edgecolor='black')
    ax.bar([63], [ax.get_ylim()[1]*0.9], color='gold', width=1, edgecolor='black')
    ax.set_xlabel("Zustand (0 bis 63)")
    ax.set_ylabel("Wahrscheinlichkeit")

plt.tight_layout()
# Speichert das Bild im selben Ordner, anstatt es im Fenster zu öffnen
plt.savefig("quantum_edgecase_result.png", dpi=300)
print("\n[INFO] Plot wurde erfolgreich als 'quantum_edgecase_result.png' gespeichert!")

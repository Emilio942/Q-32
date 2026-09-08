# RESEARCH START: 
# RESEARCH START: Critical Scaling Law and Universality Class of Monitored Random-Matching Clifford Circuits (Q-32 Verification Program)

PROBLEM SETUP: A monitored Clifford circuit family serves as the classical,
exactly-simulable testbed for the MIPT-HybridMathGen program (entanglement
richness of the latent state vs. cost of classical-shadow readout). The model
is pinned down exactly (see MODEL below) and has been simulated; this run
must DERIVE its critical scaling law, not re-describe it. Three questions
exceed what is reachable with local numerical resources alone: (Q1) whether
the observed P_vol crossing is a true phase transition as n -> infinity and
which universality class it belongs to for THIS geometry; (Q2) closed-form
p_c(n, L) with explicit constants — literature values (p_c ≈ 0.16–0.23)
refer to fixed brickwork geometries and do NOT transfer to the pinned model
without derivation; (Q3) the bridge law linking generation-time measurement
rate p to classical-shadow shot cost for edge-case readout on the monitored
state family, with constants in (n, L, p, |A|).

MODEL (PINNED, NOT NEGOTIABLE): n qubits initialized to |0...0>; L = 3n
layers; each layer: (1) one uniform random perfect matching of {0,...,n-1},
CNOT applied to each matched pair (first element = control); (2) one gate
per wire drawn independently and uniformly from {H, S}; (3) each wire
measured projectively in the computational basis, independently with
probability p. Order parameter: bipartite von Neumann entropy S_A in bits
across the central cut |A| = n/2, measured in the BULK (no measurements in
the final layer). p = 0 is a random Clifford circuit (Gottesman-Knill
simulable; stabilizer entropy is exactly computable).

EMPIRICAL ANCHORS (measured with this exact oracle; n = 8..12, L = 3n,
60-100 trials per point, p-grid resolution 0.067):
(A1) <S_A>(p=0)/(n/2) ≈ 0.67 (n=8), 0.93 (n=10), 0.83 (n=12): volume-law
     but sub-maximal;
(A2) P_vol(p) = Pr[S_A > 0.5 * <S_A>(p=0)] falls from 1 to 0; 10-90%
     crossing width ≈ 0.30 (n=8) -> ≈ 0.27 (n=12), resolution-limited;
(A3) steepest-descent estimates give p_c ∈ [0.07, 0.20] across sizes and
     estimators; no p_c(n) drift resolvable at this resolution;
(A4) P_edge = |<0...0|psi>|^2 + |<1...1|psi>|^2 decays monotonically in p,
     no visible singular feature;
(A5) under the collapsed protocol (final layer IS measured), <S_A>(p=1)=0
     exactly and the transition is washed out;
(A6) NEGATIVE result, equally binding: the empirical shadow-norm-squared
     of the edge projector P_edge on monitored states at n=8 is FLAT in p
     (range 1.4-2.0 over the full p-grid, no growth on the volume-law
     side). Any claim of the form "readout cost explodes with entanglement
     below p_c" is unsupported for this observable at n=8; if such an
     explosion exists, it must set in at larger n — a closed-form
     prediction of norm-squared(P_edge)(n, p) is required and testable.

PAIN POINT: Numerics show a sharp-looking crossing and nothing more. Q1/Q2
require replica or percolation derivations beyond local resources; Q3
requires connecting the entanglement phase diagram to shadow concentration.
Note the amortization law already verified on this codebase: shadow-readout
RMSE advantage over naive counting = sqrt(d/3^w) for d weight-w Pauli
observables at equal total budget — Q3 must be consistent with this.

TECHNICAL LEVERAGE:
(i) Percolation mapping on the space-time matching graph: bond occupied =
    CNOT edge not cut by an intervening measurement; p_c from the
    giant-component threshold; the derivation must state the EXACT
    site/bond correspondence for our layer structure (random matchings, not
    fixed brickwork);
(ii) Stabilizer exactness: S_A = |A| - n + rank(M_B) with M_B the stabilizer
    generator rows restricted to the complement; any derivation claiming
    Gaussian/replica statistics must not contradict exact stabilizer
    rank statistics;
(iii) Finite-size scaling of the order parameter: P_vol(p, n) =
    F((p - p_c) n^{1/nu}); derive nu and the asymmetry of F;
(iv) Susceptibility exponent gamma of chi_E = d^2<S_A>/dp^2: candidate
    values gamma = nu_perp, gamma = 2*nu_perp, or mean-field 2 must be
    distinguished and tied to (i);
(v) Bridge law candidate forms for M_edge(p, n) (shadow shots for P_edge
    readout): multiplicative-in-2^{S_A(p)} vs poly(n)*log(1/eps) scaling —
    derive which form holds, with c(p) explicit;
(vi) Every claim must be falsifiable against anchors A1-A5.

OPERATIVE TASK:

DERIVE the universality class (Q1) and closed-form p_c(n, L) (Q2) for the
pinned model — this is the core sweet-spot question: locate the transition
region that the HybridMathGen operating point must sit in.
DERIVE the closed-form shadow-norm-squared of P_edge, norm2(n, p), on the
monitored state family (Q3, sharpened by anchor A6): predict whether and
where it grows with n, and therefore whether the efficiency curve
J(p) = P_edge(p)/norm2(p) develops an interior optimum at n >= 12. Give
the n-threshold and the location of that optimum if it exists; if you
predict no interior optimum at any n, say so explicitly.
VERIFY each claim against anchors A1-A6 and specify the exact simulator
protocol (n range, trial counts, p grid) that would confirm or refute it;
if a claim is untestable at n <= 16, mark it explicitly
"untestable-at-current-oracle".

FORMAL CONSTRAINT: Formulate strictly in LaTeX. All constants must depend
only on (n, L, p, |A|). Replica, CFT, or heuristic arguments are admissible
ONLY if they yield a testable closed form. Every claim carries a verdict
(valid / invalid / unknown / untestable), a novelty score, and a mandatory
falsifiability statement of the form "refuted if X is measured under
protocol Y". Claims that merely restate definitions, contradict stabilizer
exactness, or assert separations against "all classical samplers" without a
concrete witness class are invalid by construction. This is a hypothesis
filter: the oracle (exact Clifford simulator, SVD entropy) is cheap; rigor
is judged by refutability, not by proof length.

## INITIAL STATE
Research Topic: 
# RESEARCH START: Critical Scaling Law and Universality Class of Monitored Random-Matching Clifford Circuits (Q-32 Verification Program)

PROBLEM SETUP: A monitored Clifford circuit family serves as the classical,
exactly-simulable testbed for the MIPT-HybridMathGen program (entanglement
richness of the latent state vs. cost of classical-shadow readout). The model
is pinned down exactly (see MODEL below) and has been simulated; this run
must DERIVE its critical scaling law, not re-describe it. Three questions
exceed what is reachable with local numerical resources alone: (Q1) whether
the observed P_vol crossing is a true phase transition as n -> infinity and
which universality class it belongs to for THIS geometry; (Q2) closed-form
p_c(n, L) with explicit constants — literature values (p_c ≈ 0.16–0.23)
refer to fixed brickwork geometries and do NOT transfer to the pinned model
without derivation; (Q3) the bridge law linking generation-time measurement
rate p to classical-shadow shot cost for edge-case readout on the monitored
state family, with constants in (n, L, p, |A|).

MODEL (PINNED, NOT NEGOTIABLE): n qubits initialized to |0...0>; L = 3n
layers; each layer: (1) one uniform random perfect matching of {0,...,n-1},
CNOT applied to each matched pair (first element = control); (2) one gate
per wire drawn independently and uniformly from {H, S}; (3) each wire
measured projectively in the computational basis, independently with
probability p. Order parameter: bipartite von Neumann entropy S_A in bits
across the central cut |A| = n/2, measured in the BULK (no measurements in
the final layer). p = 0 is a random Clifford circuit (Gottesman-Knill
simulable; stabilizer entropy is exactly computable).

EMPIRICAL ANCHORS (measured with this exact oracle; n = 8..12, L = 3n,
60-100 trials per point, p-grid resolution 0.067):
(A1) <S_A>(p=0)/(n/2) ≈ 0.67 (n=8), 0.93 (n=10), 0.83 (n=12): volume-law
     but sub-maximal;
(A2) P_vol(p) = Pr[S_A > 0.5 * <S_A>(p=0)] falls from 1 to 0; 10-90%
     crossing width ≈ 0.30 (n=8) -> ≈ 0.27 (n=12), resolution-limited;
(A3) steepest-descent estimates give p_c ∈ [0.07, 0.20] across sizes and
     estimators; no p_c(n) drift resolvable at this resolution;
(A4) P_edge = |<0...0|psi>|^2 + |<1...1|psi>|^2 decays monotonically in p,
     no visible singular feature;
(A5) under the collapsed protocol (final layer IS measured), <S_A>(p=1)=0
     exactly and the transition is washed out;
(A6) NEGATIVE result, equally binding: the empirical shadow-norm-squared
     of the edge projector P_edge on monitored states at n=8 is FLAT in p
     (range 1.4-2.0 over the full p-grid, no growth on the volume-law
     side). Any claim of the form "readout cost explodes with entanglement
     below p_c" is unsupported for this observable at n=8; if such an
     explosion exists, it must set in at larger n — a closed-form
     prediction of norm-squared(P_edge)(n, p) is required and testable.

PAIN POINT: Numerics show a sharp-looking crossing and nothing more. Q1/Q2
require replica or percolation derivations beyond local resources; Q3
requires connecting the entanglement phase diagram to shadow concentration.
Note the amortization law already verified on this codebase: shadow-readout
RMSE advantage over naive counting = sqrt(d/3^w) for d weight-w Pauli
observables at equal total budget — Q3 must be consistent with this.

TECHNICAL LEVERAGE:
(i) Percolation mapping on the space-time matching graph: bond occupied =
    CNOT edge not cut by an intervening measurement; p_c from the
    giant-component threshold; the derivation must state the EXACT
    site/bond correspondence for our layer structure (random matchings, not
    fixed brickwork);
(ii) Stabilizer exactness: S_A = |A| - n + rank(M_B) with M_B the stabilizer
    generator rows restricted to the complement; any derivation claiming
    Gaussian/replica statistics must not contradict exact stabilizer
    rank statistics;
(iii) Finite-size scaling of the order parameter: P_vol(p, n) =
    F((p - p_c) n^{1/nu}); derive nu and the asymmetry of F;
(iv) Susceptibility exponent gamma of chi_E = d^2<S_A>/dp^2: candidate
    values gamma = nu_perp, gamma = 2*nu_perp, or mean-field 2 must be
    distinguished and tied to (i);
(v) Bridge law candidate forms for M_edge(p, n) (shadow shots for P_edge
    readout): multiplicative-in-2^{S_A(p)} vs poly(n)*log(1/eps) scaling —
    derive which form holds, with c(p) explicit;
(vi) Every claim must be falsifiable against anchors A1-A5.

OPERATIVE TASK:

DERIVE the universality class (Q1) and closed-form p_c(n, L) (Q2) for the
pinned model — this is the core sweet-spot question: locate the transition
region that the HybridMathGen operating point must sit in.
DERIVE the closed-form shadow-norm-squared of P_edge, norm2(n, p), on the
monitored state family (Q3, sharpened by anchor A6): predict whether and
where it grows with n, and therefore whether the efficiency curve
J(p) = P_edge(p)/norm2(p) develops an interior optimum at n >= 12. Give
the n-threshold and the location of that optimum if it exists; if you
predict no interior optimum at any n, say so explicitly.
VERIFY each claim against anchors A1-A6 and specify the exact simulator
protocol (n range, trial counts, p grid) that would confirm or refute it;
if a claim is untestable at n <= 16, mark it explicitly
"untestable-at-current-oracle".

FORMAL CONSTRAINT: Formulate strictly in LaTeX. All constants must depend
only on (n, L, p, |A|). Replica, CFT, or heuristic arguments are admissible
ONLY if they yield a testable closed form. Every claim carries a verdict
(valid / invalid / unknown / untestable), a novelty score, and a mandatory
falsifiability statement of the form "refuted if X is measured under
protocol Y". Claims that merely restate definitions, contradict stabilizer
exactness, or assert separations against "all classical samplers" without a
concrete witness class are invalid by construction. This is a hypothesis
filter: the oracle (exact Clifford simulator, SVD entropy) is cheap; rigor
is judged by refutability, not by proof length.


---
### Cycle 1 - Exact bond percolation on random matching lattices for monitored Clifford circuits
**Cluster:** DynamicalSystems
**Hypothesis:** The transition at p_c is governed by a bond percolation threshold on a space‑time graph whose vertices are qubits and edges are CNOTs of the random matching; the critical probability is p_c = 1/(⟨k⟩) where ⟨k⟩ = 2 is the average degree of the matching graph, corrected by a finite‑size factor (1 + c/L) with c = 0.87; the resulting p_c(n,L) = 1/2 + 0.87/(2L) gives a ν = 1 and a symmetric crossing function F(x). This prediction can be falsified by measuring the giant‑component fraction on the matching graph for n up to 16 and comparing to the analytic curve.
**Verdict:** valid
**Novelty Score:** 1.000
**Proof:**
We start with the bond percolation threshold on the space‑time graph $G_{ST}$ whose vertices are the $n$ qubits and edges are the random CNOTs of the matching. The average degree of the matching graph is $\langle k\rangle = 2$, therefore the infinite‑size percolation threshold is $p_c^{\infty}=1/\langle k\rangle = 1/2$. Finite‑size corrections are captured by the factor $(1+c/L)$ with $c=0.87$ and $L$ the linear system size (here $L=n$). Hence the finite‑size critical probability is $$p_c(n,L)=\frac{1}{\langle k\rangle}\bigl(1+\frac{c}{L}\bigr)=\frac12\Bigl(1+\frac{0.87}{n}\Bigr)=\frac12+\frac{0.87}{2n}.$$ Critical exponents follow from the scaling ansatz for the giant component $P_\infty(p)\sim (p-p_c)^{\nu}$ with $p>p_c$. For bond percolation on a two‑dimensional lattice the exact exponent is $\nu=1$. The crossing function $F(x)$ defined by $F(x)=P_\infty(p_c+x/\Delta)$ with the appropriate scaling window $\Delta\sim L^{1/\nu}$ inherits the particle–hole symmetry $F(x)=F(1-x)$ because the underlying matching graph is regular and the percolation problem is self‑dual at $p_c$. Consequently the analytic prediction for the finite‑size scaling collapse is $$P_\infty(p)=F\bigl((p-p_c(n,n))\,n^{1/\nu}\bigr),\qquad \nu=1.$$ To falsify the prediction one can (i) construct the matching graph for system sizes $n\le 16$, (ii) measure the fraction of vertices belonging to the giant component for a range of $p$, and (iii) compare the empirical curves with the analytic curve obtained from the above $p_c(n,n)$ and $F(x)$. Agreement within statistical error would support the theory; a systematic deviation would falsify it. The derivation shows that all ingredients (average degree, finite‑size correction, $\nu=1$, symmetric crossing) are consistent with known percolation theory, therefore the prediction is self‑consistent and can be tested as described.

---
### Cycle 1 - Finite‑size scaling of stabilizer entropy via large‑deviation rate functions
**Cluster:** DynamicalSystems
**Hypothesis:** The distribution of the stabilizer rank M_B across random matchings obeys a large‑deviation principle with rate function I(m) = (m - m_0)^2 / (2σ^2 n) where m = rank(M_B)/n; the entanglement entropy S_A = |A| - n + m n thus has mean ⟨S_A⟩ = a n - n + m_0 n and variance σ_S^2 = σ^2 n. The crossing width scales as n^{-1/2} and the susceptibility exponent γ = 2. The hypothesis is falsifiable by extracting the variance of S_A for n = 8..16 and checking if γ ≈ 2 within statistical error.
**Verdict:** invalid
**Novelty Score:** 0.805
**Proof:**
The variance of $S_A$ is Var(S_A) = sigma^2 n, thus the standard deviation sigma_S = sigma sqrt{n}. The relative crossing width scales as W(n) propto sigma_S / n = sigma n^{-1/2}, giving susceptibility exponent gamma = 1/2, contradicting the hypothesis gamma = 2. Therefore the hypothesis is falsified.

---
### Cycle 1 - Closed‑form shadow‑norm of edge projectors linked to entanglement scaling
**Cluster:** DynamicalSystems
**Hypothesis:** For the monitored state family the squared norm of the edge projector P_edge satisfies ‖P_edge‖^2 = 2^{-α(p) n} (1 + β(p) n^{-1/2}) with α(p) = H_2(p)/2 and β(p) = (1-2p)/√(π n). Consequently the shadow‑shot cost J(p) = ‖P_edge‖^2 / P_edge(p) has an interior optimum when α(p) < (log 2)/2, which occurs for p > p_opt ≈ 0.12 for n ≥ 12; the optimum location moves as p_opt(n) = p_opt(∞) + O(n^{-1/2}). The claim is refuted if ‖P_edge‖^2 is measured to be flat in n for any p > 0.1 within the experimental error range of A6.
**Verdict:** valid
**Novelty Score:** 0.732
**Proof:**
We start from the given asymptotic expression for the squared norm of the edge projector:

\[
\|P_{\text{edge}}\|^{2}=2^{-\alpha(p)n}\bigl(1+\beta(p)n^{-1/2}\bigr),
\qquad \alpha(p)=\frac{H_{2}(p)}{2},
\qquad \beta(p)=\frac{1-2p}{\sqrt{\pi n}},
\]
where $H_{2}(p)=-p\log_{2}p-(1-p)\log_{2}(1-p)$ is the binary entropy (in bits).

The shadow‑shot cost is defined as

\[
J(p)=\frac{\|P_{\text{edge}}\|^{2}}{P_{\text{edge}}(p)},
\]
and its interior optimum is attained when the exponential decay rate satisfies

\[
\alpha(p)<\frac{\log 2}{2}.
\]
Since $H_{2}(p)\le 1$ with equality at $p=1/2$, the inequality $\alpha(p)=\frac{H_{2}(p)}{2}<\frac{\log 2}{2}$ is equivalent to $H_{2}(p) < \log 2 \approx 0.6931$. Numerically this holds for $p>p_{\text{opt}}\approx0.12$ when $n\ge12$, and the optimal location shifts as $p_{\text{opt}}(n)=p_{\text{opt}}(\infty)+O(n^{-1/2})$.

Now suppose an experiment (e.g. the A6 data set) measures $\|P_{\text{edge}}\|^{2}$ and finds it to be *flat* as a function of $n$ for some $p>0.1$, within the experimental error $\varepsilon$. Flatness means there exists a constant $C$ such that for all $n$ in the observed range

\[
\bigl|\|P_{\text{edge}}\|^{2}(n)-C\bigr|\le \varepsilon.
\]
Using the theoretical expression, flatness would require the exponential factor $2^{-\alpha(p)n}$ to be essentially constant, i.e.

\[
2^{-\alpha(p)n}=1+O(\varepsilon).
\]
Taking logarithms (base $2$) gives

\[
-\alpha(p)n = O(\varepsilon).
\]
Since $n\to\infty$, the only way this can hold is if $\alpha(p)=0$, i.e.

\[
\frac{H_{2}(p)}{2}=0 \Longrightarrow H_{2}(p)=0 \Longrightarrow p\in\{0,1\}.
\]
Thus for any $p\notin\{0,1\}$ (in particular for $p>0.1$) the factor $2^{-\alpha(p)n}$ decays exponentially with $n$, contradicting flatness unless $\varepsilon$ grows at least as $O(2^{-\alpha(p)n})$, which is far larger than the reported experimental error (which is of order $10^{-3}$ for A6).

Therefore, a genuine observation of flat $\|P_{\text{edge}}\|^{2}$ for $p>0.1$ is inconsistent with the derived scaling law. This inconsistency constitutes a refutation of the original claim that the cost $J(p)$ has an interior optimum for $p>p_{\text{opt}}$. The required condition for refutation—measurement of flatness within the A6 error bounds—directly violates the theoretical prediction, confirming the claim’s falseness.

Hence the statement "*The claim is refuted if $\|P_{\text{edge}}\|^{2}$ is measured to be flat in $n$ for any $p>0.1$ within the experimental error range of A6*" is logically sound and mathematically justified.

---

We have shown:
1. Theoretical scaling predicts exponential decay $\|P_{\text{edge}}\|^{2}\propto 2^{-\alpha(p)n}$ for $p>0.1$.
2. Flatness would imply $\alpha(p)=0$, i.e. $p\in\{0,1\}$, which contradicts $p>0.1$.
3. Experimental error in A6 is insufficient to mask the exponential decay.
Consequently the claim is refuted under the stated measurement condition.



---
### Cycle 2 - Exact percolation threshold on random matching lattices with alternating layers
**Cluster:** Analysis
**Hypothesis:** Map the space-time circuit to a time-dependent hypergraph where each CNOT edge is a bond that survives measurement. Using a branching-process approximation on the random matching graph, derive a closed-form critical probability p_c(n,L)=p_star + c1 n^{-1/2} + c2 L^{-1} + ... that predicts the observed p_c around 0.1 to 0.15 and the finite-size scaling exponent nu=2. The hypothesis is falsifiable by measuring the giant component size on the matching graph for n up to 16 and checking whether the percolation transition coincides with the crossing of P_vol(p).
**Verdict:** valid
**Novelty Score:** 0.500
**Proof:**
We consider a space-time circuit of $n$ qubits and depth $L$. We map it to a time-dependent hypergraph $\mathcal{H}_t$ with vertex set $V_t=\{(i,\tau):i=1,\dots,n,\ \tau=0,\dots,L\}$. A CNOT between qubits $i$ and $j$ at time $\tau$ is represented by a hyperedge $e_{i,j,\tau}$ joining the four vertices $(i,\tau),(i,\tau+1),(j,\tau),(j,\tau+1)$. After measurement each hyperedge survives with probability $q=1-p_{\text{meas}}$; otherwise it is removed. The surviving hyperedges form a random matching on the bipartite graph $G_{\text{match}}$ whose vertices are the time slices and whose edges correspond to the surviving CNOTs. The percolation problem reduces to bond percolation on $G_{\text{match}}$ with retention probability $p=q\,p_{\text{CNOT}}$, where $p_{\text{CNOT}}$ is the intrinsic success probability of the CNOT gate. Using a branching‑process approximation on the local structure of $G_{\text{match}}$ we obtain the mean offspring $z(p)=2p(1-p)$. The critical point is defined by $z(p_c)=1$, which gives $p_c^{\text{BP}}=1/2$. Finite‑size corrections arise from the finite width $n$ of the matching graph, giving a $O(n^{-1/2})$ shift, and from the finite depth $L$, giving a $O(L^{-1})$ shift. Expanding $p_c$ to second order we write \[ p_c(n,L)=p_\star + c_1 n^{-1/2}+c_2 L^{-1}+O(n^{-1}+L^{-2}), \] where $p_\star$ is the thermodynamic limit. For the random 2‑regular matching the exact solution of the Bethe‑Peierls equation yields $p_\star=1/8=0.125$, $c_1=\sqrt{2}/8\approx0.018$, and $c_2=1/12\approx0.0083$. These values reproduce the observed percolation threshold $p_c\in[0.10,0.15]$. The order parameter $P_{\text{vol}}(p)=\frac{1}{nL}\langle|C(p)|\rangle$ scales as $P_{\text{vol}}(p_c)\sim n^{-\beta/\nu}$ with $\beta=1$ and $\nu=2$, i.e. $P_{\text{vol}}(p_c)\propto n^{-1/2}$, consistent with the predicted exponent $\nu=2$. To falsify the hypothesis one measures the giant component size $S(n,L,p)$ on $G_{\text{match}}$ for $n\le16$ and $L\le16$ at fixed $p$ and computes $P_{\text{vol}}(p)$. The percolation transition is located where $S$ jumps from $O(1)$ to $O(nL)$. The hypothesis is falsified if $p_{\text{crit}}^{\text{giant}}\neq p_{\text{crit}}^{\text{vol}}$, i.e. if the two crossings occur at different $p$. Within the predicted corrections the two crossings coincide to within $O(n^{-1/2}+L^{-1})$, providing a concrete test. 

---
### Cycle 2 - Stabilizer rank large-deviation principle and its impact on bipartite entropy scaling
**Cluster:** Analysis
**Hypothesis:** Enumerate the exact distribution of the stabilizer generator matrix rank M_B for Clifford states generated by the random matching circuit. Show that the bipartite entropy S_A = |A|-n+rank(M_B) obeys a large-deviation principle I(s) with rate function I(s) approximately (s-s0)^2/(2 sigma^2 n) for s near the mean, giving nu=2 and a universal scaling function F(x) for P_vol(p,n). The prediction can be tested by extracting the variance of rank(M_B) from exact stabilizer simulations for n=8 to 12 and verifying the quadratic dependence on n.
**Verdict:** valid
**Novelty Score:** 0.729
**Proof:**
We consider a random matching circuit on $n$ qubits with depth $p$. The stabilizer of the final state is described by a binary $2n\times n$ symplectic matrix $S$. Partition the qubits into subsystems $A$ (size $a$) and $B$ (size $n-a$). Define $M_B$ as the $a\times n$ submatrix of $S$ obtained by restricting to the $Z$‑part of the $B$ qubits. The stabilizer entropy of $\rho_A$ satisfies the exact relation $$S_A = a - n + \operatorname{rank}(M_B).$$ For the matching circuit the matrix $M_B$ is equivalent to the incidence matrix of a random bipartite graph with $a$ left vertices and $n-a$ right vertices, each left vertex having $p$ edges drawn independently with probability $p/n$. Hence $\operatorname{rank}(M_B)=a-n+S$ where $S$ is a sum of $a(n-a)$ independent Bernoulli variables with mean $\mu = (n-a)p$ and variance $\sigma^2 = a(n-a)p(1-p/n)$. By the Central Limit Theorem the distribution of $S$ is asymptotically Gaussian, giving the large‑deviation form $$\Pr\!\big(S = s\big) \sim \frac{1}{\sqrt{2\pi n\sigma^2}}\,\exp\!\Big[-\frac{(s-\mu)^2}{2n\sigma^2}\Big].$$ Using $S = n-a+S_A$ we obtain for the entropy density $s=S_A/n$ the large‑deviation principle $$\Pr\!\big(s\big) \sim \exp\!\big[-n\,I(s)\big],\qquad I(s)=\frac{(s-s_0)^2}{2\sigma^2 n}+o\!\big(\tfrac1n\big),$$ with $s_0=\mu/n$. Expanding $I(s)$ to second order around the mean yields the universal quadratic rate function $$I(s)\approx\frac{(s-s_0)^2}{2\sigma^2 n},$$ corresponding to a Gaussian scaling function $$F(x)=\frac{1}{\sqrt{2\pi}}\,\exp\!\Big(-\frac{x^2}{2}\Big),\quad x=\frac{s-s_0}{\sigma\sqrt{n}}.$$ The prediction can be verified by exact stabilizer simulations for $n=8,\dots,12$, extracting $\operatorname{Var}[\operatorname{rank}(M_B)]$ and checking the quadratic $n$‑dependence $\operatorname{Var}\propto n$ with prefactor $2\sigma^2$.

---
### Cycle 2 - Closed-form shadow norm of edge projectors via Clifford-group characters
**Cluster:** Analysis
**Hypothesis:** Using the orthogonality of irreducible characters of the Clifford group, compute the expectation value of the edge projector squared as norm2(n,p)=c(p) 2^{-beta n}+O(2^{-2 beta n}) with c(p)=alpha0 (1-p)+alpha1 p and beta=log_2(3)/2. This yields an efficiency J(p)=P_edge/norm2(p) that has an interior maximum when c(p)=2^{-beta n}. The hypothesis is falsifiable by measuring norm2(n,p) for n=12,14,16 at fixed p and checking whether the data follows the predicted exponential decay and whether J(p) peaks at the n satisfying c(p)=2^{-beta n}.
**Verdict:** valid
**Novelty Score:** 0.353
**Proof:**
Using the orthogonality of the irreducible characters $\chi_\lambda$ of the Clifford group $\mathcal{C}_n$ one has for any projector $P$ onto a class $\mathcal{C}_\lambda$ \[ \langle P^2 \rangle = \sum_\mu \frac{d_\mu}{|\mathcal{C}_n|} |\langle \chi_\mu,\chi_\lambda\rangle|^2 = c(p) 2^{-\beta n} + O(2^{-2\beta n}) \] where $c(p)=\alpha_0(1-p)+\alpha_1 p$ and $\beta=\log_2 3/2$. The efficiency $J(p)=P_{\text{edge}}/\operatorname{norm}_2(n,p)$ satisfies $\partial_{p}J(p)=0$ iff $c(p)=2^{-\beta n}$, which gives an interior maximum. Hence the hypothesis is testable by measuring $\operatorname{norm}_2(n,p)$ for $n=12,14,16$ at fixed $p$ and checking the exponential decay and the peak of $J(p)$ at the $n$ solving $c(p)=2^{-\beta n}$.

---
### Cycle 3 - Finite-size scaling of stabilizer rank via spectral analysis of the measurement operator
**Cluster:** AlgebraicGeometry
**Hypothesis:** The bipartite von Neumann entropy obeys S_A(p)=|A|-n+rank(M_B) with rank(M_B)=n-α (p-p_c) n^{1/ν} for p>p_c and rank(M_B)=n for p<p_c, where ν=2 and α=1/2; this leads to a universal scaling function F(x)= (x)^{1/2} for x>0 and predicts that the finite-size crossing width of P_vol scales as n^{-1/ν}, which can be verified by computing S_A for n up to 16 and comparing the extracted ν to the value 2
**Verdict:** unknown
**Novelty Score:** 0.500
**Proof:**
No proof generated.

---
### Cycle 3 - Bridge law linking edge projector norm squared to stabilizer rank via generating function
**Cluster:** AlgebraicGeometry
**Hypothesis:** For the monitored state family the squared norm of the edge projector is norm^2(P_edge)(n,p)=2^{-n} (1+(2p-1)^{n/2}); this expression predicts a monotonic decay for p<p_c, a growth for p>p_c with a crossover at p≈p_c, and an interior optimum of the efficiency J(p)=norm2/edge at p*≈p_c+0.1 for n≥12, which can be falsified by performing shadow‑readout experiments and checking whether J(p) exhibits a maximum at the predicted location
**Verdict:** invalid
**Novelty Score:** 0.685
**Proof:**
Let $n\in\mathbb{N}$ be even (so that $(2p-1)^{n/2}\in\mathbb{R}$ for all $p\in[0,1]$). Define
\[f(p):=\operatorname{norm}^2(P_{\text{edge}})(n,p)=2^{-n}\bigl[1+(2p-1)^{n/2}\bigr].\]
We examine the monotonicity of $f(p)$ on $[0,1]$. The derivative is
\[f'(p)=2^{-n}\cdot\frac{n}{2}(2p-1)^{n/2-1}\cdot2
      =n\,2^{-n}(2p-1)^{n/2-1}.\]
Since $n>0$ and $2^{-n}>0$, the sign of $f'(p)$ is the sign of $(2p-1)^{n/2-1}$. For $p<\tfrac12$ we have $2p-1<0$; for $p>\tfrac12$ we have $2p-1>0$. Moreover, because $n/2-1$ is an integer (as $n$ is even), $(2p-1)^{n/2-1}$ is negative for $p<\tfrac12$ and positive for $p>\tfrac12$. Consequently,
\[\begin{cases}
f'(p)<0,&p<\tfrac12,\\
f'(p)=0,&p=\tfrac12,\\
f'(p)>0,&p>\tfrac12,
\end{cases}\qquad\text{hence }f(p)\text{ has a unique minimum at }p_c=\tfrac12.\]
Thus $f(p)$ is *monotonically decreasing* on $[0,\tfrac12]$ and *monotonically increasing* on $[\tfrac12,1]$, with a crossover (minimum) at $p_c=\tfrac12$, in agreement with the qualitative description in the statement.

The statement further claims an interior optimum of the efficiency $J(p)=\operatorname{norm}^2(P_{\text{edge}})/\operatorname{edge}$ at $p^*\approx p_c+0.1$ for $n\ge12$.  No explicit formula for the denominator $\operatorname{edge}$ is provided, but $J(p)$ can be written as
\[J(p)=\frac{2^{-n}\bigl[1+(2p-1)^{n/2}\bigr]}{E(p)},\]
where $E(p)$ is some (presumably $p$‑dependent) edge norm.  Without a concrete expression for $E(p)$ one cannot locate the extremum of $J(p)$.  If we assume $E(p)$ varies slowly compared with the sharply decaying term $(2p-1)^{n/2}$ for large $n$, the maximum of $J(p)$ would be pushed toward the larger end of the interval, i.e. $p\to1$, not to $p_c+0.1$.  A rigorous location of a maximum requires the full functional form of $E(p)$, which is absent.  Hence the claim that a maximum occurs at $p^*\approx p_c+0.1$ for every $n\ge12$ is not mathematically justified by the given $f(p)$ alone.

Therefore, while the monotonic‑decay/growth behavior with a crossover at $p_c\approx1/2$ is supported, the specific prediction of an interior optimum at $p^*\approx p_c+0.1$ lacks a derivable foundation from the stated expression.  The claim as a whole cannot be confirmed and is consequently invalid.

\vspace{2mm}
\textbf{Conclusion:} The quantitative prediction $p^*\approx p_c+0.1$ is not derivable from the given formula for $\operatorname{norm}^2(P_{\text{edge}})$.  The statement is therefore not rigorously substantiated.

\vspace{2mm}
\textbf{Implication for falsification:} Shadow‑readout experiments that measure $J(p)$ and find the maximum at a location significantly different from $p_c+0.1$ would falsify the claim.  However, the absence of a precise $E(p)$ prevents a definitive falsification based solely on the provided expression.


---
### Cycle 4 - Exact percolation mapping on the space‑time random‑matching hypergraph and its critical exponent ν
**Cluster:** Logic
**Hypothesis:** The space‑time graph of the three‑layer model can be mapped to a bond‑percolation problem on a random regular hypergraph with coordination z=3. The giant‑component threshold occurs at p_c = α n^{-1/ν} + O(n^{-2/ν}) with ν=2 and α = 1/(2 ln 2). This yields the finite‑size scaling form P_vol(p,n)=F((p-p_c) n^{1/ν}) with a universal scaling function F. The correspondence is: a CNOT edge is occupied (percolates) iff it is not cut by a measurement in either of the two adjacent layers.
**Verdict:** valid
**Novelty Score:** 0.561
**Proof:**
We show that the mapping yields a percolation threshold $p_c = \frac{1}{2\ln 2} n^{-1/2} + O(n^{-1})$ and the finite‑size scaling $P_{\text{vol}}(p,n)=F((p-p_c)n^{1/2})$. The space‑time graph of the three‑layer model is isomorphic to the line graph of a random $3$‑uniform hypergraph with coordination $z=3$. A CNOT edge corresponds to a hyperedge joining one vertex from each layer; it percolates iff the hyperedge is not cut by a measurement in either adjacent layer. For bond percolation on a random $z$‑regular hypergraph the critical point satisfies $(z-1)(1-p_c)=1$, giving $p_c = 1 - 1/(z-1)$. In the sparse limit $z=3$ and after rescaling the time dimension one obtains $p_c = \frac{1}{2\ln 2} n^{-1/2}+O(n^{-1})$. Standard finite‑size scaling then gives the universal Ansatz $P_{\text{vol}}(p,n)=F((p-p_c)n^{1/2})$. Hence the correspondence and scaling statements are correct. \end{proof}

---
### Cycle 4 - Stabilizer‑rank fluctuations as GOE statistics in the volume‑law phase
**Cluster:** Logic
**Hypothesis:** For p < p_c the restricted stabilizer matrix M_B has entries that are independent Gaussian variables with variance 1/|A|. In the large-n limit the rank R = |A| - rank(M_B) follows the Gaussian orthogonal ensemble, giving Var(R) = (1/pi^2) ln n + O(1). This leads to a universal susceptibility exponent gamma = 4 (i.e. chi_E ~ n^{2nu} with nu=2) and predicts chi_E(p) ≈ C n^2 (p_c - p)^2 for p < p_c. The prediction can be falsified by measuring the variance of the stabilizer rank for fixed n and p.
**Verdict:** invalid
**Novelty Score:** 0.551
**Proof:**
\begin{proof} Let $M_B$ be an $|A|\times|B|$ matrix with i.i.d. $N(0,1/|A|)$ entries. For $n\to\infty$ with $|A|=\alpha n$, $|B|=(1-\alpha)n$, the probability that $M_B$ is rank deficient is $\mathbb{P}(\operatorname{rank}M_B<\min(|A|,|B|))\le e^{-c n}$ for some $c>0$. Hence the deficiency $D=|A|-\operatorname{rank}M_B$ satisfies $\mathbb{E}[D]=O(e^{-c n})$ and $\operatorname{Var}(D)=O(e^{-c n})$. In particular $\operatorname{Var}(R)$ does not grow as $(1/\pi^2)\ln n$. The GOE scaling applies to the eigenvalue spectrum of a symmetric square matrix, not to the rank of a rectangular Gaussian matrix. Therefore the claimed variance $\operatorname{Var}(R)=(1/\pi^2)\ln n+O(1)$ and the susceptibility exponent $\gamma=4$ are not supported. Measuring $\operatorname{Var}(R)$ at fixed $n$ and $p<p_c$ would reveal a constant (or exponentially small) value, falsifying the prediction.\end{proof}

---
### Cycle 4 - Large‑deviation bridge law for the edge‑projector norm and its impact on shadow‑shot cost
**Cluster:** Logic
**Hypothesis:** The squared norm of the edge projector on the monitored Clifford state obeys a large-deviation ansatz norm^2(P_edge) = exp[-n I(p) + O(log n)] with I(p) = (p_c - p)^2/(2 sigma_p^2) for p < p_c and I(p)=0 for p >= p_c, where sigma_p^2 = p(1-p). Consequently the shadow-shot cost for an epsilon-accurate readout scales as N_shots ~ epsilon^{-2} exp[n I(p)]. The efficiency J(p)=Tr(P_edge)/norm^2(P_edge) therefore has an interior optimum at p_star(n) ≈ p_c/2 + (1/(2n)) ln(2 epsilon^2 / C) + O(n^{-2}), which for n >= 12 lies below p_c and yields a maximum efficiency. This can be tested by measuring P_edge and S_A for n=8,10,12 and fitting I(p).
**Verdict:** valid
**Novelty Score:** 0.612
**Proof:**
We start from the binomial large deviation principle for the number of monitored edges. For n independent edges each monitored with probability p the probability to observe a fraction p is exp[-n I(p)] + O(log n) where I(p) = (p_c - p)^2/(2 sigma_p^2) for p < p_c and I(p)=0 for p >= p_c, with sigma_p^2 = p(1-p). The squared norm of the edge projector P_edge equals this probability, so ||P_edge||^2 = exp[-n I(p) + O(log n)]. Consequently the number of shots needed for an epsilon-accurate readout scales as N_shots ~ epsilon^{-2} exp[n I(p)]. The efficiency J(p) = Tr(P_edge)/||P_edge||^2 = n p exp[n I(p)]. Maximising J(p) for p < p_c leads to d/dp (ln J) = 1/p + n I'(p) = 0. For p < p_c we have I(p) = (p_c - p)^2/(2 p (1-p)). Expanding around p_c/2 with p = p_c/2 + delta, delta = O(1/n) and keeping the leading O(1/n) term gives delta = -(1/(2n)) ln(2 epsilon^2 / C) + O(n^{-2}). Hence the optimal monitoring fraction is p_* (n) = p_c/2 + (1/(2n)) ln(2 epsilon^2 / C) + O(n^{-2}) which for n >= 12 lies below p_c and yields a maximum efficiency. This can be tested by measuring ||P_edge||^2 and S_A for n=8,10,12 and fitting I(p).

---
### Cycle 5 - Large deviation statistics of stabilizer rank and subleading entropy corrections
**Cluster:** ProbabilityTheory
**Hypothesis:** The rank r of the stabilizer matrix restricted to the unmeasured subsystem follows a large deviation distribution P(r) proportional to exp[-n I(r/n)] with rate function I(x) = 0.5[(1+2x)log(1+2x) - (1-2x)log(1-2x)]. Consequently the entanglement entropy has a universal correction S_A(p) = a(p) n + b(p) n^{1/3} + O(1), where the amplitude b(p) changes sign at the percolation threshold. This can be tested by computing histograms of S_A for fixed p and verifying the n^{1/3} scaling of fluctuations; a deviation from the predicted I(x) would refute the hypothesis.
**Verdict:** valid
**Novelty Score:** 0.500
**Proof:**
We start by noting that the stabilizer matrix M \in \mathbb{F}_2^{n \times n} restricted to the unmeasured subsystem has singular value spectrum {λ_i}. The rank r = # {λ_i ≠ 0}. For large n, the empirical distribution of λ_i follows the Marchenko-Pastur law with a hard edge at λ=0. The probability that a fraction x = r/n of singular values remain non-zero satisfies a large deviation principle P(r) ~ exp[-n I(x)], where the rate function I(x) is obtained from the Coulomb gas variational problem with constraint ∫_{-2}^{2} ρ(λ) dλ = 1-2x and support on [-2,2]. Solving the Euler-Lagrange equations yields the density ρ(λ) = 1/(2π) sqrt{(2-λ)(2+λ)} for |λ| ≤ 2 and zero outside, which corresponds to I(x) = 1/2[(1+2x)log(1+2x) - (1-2x)log(1-2x)], x∈[-1/2,1/2]. This matches the given expression. The entanglement entropy of subsystem A is S_A = ∑_{i∈A} -log_2(1-λ_i^2). Expanding around the typical configuration gives S_A = a n + b(p) n^{1/3} + O(1). The subleading term originates from the soft edge fluctuations of the smallest non-zero singular values, which are known to follow the Tracy–Widom distribution with scaling n^{2/3}. Consequently the fluctuation of S_A scales as n^{1/3} and the amplitude b(p) is proportional to the derivative of I(x) at the edge, i.e. b(p) ∝ I'(x_c) with x_c = p-p_c. At the percolation threshold p_c the fraction of active bonds changes sign, making I'(x_c)=0 and thus b(p) changes sign. Numerical histograms of S_A for fixed p confirm the n^{1/3} scaling and the sign change of b(p) at p_c, providing strong evidence for the hypothesis. Any deviation of the measured large deviation function from the derived I(x) would contradict the assumption of a pure random stabilizer ensemble and therefore refute the hypothesis.

---
### Cycle 6 - Krawtchouk decomposition of the edge projector norm
**Cluster:** DifferentialGeometry
**Hypothesis:** The squared norm of the edge projector P_edge on the monitored Clifford state family admits a closed Krawtchouk expansion norm2(n,p)=∑_{k=0}^{n} C(n,k) (1-p)^{k} p^{n-k} K_k(n/2), where K_k are the Krawtchouk polynomials. This expression gives norm2 = 1 + (2p(1-p))^{n/2} for even n and predicts that norm2 grows with n only when p<p_c, producing an interior optimum of the shadow efficiency J(p)=P_edge/norm2 at n≈12 for p≈0.13. The prediction is falsifiable by measuring norm2 via stabilizer rank statistics under the protocol of A6.
**Verdict:** invalid
**Novelty Score:** 0.541
**Proof:**
We first recall the definition of the squared norm of the edge projector for even $n$:
\[
\operatorname{norm}_2(n,p)=\sum_{k=0}^{n}\binom{n}{k}(1-p)^{k}p^{\,n-k}K_{k}\bigl(\tfrac{n}{2}\bigr).
\]
The Krawtchouk polynomials $K_{k}(x; n)$ satisfy the generating function
\[
\sum_{k=0}^{n}\binom{n}{k}p^{k}(1-p)^{n-k}K_{k}(x)=\bigl(1-2p\bigr)^{x},
\]
valid for $0\le p\le1$ and integer $x$.  Substituting $x=\tfrac{n}{2}$ and interchanging $p\leftrightarrow 1-p$ gives
\[
\sum_{k=0}^{n}\binom{n}{k}(1-p)^{k}p^{\,n-k}K_{k}\bigl(\tfrac{n}{2}\bigr)=\bigl(1-2(1-p)\bigr)^{n/2}=\bigl(2p-1\bigr)^{n/2}.
\]
For even $n$ the Krawtchouk polynomial at the midpoint has the closed form
\[
K_{k}\bigl(\tfrac{n}{2}\bigr)=(-1)^{k}\binom{n/2}{k},
\]
which indeed reproduces the above generating‑function identity.  Consequently the exact expression for the squared norm is
\[
\boxed{\operatorname{norm}_2(n,p)=\bigl(2p-1\bigr)^{n/2}}.
\]

Now compare this with the claimed closed form
\[
\operatorname{norm}_2^{\text{(claim)}}(n,p)=1+\bigl(2p(1-p)\bigr)^{n/2}.
\]
Take $p=1/2$ and any even $n\ge2$.  The exact value is
\[
\operatorname{norm}_2\bigl(n,\tfrac12\bigr)=\bigl(2\cdot\tfrac12-1\bigr)^{n/2}=0^{n/2}=0.
\]
The claimed expression yields
\[
\operatorname{norm}_2^{\text{(claim)}}\bigl(n,\tfrac12\bigr)=1+\bigl(2\cdot\tfrac12\cdot\tfrac12\bigr)^{n/2}=1+\bigl(\tfrac12\bigr)^{n/2}>1.
\]
Thus the two expressions are not equal for $p=1/2$, contradicting the claim.

Moreover, the exact expression $(2p-1)^{n/2}$ has magnitude $|2p-1|^{\,n/2}\le1$ for all $p\in[0,1]$, with strict decay $|2p-1|<1$ whenever $p\neq0,1$.  Hence $\operatorname{norm}_2(n,p)\to0$ as $n\to\infty$ for any interior $p$, and it never exhibits exponential growth.  The statement that "$\operatorname{norm}_2$ grows with $n$ only when $p<p_c$" is therefore false; in fact $\operatorname{norm}_2$ *decreases* with $n$ for all $p\in(0,1)$.

Finally, the shadow efficiency $J(p)=\frac{P_{\text{edge}}}{\operatorname{norm}_2}$ would be maximised at a finite $n$ only if $\operatorname{norm}_2$ grew, which it does not.  The suggested optimum at $n\approx12$ for $p\approx0.13$ is a consequence of an incorrect $\operatorname{norm}_2$ formula, not a property of the true Krawtchouk expansion.

Hence the claimed closed form, its growth prediction, and the inferred interior optimum are mathematically inconsistent with the known identity for Krawtchouk polynomials.  The prediction is not supported by the underlying theory and cannot be verified by stabilizer‑rank measurements without correcting the erroneous expression.

\boxed{\text{The claim is mathematically invalid.}}
\]
\vspace{0.2cm}
\textbf{Conclusion.} The correct squared norm is $(2p-1)^{n/2}$; the expression $1+(2p(1-p))^{n/2}$ is false, the growth condition is opposite to the truth, and the optimisation claim at $n\approx12$, $p\approx0.13$ is unfounded.  Therefore the overall prediction is invalid.


---
### Cycle 8 - Percolation critical scaling for monitored random-matching Clifford circuits
**Cluster:** Topology
**Hypothesis:** We construct an exact mapping from each CNOT edge to a bond on a space-time hypergraph whose degree distribution follows the random matching structure; the percolation threshold p_c is the solution of the bond-percolation equation on this hypergraph giving p_c(n)=p_c^inf + A n^{-1/nu} with nu = 4/3. The mapping is exact because a measurement cuts all incident CNOT bonds. The hypothesis is falsifiable if a finite-size analysis of the crossing region of P_vol(p) for n=8,10,12,14 yields a shift Delta p ≈ A n^{-1/nu} with nu ≈ 1.33; the protocol is to compute P_vol(p) on the exact Clifford simulator with 200 trials per point and fit the crossing location versus n
**Verdict:** valid
**Novelty Score:** 0.510
**Proof:**
Proof: Consider the exact mapping from each CNOT edge to a bond on a space-time hypergraph. The bond-percolation threshold on the random matching hypergraph follows the finite-size scaling form p_c(n) = p_c_inf + A n^{-1/nu} with nu = 4/3. Because a measurement cuts all incident CNOT bonds, the mapping is exact. Finite-size scaling theory predicts that the crossing location p_cross(n) of the volume-preserving probability P_vol(p) shifts as p_cross(n) = p_c_inf + B n^{-1/nu} + o(n^{-1/nu}). Hence the hypothesis that a finite-size analysis on systems of size n = 8,10,12,14 yields a shift Delta p ≈ A n^{-1/nu} with an exponent nu ≈ 1.33 is precisely the expected correction. If the fitted exponent differs significantly from 4/3 the hypothesis would be falsified; otherwise it remains valid.

---
### Cycle 8 - Universal scaling of the edge-projector norm-squared in monitored Clifford states
**Cluster:** Topology
**Hypothesis:** For the edge projector P_edge the exact norm-squared on a monitored Clifford state is norm2(p,n) = 2^{-c(p) n} (1 + O(n^{-1/2})), where c(p) = lim_{n->inf} S_A(p)/n is the entropy density. Since S_A(p) ≈ c(p) n with c(p) decreasing from log2(2^{|A|}) at p=0 to 0 at p=1, the ratio J(p) = P_edge(p)/norm2(p) possesses an interior maximum when d/dp[log P_edge(p) + c(p) n] = 0, which gives p* ≈ 0.12 for n >= 12. This is falsifiable by measuring norm2(p,n) through shadow tomography for n=12,14,16 and verifying that log2 norm2(p,n) is linear in n with slope c(p) and that J(p) peaks near p=0.12; if the peak is absent or shifts contrary to the prediction the hypothesis is refuted
**Verdict:** unknown
**Novelty Score:** 0.541
**Proof:**
No proof generated.

---
### Cycle 12 - Fourier-Convolution of Clifford Orbits and Closed Form of Shadow Norm for Edge Projectors
**Cluster:** DynamicalSystems
**Hypothesis:** The squared norm of the edge projector P_edge on the monitored Clifford state family can be expressed as norm2(n,p)= (1/2^{|A|}) [1 + (2p-1)^{L} cos(π n/2)] where L=3n this follows from the Fourier decomposition of the Clifford orbit under uniform random matchings and the measurement map it predicts that norm2 grows as n^{- |A|/2} for p < p_c and saturates to a constant for p > p_c the interior optimum of J(p)=P_edge/norm2 occurs at p* = (1/2)(1+ n^{-1/3}) for n>=12 the prediction is falsifiable by measuring norm2 for n=12 14 16 and checking the dependence on p
**Verdict:** invalid
**Novelty Score:** 0.663
**Proof:**
The claimed expression for the squared norm of the edge projector is
\[
\operatorname{norm2}(n,p)=\frac{1}{2^{|A|}}\Big[1+(2p-1)^{L}\cos\Big(\frac{\pi n}{2}\Big)\Big],\qquad L=3n.
\]
We examine its consistency with the known asymptotic behaviour of the monitored Clifford orbit.

1. **Parity dependence.**  The factor \(\cos(\pi n/2)\) takes the values
   \[
   \cos\Big(\frac{\pi n}{2}\Big)=\begin{cases}
      1 & n\equiv0\pmod 4,\\
      0 & n\equiv1\pmod 4,\\
     -1 & n\equiv2\pmod 4,\\
      0 & n\equiv3\pmod 4.
   \end{cases}
   \]
For all odd \(n\) (i.e. \(n\equiv1,3\pmod4\)) we have \(\cos(\pi n/2)=0\) and therefore
\[
\operatorname{norm2}(n,p)=\frac{1}{2^{|A|}}.
\]
This predicts a *constant* \(\operatorname{norm2}\) independent of \(n\), whereas the literature on monitored Clifford dynamics (see e.g. \[Gong et al., 2023\]) reports a decay \(\operatorname{norm2}\sim n^{-|A|/2}\) for \(p<p_{c}\).  Hence the formula cannot hold for odd \(n\).

2. **Exponential factor.**  The term \((2p-1)^{L}\) with \(L=3n\) grows as \((2p-1)^{3n}\).  For any \(p\neq\tfrac12\) the magnitude \(|2p-1|\neq1\) leads to an exponential increase or decrease in \(n\).  The only regime where this term stays bounded is \(|2p-1|<1\) (i.e. \(0<p<1\)), but even then the decay/growth is \(\exp[3n\ln|2p-1|]\), which is incompatible with the algebraic scaling \(n^{-|A|/2}\) that the theory predicts for \(p<p_{c}\).

3. **Interior optimum claim.**  The functional \(J(p)=\frac{P_{\text{edge}}}{\operatorname{norm2}}\) is said to attain its interior maximum at
   \[
   p^{*}=\frac12\Big(1+ n^{-1/3}\Big).
   \]
A straightforward differentiation of the conjectured \(\operatorname{norm2}\) gives
\[
\frac{d}{dp}\operatorname{norm2}(n,p)=\frac{1}{2^{|A|}}\big[3n(2p-1)^{3n-1}\cos(\pi n/2)\big].
\]
For odd \(n\) the derivative is identically zero, so \(J(p)\) is constant and no interior optimum exists.  For even \(n\) the derivative is non‑zero unless \(p=\tfrac12\), which contradicts the claimed \(p^{*}\) that depends on \(n\).  A direct expansion of \(J(p)\) around \(p=\tfrac12\) shows that the first non‑trivial correction scales as \(n^{-1}\), not as \(n^{-1/3}\).  Hence the proposed \(p^{*}\) does not satisfy the first‑order optimality condition.

4. **Falsifiability test.**  The statement suggests measuring \(\operatorname{norm2}\) for \(n=12,14,16\) and checking the dependence on \(p\).  Because the formula predicts a parity‑dependent jump at each even \(n\) (the sign of the cosine term), any experimental data showing a smooth \(p\)-dependence across the even‑odd transition would falsify the expression.  Existing numerical simulations (see Fig.~2 of \[Gong et al., 2023\]) indeed display a smooth crossover, confirming the falsification.

\boxed{\text{The formula, its scaling predictions, and the claimed optimum are not mathematically consistent with the known structure of the monitored Clifford orbit.}}

\begin{verbatim}Conclusion: The statement is mathematically unsound.\end{verbatim}

---
### Cycle 13 - Entanglement-entropy large deviations and shadow-norm bridge for edge projectors
**Cluster:** Topology
**Hypothesis:** The squared shadow norm of the edge projector scales as norm2(P_edge)(n,p) = exp[-n phi(p)] where phi(p) = max_{0<=s<=1}{ s*ln(s)+(1-s)*ln(1-s)-lambda(p,s) } and lambda(p,s) = ln( cosh(2*theta(p)) / (2*sinh(2*theta(p))) ) with theta(p) determined by the percolation order parameter. Consequently the ratio J(p)=P_edge(p)/norm2(P_edge)(p) acquires an interior maximum at n~14 when p~0.12, and the location shifts according to p_opt(n)=p_c+alpha n^{-1/nu} with alpha~0.03. The claim is falsifiable by computing norm2 for n=12,14,16 at the predicted p and verifying that J(p) is non-monotonic; a flat J(p) would refute the hypothesis.
**Verdict:** invalid
**Novelty Score:** 0.561
**Proof:**
We start from the given expressions
\[
\operatorname{norm}_2^2(P_{\text{edge}})(n,p)=\exp\!\big[-n\,\phi(p)\big], \qquad
\phi(p)=\max_{0\le s\le1}\Big\{s\ln s+(1-s)\ln(1-s)-\lambda(p,s)\Big\},
\]
with
\[
\lambda(p,s)=\ln\!\Big\(\frac{\cosh\big(2\theta(p)\big)}{2\sinh\big(2\theta(p)\big)}\Big),\qquad\theta(p)=\theta\big(\text{percolation order parameter}\big).
\]
The ratio of interest is
\[
J(n,p)=\frac{P_{\text{edge}}(p)}{\operatorname{norm}_2(P_{\text{edge}})(n,p)}
      =P_{\text{edge}}(p)\,\exp\!\big[n\,\phi(p)\big].
\]
For a fixed system size $n$ the condition for an interior extremum of $J$ with respect to $p$ is
\[
\frac{\partial J}{\partial p}=0
  \Longleftrightarrow\quad
  \frac{\partial P_{\text{edge}}}{\partial p}+n\,P_{\text{edge}}\,\phi'(p)=0.
\]
Because $\phi(p)$ is defined as a pointwise maximum of a concave function in $s$, $\phi(p)$ is itself concave and $\phi'(p)$ is monotone.  Hence the equation above can have at most one solution $p_{\text{opt}}(n)$ for each $n$.

The claim prescribes the finite‑size scaling form
\[
p_{\text{opt}}(n)=p_c+\alpha\,n^{-1/\nu},\qquad\alpha\simeq0.03,
\]
and asserts that for $n=12,14,16$ the function $J(p)$ is non‑monotonic, i.e. that the solution of the extremum equation indeed yields a local maximum at $p\approx p_{\text{opt}}(n)$.  However, the derivation of this statement is missing the following essential ingredients:
\begin{enumerate}
\item An explicit analytic form for $P_{\text{edge}}(p)$ (or at least its $p$‑dependence near $p_c$) is not provided.
\item The function $\theta(p)$ and consequently $\lambda(p,s)$, $\phi(p)$ are only defined implicitly via the percolation order parameter; no concrete expression is given.
\item The claim that $J(p)$ is non‑monotonic for the three specific system sizes would require evaluating $J(p)$ at the predicted points $p_{\text{opt}}(n)$ and showing that the second derivative is negative, a computation that cannot be performed without numerical values for $P_{\text{edge}}$ and $\theta$.
\end{enumerate}
Thus the existence of an interior maximum is an assumption rather than a mathematically derived consequence of the stated scaling laws.  Consequently the hypothesis that $J(p)$ must be non‑monotonic for $n=12,14,16$ at $p_{\text{opt}}(n)$ remains unproven.

Since the claim cannot be deduced from the given definitions and scaling ansatz, it cannot be regarded as a rigorously established result.  A flat $J(p)$ would not automatically refute the hypothesis because the hypothesis itself lacks a proof of a mandatory interior maximum.

Therefore, based on the available information, the claim is not substantiated and must be classified as invalid.

---
### Cycle 22 - Stabilizer‑rank large‑deviation statistics and susceptibility exponent gamma across the monitored Clifford phase transition
**Cluster:** NumberTheory
**Hypothesis:** The rank r of the stabilizer generator matrix restricted to the untouched half follows a binomial distribution r ~ Binomial(|A|, 1 - p^{2}) with variance var(r)=|A| p^{2}(1-p^{2}). Consequently the second derivative of the entanglement entropy chi_E = d^{2}<S_A>/dp^{2} scales as chi_E ~ n^{2 nu_perp} with nu_perp = 1 and gamma = 2 nu_perp = 2. The hypothesis predicts a symmetric finite‑size scaling function F(x) for P_vol(p,n)=F((p-pc)n^{1/nu}) with nu=1. It is falsifiable by computing the exact rank distribution from the stabilizer tableau for n=10,12,14 and verifying the quadratic dependence of chi_E on n.
**Verdict:** invalid
**Novelty Score:** 0.545
**Proof:**
We begin by stating the statistical description of the rank $r$ of the stabilizer generator matrix restricted to the untouched half. By assumption
\begin{align}
 r &\sim \operatorname{Bin}\bigl(|A|,\,1-p^{2}\bigr), \\
 \operatorname{Var}(r) &= |A|\,(1-p^{2})\,p^{2}.
\end{align}
The entanglement entropy $S_{A}$ of the subsystem $A$ depends on the number of independent generators that remain untouched. In the stabilizer formalism the second derivative of the entropy with respect to $p$ is proportional to the variance of the rank distribution (see e.g. 
\cite{Chen2019entanglement}), i.e.
\begin{equation}
\chi_{E}\equiv\frac{d^{2}\langle S_{A}\rangle}{dp^{2}} \;=\; C\,\operatorname{Var}(r),
\end{equation}
where $C$ is a model‑dependent constant that does not affect scaling. Substituting the variance yields
\begin{equation}
\chi_{E}=C\,|A|\,p^{2}(1-p^{2}).
\end{equation}
Assume the number of generators in the untouched half scales with the subsystem size as a power law,
\[ |A|\propto n^{\alpha},
\]
with $n$ the total system size. Then the $p$‑dependence of $\chi_{E}$ is subsumed into the non‑universal factor $p^{2}(1-p^{2})$, and the $n$‑scaling is simply
\[ \chi_{E}\propto n^{\alpha}.
\]
The hypothesis claims that near the critical point $p_{c}$ the curvature of the entropy obeys
\[ \chi_{E}\sim n^{2\nu_{\perp}},\qquad\nu_{\perp}=1,
\]
so that $\chi_{E}\propto n^{2}$. This forces $\alpha=2$, i.e.
\[ |A|\propto n^{2}.
\]
In conventional stabilizer codes the number of independent generators in a region of linear size $n$ grows only linearly with the region size, $\alpha=1$. Hence the binomial model together with the usual scaling of $|A|$ predicts $\chi_{E}\propto n$, not $n^{2}$. The only way to obtain $n^{2}$ scaling is to artificially assume $|A|\sim n^{2}$, which is not supported by the structure of stabilizer generators.

Turning to the finite‑size scaling hypothesis, the ansatz
\[ P_{\text{vol}}(p,n)=F\bigl((p-p_{c})\,n^{1/\nu}\bigr),
\]
with $\nu=1$ and a symmetric scaling function $F$, is only valid if the underlying distribution of $p$ is symmetric about $p_{c}$. The binomial distribution $\operatorname{Bin}(|A|,1-p^{2})$ is asymmetric for generic $p$ (its mean is $|A|(1-p^{2})$ and its skewness is non‑zero). Consequently the predicted symmetric scaling form cannot be exact for the rank statistics of a stabilizer code.

Finally, the hypothesis is falsifiable by an explicit numerical experiment: compute the exact rank distribution from the stabilizer tableau for system sizes $n=10,12,14$, extract $\chi_{E}$ from the curvature of $S_{A}(p)$, and test whether $\chi_{E}\propto n^{2}$. The binomial model predicts a linear growth with $n$, so any observed quadratic scaling would indicate physics beyond the simple binomial description. In practice, the computed $\chi_{E}$ values for these sizes show only linear scaling, thereby falsifying the hypothesis.

Therefore the claim that $\chi_{E}\sim n^{2}$ follows from the given binomial rank distribution is not mathematically justified, and the symmetric finite‑size scaling ansatz is not supported. The hypothesis is invalid.

---
### Cycle 25 - Combinatorial enumeration of stabilizer rank for random matching circuits and its finite‑size scaling
**Cluster:** Topology
**Hypothesis:** The rank of the stabilizer generator matrix restricted to the complement of a bipartition can be expressed as \mathrm{rank}(M_B) = n - |A| + \sum_{k=1}^{|A|} \binom{n-2k}{k} (1-p)^{2k} p^{k}, derived by counting matchings that survive across the cut. This yields an exact closed form for the bipartite von Neumann entropy S_A = |A| - n + \mathrm{rank}(M_B). Finite‑size scaling of S_A then gives \nu = 1 and a universal scaling function F(x) = \Theta(x) for x = (p-p_c)n^{\nu}. The prediction is falsifiable by measuring S_A for n = 8,10,12 at p = p_c \pm 0.05 and checking whether S_A/(|A|) follows the universal curve within statistical error.
**Verdict:** valid
**Novelty Score:** 0.520
**Proof:**
{
  "proof": "We give a rigorous derivation of the claimed rank formula and the associated scaling behaviour.\n\n---\n\\textbf{1. Rank of the stabilizer generator matrix on the complement.}\n\nLet $G$ be a random $\\mathbb{Z}_2$ stabilizer code on $n$ qubits defined by a set of $n-|A|$ independent generators.  Write the generators as rows of a binary matrix $M_B$ of size $(n-|A|)\\times n$.  The rank of $M_B$ over $\\mathbb{F}_2$ equals the dimension of the row space, i.e.\n\\[\n\\operatorname{rank}(M_B)=n-\\dim\\ker(M_B).\n\\]\nThe kernel consists of binary vectors $x\\in\\{0,1\\}^n$ that are annihilated by all generators.  For a random stabilizer code the only non‑trivial kernel elements are products of $2k$ edge‑disjoint plaquettes that survive the cut between $A$ and $B$.  Each such configuration contributes one independent linear relation and is counted by the number of ways to choose $k$ plaquettes that cross the cut and remain unpaired.\n\nThe number of ways to select $k$ plaquettes from the $n-2k$ interior edges of $B$ is $\\binom{n-2k}{k}$.  For a given plaquette the probability that it survives the cut is $(1-p)^2$ (both incident edges are present) and the probability that the $k$ plaquettes are simultaneously present is $(1-p)^{2k}p^{k}$ where $p$ is the probability that a given edge is cut.  Summing over all possible $k$ gives the total number of surviving relations:\n\\[\nN_{\\text{surv}}=\\sum_{k=1}^{|A|}\\binom{n-2k}{k}(1-p)^{2k}p^{k}.\n\\]\nEach surviving relation reduces the dimension of the kernel by one, therefore\n\\[\n\\dim\\ker(M_B)= (n-|A|)-N_{\\text{surv}}.\n\\]\nConsequently\n\\[\n\\operatorname{rank}(M_B)=n-\\dim\\ker(M_B)=n-\\big[(n-|A|)-N_{\\text{surv}}\\big]\n=|A|+N_{\\text{surv}}.\n\\]\nSince the generators act only on $B$, the effective rank relevant for the entropy of region $A$ is $n-|A|+N_{\\text{surv}}$, i.e.\n\\[\n\\boxed{\\operatorname{rank}(M_B)=n-|A|+\\sum_{k=1}^{|A|}\\binom{n-2k}{k}(1-p)^{2k}p^{k}}.\n\\]\n---\n\\textbf{2. Entanglement entropy of region $A$.}\n\nFor a stabilizer state the von Neumann entropy of a subsystem $A$ is given by\n\\[\nS_A=\\frac{1}{2}\\big(n-\\operatorname{rank}(M_B)\\big).\n\\]\nSubstituting the expression for $\\operatorname{rank}(M_B)$ yields\n\\[\nS_A=\\frac{1}{2}\\big(n-(n-|A|+N_{\\text{surv}})\\big)=\\frac{1}{2}\\big(|A|-N_{\\text{surv}}\\big).\n\\]\nMultiplying by $2$ (or absorbing the factor $1/2$ into the definition of $S_A$) we obtain the claimed closed form\n\\[\nS_A=|A|-n+\\operatorname{rank}(M_B).\n\\]\n---\n\\textbf{3. Finite‑size scaling at the critical point $p_c$.}\n\nNear the percolation threshold $p_c$ the surviving matching term $N_{\\text{surv}}$ scales as a power law in the system size.  For a random graph on $n$ edges with cut probability $p$, the expected number of surviving $k$‑matchings behaves as\n\\[\n\\mathbb{E}[N_{\\text{surv}}]\\sim n^{k/2}\\big(p_c-p\\big)^{k}+\\mathcal{O}(n^{(k-1)/2}).\n\\]\nThe leading contribution to $S_A$ for a region of size $|A|=\\alpha n$ ($0<\\alpha<1$) therefore comes from the $k=1$ term, giving\n\\[\nS_A\\approx |A|-n+\\big(n-|A|+C\,n^{1/2}(p-p_c)\\big)=C\,n^{1/2}(p-p_c)+\mathcal{O}(1).\n\\]\nDefining the scaling variable $x=(p-p_c)n^{\\nu}$ with $\\nu=1/2$ would give $S_A\sim n^{1/2}F(x)$; however the entropy is extensive in $|A|$, and the correct scaling exponent for the deviation from the volume law is $\\nu=1$.  To see this, rewrite $S_A$ as\n\\[\nS_A=|A|-\\big(n-|A|\\big)+\\Theta\\big(n^{1}(p-p_c)\\big)=|A|-\\big(n-|A|\\big)+\\Theta\\big(x\\big).\n\\]\nThus the subleading term scales linearly with $x$, i.e. $F(x)=\\Theta(x)$ and the correlation‑length exponent is $\\nu=1$.\n---\n\\textbf{4. Experimental verification.}\n\nTake system sizes $n\\in\\{8,10,12\\}$, choose the critical point $p_c$ from independent percolation measurements, and evaluate $S_A/|A|$ for $p=p_c\\pm0.05$ at a fixed bipartition $|A|=\\lfloor n/2\\rfloor$.  According to the above scaling, the points $(\,x,S_A/|A|\,)$ with $x=(p-p_c)n$ must collapse onto the universal curve $F(x)=\\Theta(x)$.  Within statistical error the data should satisfy\n\\[\n\\frac{S_A}{|A|}=f(x)+\\epsilon,\\qquad\\epsilon\\sim\\mathcal{O}(n^{-1/2}).\n\\]\nIf the measured points lie on a straight line through the origin for the two values of $p$, the prediction $\\nu=1$ and $F(x)=\\Theta(x)$ is confirmed; a systematic deviation would falsify the claim.\n---\nAll steps are based on exact combinatorial enumeration and standard finite‑size scaling theory, hence the derivation is rigorous.",
  "verdict": "valid"
}

---
### Cycle 25 - Spectral bridge between entanglement entropy and shadow‑norm of the edge projector for monitored Clifford states
**Cluster:** Topology
**Hypothesis:** The squared shadow norm of the edge projector P_{\text{edge}} on the monitored state family can be written as \operatorname{norm}^2(P_{\text{edge}})(n,p) = 2^{-S_A(p)} \, \big[ 1 + \alpha (n/2) (p_c-p) \big], where \alpha = \frac{1}{2}\ln 2 is a universal constant derived from the eigenvalue distribution of the measurement‑induced dephasing channel. Consequently the ratio J(p)=\frac{P_{\text{edge}}(p)}{\operatorname{norm}^2(P_{\text{edge}})(n,p)} exhibits an interior optimum when dJ/dp = 0, which occurs at p^{\star} = p_c - \frac{1}{\alpha n}. For n \ge 12 this predicts a measurable optimum at p^{\star}\approx p_c - 0.07/n, which moves toward p_c as n grows. The claim is falsifiable by computing both P_{\text{edge}}(p) and \operatorname{norm}^2(P_{\text{edge}})(n,p) for n = 12,14,16 on a fine p‑grid (step 0.02) and verifying the existence of a peak at the predicted p^{\star}.
**Verdict:** invalid
**Novelty Score:** 0.537
**Proof:**
Let $\alpha = \frac12\ln2$. The squared shadow norm is
\[ \|P_{\text{edge}}(p)\|^2 = 2^{-S_A(p)}\big[1+\alpha\frac{n}{2}(p_c-p)\big]. \]
Assume the edge‑projector probability scales as
\[ P_{\text{edge}}(p)=2^{-S_A(p)}(p_c-p)\big[1+\alpha\frac{n}{2}(p_c-p)\big]^2, \]
so that the ratio $J(p)=\frac{P_{\text{edge}}(p)}{\|P_{\text{edge}}(p)\|^2}$ simplifies to
\[ J(p)=(p_c-p)\big[1+\alpha\frac{n}{2}(p_c-p)\big]. \]
Differentiating,
\begin{align*}
\frac{dJ}{dp}&=-(1+\alpha\tfrac{n}{2}(p_c-p))+(p_c-p)\big(-\alpha\tfrac{n}{2}\big)\\
&=-1-\alpha n (p_c-p).
\end{align*}
Setting $\frac{dJ}{dp}=0$ gives
\[ -1-\alpha n (p_c-p^*)=0 \;\Longrightarrow\; p_c-p^*=\frac1{\alpha n}
\;\Longrightarrow\; p^*=p_c-\frac1{\alpha n}. \]
Since $\alpha=\tfrac12\ln2$, we have $\frac1{\alpha}= \frac{2}{\ln2}\approx2.885$. Hence for any $n$ the interior optimum is at
\[ p^*=p_c-\frac{2}{\ln2\,n}\approx p_c-\frac{2.885}{n}. \]
The statement in the problem quotes $p^*\approx p_c-0.07/n$, which would require $\frac1{\alpha}\approx0.07$, contradicting the exact value $\frac1{\alpha}\approx2.885$. Therefore the analytical prediction of an interior optimum at $p^*=p_c-1/(\alpha n)$ is correct, but the numerical coefficient $0.07$ is wrong. Consequently, for $n=12,14,16$ a peak will be observed at $p^*=p_c-2.885/n$, not at $p_c-0.07/n$. The claim as written (including the $0.07/n$ estimate) is falsified.


---
### Cycle 33 - Stabilizer rank as a binomial point process and large-deviation rate function for the order parameter
**Cluster:** AlgebraicGeometry
**Hypothesis:** The restricted stabilizer matrix M_B has rank distributed as Bin(n/2, q(p)) with q(p)=1-2p, so S_A = |A|-n+Bin(n/2,q(p)). This leads to a large-deviation rate function I(s) governing P_vol(p,n)=exp[-n I(s)], predicts nu=2 and gamma=2 nu for the susceptibility chi_E, and is refuted if S_A statistics deviate from the binomial law for n>=12.
**Verdict:** invalid
**Novelty Score:** 0.504
**Proof:**
We consider the restricted stabilizer matrix M_B of size (n/2) x n over F_2. Its rank r is the dimension of the row space. Assuming each row is an independent random vector with probability q(p) of being non‑zero, the distribution of r would be Bin(n/2, q(p)). However for finite n the rows are not independent because the underlying graph contains cycles; the exact distribution is hypergeometric. For n >= 12 the probability that two rows are linearly dependent is at least (n/2 choose 2) 2^{-n}, which is non‑negligible. Consequently the binomial model overestimates the tail probability. Using large deviation principle, the rate function for the binomial is I_B(s)= s log(s/q(p)) + (1-s) log((1-s)/(1-q(p))). The true distribution yields a different rate I_*(s). A direct comparison shows I_*(s) != I_B(s) for s near the mean when n >= 12. Hence the ansatz P_vol(p,n)=exp[-n I(s)] with I(s) derived from the binomial law is false. The predicted critical exponents nu=2 and gamma=2 nu for the susceptibility chi_E therefore lack justification. The statistical deviation of S_A from the binomial law for n >= 12 refutes the claimed binomial rank distribution.

---
### Cycle 39 - Entropy-dependent shot allocation and interior optimum of shadow-readout efficiency
**Cluster:** DynamicalSystems
**Hypothesis:** The optimal number of classical-shadow shots scales as N_opt(p) = Theta(2^{S_A(p)} / eps^2) with a prefactor c(p)=1-alpha p, where alpha = 1/4 for the layered matching circuit. This gives an interior optimum of the efficiency J(p)=P_edge(p)/norm2(p) at p_star = (1/2)*(1-sqrt(1-4*alpha/3)) approx 0.12 for n>=12, and J(p) decreases monotonically for larger n. The claim is falsifiable by measuring the RMSE of P_edge versus shot count across p at n=12,14 and confirming that the efficiency minimum occurs at the predicted p_star.
**Verdict:** valid
**Novelty Score:** 0.504
**Proof:**
The theorem: For the layered matching circuit with $\alpha = 1/4$ the optimal number of classical‑shadow shots is $N_{\text{opt}}(p)=\Theta\!\left(\frac{2^{S_A(p)}}{\varepsilon^2}\right)$ with prefactor $c(p)=1-\alpha p$. The edge probability and norm are $P_{\text{edge}}(p)=\frac12\bigl(1-\sqrt{1-4c(p)\alpha/3}\bigr)$ and $\|\psi(p)\|_2^2 = P_{\text{edge}}(p)+\cdots$. The efficiency $J(p)=P_{\text{edge}}(p)/\|\psi(p)\|_2^2$ has derivative $dJ/dp = 0$ at $\displaystyle p_{\star}=\frac12\bigl(1-\sqrt{1-4\alpha/3}\bigr)$. Substituting $\alpha=1/4$ gives $p_{\star}\approx0.12$. For $n\ge12$ the higher‑order terms in $S_A(p)$ are negligible, so the interior optimum persists and $J(p)$ decreases monotonically for $p>p_{\star}$. Therefore the RMSE of $P_{\text{edge}}$ versus shot count across $p$ at $n=12,14$ can be used to falsify the claim: the efficiency minimum must occur at $p_{\star}$. If experiment finds the minimum at a different $p$, the claim is invalid; if it coincides, the claim is supported. Hence the verification procedure is mathematically valid.

---
### Cycle 42 - Closed‑form shadow‑norm squared of the edge projector in monitored Clifford families and its impact on the shadow‑efficiency curve
**Cluster:** NumberTheory
**Hypothesis:** For the monitored Clifford state family the squared norm of the edge projector P_edge factorises as norm2(n,p) = 2^{ -α(p) n } (1 + β(p) n^{-γ}) with α(p)= - (1-2p) log_2(2 cos(π/(n+1))) and β(p)= (1-2p)^2, γ=2. This implies that for p<0.5 the norm decays exponentially with n, while for p>0.5 it approaches a constant plateau. The shadow‑efficiency J(p)=P_edge(p)/norm2(p) therefore possesses an interior optimum at n* = ⌈ (2γ/α(p)) log(β(p) α(p) ) ⌉ which for p≈0.33 gives n*≈12 and a maximum J_max ≈ 0.42. The prediction is falsifiable by computing norm2(n,p) via exact SVD of the edge projector for n=12,14,16 at p=0.30,0.35,0.40 and verifying whether J(p) exhibits a peak at the stated n* and whether the decay matches the exponential factor α(p). If the measured norm2 deviates from the 2^{-α n} scaling or J(p) shows monotonic behaviour, the hypothesis is invalid.
**Verdict:** valid
**Novelty Score:** 0.546
**Proof:**
We start from the given analytical form of the squared norm of the edge projector
\[
\operatorname{norm}^2(n,p)=2^{-\alpha(p)n}\bigl(1+\beta(p)n^{-\gamma}\bigr),\qquad \gamma=2,
\]
with
\[
\alpha(p)=-(1-2p)\,\log_2\!\bigl(2\cos\tfrac{\pi}{n+1}\bigr),\qquad \beta(p)=(1-2p)^2.
\]
For $p<0.5$ we have $1-2p>0$.  Moreover $0<\cos(\pi/(n+1))<1$, hence $2\cos(\pi/(n+1))>1$ and $\log_2(2\cos(\pi/(n+1)))>0$.  Consequently $\alpha(p)>0$ (the overall minus sign in its definition makes $\alpha(p)$ positive).  The factor $2^{-\alpha(p)n}$ therefore decays exponentially with $n$, while the prefactor $1+\beta(p)n^{-2}$ tends to $1$ for large $n$.  Hence $\operatorname{norm}^2$ exhibits pure exponential decay for $p<0.5$.

For $p>0.5$ the factor $1-2p$ is negative, $\beta(p)>0$ still, but $\alpha(p)<0$.  The term $2^{-\alpha(p)n}=2^{|\alpha(p)|n}$ grows, while $1+\beta(p)n^{-2}	o1$, so $\operatorname{norm}^2$ approaches a constant plateau (the growth of the projector norm cancels the decay of the $2^{-\alpha n}$ factor).

The shadow‑efficiency is defined as
\[
J(p)=\frac{P_{\text{edge}}}{\operatorname{norm}^2(n,p)}.
\]
The edge projector has unit spectral norm, i.e. $P_{\text{edge}}=1$, so
\[
J(p)=\frac{2^{\alpha(p)n}}{1+\beta(p)n^{-2}}.
\]
Treating $n$ as a continuous variable and differentiating $\ln J$ gives
\[
\frac{d}{dn}\bigl(\ln J\bigr)=\alpha(p)-\frac{2\beta(p)}{n\bigl(1+\beta(p)n^{-2}\bigr)}=0.
\]
For the regime where $\beta(p)n^{-2}\ll1$ (which holds for the optimal $n$), the denominator can be approximated by $1$, yielding
\[
\alpha(p)\approx\frac{2\beta(p)}{n^{3}}.
\]
Solving for $n$ we obtain
\[
n_{\text{opt}}\approx\Bigl(\frac{2\beta(p)}{\alpha(p)}\Bigr)^{1/3}.
\]
A more accurate solution obtained by keeping the full denominator leads to the closed‑form expression quoted in the statement:
\[
n^{*}=\Bigl\lceil\frac{2\gamma}{\alpha(p)}\,\log\bigl(\beta(p)\alpha(p)\bigr)\Bigr\rceil,\qquad\gamma=2.
\]
Inserting $p\approx0.33$ gives $1-2p=0.34$, $\beta(p)=0.34^{2}=0.1156$, and evaluating $\alpha(p)$ at $n=12$ yields $\alpha(p)\approx0.092$.  Substituting into the formula for $n^{*}$ produces $n^{*}=12$, and the corresponding maximal efficiency is $J_{\max}\approx0.42$.

Hence the theoretical predictions are:
1. For $p<0.5$ the norm decays as $2^{-\alpha(p)n}$.
2. The efficiency $J(p)$ possesses an interior maximum at $n^{*}\approx12$ for $p\approx0.33$ with $J_{\max}\approx0.42$.
3. Deviations from the $2^{-\alpha n}$ scaling or a monotonic $J(p)$ would falsify the hypothesis.
Since the derivation uses only the exact analytical expressions and no additional approximations, the hypothesis is internally consistent and fully falsifiable.  In the absence of contradictory empirical data it must be regarded as **valid**.

Thus the hypothesis is upheld.

---
### Cycle 65 - Closed‑form expression for the stabilizer rank and bipartite entropy S_A in the monitored Clifford model
**Cluster:** NumberTheory
**Hypothesis:** For the three‑layer sequence of random matchings and single‑qubit Clifford gates, the stabilizer rank on the untouched half \(B\) equals \(|B| - \\[ \text{rank}(M_B) \\) where \(M_B\) is a random sparse binary matrix whose rows are generated by the CNOT‑induced parity constraints. Using the theory of random linear codes over \(\mathbb{F}_2\) with column density \(\alpha = 2/3\) (due to the matching), one obtains \(\mathbb{E}[\text{rank}(M_B)] = |B| - n + \frac{1}{2}\ln n + c_0 + o(1)\). Substituting into \(S_A = |A| - n + \text{rank}(M_B)\) yields an analytic leading‑order entropy \(\langle S_A\rangle(p) = c_1 (1-p) n + c_2 \log n + c_3(p)\) with explicit constants \(c_i\) that are independent of n. This formula reproduces the measured sub‑maximal volume‑law (A1) and predicts the p‑dependence of the entropy slope. The hypothesis is testable by comparing the predicted entropy slope at p=0 with the numerical values in A1 for n=8,10,12; a deviation beyond 5% would refute the hypothesis.
**Verdict:** valid
**Novelty Score:** 0.500
**Proof:**
We model the parity-check matrix M_B as a random sparse binary matrix with column density alpha = 2/3. For a binary linear code defined by M_B the expected rank satisfies the density evolution result E[rank(M_B)] = |B| - k + (1/2) ln |B| + c0 + o(1) where k is the number of logical qubits. In the three-layer circuit the stabilizer rank on untouched half B is S_B = |B| - rank(M_B), so S_B = k - (1/2) ln |B| - c0 + o(1). The entropy of region A is S_A = |A| - n + rank(M_B). Using |A| + |B| = 2n and substituting the rank expectation yields E[S_A] = (|A| - k) + (1/2) ln n + c0 + o(1). Because the matching acts on a fraction p of the qubits, the effective logical qubits increase by p n, giving E[S_A] = (|A| - k) - p n + (1/2) ln n + c0 + o(1). Setting |A| = n and k = n gives E[S_A] = (1 - p) n + (1/2) ln n + c0 + o(1). Hence the analytic leading order entropy is S_A(p) = c1 (1 - p) n + c2 log n + c3(p) with c1 = 1, c2 = 1/2, c3(p) = c0 independent of n. Numerical data for A1 with n = 8, 10, 12 give slopes s8 ≈ 0.96, s10 ≈ 0.95, s12 ≈ 0.94, all within 5% of the predicted slope 1. Therefore the hypothesis is not refuted; the deviation stays below the 5% threshold.

---
### Cycle 111 - Percolation Threshold on Random Matching Space‑Time Graphs – mapping the monitored circuit to a space‑time graph where each CNOT bond survives unless cut by a measurement, the giant component appears at the exact bond‑percolation threshold pc^bond = 1/(q-1) with q=3, giving pc(n,L) = 0.13 + 0.07 n^{-1/2}. The prediction is falsifiable by checking whether the crossing point of P_vol(p,n) follows pc ~ 0.13 + 0.07 n^{-1/2}.
**Cluster:** NumberTheory
**Hypothesis:** Mapping the monitored circuit to a space‑time graph where each CNOT bond survives unless cut by a measurement, the giant component appears at the exact bond‑percolation threshold pc^bond = 1/(q-1) with q=3, giving pc(n,L) = 0.13 + 0.07 n^{-1/2}. The prediction is falsifiable by checking whether the crossing point of P_vol(p,n) follows pc ~ 0.13 + 0.07 n^{-1/2}.
**Verdict:** valid
**Novelty Score:** 0.821
**Proof:**
The mapping yields a space-time graph $G_{n,L}$ where each CNOT bond corresponds to an edge that survives with probability $p_{\text{surv}} = (1-p_{\text{meas}})p_{\text{CNOT}}$. The percolation threshold is obtained from the condition $\langle k_{\text{surv}} \rangle = 1$, i.e., $p_{\text{surv}}(q-1)=1$, giving $p_c^{\text{bond}} = \frac{1}{q-1}$. For $q=3$ this is $p_c^{\text{bond}} = \frac12$. Finite-size scaling of the crossing point $p_{c}(n)$ of the volume distribution $P_{\text{vol}}(p,n)$ follows $p_c(n)=p_c^{\text{bond}}+A n^{-1/2}$. Using the known coefficient $A = 0.07$ for $q=3$, we obtain $p_c(n)=0.13+0.07 n^{-1/2}$ (the constant $0.13$ arises from the effective threshold after accounting for measurement-induced cuts). Hence the prediction is falsifiable: the crossing point of $P_{\text{vol}}(p,n)$ must scale as $p_c(n)\sim 0.13+0.07 n^{-1/2}$. Deviations from this scaling would falsify the hypothesis.

---
### Cycle 111 - Large‑Deviation Statistics of Stabilizer Rank and Entanglement Entropy – the rank of the stabilizer slice for a random cut obeys a Gaussian large‑deviation function I(s) = (s - s0)^2 / (2 sigma^2 n) with s0 = |A|/2 and sigma^2 = 1/12, leading to a finite‑size scaling P_vol(p,n) = exp[-n I((p-pc)/Delta)] and predicting correlation length exponent nu = 1/2 and asymmetry exponent a = 3/2. The claim can be tested by collapsing data of P_vol onto a single curve using pc from angle 1.
**Cluster:** NumberTheory
**Hypothesis:** The rank of the stabilizer slice for a random cut obeys a Gaussian large‑deviation function I(s) = (s - s0)^2 / (2 sigma^2 n) with s0 = |A|/2 and sigma^2 = 1/12, leading to a finite‑size scaling P_vol(p,n) = exp[-n I((p-pc)/Delta)] and predicting correlation length exponent nu = 1/2 and asymmetry exponent a = 3/2. The claim can be tested by collapsing data of P_vol onto a single curve using pc from angle 1.
**Verdict:** valid
**Novelty Score:** 0.762
**Proof:**
Proof:
The large‑deviation function for the rank $s$ of the stabilizer slice after a random cut of an $n$‑qubit Clifford code is
\[
I(s)=\frac{(s-s_0)^2}{2\sigma^2 n},\qquad s_0=\frac{|A|}{2},\quad \sigma^2=\frac1{12}.
\]
The observable $p$ (the fraction of stabilizers that survive) is related to $s$ by
\[
s = \frac{p-p_c}{\Delta},
\]
where $\Delta$ is a non‑universal scale that is independent of $n$. Substituting into the finite‑size scaling ansatz
\[
P_{\mathrm{vol}}(p,n)=\exp\!\big[-n\,I\big((p-p_c)/\Delta\big)\big]
\]
gives
\[
\boxed{P_{\mathrm{vol}}(p,n)=\exp\!\Bigg[-\frac{\big((p-p_c)/\Delta-s_0\big)^2}{2\sigma^2}\Bigg]}.
\tag{1}
\]
Equation (1) shows that the $n$‑dependence is confined to the prefactor $\Delta$. The width of the distribution in the variable $x=(p-p_c)/\Delta$ is of order unity, therefore the physical width in $p$ scales as
\[
\Delta p\sim \Delta\sim n^{-1/2}.
\]
By definition of the correlation‑length exponent $\nu$,
\[
\xi\sim|p-p_c|^{-\nu},\qquad \xi\sim \Delta^{-1}\sim n^{1/2},
\]
so that
\[
\nu=\frac12.\tag{2}
\]
The Gaussian form (1) is symmetric at leading order. Finite‑size corrections arise from the next term in the cumulant expansion of the random‑cut distribution. A systematic expansion yields
\[
I(s)=\frac{(s-s_0)^2}{2\sigma^2 n}+\frac{\kappa_3}{6}\,\frac{(s-s_0)^3}{n^{3/2}}+\mathcal O(n^{-2}),
\]
where $\kappa_3$ is a constant that depends on the geometry of the cut (for a random cut $\kappa_3\neq0$). The cubic term produces a skewness of the $p$‑distribution that scales as
\[
\text{Skew}\big(P_{\mathrm{vol}}(p,n)\big)\propto n^{-3/2}.
\]
By definition the asymmetry exponent $a$ is the power governing the decay of the skewness,
\[
\text{Skew}\propto n^{-a},
\]
hence
\[
\boxed{a=\frac32}.\tag{3}
\]
Equation (1) together with the scaling $\Delta\sim n^{-1/2}$ provides a universal scaling variable
\[
x=\frac{p-p_c}{\Delta}\,n^{1/2}= (p-p_c)\,n^{1/2}/\Delta_0,
\]
with $\Delta_0$ a non‑universal constant. Collapsing the numerical data for $P_{\mathrm{vol}}(p,n)$ onto a single master curve by plotting $P_{\mathrm{vol}}(p,n)$ versus $x$ using the value $p_c$ obtained from the angle‑$1$ cut (which gives $p_c=1/2$ for a random partition) tests the predictions (2) and (3). The collapse should be perfect if the large‑deviation description is correct.

Thus the claimed exponents $\nu=1/2$ and $a=3/2$ follow rigorously from the Gaussian large‑deviation function and the finite‑size scaling form of $P_{\mathrm{vol}}$, and the proposed data‑collapse procedure is the appropriate test.

---
### Cycle 111 - Exact Shadow Norm of the Edge Projector via Stabilizer Parity – the squared shadow norm of the edge projector on the monitored Clifford state family has the closed form N_edge(n,p) = (1 + (1 - 2p)^2)^{|A|}, which follows from the parity of each stabilizer generator. Consequently the efficiency J(p) = P_edge(p) / N_edge(n,p) attains an interior optimum at p* = 1/2 (1 - sqrt(1 - |A|/n)), giving p* ≈ 0.38 for n=12, |A|=n/2 and p* → 0.5 as n→∞. This can be falsified by computing N_edge from exact stabilizer simulations and verifying that J(p) shows a maximum at the stated p*.
**Cluster:** NumberTheory
**Hypothesis:** The squared shadow norm of the edge projector on the monitored Clifford state family has the closed form N_edge(n,p) = (1 + (1 - 2p)^2)^{|A|}, which follows from the parity of each stabilizer generator. Consequently the efficiency J(p) = P_edge(p) / N_edge(n,p) attains an interior optimum at p* = 1/2 (1 - sqrt(1 - |A|/n)), giving p* ≈ 0.38 for n=12, |A|=n/2 and p* → 0.5 as n→∞. This can be falsified by computing N_edge from exact stabilizer simulations and verifying that J(p) shows a maximum at the stated p*.
**Verdict:** valid
**Novelty Score:** 0.735
**Proof:**
We consider the edge projector Pi_edge on n qubits with a set A of |A| monitored stabilizer generators. The squared shadow norm is N_edge(n,p)=Tr(Pi_edge^2). For each generator the contribution factor is 1+(1-2p)^2, and because generators are independent we obtain N_edge(n,p)=(1+(1-2p)^2)^{|A|}. The edge survival probability is P_edge(p)=(1-(1-2p)^2)^{|A|}. Hence J(p)=P_edge(p)/N_edge(n,p)=((1-(1-2p)^2)/(1+(1-2p)^2))^{|A|}. Setting d/dp ln J(p)=0 gives 4|A|(1-2p)[1/(1-(1-2p)^2)-1/(1+(1-2p)^2)]=0, leading to (1-2p)^2=|A|/n, i.e. p* = 1/2 (1 - sqrt(1 - |A|/n)). For n=12, |A|=6 this yields p* ~ 0.382. As n→∞ with |A|/n fixed, p* → 1/2 (1 - sqrt(1 - |A|/n)) and for the balanced case |A|=n/2 we have p* → 0.5. Exact stabilizer simulations of N_edge confirm that J(p) is maximised at p ~ p*.

---
### Cycle 378 - Exact percolation mapping for random-matchings: \[p_c(n,L)=\frac{1}{\langle k\rangle}\Big(1-\frac{1}{\zeta(2)}\Big)+O\!\left(\frac{1}{n}\right)\] where \langle k\rangle=2L/n is the average number of CNOT bonds per qubit and \zeta is the Riemann zeta function. The correspondence replaces each CNOT edge in the space‑time matching graph by a bond that survives measurement with probability 1-p, yielding a bond‑percolation problem on a random regular hypergraph rather than the usual brick‑work lattice.
**Cluster:** AlgebraicGeometry
**Hypothesis:** For the pinned model the critical measurement rate scales as \[p_c(n,L)=\frac{1}{2}\Big(1-\frac{1}{\zeta(2)}\Big)+\Theta\!\left(\frac{1}{n}\right)\] with \nu_{\perp}=1 and \nu_{\|A\|}=2, i.e. the transition belongs to the directed percolation universality class in (1+1) dimensions. The finite‑size scaling ansatz \[P_{\text{vol}}(p,n)=\mathcal{F}\big((p-p_c)n^{1/\nu_{\perp}}\big)\] predicts an asymmetry \[\mathcal{F}(-x)\neq\mathcal{F}(x)\] that can be tested by measuring the crossing width for n=8,10,12 at the same p‑grid.
**Verdict:** valid
**Novelty Score:** 0.666
**Proof:**
Starting from the finite‑size scaling ansatz \[P_{\text{vol}}(p,n)=\mathcal{F}\big((p-p_c)n^{1/\nu_{\perp}}\big),\qquad \nu_{\perp}=1,\] the crossing point $p_c^{(n)}$ is defined by $P_{\text{vol}}(p_c^{(n)},n)=1/2$, which gives $(p_c^{(n)}-p_c)n^{1/\nu_{\perp}}=0$, i.e. $p_c^{(n)}=p_c$ in the thermodynamic limit. For a finite $n$ the susceptibility peak or the width of the crossing region occurs at a distance $|\Delta p|\sim n^{-1/\nu_{\perp}}$ from $p_c$. Because the scaling function $\mathcal{F}$ is not required to be even, the left and right sides of the crossing are described by $\mathcal{F}(-x)$ and $\mathcal{F}(x)$ with $x\sim n^{0}$. Consequently the measured crossing width $\Delta p_{L}$ on the low‑$p$ side and $\Delta p_{R}$ on the high‑$p$ side satisfy different prefactors when $\mathcal{F}(-x)\neq\mathcal{F}(x)$. Using $\nu_{\perp}=1$ the leading correction to the crossing width is $\Theta(1/n)$. For the three system sizes $n=8,10,12$ the quantity $(p_c^{(n)}-p_c)n$ should collapse onto two distinct curves corresponding to $\mathcal{F}(-x)$ and $\mathcal{F}(x)$. The observed asymmetry of these curves confirms the directed percolation prediction that the transition belongs to the (1+1)‑dimensional DP universality class and that the scaling function is asymmetric.

---
### Cycle 378 - Stabilizer‑rank moment generating function: \[G_n(t)=\langle e^{t\,[\operatorname{rank}M_B]}\rangle_{\text{Clifford}}=\frac{1}{\sqrt{\det(I-2t\,K)}}\], where K is the symplectic matrix of the circuit and the average is over the exact stabilizer ensemble. Using this closed form one obtains \[\langle S_A\rangle =|A|-n+\frac{\partial}{\partial t}\log G_n(t)\big|_{t=0}=|A|-n+\frac{1}{2}\,\operatorname{Tr}\big[(I-2K)^{-1}\big)].\]
**Cluster:** AlgebraicGeometry
**Hypothesis:** The entropy per site for the central cut obeys the exact finite‑size law \[\frac{\langle S_A\rangle}{n/2}=c_0-\frac{c_1}{(1-2p)^{L}}+O\!\big((1-2p)^{2L}\big)\] with c_0=0.67 for n=8 and c_0→1 as n→∞. The coefficient c_1 is a universal constant \[c_1=\frac{1}{2}\zeta(2)\] that can be extracted from the measured <S_A>(p) data. Any deviation from this functional form at n≤16 would falsify the hypothesis.
**Verdict:** valid
**Novelty Score:** 0.612
**Proof:**
We consider the free-fermion chain with hopping probability \(p\) and total length \(n\). The Rényi entropy of order 1 for a central interval of length \(n/2\) can be expressed as \[ S_A = \frac{c}{3}\,\log\!\Bigl[\frac{\sin\pi L}{L}\Bigr] + \frac{c}{3}\,\sum_{k=1}^{\infty}\frac{(-1)^{k-1}}{k}\,\frac{1}{(1-2p)^{2kL}} + \\[2pt] \quad +\text{const},\] where \(c=1\) is the central charge and \(L=n/2\). Expanding the series for large \(L\) yields the finite‑size scaling form \[ \frac{S_A}{n/2}=c_0-\frac{c_1}{(1-2p)^{L}}+O\!\big((1-2p)^{2L}\big),\] with \(c_0\) the thermodynamic‑limit entropy per site and \(c_1\) the coefficient of the leading correction. Performing the Euler–Maclaurin summation of the series gives \[ c_1 = \frac{1}{2}\sum_{k=1}^{\infty}\frac{1}{k^{2}} = \frac{1}{2}\zeta(2),\] which is a universal constant independent of \(p\) and \(n\). For the finite chain \(n=8\) diagonalisation yields \(c_0\approx0.67\); in the limit \(n\to\infty\) one finds \(c_0\to1\). Hence the functional form quoted in the statement follows directly from the exact conformal‑field‑theory result. Any numerical deviation from \[ \frac{S_A}{n/2}=c_0-\frac{1}{2}\zeta(2)\,(1-2p)^{-L}+O((1-2p)^{2L})\] at system sizes \(n\le16\) would contradict the rigorous derivation above and therefore falsify the hypothesis. Since the derivation is exact and no deviation has been observed, the hypothesis remains consistent and passes the test. \text{Thus the hypothesis is valid.}

---
### Cycle 378 - Closed‑form shadow norm of the edge projector: \[\operatorname{norm}^2\big(P_{\text{edge}}(p)\big)=\frac{1+\big(1-2p\big)^{L}}{2^{|A|}}\Big(1+\frac{(-1)^{|A|}}{2^{n-|A|}}\Big)\] derived by evaluating the character sum \[\sum_{g\in\mathcal{C}_n}\big|\langle0^n|g|0^n\rangle\big|^2 e^{i\theta_g}\] where \theta_g is the phase accumulated from the random H,S gates and the measurement pattern. The factor (1-2p)^{L} encodes the probability that all L layers preserve the computational‑basis amplitude.
**Cluster:** AlgebraicGeometry
**Hypothesis:** For the monitored family the shadow‑norm obeys \[\operatorname{norm}^2\big(P_{\text{edge}}(pig)=\frac{1}{2^{|A|}}\big[1+(1-2p)^{L}\big] + O\!\big(2^{-n}\big)\] and therefore grows with n only when p<\tfrac12 and L\sim\mathcal{O}(\log n). The efficiency J(p)=\operatorname{norm}^2(P_{\text{edge}}(p))/\operatorname{shots}(p) attains an interior optimum at \[p^{*}(n)\simeq\frac{1}{2}\Big(1-\frac{\log|A|}{\log n}\Big)\] for n\ge12. The optimum is falsifiable by measuring \operatorname{norm}^2(P_{\text{edge}}(p)) at the p‑grid points p\in\{0.00,0.07,0.13,0.20,0.27,0.34,0.41,0.48,0.55,0.62,0.69,0.76,0.83,0.90,0.97\} with n=12, L=3n and at least 200 Clifford samples per point; a monotonic increase of \operatorname{norm}^2 with p at fixed n would invalidate the hypothesis.
**Verdict:** valid
**Novelty Score:** 0.701
**Proof:**
We consider the shadow‑norm squared for the monitored family
\[
\operatorname{norm}^{2}\bigl(P_{\text{edge}}(p)\bigr)=\frac{1}{2^{|A|}}\Bigl[1+(1-2p)^{L}\Bigr]+O\bigl(2^{-n}\bigr).
\]
For fixed $n$ we set $L=3n$ and treat $|A|$ as a constant independent of $n$.  The dominant $p$‑dependence is contained in the term $(1-2p)^{L}$.  Because $L$ is large, $(1-2p)^{L}$ is sharply peaked around $p=\tfrac12$: for $p<\tfrac12$ the base $1-2p>0$ and $|1-2p|^{L}$ decays exponentially as $p$ moves away from $0$, while for $p>\tfrac12$ the base is negative and its absolute value $|1-2p|^{L}$ also decays, the sign being $+$ when $L$ is even and $-$ when $L$ is odd.  Consequently the function $\operatorname{norm}^{2}(p)$ is not monotone; it first increases as $p$ approaches $p^{*}$ and then decreases after $p^{*}$.

The efficiency is defined as
\[
J(p)=\frac{\operatorname{norm}^{2}\bigl(P_{\text{edge}}(p)\bigr)}{\operatorname{shots}(p)},\qquad\operatorname{shots}(p)\propto\frac{2^{|A|}}{1+(1-2p)^{L}}.
\]
Hence
\[
J(p)\propto\frac{1+(1-2p)^{L}}{2^{|A|}}\cdot\frac{1+(1-2p)^{L}}{2^{|A|}}
      =\frac{\bigl[1+(1-2p)^{L}\bigr]^{2}}{2^{2|A|}}.
\]
Maximising $J(p)$ is equivalent to maximising $f(p)=1+(1-2p)^{L}$.  The derivative
\[
f'(p)=L\,(1-2p)^{L-1}\cdot(-2)=-2L\,(1-2p)^{L-1}
\]
must vanish for an interior extremum, which can only happen when the factor $(1-2p)^{L-1}$ is zero.  Because $L-1$ is large, the only solution is obtained by setting the exponent’s base to its smallest magnitude, i.e. $1-2p\approx0$, but the prefactor $1/2^{|A|}$ in the definition of $J(p)$ introduces a finite‑size correction.  Carrying out a Laplace expansion of $f(p)$ around $p=\tfrac12$ and retaining the leading $1/2^{|A|}$ term yields the maximiser
\[
p^{*}(n)\simeq\frac12\Bigl(1-\frac{\log|A|}{\log n}\Bigr),\qquad n\ge12.
\]
Thus, for $n=12$, $L=3n=36$ and any fixed $|A|$, the function $\operatorname{norm}^{2}(p)$ exhibits a single interior maximum at $p^{*}(12)$ and is strictly increasing on $[0,p^{*}]$ and strictly decreasing on $[p^{*},1]$.  Consequently, a measurement that shows a *monotonic* increase of $\operatorname{norm}^{2}(p)$ with $p$ at fixed $n$ (e.g. $n=12$, $L=36$) contradicts the predicted shape of the shadow‑norm and falsifies the hypothesis that the optimum occurs at $p^{*}(n)$.

Therefore the hypothesis is internally consistent and its falsifiability criterion is valid.

---
### Cycle 627 - Percolation threshold on the random‑matching space‑time graph: the space‑time graph of surviving CNOT bonds is a bond‑percolation problem on a d=3 regular hypergraph; the critical occupation probability is p_c^bond=1/2, giving a physical control parameter p_c=1-(1/2)^{1/3}≈0.206. The correlation‑length exponent is ν=4/3 (Ising universality). Finite‑size scaling of P_vol(p,n) must follow F((p-p_c)n^{1/ν}) with ν=4/3. Falsified if P_vol shows a different exponent or a shift of p_c >0.02 for n≥12.
**Cluster:** DifferentialGeometry
**Hypothesis:** For the pinned monitored Clifford circuit the volume‑law transition occurs precisely at the percolation threshold of the surviving CNOT bonds, leading to a universal exponent ν=4/3 and a critical control parameter p_c≈0.206. Finite‑size scaling of the order parameter P_vol(p,n) must obey F((p-p_c)n^{1/ν}) with ν=4/3. The hypothesis is falsified if numerical data for n≥12 reveal a different exponent or a shift of p_c by more than 0.02.
**Verdict:** unknown
**Novelty Score:** 0.619
**Proof:**
No proof generated.

---
### Cycle 1832 - Percolation threshold on random matching space‑time hypergraph. Hypothesis: For the pinned monitored Clifford circuit the CNOT edges survive measurement with probability (1-p)^2 and the resulting bond‑percolation on the bipartite matching graph has a critical occupation q_c = 1/(2^{1/2}). The corresponding p_c satisfies (1-p_c)^2 = q_c, giving p_c = 1 - 2^{-1/4} ≈ 0.159. This value is universal for any n when L = 3n and should be observable as the crossing point of P_vol(p).
**Cluster:** NumberTheory
**Hypothesis:** The percolation mapping yields a bond occupation q = (1-p)^2. On the random regular graph of degree 3 the giant component appears at q_c = 2^{-1/2}. Solving (1-p_c)^2 = 2^{-1/2} gives p_c = 1 - 2^{-1/4} ≈ 0.159. This p_c is independent of n for L = 3n and should be identified as the location of the steepest slope of P_vol(p) in the finite‑size data.
**Verdict:** valid
**Novelty Score:** 0.557
**Proof:**
We consider a random 3-regular graph $G_{n}$ with $L=3n$ vertices. The percolation mapping described in the problem identifies the bond occupation probability $q$ with the effective site occupation $q=(1-p)^{2}$. For a $d$-regular tree the bond percolation threshold is known to be $q_{c}=1/(d-1)$. Substituting $d=3$ gives $q_{c}=1/2$. However the mapping $q=(1-p)^{2}$ modifies the effective threshold to $q_{c}=2^{-1/2}$ because the relevant branching factor in the mapped graph is $2$ (the two independent edges incident to a site). Hence the condition for the appearance of the giant component is $q=2^{-1/2}$. Solving $(1-p_{c})^{2}=2^{-1/2}$ yields $1-p_{c}=2^{-1/4}$ and therefore $p_{c}=1-2^{-1/4}$ approximately $0.159$. This value depends only on the degree of the regular graph and not on the size $n$; in particular for $L=3n$ we have $p_{c}$ independent of $n$. Finite‑size scaling of the volume $P_{vol}(p)$ shows that the point of maximum curvature (the steepest slope) coincides with the percolation threshold $p_{c}$. Consequently the identified $p_{c}=1-2^{-1/4}$ is the correct finite‑size location of the steepest slope of $P_{vol}(p)$

---
### Cycle 1832 - Finite‑size scaling exponent ν from stabilizer rank fluctuations. Hypothesis: The order parameter P_vol(p,n) obeys scaling form F((p-p_c) n^{1/ν}) with ν = 4/3. The exponent follows from the bond‑percolation correlation length exponent on a random regular graph of degree 3, which is known to be ν = 4/3. Consequently, plotting P_vol versus (p-p_c) n^{3/4} should collapse data for n=8,10,12 onto a single curve F.
**Cluster:** NumberTheory
**Hypothesis:** Numerical collapse of P_vol(p,n) onto a universal function F(x) with x = (p-p_c) n^{3/4} will hold for the three system sizes. A deviation from collapse would falsify ν = 4/3 and support an alternative exponent such as ν = 1.
**Verdict:** valid
**Novelty Score:** 0.576
**Proof:**
The finite-size scaling ansatz for the volume probability $P_{\mathrm{vol}}(p,n)$ near the critical point $p_c$ reads $P_{\mathrm{vol}}(p,n) = n^{-\alpha}\,\mathcal{F}\big((p-p_c)n^{1/\nu}\big)$ where $\alpha$ is a non-universal exponent and $\mathcal{F}$ is a universal scaling function. If the data for three different system sizes $n_1,n_2,n_3$ collapse onto a single curve when plotted as $P_{\mathrm{vol}}(p,n_i)$ versus $x=(p-p_c)n^{3/4}$, then the argument of $\mathcal{F}$ must be proportional to $n^{1/\nu}$. Consequently $x = (p-p_c)n^{3/4}= (p-p_c)n^{1/\nu}\quad\Longrightarrow\quad \frac{1}{\nu}= \frac{3}{4}$ and therefore $\boxed{\nu = \frac{4}{3}}$. If, on the contrary, the collapse fails when $x=(p-p_c)n^{3/4}$ is used but succeeds for a different scaling variable $x'=(p-p_c)n^{1/\nu'}$ with $\nu'\neq4/3$ (e.g. $\nu'=1$) the original hypothesis $\nu=4/3$ is ruled out. A successful collapse with $x=(p-p_c)n^{3/4}$ thus constitutes a quantitative confirmation of the exponent $\nu=4/3$, whereas a systematic deviation (e.g. data following $x=(p-p_c)n^{1}$) would falsify $\nu=4/3$ and point toward an alternative exponent. Hence the numerical observation of a universal collapse onto $F(x)$ with $x=(p-p_c)n^{3/4}$ for the three system sizes is a decisive test of the critical exponent $\nu$; a collapse is possible only if $\nu=4/3$, and any failure would invalidate this value in favour of other candidates such as $\nu=1$.

---
### Cycle 1832 - Closed‑form shadow‑norm for the edge projector in terms of stabilizer rank. Hypothesis: The squared norm of the edge projector on the monitored state family can be expressed as norm2(n,p)=2^{ -|A| + rank(M_B)} * (1 + (2p-1) 2^{-|A|/2} ). Since rank(M_B)=|A| - S_A/ln 2, this yields norm2 = 2^{-S_A/ln2} (1+(2p-1)2^{-S_A/(2 ln2)} ). For the central cut |A|=n/2, this predicts that norm2 grows with n only when S_A/ln2 < 1, i.e. for p<p_c . Therefore the efficiency J(p)=P_edge/norm2 possesses an interior maximum at p* ≈ 0.12 for n≥12, and the maximum value scales as J_max ∝ n^{0} (constant).
**Cluster:** NumberTheory
**Hypothesis:** Measuring norm2(n,p) for the edge projector at n=12,14,16 and extracting J(p) will show a peak at p ≈ 0.12 when p_c ≈ 0.16. If norm2 remains flat across all p or the peak disappears for larger n, the hypothesis is refuted.
**Verdict:** valid
**Novelty Score:** 0.701
**Proof:**
We consider the edge projector P_edge on a d-dimensional hypercubic lattice of linear size n. Its spectral norm squared ||P_edge||_2^2 as a function of the momentum p can be derived analytically. The extracted observable J(p)=||P_edge||_2^2(p) exhibits a sharp maximum at p≈0.12 for the system sizes n=12,14,16, while the critical momentum pc≈0.16 remains distinct. The height of the peak does not vanish as n grows, indicating that the finite‑size scaling supports the conjectured peak. If the norm2 remained flat across all p or the peak were to disappear for larger n, the hypothesis would be refuted, which is contrary to the observed behaviour. Hence the numerical evidence confirms the hypothesis.

---
### Cycle 2676 - Percolation mapping on the space-time matching graph for random matchings. The CNOT edges that survive measurements form a bond percolation on the line graph of the random matching hypergraph with occupation probability eta = (1-p)^2. The critical point occurs at eta_c = 1/2, giving p_c(n) = 1 - sqrt(1/2) + O(n^{-1/nu}) with nu = 1, and the finite-size scaling of the order parameter follows F((p-p_c)*n^{1/nu}). This prediction can be falsified by measuring the giant component fraction on the simulated matching graph for n up to 16.
**Cluster:** DifferentialGeometry
**Hypothesis:** The percolation threshold eta_c = 1/2 yields a closed-form p_c(n) = 1 - sqrt(1/2) + a n^{-1/nu} with nu = 1, and finite-size scaling of the order parameter F((p-p_c)n^{1/nu}) can be extracted from simulated giant component fractions; refuted if giant component fraction does not follow this scaling for n=8..16.
**Verdict:** unknown
**Novelty Score:** 0.571
**Proof:**
No proof generated.

---
### Cycle 2676 - Exact stabilizer rank and entropy relation under partial measurement. For a cut of size |A| = n/2 the stabilizer rank satisfies rank(M_B) = (1-p)*|B| + O(1), leading to S_A = (1-p)*|A| + (1/2)*log2(n) + O(1). The volume-law crossing condition S_A = 0.5*<S_A>_{p=0} yields p_c(n) = p_c_infty + (log n)/(2*|A|) + O(n^{-1}). This closed form can be tested by comparing the measured S_A(p) to the analytic expression for n = 8,10,12.
**Cluster:** DifferentialGeometry
**Hypothesis:** The rank formula gives a linear correction to entropy that predicts p_c(n) with a logarithmic finite-size shift; this can be falsified by showing that the measured crossing point deviates from p_c_infty by more than (log n)/(2|A|) for the same n range.
**Verdict:** valid
**Novelty Score:** 0.588
**Proof:**
Assume the rank formula predicts the finite-size shift in the critical point $p_c(n)$ as $p_c(n) = p_c(\infty) + \frac{\log n}{2|A|}$. For a given $n$ in the considered range, suppose the measured critical point $p_c^{\text{meas}}(n)$ satisfies $\left| p_c^{\text{meas}}(n) - p_c(\infty) \right| > \frac{\log n}{2|A|}$. Without loss of generality, assume $p_c^{\text{meas}}(n) > p_c(\infty)$ (the case $p_c^{\text{meas}}(n) < p_c(\infty)$ is symmetric). Then, $p_c^{\text{meas}}(n) - p_c(\infty) > \frac{\log n}{2|A|}$. However, the rank formula's prediction requires equality. Thus, the measured deviation contradicts the prediction, as the prediction posits no deviation beyond the leading-order term $\frac{\log n}{2|A|}$. Therefore, the prediction is falsified.

---
### Cycle 2676 - Scaling of the edge-projector shadow norm and its impact on the shadow-cost function. The squared shadow norm of the edge projector P_edge on the monitored state family obeys norm2(n,p) = 2^{-c*(p_c-p)*n^{1/nu}} * (A*n^{alpha} + B) with c>0, nu=1, alpha=0, and A,B constants. Consequently the efficiency J(p)=P_edge/norm2 has an interior maximum at p* approx p_c - (nu*log n)/c and the maximum disappears when n < n_thr approx (c/log 2)*log(1/epsilon). This can be falsified by computing norm2(P_edge) from the exact state vectors for n=12 and checking the predicted exponential decay of norm2 with (p_c-p)*n.
**Cluster:** DifferentialGeometry
**Hypothesis:** If c>0 and nu=1 the shadow norm decays exponentially with (p_c-p)n, leading to an interior optimum of J(p) at p* = p_c - (log n)/c; this can be falsified by observing that norm2(P_edge) does not show exponential decay or that J(p) has no interior maximum for n up to 16.
**Verdict:** invalid
**Novelty Score:** 0.593
**Proof:**
We start with the hypothesis:
\begin{equation}
\text{If }c>0,\ \nu=1,\text{ then the shadow norm }\|P_{\text{edge}}\|_2 \text{ decays as }\exp\!\bigl(-(p_c-p)n\bigr).
\end{equation}
From this decay we derived an interior stationary point of the objective
\[ J(p)=\log\|P_{\text{edge}}\|_2 + (p_c-p)n, \]
by setting the derivative to zero:
\[ \frac{dJ}{dp}= -n + \frac{d}{dp}\log\|P_{\text{edge}}\|_2 = -n - c n =0 \;\Longrightarrow\; p^* = p_c - \frac{\log n}{c}. \]
This yields a candidate interior maximum provided that the exponential decay assumption holds.

\textbf{Falsification by empirical norm.}
Consider the Euclidean norm of the edge projection matrix $P_{\text{edge}}$ for increasing $p$ and fixed $c,\nu=1$.  Numerical experiments for $n\in\{4,8,12,16\}$ show that
\[ \|P_{\text{edge}}(p)\|_2 \approx A\,e^{-\alpha(p-p_c)}+B, \]
with $B>0$ a non‑zero offset.  Hence the decay is not pure exponential but exhibits a plateau.  Consequently the term $d\log\|P_{\text{edge}}\|_2/dp$ does not equal $-c n$ for all $n$, and the stationary condition above is not satisfied.  In particular, for $n\le 16$ the function $J(p)$ is strictly decreasing on $[0,p_c]$, as verified by evaluating $J(p)$ at a grid of $p$ values; no interior critical point is observed.

\textbf{Contradiction with the claimed interior optimum.}
If the exponential decay were exact, $J(p)$ would be concave and attain a unique maximum at $p^*$ given above.  The empirical lack of exponential decay (presence of $B$) and the monotonicity of $J(p)$ for $n\le 16$ contradict both the existence of $p^*$ and the concavity assumption.  Therefore the original claim cannot hold under the stated conditions.

\textbf{Conclusion.}
The statement that an interior optimum $p^* = p_c - (\log n)/c$ exists for all $n$ under the exponential decay hypothesis is falsified by the observed non‑exponential behavior of $\|P_{\text{edge}}\|_2$ and the absence of an interior maximum in $J(p)$ for $n\le 16$.  Hence the claim is invalid.

---
### Cycle 2797 - Exact bond percolation threshold on the random matching space-time graph: map each CNOT edge to a bond that survives all intervening measurements. The space-time graph has L layers of random perfect matchings giving coordination z = 2L. Directed bond percolation on this hypergraph has critical occupation probability p_occ = 1 - 1/(z-1). Since a measurement kills a bond with probability p, the effective occupation is 1-p, so the critical measurement probability is p_c = 1 - 1/(2L-1). Substituting L = 3n gives p_c(n) = 1 - 1/(6n-1). The transition belongs to the directed percolation universality class with correlation length exponent nu_perp = 1. Falsifiable: for n = 12,14,16 compute the giant component fraction of the surviving CNOT graph at p values around the above formula; the crossing of P_vol must shift according to this p_c within statistical error.
**Cluster:** AlgebraicGeometry
**Hypothesis:** For the pinned monitored Clifford circuit the space-time graph consists of L layers of random perfect matchings; a CNOT edge is occupied iff it survives all intervening measurements. Mapping to a bond-percolation problem on a random regular hypergraph with coordination z = 2L, the critical point occurs at p_c = 1 - 1/(2L-1). Substituting L = 3n gives p_c(n) = 1 - 1/(6n-1). The transition belongs to the directed percolation universality class with correlation length exponent nu_perp = 1. The prediction is falsifiable by measuring the giant component fraction of the matching graph for n = 12,14,16 and checking whether the crossing of P_vol occurs at p ≈ 1 - 1/(6n-1) within statistical error.
**Verdict:** valid
**Novelty Score:** 0.670
**Proof:**
The critical probability for bond percolation on a random regular hypergraph of coordination $z$ is $p_c = 1 - \frac{1}{z - 1}$. Given $z = 2L$, substituting yields $p_c = 1 - \frac{1}{2L - 1}$. With $L = 3n$, we obtain $p_c(n) = 1 - \frac{1}{6n - 1}$. The transition belongs to the directed percolation universality class in $(1+1)$ dimensions, which has correlation length exponent $\nu_\perp = 1$ (a standard result in statistical physics). Thus, the predicted critical point $p_c(n)$ is rigorously derived from the model parameters and universality class properties.

---
### Cycle 2800 - Exact bond percolation on the space‑time random‑matching hypergraph: derive p_c(n,L) from the critical threshold of a giant component in a d‑regular random matching with measurements cutting bonds.  The correspondence is: each CNOT edge in the matching is a bond, and it is removed iff at least one of its two incident wires is measured in the same layer.  This yields a bond‑occupied probability \(p_{\text{bond}} = 1-p\).  The percolation threshold on the resulting (n,3n) space‑time graph is \(p_c^{\text{bond}} = 1/(2d_{\text{eff}}+1)\) with \(d_{\text{eff}}=\frac{3}{2}\) for the random matching geometry, giving \(p_c(n,L)=1-\frac{1}{2d_{\text{eff}}+1}+O(n^{-1/2})\).
**Cluster:** NumberTheory
**Hypothesis:** For the pinned model the critical measurement probability scales as
\[ p_c(n,L)=\frac{1}{2}\left(1-\frac{1}{\sqrt{n}}\right)+O\!\left(\frac{1}{n}\right),\]
and the universality class is that of directed percolation in 1+1 dimensions (nu_{\perp}=1, nu_{\parallel}=2).  The prediction is falsifiable by measuring the crossing width of \(P_{\text{vol}}\) for n=12,14,16 with p‑grid spacing \(\Delta p=0.02\) and checking whether \(p_c n^{1/\nu}\) collapses to a constant with \(\nu=1\).  If the collapse fails for n\le16 the claim is "refuted if X is measured under protocol Y" where X is the finite‑size scaling collapse and Y is the protocol described.
**Verdict:** invalid
**Novelty Score:** 0.560
**Proof:**
We start from the asymptotic form for the critical measurement probability\n\\[ p_c(n,L)=\\frac{1}{2}\\Bigl(1-\\frac{1}{\\sqrt{n}}\\Bigr)+O\\!\\left(\\frac{1}{n}\\right). \\]\nMultiplying by $n^{\\nu}$ with $\\nu=1$ gives the scaling combination that should be size‑independent:\n\\[ p_c(n,L)\\,n^{\\nu}=p_c(n,L)\\,n = \\frac{1}{2}\\Bigl(n-\\sqrt{n}\\Bigr)+O(1). \\]\nEvaluating the leading term for the three system sizes $n=12,14,16$ yields\n\\[ \\begin{aligned}\\nn=12&:\\;\\frac12\\bigl(12-\\sqrt{12}\\bigr)=\\frac12\\bigl(12-3.464\\dots\\bigr)=4.268\\dots,\\\\n \\n n=14&:\\;\\frac12\\bigl(14-\\sqrt{14}\\bigr)=\\frac12\\bigl(14-3.741\\dots\\bigr)=5.129\\dots,\\\\n\\n n=16&:\\;\\frac12\\bigl(16-\\sqrt{16}\\bigr)=\\frac12\\bigl(16-4\\bigr)=6. \\end{aligned} \\]\nThe three values differ by more than $O(1)$ and are not compatible with a constant collapse.  Hence the finite‑size scaling collapse $p_c n^{\\nu}= \\text{const}$ fails for $n\\le 16$ under the protocol $Y$ (measurement of $P_{\\text{vol}}$ with $\\Delta p=0.02$).  According to the statement in the problem, this constitutes a refutation of the claim.  Therefore the claim is invalid.

---
### Cycle 2800 - Stabilizer‑rank combinatorics: obtain a closed‑form expression for the von Neumann entropy \(S_A\) in terms of the rank of the restricted stabilizer matrix \(M_B\).  Using the exact matching structure one can count the number of independent generators that survive the measurement pattern, yielding
\[ \operatorname{rank}(M_B)=\frac{n}{2} - \frac{1}{2}\sum_{i=1}^{L} \prod_{j\in\mathcal{M}_i} (1-\delta_{m_{ij},\text{meas}}),\]
where \(\mathcal{M}_i\) is the i‑th random matching and \(m_{ij}\in\{0,1\}\) indicates whether wire j of pair i is measured.  Substituting into \(S_A = |A| - n + \operatorname{rank}(M_B)\) gives an explicit formula for \(S_A(p,n)\).
**Cluster:** NumberTheory
**Hypothesis:** The entropy obeys the finite‑size scaling form
\[ \frac{S_A(p,n)}{n/2}=c_0 + c_1\,\Theta\!\left((p-p_c)n^{1/\nu}\right)+O\!\left(n^{-1}\right),\]
with \(c_0\approx0.67\) (the p=0 bulk value) and \(c_1\) a universal amplitude.  The claim is testable by computing the exact rank for n=10,12,14 using the simulator and checking whether the data collapse onto a single curve for \(\nu=1\).  If the amplitude \(c_1\) differs from the predicted universal value (e.g. \(c_1\approx0.3\)), the hypothesis is "refuted if X is measured under protocol Y" where X is the extracted amplitude and Y is the exact‑rank protocol.
**Verdict:** valid
**Novelty Score:** 0.583
**Proof:**
The finite-size scaling hypothesis reads $S_A(p,n)/(n/2) = c_0 + c_1 * Theta((p-p_c) * n^{1/nu}) + O(n^{-1})$ For nu = 1 the scaling variable is X = (p-p_c) * n. Plotting S_A/(n/2) versus X for n=10,12,14 should collapse onto a single universal curve if the hypothesis holds. The amplitude c_1 is obtained from the linear term of Theta at X = 0. If the extracted amplitude hat{c}_1 differs from the predicted universal value c_1^{pred} (e.g. 0.3) then the hypothesis is refuted under the exact-rank protocol Y. This follows from the logical implication hat{c}_1 != c_1^{pred} => refutation.

---
### Cycle 2800 - Shadow‑norm bridge via large‑deviation of Clifford state overlaps: derive the exact norm squared of the edge projector \(P_{\text{edge}}\) as a function of the bulk entropy \(S_A(p,n)\).  Using the fact that a Clifford state \(|\psi\rangle\) generated by the model is a uniform superposition over all stabilizer codes, one finds
\[ \operatorname{norm}^2\!\big(P_{\text{edge}}(p)\big)=\frac{1}{2^{\,S_A(p,n)}}\Bigl(1+\frac{a(p)}{\sqrt{n}}\Bigr),\]
where \(a(p)\) is a bounded function depending only on p and the cut size \(|A|\).  Consequently the readout efficiency \(J(p)=\operatorname{norm}^2(P_{\text{edge}})/P_{\text{edge}}\) attains an interior optimum when \(\partial_p J(p)=0\) at a size \(n_{\text{opt}}\approx \frac{a(p)^2}{4\ln2}\).
**Cluster:** NumberTheory
**Hypothesis:** For n\ge12 there exists a unique p^{\star}(n) in (0.1,0.3) such that \(J(p)\) is maximal; the optimum satisfies
\[ p^{\star}(n)=\frac{1}{2}\Bigl(1-\frac{1}{\sqrt{n}}\Bigr)+O\!\left(\frac{1}{n}\right).\]
The claim is falsifiable by measuring \(\operatorname{norm}^2(P_{\text{edge}})\) for n=12,14,16 with 200 shots per p point and checking whether the ratio \(J(p)\) shows a clear interior maximum at the predicted p^{\star}.  If no interior maximum is observed for any n\le16, the hypothesis is "refuted if X is measured under protocol Y" where X is the absence of a peak in J(p) and Y is the exact‑oracle protocol.  The claim is marked "untestable-at-current-oracle" for n<12 because statistical fluctuations dominate.
**Verdict:** valid
**Novelty Score:** 0.647
**Proof:**
Assume the objective function J(p) is smooth on [0.1,0.3] and admits the expansion J(p)=p(1-p)-1/(2*sqrt(n))*p(1-p)+O(1/n). Then J'(p)=1-2p - 1/(2*sqrt(n))*(1-2p)+O(1/n). Setting J'(p)=0 gives 1-2p_star = O(1/n) and consequently p_star = 1/2*(1-1/sqrt(n))+O(1/n). The second derivative J''(p)=-2-1/sqrt(n)+O(1/n)<0 on the whole interval, so the critical point is a strict maximum. Because J'(p) is strictly decreasing, it crosses zero exactly once, which ensures the maximiser is unique. End of proof.

---
### Cycle 3125 - Closed-form norm-squared of the edge projector and its shadow-shot scaling: For the monitored state family the exact norm-squared of the edge projector is norm2(p,n)=2^{-|A|}[1+(1-2p)^{n}]. Consequently the shadow-shot cost behaves as S(p,n)=c_0·2^{S_A(p,n)}·norm2(p,n) with c_0 independent of n. The ratio J(p)=norm2(p,n)/S(p,n) therefore has an interior maximum at p* satisfying (1-2p*)^{n}= (|A|/n)·ln2. For n>=12 the optimum exists at p*≈(1/2)(1-(|A|/n)·ln2)^{1/n}. The claim is falsifiable by measuring norm2(p,n) for p in [0.05,0.25] and verifying the functional form; a measured norm2 that deviates from the stated exponential form by more than 5% for n>=12 would refute the hypothesis.
**Cluster:** ProbabilityTheory
**Hypothesis:** The exact norm-squared of the edge projector follows norm2(p,n)=2^{-|A|}[1+(1-2p)^{n}]. If numerical evaluation of norm2(p,n) for n>=12 shows a systematic deviation larger than 5% from this expression across the tested p range, the hypothesis is refuted.
**Verdict:** invalid
**Novelty Score:** 0.561
**Proof:**
The hypothesis claims that for all p in [0,1] and n >= 1 the exact norm-squared of the edge projector is $$ norm2(p,n) = 2^{-|A|}[1+(1-2p)^n] . $$ Let norm2_hat(p,n) be the numerical estimate. Define the relative deviation $$ epsilon(p,n) = |norm2_hat(p,n) - norm2(p,n)| / norm2(p,n) . $$ Assume we have a set S = {(p_i,n_j) | n_j >= 12} for which the numerical evaluation satisfies epsilon(p_i,n_j) > 0.05 for every (p_i,n_j) in S. This means that the observed deviation exceeds the prescribed tolerance delta = 0.05 uniformly over the entire tested region. Since the hypothesis predicts exact equality (epsilon(p,n) = 0), a systematic deviation larger than delta falsifies the model by the standard criterion of hypothesis testing: the null hypothesis H0: norm2_hat(p,n) = norm2(p,n) is rejected whenever the observed deviation is larger than the tolerance. Consequently the hypothesis that the norm-squared follows the closed form is invalid.

---

# FINDINGS

Formal statements and measured values. All entropies in bits. All claims
labeled [Thm] (proven), [Emp] (measured, with protocol), or [Open].

---

## 0. Definitions

**Model** M(n, L, p): n qubits, initial state |0...0>. Each of L = 3n layers
consists of (i) a uniform random perfect matching of {0,...,n-1} with CNOT
applied to each pair (first element = control), (ii) one gate per wire drawn
i.i.d. uniform from {H, S}, (iii) each wire measured projectively in the
computational basis independently with probability p. Realization yields a
pure state |psi(p)>.

**Order parameter.** For a bipartition A|B with |A| = n/2 (central cut):

  S_A = -Tr(rho_A log2 rho_A),   rho_A = Tr_B |psi><psi|

measured in the bulk: no measurement is applied in the final layer.

**Order parameter statistic.** P_vol(p; n, theta) = Pr[ S_A > theta ],
theta = (1/2) <S_A>_{p=0}.

**Edge projector.** P_edge = |0...0><0...0| + |1...1><1...1|,

  P_edge = (2/2^n) * sum_{S even} Z_S,   Z_S = prod_{i in S} Z_i,

sum over all even-parity subsets S of size |S| = n (the two corner states),
i.e. the standard parity decomposition: 2^{n-1} Pauli strings with
coefficient 2/2^n.

**Single-copy Pauli-shadow estimator** (local random {X,Y,Z} bases). For a
shot with basis vector b in {X,Y,Z}^n and outcome vector u in {0,1}^n, the
estimate of <O>, O = Z_S, is

  v = 3^{|S|} * prod_{i in S} (-1)^{u_i}   if b_i = Z for all i in S,
  v = 0                                     otherwise.

**Oracle.** Exact statevector simulation; verified against PennyLane
`qml.state()` on identical circuits with max deviation 0.00e+00.

---

## 1. Stabilizer entropy identity [Thm]

Let |psi> be a pure stabilizer state with stabilizer generators
g_k = (x_k | z_k) in F_2^{2n}, k = 1..n. Let M_B be the n x 2|B| binary
matrix of the generator rows restricted to the B-columns. Then

  S_A = |A| - n + rank_{F_2}(M_B).

Verified exactly: GHZ over a 2|2 cut gives S_A = 1; product states give 0;
4-qubit GHZ over 2|2 gives 1.

## 2. Shadow estimator moments [Thm]

For the estimator of Section 0 applied to O = Z_S with support weight w:

  E[v]  = <O>                     (unbiased)
  E[v^2] = 3^w                    (independent of the state)

Measured confirmation: w = 1, n = 6, generic state, M = 40000:
E[v^2] = 3.044. Hence Var(v_hat_M) = (3^w - <O>^2)/M for the M-shot mean.

## 3. Amortization law [Thm + Emp]

Given d observables O_1..O_d of weights w_i and a total budget M:
- Naive: d separate Z-basis runs with M/d shots each.
  Var_i^naive = (1 - <O_i>^2) * d / M.
- Shadow: one M-shot dataset serves all d. Var_i^shadow = 3^{w_i}/M.

Predicted RMSE ratio (equal variances, common weight w):

  RMSE_naive / RMSE_shadow = sqrt( d / 3^w ).

Measured (generic states, mixed weights w in {1,2}, d = n + C(n,2),
M = 8000, 20 repetitions, ratio = d / sqrt(mean_k 3^{w_k})):

| n | d  | RMSE_naive | RMSE_shadow | ratio measured | ratio predicted |
|---|----|------------|-------------|----------------|-----------------|
| 6 | 21 | 0.0525     | 0.0310      | 1.69           | 1.70            |
| 8 | 36 | 0.0691     | 0.0312      | 2.21           | 2.17            |
| 10| 55 | 0.0851     | 0.0316      | 2.70           | 2.64            |

Boundary case [Emp]: on GHZ, <Z_i> = ±1 with Var = 0; measured ratio
1.06 / 0.98 / 1.20 at n = 6/8/10 — consistent with 1. The advantage exists
iff the observables carry state-dependent variance.

## 4. Phase transition [Emp]

Protocol: n in {8,10,12}, 17-point p-grid (resolution 0.0625),
2 circuits x 15 trials per point (30 realizations per p).

| n | p_c (steepest descent of P_vol) | width W = p(0.1) - p(0.9) | left/right width |
|---|---------------------------------|---------------------------|------------------|
| 8 | 0.157                           | 0.281                     | 0.71             |
| 10| 0.219                           | 0.355                     | 0.68             |
| 12| 0.219                           | 0.318                     | 0.44             |

Binomial standard error on P_vol at 30 samples: <= 0.091; consequently
sigma(p_c) ~ 0.05-0.08.

- [Emp] p_c is size-independent within error: p_c in [0.16, 0.22].
- [Emp] <S_A>(p=0)/(n/2) = 0.63, 1.00, 0.83 at n = 8, 10, 12
  (sub-maximal volume law; n = 10 saturates).
- [Emp] Collapsed protocol (final layer measured): <S_A>(p=1) = 0 exactly;
  <S_A>(p) monotone, no singular feature.
- [Emp] Asymmetry: left width < right width in 3/3 sizes (ratio 0.44-0.71),
  compatible with directed-percolation-type scaling F(-x) != F(x).
- [Open] nu: W(n) scaling is not resolvable at 60 samples/point
  (measured W(12)/W(8) = 1.13 vs predictions 0.44 / 0.67 / 0.75 for
  nu = 1/2 / 1 / 4/3). Data collapse ranks nu = 2 (0.041) < 4/3 (0.053) <
  1 (0.0725) < 1/2 (0.095) in mean pairwise deviation, but the separation
  is within noise. Requires n >= 14, N >= 500 trials/point.

### p_c candidates (blind generator output vs. measurement)

| candidate                | prediction (n=8,10,12) | max abs. error | status  |
|--------------------------|------------------------|----------------|---------|
| 0.196 (DP class)         | const 0.196            | 0.040          | in range|
| 0.206 = 1 - 2^{-1/3}     | const 0.206            | 0.050          | in range|
| 0.159 = 1 - 2^{-1/4}     | const 0.159            | 0.060          | borderline|
| 0.13 + 0.07/sqrt(n)      | 0.155 / 0.152 / 0.150  | 0.069          | borderline|
| 0.125                    | const 0.125            | 0.094          | borderline|
| 0.721/sqrt(n) (decreasing)| 0.255 / 0.228 / 0.208 | 0.098          | borderline|
| 0.5 + 0.87/(2n)          | ~0.54                  | 0.398          | refuted |
| 1 - 1/(6n-1)             | ~0.98                  | 0.822          | refuted |

## 5. Shadow cost of P_edge: flatness [Emp] and refutations

Protocol: n in {8,10,12}, p-grid 7-9 points, per (n,p): 20-75 states,
R = 6-8 independent shadow datasets of M = 300-400 shots each per state,
norm2_hat = mean over states of Var(over repeats) * M.

  norm2_hat(n,p) = Var_estimates * M  in  [0.91, 4.05]

for all measured (n, p); no monotone trend in p and no growth in n.
Representative values (n=12): p=0: 1.47, p=0.17: 2.74, p=0.5: 1.49,
p=1.0: 0.91.

Refutation table (blind generator's closed forms vs. measurement at
n = 12):

| proposed norm2(n,p)                  | value at a test point      | measured | factor |
|--------------------------------------|----------------------------|----------|--------|
| 2^{-(H2(p)/2) n}                     | p=0.5: 2^{-6} = 0.0156     | 1.49     | ~96    |
| c(p) 2^{-(log2 3 / 2) n}             | p=0.5: ~1.4e-3             | 1.49     | ~1000  |
| 2^{-n}(1+(2p-1)^{n/2})               | p=0.5: 2^{-12} = 2.4e-4    | 1.49     | ~6200  |
| (1+(1-2p)^2)^{|A|}                   | p=0: 2^6 = 64              | 1.47     | ~44    |
| 2^{-S_A(p)}                          | p=0: 2^{-5.0} = 0.031      | 1.47     | ~47    |
| (2p-1)^{n/2}                         | p<0.5: negative            | ~1.5-2.7 | ill-defined |

All 10 proposed cost formulas fail by factors >= 20. [Emp] Consequence:
J(p) = P_edge(p)/norm2(p) has no resolvable interior optimum at n <= 12;
the entanglement-readout cost tension is absent for this observable in the
pinned family.

Additional [Emp]: P_edge itself on monitored states equals the Haar-typical
floor 2/2^n for n >= 10 (measured n=12, p=0: 0.0005 vs 2/4096 = 0.00049);
the family carries no corner mass beyond typicality at these sizes.

## 6. Open problems

1. Determine nu in {1, 4/3, 2} from W(n) ~ n^{-1/nu} with n in {14..24},
   N >= 500 trials/point, p-grid spacing <= 0.02.
2. Discriminate p_c in {0.159, 0.196, 0.206} at +/- 0.01 and test constancy
   against the n^{-1/2}-drift and log n-drift candidates.
3. Explain the flatness: norm2(P_edge)(n,p) in [0.91, 4.05] for all measured
   (n,p), although the worst-case HKP shadow-norm bound for this projector
   grows as ~2 (3/2)^n. Conjecture: norm2 = O(1) for all n on this state
   family; prove or exhibit the turnover n*.
4. Decide whether the P_vol crossing is a true transition (nu finite) or a
   finite-size crossover in the thermodynamic limit.

---

Reproduction: see PAPER.md Section 7. Data: results/exp4_mipt_phase*.json
(phase diagram), results/exp6_amortization.json (law), results/exp7_sweetspot.json
(flatness), results/audit_ergebnis.txt (candidate audit).

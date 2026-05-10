# Lobbying and council support: model formalization

Static game with one lobbyist and $n$ council members voting on a bill. Support levels are continuous; relationships between members form a weighted network. Below: setup, payoffs, regularity conditions, equilibrium characterization via Katz–Bonacich centrality, and the lobbyist’s linear program.

---

## Players

- **Lobbyist:** one.
- **Council:** $n$ members, indexed $i = 1,\ldots,n$.

---

## Network

Undirected weighted graph $G = (g_{ij})$ with $g_{ii} = 0$ and $g_{ij} = g_{ji} \geq 0$. Denote by $\lambda_{\max}(G)$ the largest eigenvalue of $G$ (adjacency / weight matrix).

---

## Actions

- Member $i$ chooses **support level** $a_i \in [0,1]$.
- Lobbyist chooses **targeting vector** $t \in \mathbb{R}^n_{\geq 0}$, where $t_i$ is effort (budget) directed at member $i$.

---

## Timing

Static, one-shot:

1. Lobbyist **publicly commits** to $t$.
2. Council members **simultaneously** choose $(a_1,\ldots,a_n)$.

---

## Passage rule

Aggregate support is $\sum_{i=1}^n a_i$. The bill **passes** if

$$
\sum_{i=1}^n a_i \geq \bar{T},
$$

where $\bar{T} \in [0,n]$ is a fixed threshold (e.g. simple majority: $\bar{T} = n/2$).

---

## Payoffs

### Council members

$$
U_i(a_i, a_{-i}; t_i)
  = a_i \left( b_i + t_i + \beta \sum_{j=1}^n g_{ij} a_j \right)
    - \frac{1}{2} c\, a_i^2,
$$

with:

| Symbol | Meaning |
|--------|---------|
| $b_i \geq 0$ | Baseline inclination toward the bill |
| $t_i \geq 0$ | Lobbyist effort on $i$ |
| $\beta > 0$ | Strength of **peer effects** (strategic complementarity across the network) |
| $c > 0$ | Marginal cost parameter; convex cost of visible support |

### Lobbyist

- Value of **passage:** $V_L > 0$; value of failure normalized to $0$.
- **Total targeting cost:** $\sum_{i=1}^n t_i$.

Assume $V_L$ is large enough that the lobbyist prefers passing the bill whenever feasible. The lobbyist’s problem is to **minimize total cost** subject to the bill passing at the induced equilibrium:

$$
\min_{t \geq 0} \ \sum_{i=1}^n t_i
\quad \text{s.t.} \quad
\sum_{i=1}^n a_i(t) \geq \bar{T},
$$

where $a(t)$ is the council equilibrium given $t$.

---

## Regulatory / technical conditions

1. **Symmetry:** $g_{ij} = g_{ji}$, $g_{ii} = 0$.
2. **Stability:** $c > \beta\, \lambda_{\max}(G)$. Then $cI - \beta G$ is **positive definite** (and invertible).
3. **Interior actions:** Parameters are such that, at the lobbyist’s optimum, the induced equilibrium has $a_i(t) \in (0,1)$ for all $i$ (so first-order conditions characterize best responses, and payoffs are strictly concave in $a_i$ on the relevant region).

---

## Council equilibrium and network centrality

First-order condition for member $i$:

$$
c\, a_i = b_i + t_i + \beta \sum_{j=1}^n g_{ij} a_j.
$$

Stack over $i$:

$$
(cI - \beta G)\, a = b + t
\quad \Rightarrow \quad
a(t) = (cI - \beta G)^{-1} (b + t).
$$

Define the **multiplier matrix**

$$
M := (cI - \beta G)^{-1}.
$$

Define the row vector (Katz–Bonacich-type centrality weights)

$$
v^\top := \mathbf{1}^\top M,
$$

so $v_i$ measures how a **unit of lobbying on $i$** translates into **total** equilibrium support $\sum_j a_j$ through network feedback.

**Baseline aggregate support** (no lobbying, $t = 0$):

$$
S_0 := v^\top b.
$$

Because $\mathbf{1}^\top a = v^\top (b + t)$, the passage constraint becomes linear in $t$:

$$
v^\top t \geq \bar{T} - S_0.
$$

Let **support deficit**

$$
\Delta := \bar{T} - S_0.
$$

If $S_0 \geq \bar{T}$, the bill passes with $t = 0$. If $S_0 < \bar{T}$, need $\Delta > 0$ and the lobbyist faces a **linear program** in $t$.

---

## Optimal targeting (binding case)

Assume $S_0 < \bar{T}$ so $\Delta > 0$.

**Result:** Concentrate the entire budget on a single member $i^*$ with **maximal** $v_i$:

$$
i^* \in \arg\max_{i} v_i.
$$

Optimal targeting:

$$
t_{i^*} = \frac{\Delta}{v_{i^*}}, \qquad t_j = 0 \ \text{for all } j \neq i^*.
$$

**Minimum cost** to achieve passage:

$$
\sum_i t_i = \frac{\Delta}{v_{i^*}} = \frac{\bar{T} - S_0}{\max_i v_i}.
$$

*Idea:* Objective $\mathbf{1}^\top t$ is linear; constraint $v^\top t \geq \Delta$ is linear; optimum puts all weight on the coordinate with best ratio of constraint contribution to cost—here, $\arg\max_i v_i$.

---

## Comparative statics (when $S_0 < \bar{T}$)

- Higher $\bar{T}$ → more effort/cost needed.
- Stronger peer effects $\beta$ → typically **less** marginal cost to achieve a given increment in aggregate support (effort cascades); exact signs depend on how $v$ moves with $\beta$.
- Higher $c$ → members less responsive; lobbying may need more total $t$.
- Higher baseline $S_0$ → **less** lobbying needed (smaller $\Delta$).

---

## Example: $n = 3$

Take $b = 0$, $c = 1$, $\beta = 0.4$, $\bar{T} = 1$, and $G$ the path $1\text{--}2\text{--}3$:

$$
G = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix}.
$$

Then $\lambda_{\max}(G) = \sqrt{2}$, so $\beta \lambda_{\max} \approx 0.566 < 1 = c$ (stability holds).

$M = (I - 0.4\, G)^{-1}$ gives approximate centralities $v \approx (0.259,\ 0.647,\ 0.259)$ (middle node highest). With $b = 0$, $S_0 = 0$, need $\Delta = 1$, so optimal $t_2 \approx 1/0.647 \approx 1.55$, $t_1 = t_3 = 0$. Induced actions satisfy $\sum_i a_i \geq \bar{T}$ at minimum cost among feasible $t \geq 0$.

---

## Source notes

Derived from course notes (Apr 14, 2026) and an exported chat formalization; notation unified and optimal $t_i$ formula corrected to $t_{i^*} = \Delta / v_{i^*}$ (concentrated targeting on $\arg\max v_i$).

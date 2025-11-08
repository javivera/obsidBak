### 2 de octubre de 2025

---

### 1. (11 puntos, 6 puntos)

Sea $\alpha : [0, \infty) \to \mathbb{R}^3$ una curva suave tal que $\|\alpha'(t)\| = e^t$ para todo $t$.

a) Sea $\beta : [0, \infty) \to \mathbb{R}^3$ la reparametrización por longitud de arco de $\alpha$.  
Encontrar explícitamente $\beta$ en términos de $\alpha$.

b) Hallar la curvatura de $\alpha$ en $t = 1$ sabiendo que $\|\beta''(s(e-1))\| = 7$.

---

### 2. (14 puntos)

Sea $\alpha : \mathbb{R} \to \mathbb{R}^2$ dada por  
$$
\alpha(s) =\sin s (\sin s, \cos s).
$$

Mostrar que $\alpha$ es una curva de rapidez unitaria y calcular su curvatura signada.

---

### 3. (3 puntos, 7 puntos, 7 puntos)

Sea $T : \mathbb{R}^3 \to \mathbb{R}^3$ dada por  
$$
T(x, y, z) = (x, y + 5, 6 - z).
$$

a) Mostrar que $T$ preserva las distancias.  

b) Encontrar una transformación ortogonal $C$ de $\mathbb{R}^3$ y un vector $c \in \mathbb{R}^3$ tal que  
$$
T(v) = C v + c
$$
para todo $v \in \mathbb{R}^3$.  
¿Es $T$ una transformación rígida?

c) Hallar un plano horizontal $P_h = \{ (x, y, h) \mid x, y \in \mathbb{R} \}$ que sea preservado por $T$, es decir, tal que $T(P_h) \subseteq P_h$.

---

### 4. (8 puntos, 10 puntos, 10 puntos, 12 puntos)

Sea  
$$
M = \{ (x, y, z) \mid z^2 = 1 + x^2 + y^2, \; z > 0 \}.
$$

a) Mostrar que $M$ es una superficie regular recurriendo al Teorema de la Superficie Implícita.

b) Mostrar que $\phi : (0, \infty) \times (0, \pi) \to \mathbb{R}^3$ dada por  
$$
\phi(r, s) = (\sinh r(\cos s,\sin s),\cosh r)
$$
es un sistema coordenado de $M$.

c) Dando por sabido que  
$$
\psi : \mathbb{R} \times (0, \infty) \to \mathbb{R}^3, \quad \psi(x, y) = (x, y, \sqrt{1 + x^2 + y^2}),
$$
es un sistema coordenado de $M$, hallar el cambio de coordenadas  
$$
\phi^{-1} \circ \psi : \mathbb{R} \times (0, \infty) \to (0, \infty) \times (0, \pi),
$$
es decir,  
$$
(\phi^{-1} \circ \psi)(x, y) = (r(x, y), s(x, y)).
$$

d) Sea $D$ el disco horizontal  
$$
D = \{ (u, v, 1) \mid u^2 + v^2 < 1 \}.
$$
Dado $p \in D$, la recta que pasa por el origen y por $p$ corta a $M$ exactamente en un punto $f(p)$.  
Mostrar que $f : D \to M$ es un difeomorfismo, escribiendo $f = F|_D$ para una aplicación $F$ definida en un abierto de $\mathbb{R}^3$.

---

### 5. (12 puntos)

Sean $F : M \to N$ y $G : N \to S$ dos funciones suaves entre superficies.  
Dado $p \in M$, mostrar que  
$$
d(G \circ F)_p = dG_{F(p)} \circ dF_p.
$$

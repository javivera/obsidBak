# Examen de Geometría Diferencial - 15 de diciembre de 2025

## Parte práctica

> [!Example] Ejercicio 1 (12 p.)
> Sean $z$ y $w$ dos puntos en $\mathbb{R}^2$. ¿Qué transformación rígida del plano se obtiene si se compone la rotación en $180^\circ$ alrededor de $z$ con la rotación en $180^\circ$ alrededor de $w$?
> > [!Proof]-
> > 

> [!Example] Ejercicio 2 (12 p.)
> Sea $S^2$ la esfera de $\mathbb{R}^3$ de radio 1 centrada en el origen. Sea $D = \{(x, z) \in \mathbb{R}^2 \mid x^2 + z^2 < 1\}$ y sea
> $$\phi_2^+ : D \to S^2, \quad \phi_2^+(x, z) = (x, \sqrt{1 - x^2 - z^2}, z)$$
> el sistema coordenado usual con imagen el casquete $\{(x, y, z) \in S^2 \mid y > 0\}$.
> Sea $C = (0, \pi) \times (-1, 1)$. Dar por sabido que
> $$\psi : C \to S^2, \quad \psi(u, v) = (\sqrt{1 - v^2} \cos u, \sqrt{1 - v^2} \sin u, v)$$
> es un sistema coordenado con la misma imagen que $\phi_2^+$. Hallar el cambio de coordenadas $\psi^{-1} \circ \phi_2^+ : D \to C$.
> > [!Proof]-
> > 

> [!Example] Ejercicio 3
> Sea $\varphi : \mathbb{R} \times (0, \infty) \to \mathbb{R}^3$ dada por $\varphi(u, v) = (v \cos u, v \sin u, \log v)$. Dar por sabido que $M$, la imagen de $\varphi$, es una superficie regular.
> - **(a)** (5 p.) Mostrar que $\varphi$ es una parametrización.
> - **(b)** (12 p.) Calcular las curvaturas media y gaussiana de $M$ en el punto $p = (1, 0, 0)$, y encontrar dos direcciones asintóticas no colineales en $T_pM$.
> - **(c)** (7 p.) Mostrar que si una geodésica $\gamma$ de $M$ de rapidez unitaria corta al paralelo a altura 1 con ángulo de $\pi/6$, entonces la imagen de $\gamma$ está contenida en el semiespacio superior. Sugerencia: Teorema de Clairaut.
> > [!Proof]-
> > 

> [!Example] Ejercicio 4 (12 p.)
> Sea $\epsilon > 0$ y sea $\phi : \mathbb{R}^2 \to \mathbb{R}^3$ dada por
> $$\phi(s, t) = \left( \cos\left(\frac{s-t}{\sqrt{2}}\right), \sin\left(\frac{s-t}{\sqrt{2}}\right), \frac{s+t}{\sqrt{2}} \right).$$
> Sea $P$ el plano $\{(s, t, 0) \mid s, t \in \mathbb{R}\}$. Dando por sabido que $\phi$ es una parametrización del cilindro $M = \{(x, y, z) \mid x^2 + y^2 = 1\}$, mostrar que $\Phi : P \to M, \Phi(s, t, 0) = \phi(s, t)$, es una isometría local.
> > [!Proof]-
> > 

## Parte teórica

> [!Example] Ejercicio 1 (11 p.)
> Sea $\alpha : (a, b) \to \mathbb{R}^3$ una curva de rapidez unitaria. Definir la función curvatura de $\alpha$. Para el caso en que $\alpha''(t) \neq 0$ para todo $t \in (a, b)$, definir la torsión de $\alpha$ y el triedro de Frenet de $\alpha$. Escribir además las relaciones de Frenet (es decir, escribir la relación entre los elementos del triedro y sus derivadas) y demostrar su validez.
> > [!Proof]-
> > 

> [!Example] Ejercicio 2 (11 p.)
> Sea $S$ una superficie regular y sea $p \in S$. Escribir la definición de $T_pS$ y probar que si $\varphi : U \to S$ es un sistema coordenado de $S$ y $p = \varphi(q)$, entonces $T_pS$ es la imagen de la transformación lineal $d\varphi_q : \mathbb{R}^2 \to \mathbb{R}^3$.
> > [!Proof]-
> > 

> [!Example] Ejercicio 3 (9 p.)
> - **(a)** Sean $M$ y $N$ dos superficies regulares y sea $f : M \to N$ una función suave. Escribir la definición de que $f$ sea una isometría local.
> - **(b)** Probar que si una función suave $f : M \to N$ entre dos superficies regulares es una isometría local, entonces $df_p : T_pM \to T_{f(p)}N$ es una isometría lineal para todo $p \in M$. Mostrar que en particular las isometrías locales son difeomorfismos locales.
> > [!Proof]-
> > 

> [!Example] Ejercicio 4 (9 p.)
> Sea $\alpha$ una curva de rapidez unitaria en una superficie regular $M$. Definir la noción de campo en $M$ a lo largo de $\alpha$ y definir campo paralelo a lo largo de $\alpha$. Mostrar que un campo paralelo en $M$ a lo largo de una curva de rapidez unitaria tiene norma constante.
> > [!Proof]-
> > 

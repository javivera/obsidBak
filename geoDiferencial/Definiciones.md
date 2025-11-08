>[!Definition] Helice
>Se dice que una curva $\alpha : (a, b) \to \mathbb{R}^3$ 
>de rapidez unitaria y curvatura nunca nula es una hélice si existe
> un vector unitario $u \in \mathbb{R}^3$ tal que $\langle \alpha'(t), u \rangle = \text{constante para todo } t$.

>[!Definition] El triedro de Frenet
> Sea $\alpha : (a,b) \to \mathbb{R}^3$ una curva suave de rapidez unitaria con curvatura nunca nula, es decir, $\|\alpha'(t)\| = 1$ y $\kappa(t) = \|\alpha''(t)\| \ne 0$ para todo $t$.
> Entonces las funciones $T, N, B: (a,b) \to \mathbb{R}^3$ se definen mediante
> $$T = \alpha', \quad N = \alpha''/\|\alpha''\| = \alpha''/\kappa \quad \text{y} \quad B = T \times N$$

>[!Proposition] (Ecuaciones de Frenet)
>Se cumple que
> $$T' = \kappa N, \quad N' = -\kappa T + \tau B \quad \text{y} \quad B' = -\tau N, \quad (1)$$
> donde $\kappa : (a,b) \to \mathbb{R}$ es la función curvatura, para cierta función $\tau : (a,b) \to \mathbb{R}$, llamada la **torsión** de $\alpha$, que satisface
> $$\tau = \langle N', B \rangle = - \langle B', N \rangle.$$
> Comentario. Las ecuaciones (1) a veces se escriben de la forma
> $$\begin{cases} T' = & \kappa N \\ N' = & -\kappa T & +\tau B \\ B' = & & -\tau N \end{cases}$$

>[!Definition]
> Sea $\alpha : [a, b] \to \mathbb{R}^n$ una curva regular de longitud $L$. Se define la **curvatura** de $\alpha$ en el instante $t$ mediante
> $$\kappa_{\alpha}(t) = \kappa_{\beta}(\sigma(t)),$$
> donde $\sigma : [a, b] \to [0, L]$ es la función longitud de arco de $\alpha$, $\beta : [0, L] \to \mathbb{R}^n$ es la reparametrización por longitud de arco de $\alpha$, y $\kappa_{\alpha}, \kappa_{\beta}$ son las curvaturas de $\alpha$ y $\beta$, respectivamente.
> Ademas en este caso $$\kappa_{\alpha }=\frac{\lVert \alpha '\times\alpha '' \rVert}{\lVert \alpha ' \rVert ^{3} }$$  
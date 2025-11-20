>[!Definition] Reparametrización por longitud de arco
>Sea $\alpha : [a, b] \to \mathbb{R}^n$ una curva regular de longitud $L$, y sea $\sigma : [a, b] \to [0, L]$ definida por
> $$ \sigma(t) = \text{long} \left( \alpha|_{[a, t]} \right) = \int_a^t \|\alpha'(u)\| \, du $$
>Por el Teorema Fundamental del Cálculo, $\sigma'(t) = \|\alpha'(t)\| > 0$ (pues $\alpha$ es regular). Luego, $\sigma$ es creciente y resulta una biyección sobre el intervalo $[0, L]$.
>La curva $\beta : [0, L] \to \mathbb{R}^n$ definida por $\beta = \alpha \circ \sigma^{-1}$ se llama la **reparametrización de $\alpha$ por longitud de arco**.

>[!Proposition]
>La curva $\beta$ tiene rapidez unitaria.
>>[!Proof]-
>>1. Como $\alpha = \beta \circ \sigma$, tenemos que $\alpha' = (\beta' \circ \sigma) \sigma'$. Luego $$ \|\alpha'\| = \|\beta' \circ \sigma\| |\sigma'| = \|\beta' \circ \sigma\| \|\alpha'\| $$
>>2. De allí, $\|\beta' \circ \sigma\| = 1$. 
>>3. Como $\sigma$ es sobre $[0, L]$, tenemos que $\|\beta'\| = 1$.

>[!Proposition] 
>Si $\alpha$ es una curva suave, entonces $\beta$ es una curva suave.
>>[!Proof]-
>>1. Si $\alpha$ es suave (clase $C^\infty$), entonces $\alpha'$ es suave.
>>2. La función $\sigma(t) = \int_a^t \|\alpha'(u)\| du$ tiene derivada $\sigma'(t) = \|\alpha'(t)\|$.
>>3. Como $\alpha$ es regular, $\alpha'(t) \neq 0$. 
>>4. La función norma $\|\cdot\|$ es suave en $\mathbb{R}^n \setminus \{0\}$.Por tanto, $\sigma'(t)$ es suave, lo que implica que $\sigma(t)$ es suave.
>>5. Además, como $\sigma'(t) > 0$, por el Teorema de la Función Inversa (versión $C^\infty$), la función inversa $\sigma^{-1}$ es suave.
>>6. Finalmente, $\beta = \alpha \circ \sigma^{-1}$ es composición de funciones suaves, luego $\beta$ es suave.

>[!Definition] Curvatura $\kappa$ 
>Sea $\alpha : (a, b) \to \mathbb{R}^n$ una curva de rapidez unitaria. La **curvatura** de $\alpha$ es la función
> $$ \kappa : (a, b) \to \mathbb{R}, \quad \kappa(s) = \|\alpha''(s)\|. $$

>[!Definition] El triedro de Frenet
> Sea $\alpha : (a,b) \to \mathbb{R}^3$ una curva suave de rapidez unitaria con curvatura nunca nula, es decir, $\|\alpha'(t)\| = 1$ y $\kappa(t) = \|\alpha''(t)\| \ne 0$ para todo $t$.
> Entonces las funciones $T, N, B: (a,b) \to \mathbb{R}^3$ se definen mediante
> $$T = \alpha', \quad N = \alpha''/\|\alpha''\| = \alpha''/\kappa \quad \text{y} \quad B = T \times N$$
>Para cada $t \in (a,b)$, $\{T(t), N(t), B(t)\}$ es una base ortonormal de $\mathbb{R}^3$.
>>[!Proof]-
>>1. Como $\alpha$ tiene rapidez unitaria, $\|T\| = \|\alpha'\| = 1$. Claramente, $\|N\| = 1$.
>>2. Derivando con respecto a $t$ la expresión $1 = \|\alpha'(t)\|^2 = \langle \alpha'(t), \alpha'(t) \rangle$ tenemos que $$ 0 = 2 \langle \alpha''(t), \alpha'(t) \rangle = 2 \langle N(t) \kappa(t), T(t) \rangle = 2\kappa(t) \langle N(t), T(t) \rangle $$que vale para todo $t$. 
>>3. Como $\kappa$ nunca se anula por hipótesis, resulta que $\langle T, N \rangle = 0$
>>4. Además, $\langle B, T \rangle = \langle T\times N, N \rangle = 0$ analogo $\langle B,N\rangle=0$  y $$ \|B\| = \|T \times N\| = \|T\| \|N\|\sin\left( \frac{\pi}{2} \right) = 1.1.1=1 $$

>[!Proposition] Ecuaciones de Frenet
>Se cumple que
> $$T' = \kappa N, \quad N' = -\kappa T + \tau B \quad \text{y} \quad B' = -\tau N, \quad (1)$$
> donde $\kappa : (a,b) \to \mathbb{R}$ es la función curvatura, para cierta función $\tau : (a,b) \to \mathbb{R}$, llamada la **torsión** de $\alpha$, que satisface
> $$\tau = \langle N', B \rangle = - \langle B', N \rangle.$$
> Comentario. Las ecuaciones (1) a veces se escriben de la forma
> $$\begin{cases} T' = & \kappa N \\ N' = & -\kappa T & +\tau B \\ B' = & & -\tau N \end{cases}$$
>>[!Proof]-
>>1. Tenemos que $$ T' = (\alpha')' = \alpha'' = \|\alpha''\| \frac{\alpha''}{\|\alpha''\|} = \kappa N. $$
>>2. Como sabemos que $\{T, N, B\}$ es una base ortonormal, podemos escribir $$ N' = \langle N', T \rangle T + \langle N', N \rangle N + \langle N', B \rangle B. $$
>>3. $\langle N', N \rangle = 0$, pues $1=\|N\|^{2} = (N,N)$ y luego derivando 
>>4. "Integrando"podemos obtener $$ \langle N', T \rangle = \langle N, T \rangle' - \langle N, T' \rangle = 0 - \langle N, \kappa N \rangle = -\kappa \|N\|^2 = -\kappa. $$
>>5. De esta manera $$ N' = -\kappa T + 0.N + \tau B $$ Donde definimos $\langle N', B \rangle=\tau$.
>>6. Ahora escribimos $$ B' = \langle B', T \rangle T + \langle B', N \rangle N + \langle B', B \rangle B. $$
>>7. Tenemos que $\langle B', B \rangle = 0$, pues $\|B\| = \text{constante}$. 
>>8. También, $$ \langle B', N \rangle = \langle B, N \rangle' - \langle B, N' \rangle = 0 - \langle B, \kappa T + \tau B \rangle = -\tau \|B\|^2 = -\tau. $$
>>9. Analogamente $$\langle B', T \rangle=\langle B,T\rangle'-\langle B,T '\rangle=0-\langle B,\kappa N\rangle=0$$
>>10. Mostrando que $B'=-\tau N$ 

>[!Definition] Plano osculador, normal y osculador afín
>Para cada $t$, el plano generado por $T(t)$ y $N(t)$, o sea,
>$$ \text{span } \{T(t), N(t)\} = B(t)^\perp, $$
>se llama **plano osculador** de $\alpha$ en el instante $t$ y el plano
>$$ \text{span } \{N(t), B(t)\} = T(t)^\perp $$
>se denomina **plano normal** de $\alpha$ en el instante $t$. El plano
>$$ \alpha(t) + \text{span } \{T(t), N(t)\} $$
>se llama **plano osculador afín** de $\alpha$ en $t$. Notar que los dos primeros son subespacios de $\mathbb{R}^3$, pero el tercero no necesariamente lo es.

>[!Theorem]
>Sea $\alpha : (a, b) \to \mathbb{R}^3$ una curva suave de rapidez unitaria, curvatura nunca nula y torsión $\tau$. Entonces la trayectoria de $\alpha$ está contenida en un plano si y solo si $\tau = 0$.
>>[!Proof]-
>>- $(\Longleftarrow)$ 
>>	1. Como $B' = -\tau N = 0$, resulta $B$ constante. Lo llamamos $n$. Sea $t_o \in (a, b)$. Veamos que para todo $t$, $\alpha(t)$ está en el plano $P$ que pasa por $\alpha(t_o)$ y es ortogonal a $n$, o sea,$$ P = \{ q \in \mathbb{R}^3 \mid \langle q - \alpha(t_o), n \rangle = 0 \} . \quad (2) $$
>>	2. Debemos mostrar que $\langle \alpha(t) - \alpha(t_o), n \rangle = 0$ para todo $t$. Sea $f : (a, b) \to \mathbb{R}$ definida por $f(t) = \langle \alpha(t) - \alpha(t_o), n \rangle$.
>>	3. Calculamos $$ f'(t) = \langle \alpha'(t), n \rangle = \langle T(t), B(t) \rangle = 0. $$
>>	4. Luego $f$ es constante y $f(t) = f(t_o) = \langle \alpha(t_o) - \alpha(t_o), n \rangle = 0$.
>>- $(\Longrightarrow)$ 
>>	1. Llamamos $P$ al plano donde está contenida la trayectoria de $\alpha$. Sea $t_o \in (a, b)$. Como $\alpha(t_o) \in P$, entonces $P$ es de la forma (2) para cierto vector unitario $n$.
>>	2. Tenemos que $\langle \alpha(t) - \alpha(t_o), n \rangle = 0$ para todo $t$. Derivamos miembro a miembro y obtenemos $$ \langle \alpha'(t), n \rangle = 0, \quad \text{o sea}, \quad \langle T(t), n \rangle = 0 $$para todo $t$. 
>>	3. Derivando nuevamente,$$ 0 = \langle T'(t), n \rangle = \langle \kappa(t) N(t), n \rangle = \kappa(t) \langle N(t), n \rangle . $$
>>	4. De allí, $\langle N(t), n \rangle = 0$ para todo $t$, ya que $\kappa$ es nunca nula.
>>	5. Tenemos entonces que $\langle T, n \rangle = 0 = \langle N, n \rangle$. 
>>	6. Luego, para cada $t$, como $\{T, N, B\}$ es una base ortonormal y $n$ es un vector unitario ortogonal a $T$ y $N$, necesariamente $n$ es colineal con $B$. 
>>	7. Como $B$ y $n$ son ambos unitarios, $$ B(t) = \pm n. $$
>>	8. O sea, existe una función $\varepsilon : (a, b) \to \mathbb{R}$ con $|\varepsilon| = 1$ tal que $$ B(t) = \varepsilon(t) n$$
>>	9. Luego $$ \langle B(t), n \rangle = \langle \varepsilon(t) n, n \rangle = \varepsilon(t) \langle n, n \rangle = \varepsilon(t) $$
>>	10. Como $\varepsilon$ es continua (por que $B$ lo es, porque $N$ y $T$ los son porque $\alpha$ es suave), por el teorema de los valores intermedios resulta que $\varepsilon$ es constante, igual a $1$ o a $-1$. 
>>	11. En el primer caso, $B = n$, con lo cual $0 = B' = -\tau N$, de donde $\tau = 0$. Si $B = -n$, el argumento es similar.
>

>[!Remark]
>El signo de la torsión indica si la curva se parece al pasamanos de una escalera de caracol para diestros ($\tau > 0$) o zurdos ($\tau < 0$). O si se parece a la vid ($\tau > 0$) o al lúpulo ($\tau < 0$), por la manera en que se enroscan los tallos de estas plantas.

>[!Definition] Helice
>Se dice que una curva $\alpha : (a, b) \to \mathbb{R}^3$ 
>de rapidez unitaria y curvatura nunca nula es una hélice si existe
> un vector unitario $u \in \mathbb{R}^3$ tal que $\langle \alpha'(t), u \rangle = \text{constante para todo } t$.

>[!Theorem]
>Si $\alpha : (a, b) \to \mathbb{R}^3$ es una hélice con curvatura $\kappa : (a, b) \to \mathbb{R}$ positiva y torsión $\tau : (a, b) \to \mathbb{R}$, entonces $\tau/\kappa$ es constante.
>**Nota.** La recíproca se prueba en el práctico.
>>[!Proof]-
>>- $(\Rightarrow)$
>>	1. Como $\alpha'$ y $u$ son unitarios, $\langle \alpha'(t), u \rangle = \cos \theta$, donde $\theta$ es el ángulo entre $\alpha'(t)$ y $u$, que es constante por hipótesis. Mostrar como ejercicio que $|\cos \theta| < 1$.
>>	2. Derivamos miembro a miembro $$ 0 = \langle T', u \rangle + \langle T, u' \rangle = \langle \kappa N, u \rangle + 0 = \kappa \langle N, u \rangle$$
>>	3. Como $\kappa$ es nunca nula $\langle N, u \rangle = 0$. 
>>	4. Derivamos nuevamente $$ 0 = \langle N', u \rangle + \langle N, u' \rangle = \langle -\kappa T + \tau B, u \rangle = -\kappa \langle T, u \rangle + \tau \langle B, u \rangle = -\kappa \cos \theta + \tau \langle B, u \rangle . \quad (3) $$
>>	5. Ahora vemos que $\langle B, u \rangle$ es constante. Calculamos $$\langle B', u \rangle = \langle -\tau N, u \rangle = -\tau \langle N, u \rangle = 0$$
>>	6. Para cada $t$, escribimos $u$ en la base $\{T(t), N(t), B(t)\}$, $$ u = \langle u, T \rangle T + \langle u, N \rangle N + \langle u, B \rangle B = (\cos \theta) T + \langle u, B \rangle B$$
>>	7. Como $u$ es unitario y la base es ortonormal $$ 1 = \|u\|^2 = \cos^2 \theta + \langle u, B \rangle^2$$
>>	8. Luego, $\langle u, B \rangle = \pm \text{sen } \theta = \text{constante}$. Por (3) $$-\kappa \cos \theta \pm \tau \text{sen } \theta = 0$$
>>	9. De allí, $\tau/\kappa = \pm \cot \theta = \text{constante}$.
>>- $(\Leftarrow)$
>>	1. Supongamos que $\tau/\kappa = c$ para alguna constante $c \in \mathbb{R}$. Podemos escribir $c = \cot \theta$ para algún $\theta \in (0, \pi)$, con $\theta \ne \pi/2$.
>>	2. Definimos el vector $u(t) = (\cos \theta) T(t) + (\sin \theta) B(t)$ y derivamos con respecto a $t$ $$ u' = (\cos \theta) T' + (\sin \theta) B' = (\cos \theta) \kappa N + (\sin \theta) (-\tau N) = (\kappa \cos \theta - \tau \sin \theta) N. $$
>>	3. Como $\tau/\kappa = \cot \theta$, tenemos $\tau \sin \theta = \kappa \cos \theta$, por lo que $u' = 0$.
>>	4. Así, $u$ es un vector constante. Además $$ \|u\|^2 = \cos^2 \theta + \sin^2 \theta = 1, $$por lo que $u$ es unitario. 
>>	5. Finalmente $$ \langle \alpha'(t), u \rangle = \langle T(t), (\cos \theta) T(t) + (\sin \theta) B(t) \rangle = \cos \theta, $$que es constante. 
>>	6. Por definición, $\alpha$ es una hélice. $\square$


>[!Definition]
> Sea $\alpha : [a, b] \to \mathbb{R}^n$ una curva regular de longitud $L$. Se define la **curvatura** de $\alpha$ en el instante $t$ mediante
> $$\kappa_{\alpha}(t) = \kappa_{\beta}(\sigma(t)),$$
> donde $\sigma : [a, b] \to [0, L]$ es la función longitud de arco de $\alpha$, $\beta : [0, L] \to \mathbb{R}^n$ es la reparametrización por longitud de arco de $\alpha$, y $\kappa_{\alpha}, \kappa_{\beta}$ son las curvaturas de $\alpha$ y $\beta$, respectivamente.
> Ademas en este caso $$\kappa_{\alpha }=\frac{\lVert \alpha '\times\alpha '' \rVert}{\lVert \alpha ' \rVert ^{3} }$$  
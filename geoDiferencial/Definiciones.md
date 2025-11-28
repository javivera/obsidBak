# Curvas y parametrizaciones

>[!Definition] Reparametrización por longitud de arco
>Sea $\alpha : [a, b] \to \mathbb{R}^n$ una curva regular de longitud $L$, y sea $\sigma : [a, b] \to [0, L]$ definida por
> $$ \sigma(t) = \text{long} \left( \alpha|_{[a, t]} \right) = \int_a^t \|\alpha'(u)\| \, du $$
>Por el Teorema Fundamental del Cálculo, $\sigma'(t) = \|\alpha'(t)\| > 0$ (pues $\alpha$ es regular). Luego, $\sigma$ es creciente y resulta una biyección sobre el intervalo $[0, L]$.
>La curva $\beta : [0, L] \to \mathbb{R}^n$ definida por $\beta = \alpha \circ \sigma^{-1}$ se llama la **reparametrización de $\alpha$ por longitud de arco**.

^4b79f2

>[!Proposition]
>La curva $\beta$ tiene rapidez unitaria.
>>[!Proof]-
>>1. Como $\alpha = \beta \circ \sigma$, tenemos que $\alpha' = (\beta' \circ \sigma) \sigma'$. Luego $$ \|\alpha'\| = \|\beta' \circ \sigma\| |\sigma'| = \|\beta' \circ \sigma\| \|\alpha'\| $$
>>2. De allí, $\|\beta' \circ \sigma\| = 1$. 
>>3. Como $\sigma$ es sobre $[0, L]$, tenemos que $\|\beta'\| = 1$.

>[!Proposition] 
>Si $\alpha$ es una curva suave, entonces $\beta$ es una curva suave.
>>[!Proof]-
>>4. Si $\alpha$ es suave (clase $C^\infty$), entonces $\alpha'$ es suave.
>>5. La función $\sigma(t) = \int_a^t \|\alpha'(u)\| du$ tiene derivada $\sigma'(t) = \|\alpha'(t)\|$.
>>6. Como $\alpha$ es regular, $\alpha'(t) \neq 0$. 
>>7. La función norma $\|\cdot\|$ es suave en $\mathbb{R}^n \setminus \{0\}$.Por tanto, $\sigma'(t)$ es suave, lo que implica que $\sigma(t)$ es suave.
>>8. Además, como $\sigma'(t) > 0$, por el Teorema de la Función Inversa (versión $C^\infty$), la función inversa $\sigma^{-1}$ es suave.
>>9. Finalmente, $\beta = \alpha \circ \sigma^{-1}$ es composición de funciones suaves, luego $\beta$ es suave.

>[!Definition] Curvatura $\kappa$ 
>Sea $\alpha : (a, b) \to \mathbb{R}^n$ una curva de rapidez unitaria. La **curvatura** de $\alpha$ es la función
> $$ \kappa : (a, b) \to \mathbb{R}, \quad \kappa(s) = \|\alpha''(s)\|. $$

>[!Definition] El triedro de Frenet
> Sea $\alpha : (a,b) \to \mathbb{R}^3$ una curva suave de rapidez unitaria con curvatura nunca nula, es decir, $\|\alpha'(t)\| = 1$ y $\kappa(t) = \|\alpha''(t)\| \ne 0$ para todo $t$.
> Entonces las funciones $T, N, B: (a,b) \to \mathbb{R}^3$ se definen mediante
> $$T = \alpha', \quad N = \alpha''/\|\alpha''\| = \alpha''/\kappa \quad \text{y} \quad B = T \times N$$
>Para cada $t \in (a,b)$, $\{T(t), N(t), B(t)\}$ es una base ortonormal de $\mathbb{R}^3$.
>>[!Proof]-
>>10. Como $\alpha$ tiene rapidez unitaria, $\|T\| = \|\alpha'\| = 1$. Claramente, $\|N\| = 1$.
>>11. Derivando con respecto a $t$ la expresión $1 = \|\alpha'(t)\|^2 = \langle \alpha'(t), \alpha'(t) \rangle$ tenemos que $$ 0 = 2 \langle \alpha''(t), \alpha'(t) \rangle = 2 \langle N(t) \kappa(t), T(t) \rangle = 2\kappa(t) \langle N(t), T(t) \rangle $$que vale para todo $t$. 
>>12. Como $\kappa$ nunca se anula por hipótesis, resulta que $\langle T, N \rangle = 0$
>>13. Además, $\langle B, T \rangle = \langle T\times N, N \rangle = 0$ analogo $\langle B,N\rangle=0$  y $$ \|B\| = \|T \times N\| = \|T\| \|N\|\sin\left( \frac{\pi}{2} \right) = 1.1.1=1 $$

>[!Proposition] Ecuaciones de Frenet
>Se cumple que
> $$T' = \kappa N, \quad N' = -\kappa T + \tau B \quad \text{y} \quad B' = -\tau N, \quad (1)$$
> donde $\kappa : (a,b) \to \mathbb{R}$ es la función curvatura, para cierta función $\tau : (a,b) \to \mathbb{R}$, llamada la **torsión** de $\alpha$, que satisface
> $$\tau = \langle N', B \rangle = - \langle B', N \rangle.$$
> Comentario. Las ecuaciones (1) a veces se escriben de la forma
> $$\begin{cases} T' = & \kappa N \\ N' = & -\kappa T & +\tau B \\ B' = & & -\tau N \end{cases}$$
>>[!Proof]-
>>14. Tenemos que $$ T' = (\alpha')' = \alpha'' = \|\alpha''\| \frac{\alpha''}{\|\alpha''\|} = \kappa N. $$
>>15. Como sabemos que $\{T, N, B\}$ es una base ortonormal, podemos escribir $$ N' = \langle N', T \rangle T + \langle N', N \rangle N + \langle N', B \rangle B. $$
>>16. $\langle N', N \rangle = 0$, pues $1=\|N\|^{2} = (N,N)$ y luego derivando 
>>17. "Integrando"podemos obtener $$ \langle N', T \rangle = \langle N, T \rangle' - \langle N, T' \rangle = 0 - \langle N, \kappa N \rangle = -\kappa \|N\|^2 = -\kappa. $$
>>18. De esta manera $$ N' = -\kappa T + 0.N + \tau B $$ Donde definimos $\langle N', B \rangle=\tau$.
>>19. Ahora escribimos $$ B' = \langle B', T \rangle T + \langle B', N \rangle N + \langle B', B \rangle B. $$
>>20. Tenemos que $\langle B', B \rangle = 0$, pues $\|B\| = \text{constante}$. 
>>21. También, $$ \langle B', N \rangle = \langle B, N \rangle' - \langle B, N' \rangle = 0 - \langle B, \kappa T + \tau B \rangle = -\tau \|B\|^2 = -\tau. $$
>>22. Analogamente $$\langle B', T \rangle=\langle B,T\rangle'-\langle B,T '\rangle=0-\langle B,\kappa N\rangle=0$$
>>23. Mostrando que $B'=-\tau N$ 

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
>>[!Proof]-
>>- $(\Rightarrow)$
>>	1. Por definicion de helice $\alpha'$ y $u$ son unitarios
>>	2. $\langle \alpha'(t), u \rangle = \cos \theta$, donde $\theta$ es el ángulo entre $\alpha'(t)$ y $u$, que es constante por hipótesis.
>>	3. Mostrar como ejercicio que $|\cos \theta| < 1$.
>>	4. Derivamos miembro a miembro $$ 0 = \langle T', u \rangle + \langle T, u' \rangle = \langle \kappa N, u \rangle + 0 = \kappa \langle N, u \rangle$$
>>	5. Como $\kappa$ es nunca nula $\langle N, u \rangle = 0$. 
>>	6. Derivamos nuevamente $$ 0 = \langle N', u \rangle + \langle N, u' \rangle = \langle -\kappa T + \tau B, u \rangle = -\kappa \langle T, u \rangle + \tau \langle B, u \rangle = -\kappa \cos \theta + \tau \langle B, u \rangle . \quad (3) $$
>>	7. Ahora vemos que $\langle B, u \rangle$ es constante. Calculamos $$\langle B', u \rangle = \langle -\tau N, u \rangle = -\tau \langle N, u \rangle = 0$$
>>	8. Para cada $t$, escribimos $u$ en la base $\{T(t), N(t), B(t)\}$, $$ u = \langle u, T \rangle T + \langle u, N \rangle N + \langle u, B \rangle B = (\cos \theta) T + \langle u, B \rangle B$$
>>	9. Como $u$ es unitario y la base es ortonormal $$ 1 = \|u\|^2 = \cos^2 \theta + \langle u, B \rangle^2$$
>>	10. Luego, $\langle u, B \rangle = \pm \text{sen } \theta = \text{constante}$. Ademas Por (3) $$-\kappa \cos \theta \pm \tau \text{sen } \theta = 0$$
>>	11. De allí, $\tau/\kappa = \pm \cot \theta = \text{constante}$.
>>- $(\Leftarrow)$
>>	1. Supongamos que $\tau/\kappa = c$ para alguna constante $c \in \mathbb{R}$. Podemos escribir $c = \cot \theta$ para algún $\theta \in (0, \pi)$, con $\theta \ne \pi/2$.
>>	2. Definimos el vector $u(t) = (\cos \theta) T(t) + (\sin \theta) B(t)$ y derivamos con respecto a $t$ $$ u' = (\cos \theta) T' + (\sin \theta) B' = (\cos \theta) \kappa N + (\sin \theta) (-\tau N) = (\kappa \cos \theta - \tau \sin \theta) N. $$
>>	3. Como $\tau/\kappa = \cot \theta$, tenemos $\tau \sin \theta = \kappa \cos \theta$, por lo que $u' = 0$.
>>	4. Así, $u$ es un vector constante. Además $$ \|u\|^2 = \cos^2 \theta + \sin^2 \theta = 1, $$por lo que $u$ es unitario. 
>>	5. Finalmente $$ \langle \alpha'(t), u \rangle = \langle T(t), (\cos \theta) T(t) + (\sin \theta) B(t) \rangle = \cos \theta, $$que es constante. 
>>	6. Por definición, $\alpha$ es una hélice. $\square$


>[!Definition] Curvatura de reparametrizacion
>Sea $\alpha : [a, b] \to \mathbb{R}^3$ una curva regular de longitud $L$. Se define la **curvatura** de $\alpha$ en el instante $t$ mediante
> $$\kappa_{\alpha}(t) = \kappa_{\beta}(\sigma(t)),$$
>donde $\sigma : [a, b] \to [0, L]$ es la función longitud de arco de $\alpha$, $\beta : [0, L] \to \mathbb{R}^3$ es la reparametrización por longitud de arco de $\alpha$, y $\kappa_{\alpha}, \kappa_{\beta}$ son las curvaturas de $\alpha$ y $\beta$, respectivamente.
>Bajo estas condiciones vale,
>$$\kappa_{\alpha }=\frac{\lVert \alpha '\times\alpha '' \rVert}{\lVert \alpha ' \rVert ^{3} }$$
>>[!Proof]-
>>1. Como $\sigma$ es la función longitud de arco, sabemos que $\sigma'(t) = \|\alpha'(t)\|$ para todo $t$ por [[Definiciones#^4b79f2]]
>>2. Tenemos que $\alpha(t) = \beta(\sigma(t))$ entonces $\alpha'(t) = \beta'(\sigma(t))\sigma'(t)$ y $$ \alpha''(t) = \beta''(\sigma(t))(\sigma'(t))^2 + \beta'(\sigma(t))\sigma''(t)$$
>>3. Entonces, como $x \times x = 0$ para todo $x \in \mathbb{R}^3$, y usando distributiva en producto escalar y ademas que la imagen de $\sigma$ es un escalar, tenemos: $$ \alpha' \times \alpha'' = \beta'(\sigma)\sigma' \times (\beta''(\sigma)(\sigma')^2 + \beta'(\sigma)\sigma'') = \beta'(\sigma) \times \beta''(\sigma)(\sigma')^3 $$
>>4. Tomando norma miembro a miembro y usando 1. $$ \|\alpha' \times \alpha''\| = \|\beta'(\sigma) \times \beta''(\sigma)\| |\sigma'|^3 = \|\beta'(\sigma) \times \beta''(\sigma)\| \|\alpha'(t)\|^3. $$
>>5. Como $\|\beta'\| = 1$, resulta que $\langle \beta', \beta'' \rangle = 0$. osea el angulo entre ellos es 0  
>>6. Así por 5. , defincion de producto cruz y $\beta''=\kappa_{\beta} N$ $$ \|\beta'(\sigma) \times \beta''(\sigma)\| = \|\beta'(\sigma)\| \|\beta''(\sigma)\|\lVert \cos(0) \rVert  = \lVert \beta''(\sigma) \rVert =\kappa_\beta(\sigma). $$
>>7. En consecuencia $$ \kappa_\alpha = \kappa_\beta(\sigma) = \frac{\|\alpha' \times \alpha''\|}{\|\alpha'\|^3}$$como deseábamos.  

# Curvas Planas

>[!Definition] Curvatura signada
>La **curvatura signada** de una curva suave $\alpha : (a, b) \to \mathbb{R}^2$ de rapidez unitaria es la función
>$$ k : (a, b) \to \mathbb{R}, \quad k(t) = \det(\alpha'(t), \alpha''(t)). $$
>
>**Nota.** En el práctico se ve que $|k| = \kappa$.

>[!Remark]
>Sea $I : \mathbb{R}^2 \to \mathbb{R}^2$ la rotación en un ángulo recto en sentido antihorario alrededor del origen, o sea, $I(x, y) = (-y, x)$. Equivalentemente, $I$ es la multiplicación por $i$, previa la identificación canónica de $\mathbb{R}^2$ con $\mathbb{C}$.

>[!Proposition]
>Sean $\alpha$ y $k$ como en la definición de más arriba. Entonces para todo $s$ vale
>$$ k(s) = \langle I(\alpha'(s)), \alpha''(s) \rangle. $$
>Notar ademas que $I(\alpha '(s))=N(s)$ por que es rotar  
>>[!Proof]-
>>1. En general, para todo par de vectores $u, v \in \mathbb{R}^2$ se cumple que $\det(u, v) = \langle I(u), v \rangle$, en particular para $u = \alpha'(s)$ y $v = \alpha''(s)$.
>>2. Veamoslo, si $u = (x, y)$ y $v = (\xi, \eta)$, tenemos $$ \det(u, v) = \det \begin{pmatrix} x & \xi \\ y & \eta \end{pmatrix} = x\eta - y\xi, $$
>>3. Y por el otro lado
>>$$ \langle I(x, y), (\xi, \eta) \rangle = \langle (-y, x), (\xi, \eta) \rangle = -y\xi + x\eta = x\eta - y\xi. $$

>[!Definition]
>La curvatura signada de curvas regulares planas, no necesariamente de rapidez unitaria, se define de manera análoga a la curvatura de curvas regulares en $\mathbb{R}^2$.

>[!Proposition]
>Sea $\alpha : (a, b) \to \mathbb{R}^2$ una curva de rapidez unitaria con curvatura signada $k : (a, b) \to \mathbb{R}$. Si $\alpha'(s) = (\cos \theta(s), \sin \theta(s))$ para cierta función $\theta : (a, b) \to \mathbb{R}$ de clase $C^2$, entonces $k = \theta'$.
>
>**Comentario.** Se puede demostrar que funciones $\theta$ así siempre existen y dos cualesquiera difieren en un múltiplo entero de $2\pi$.
>>[!Proof]-
>>Calculamos
>>$$ k(s) = \det(\alpha'(s), \alpha''(s)) = \det \begin{pmatrix} \cos \theta(s) & -\sin(\theta(s))\theta'(s) \\ \sin \theta(s) & \cos(\theta(s))\theta'(s) \end{pmatrix} $$
>>$$ = (\cos^2 \theta(s) + \sin^2 \theta(s))\theta'(s) = \theta'(s). $$

^bb97e8

>[!Definition]
>Sea $\beta : [a, b] \to \mathbb{R}^n$ una curva continua. Si $\beta(t) = (y_1(t), \dots, y_n(t))$, se define
>$$ \int_a^b \beta(t) \, dt = \left( \int_a^b y_1(t) \, dt, \dots, \int_a^b y_n(t) \, dt \right). $$

>[!Theorem] Teorema fundamental de las curvas planas
>Sea $\tilde{k} : [a, b] \to \mathbb{R}$ una función de clase $C^2$ y sean $p, u \in \mathbb{R}^2$ con $\|u\| = 1$. Entonces existe una curva plana $\alpha : [a, b] \to \mathbb{R}^2$ suave de rapidez unitaria tal que $\alpha(a) = p$, $\alpha'(a) = u$ y $\tilde{k}$ es la función curvatura signada de $\alpha$.
>
>**Comentario.** Se puede demostrar que una curva $\alpha$ con esas propiedades es única.
>>[!Proof]-
>>1. Proponemos $\alpha : [a, b] \to \mathbb{R}^2$ de la forma $$ \alpha(s) = p + \int_a^s (\cos \theta(t), \sin \theta(t)) \, dt $$para cierta función $\theta : [a, b] \to \mathbb{R}$. 
>>2. Como $u$ es unitario, $u = (\cos(\theta_o), \sin(\theta_o))$ para cierto ángulo $\theta_o$.
>>3. Se cumple que $$ \alpha(a) = p \quad \text{y} \quad \alpha'(s) = (\cos \theta(s), \sin \theta(s))$$
>>4. Necesitamos que $\tilde{k}(s) = k(s)$, o equivalentemente, por [[Definiciones#^bb97e8]], que $\tilde{k}(s) = \theta'(s)$.
>>5. Luego, tomando $$ \theta(s) = \theta_o + \int_a^s \tilde{k}(t) \, dt $$la curva $\alpha$ satisface lo requerido

>[!Theorem] Teorema fundamental de las curvas espaciales
>Sea $\kappa : (a, b) \to \mathbb{R}$ una función positiva de clase $C^2$ y sea $\tau : (a, b) \to \mathbb{R}$ una función de clase $C^1$. Dados $t_o \in (a, b)$, $p \in \mathbb{R}^3$ y una base ortonormal $\{t, n, t \times n\}$ de $\mathbb{R}^3$, existe una única curva suave de rapidez unitaria $\alpha : (a, b) \to \mathbb{R}^3$ tal que su curvatura y su torsión son $\kappa$ y $\tau$, respectivamente, y además $\alpha(t_o) = p$, $T(t_o) = t$, $N(t_o) = n$ y $B(t_o) = t \times n$ 
>($\{T, N, B\}$ es el aparato de Frenet de $\alpha$).
>>[!Proof]
>>No damos la prueba.

>[!Proposition]
>La longitud de cualquier curva suave $\alpha : [a, b] \to \mathbb{R}^n$ con $\alpha(a) = p$ y $\alpha(b) = q$ es mayor o igual que $\|q - p\|$.
>>[!Proof]-
>>6. Escribimos $$ q - p = \alpha(b) - \alpha(a) = \int_a^b \alpha'(t) \, dt $$
>>7. Hacemos producto escalar contra $q - p$ miembro a miembro y obtenemos $$ \begin{align}\|q - p\|^2 & = \left\langle \int_a^b \alpha'(t) \, dt, q - p \right\rangle \\ & = \int_a^b \langle \alpha'(t), q - p \rangle \, dt\\& \le \int_a^b \|\alpha'(t)\| \|q - p\| \, dt \\& = \|q - p\| \int_a^b \|\alpha'(t)\| \, dt \end{align}$$ (hemos usado la desigualdad de Schwarz).
>>8. Ahora, si $q = p$, el enunciado es claramente verdadero. Si $q \ne p$, tenemos $\|q - p\| \ne 0$ y así $$ \|q - p\| \le \int_a^b \|\alpha'(t)\| \, dt = \text{long}(\alpha), $$como queríamos.

>[!Definition] Circunferencia osculatriz y Evoluta
>Sea $\alpha : (a, b) \to \mathbb{R}^2$ una curva de rapidez unitaria y curvatura signada $k : (a, b) \to \mathbb{R}$ positiva.
>La **circunferencia osculatriz** en el instante $t$ es la circunferencia $C_t$ de radio $$r(t) := \frac{1}{k(t)}$$ (el radio de curvatura en $t$) y centro
>$$ c(t) = \alpha(t) + r(t) I \alpha'(t), $$
>donde $I(x, y) = (-y, x)$, la trasformación de matriz $I = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$.
>Se ve en el práctico que $C_t$ es la circunferencia que mejor aproxima a la curva $\alpha$ en $t$.
>La curva $c$ se llama la **evoluta** de $\alpha$.

>[!Proposition]
>Sea $\alpha$ como arriba, que cumpla además que $k$ es estrictamente decreciente. Entonces para $t_1 < t_2$ en $(a, b)$ vale que
>$$ \text{long}\left( c|_{[t_1, t_2]} \right) = r(t_2) - r(t_1). $$
>Es decir, la longitud de un arco de evoluta de $\alpha$ es igual al incremento del radio de curvatura.
>>[!Proof]-
>>9. Notar que $r' > 0$ pues $k$ decrece. 
>>10. Sabemos $\alpha''(s)=T'=\tilde{k}(s) N$ para alguna funcion $\tilde{k}$ entonces $$k(s)=(\alpha ''(s),I(\alpha '(s)))=\langle \tilde{k}(s)N,N(s)\rangle=\tilde{k}(s)$$ tenemos que $\alpha''(s)=k(s)N(s) = k(s) I \alpha'(s)$.
>>11. Calculamos $$ c' = \alpha' + r' I \alpha' + r I \alpha'' = \alpha' + r' I \alpha' + r I k I \alpha' = \alpha' + r' I \alpha' - r k \alpha' = r' I \alpha', $$pues $I^2(z) = -z$ para todo $z \in \mathbb{R}^2$.
>>12. Así, $\|c'(t)\| = r'(t)$ ($k$ es positiva por eso no hay modulo y rapidez unitaria) para todo $t$. 
>>13. Luego si $t_1 < t_2$ están en $(a, b)$ resulta que
>>$$ \text{long}\left( c|_{[t_1, t_2]} \right) =\int_{t_{1}}^{t_{2}}\lVert c'(t) \rVert dt  = \int_{t_1}^{t_2} r'(t) \, dt = r(t_2) - r(t_1), $$

>[!Theorem] Teorema de Tait-Kneser
>Sea $\alpha : (a, b) \to \mathbb{R}^2$ una curva de rapidez unitaria y curvatura signada $k : (a, b) \to \mathbb{R}$ positiva y estrictamente decreciente. Entonces las circunferencias osculatrices de $\alpha$ son disjuntas dos a dos y anidadas.
>>[!Proof]-
>>14. Sean $t_1 < t_2$ en $(a, b)$. Mostramos a continuación que $C_{t_1} \subsetneq C_{t_2}$.
>>15. Por la proposición anterior, la distancia entre los centros de esas circunferencias satisface $$ \|c(t_2) - c(t_1)\| \le \text{long}\left( c|_{[t_1, t_2]} \right) = r(t_2) - r(t_1). \quad (5) $$
>>16. Sea $p \in C_{t_1}$, o sea, $\|p - c(t_1)\| = r(t_1)$. Veamos que $p$ está en el interior de $C_{t_2}$ o sea, $\|p - c(t_2)\| < r(t_2)$. Calculamos
>>$$ \begin{align} \|p - c(t_2)\| & = \|p - c(t_1) + c(t_1) - c(t_2)\| \\ & \le \|p - c(t_1)\| + \|c(t_1) - c(t_2)\| \\ & \le r(t_1) + r(t_2) - r(t_1) = r(t_2), \end{align} $$
>>con lo cual $\|p - c(t_2)\| \le r(t_2)$.

# Transformaciones Rigidas

>[!Definition] Transformaciones ortogonales
>Una matriz $C$ $n \times n$ se dice **ortogonal** si sus columnas forman una base ortonormal de $\mathbb{R}^n$, o equivalentemente, si $C^T C = I_{n \times n}$, donde el supraíndice $T$ denota transpuesta.
>Si $C$ es ortogonal, $\det C = \pm 1$. En efecto,
>$$ 1 = \det I = \det(C^T C) = \det C^T \det C = \det C \det C = (\det C)^2. $$
>Si $\det C = 1$, $C$ se llama **rotación**.
>La matriz $C$ induce una transformación lineal de $\mathbb{R}^n$ en $\mathbb{R}^n$, $x \mapsto Cx$ ($x$ vector columna), que también llamamos $C$, por abuso de notación.

>[!Proposition]
>Sea $C : \mathbb{R}^n \to \mathbb{R}^n$ una transformación lineal. Entonces son equivalentes:
>a) $C$ es ortogonal.
>b) $C$ preserva productos internos.
>c) $C$ preserva normas.
>>[!Proof]-
>>- a) $\Rightarrow$ b) $\langle Cx, Cy \rangle = (Cx)^T Cy = x^T C^T C y = x^T I y = x^T y = \langle x, y \rangle$.
>>- b) $\Rightarrow$ c) $\|Cx\|^2 = \langle Cx, Cx \rangle = \langle x, x \rangle = \|x\|^2$.
>>- c) $\Rightarrow$ b) Ejercicio. Se deduce de la identidad de polarización:
>>$$ 4 \langle x, y \rangle = \|x + y\|^2 - \|x - y\|^2. $$
>>- b) $\Rightarrow$ a) Resulta de que si $C$ preserva poductos internos, entonces lleva la base canónica (que es ortonormal) en una base ortonormal. $\square$

>[!Proposition]
>Sea $C$ una matriz ortogonal $3 \times 3$. Entonces para todo par de vectores $x, y \in \mathbb{R}^3$ vale que
>$$ Cx \times Cy = \det(C) C(x \times y). $$
>>[!Proof]-
>>1. **Ejercicio.** Mostrar que si $\langle x, z \rangle = \langle y, z \rangle$ para todo $z$, entonces $x = y$.
>>2. Hacemos producto escalar miembro a miembro contra un vector cualquiera $z'$, digamos $z' = Cz$ (notar que $C$ es suryectiva). Por el ejercicio, debemos ver que
>>$$ \langle Cx \times Cy, Cz \rangle = \det(C) \langle C(x \times y), Cz \rangle, $$
>>3. o equivalentemente,
>>$$ \det(Cx, Cy, Cz) = \det(C) \langle x \times y, z \rangle = \det(C) \det(x, y, z) $$
>>(con $x, y, z$ vectores columna). 
>>4. Eso es lo mismo que ver que
>>$$ \det(C(x, y, z)) = \det(C) \det(x, y, z) $$
>>que es verdadero. $\square$

>[!Proposition]
>Sea $C$ una transformación ortogonal de $\mathbb{R}^3$. Entonces la matriz de $C$ respecto de alguna base ortonormal de $\mathbb{R}^3$ tiene la forma
>$$ \begin{pmatrix} R_\theta & 0 \\ 0 & \det C \end{pmatrix} $$
>para cierto $\theta \in \mathbb{R}$. En particular, si $\det C = 1$, $C$ es una rotación alrededor de una recta que pasa por el origen.

>[!Definition] Transformacion Euclideana
>Una función $T : \mathbb{R}^n \to \mathbb{R}^n$ se llama **transformación euclidiana** de $\mathbb{R}^n$ si es de la forma $T(x) = Cx + u$, donde $C$ es una transformación ortogonal y $u \in \mathbb{R}^n$.
>La transformación euclidiana se dice **rígida** (o que **preserva la orientación**) si $C$ es una rotación, o sea, si $\det C = 1$.

>[!Proposition]
>Las transformaciones euclidianas de $\mathbb{R}^n$ preservan distancia.
>>[!Proof]-
>>$$ \|Tx - Ty\| = \|Cx + u - (Cy + u)\| = \|Cx - Cy\| = \|C(x - y)\| = \|x - y\|. $$

>[!Remark]
>Antes de enunciar el teorema que sigue, veamos que para derivar un producto de dos curvas matriciales vale una regla similar a la que usamos para derivar el producto de dos funciones.
>
>Sean $A : (a, b) \to \mathbb{R}^{n \times m}$ una función suave, es decir, $A_{i,j} : (a, b) \to \mathbb{R}$ es una función suave para todo $1 \le i \le n$, $1 \le j \le m$.
>Se define la función $A' : (a, b) \to \mathbb{R}^{n \times m}$ mediante
>$$ (A'(t))_{i,j} = (A_{i,j})'(t) $$
>(o sea, se deriva entrada por entrada).

>[!Theorem]
>Sea $\alpha : (a, b) \to \mathbb{R}^2$ una curva suave de rapidez unitaria y curvatura signada $k : (a, b) \to \mathbb{R}$. Sea $T : \mathbb{R}^2 \to \mathbb{R}^2$ una transformación euclidiana del plano y sea $\bar{\alpha} = T \circ \alpha$. Entonces $\bar{\alpha}$ tiene rapidez unitaria y la curvatura signada $\bar{k}$ de $\bar{\alpha}$ es $\pm k$, con $+$ si $T$ es rígida y $-$ si no.
>>[!Proof]-
>>1. Supongamos que $T(x) = Cx + u$ con $C$ ortogonal. Calculamos $$ \bar{\alpha}(t) = T(\alpha(t)) = C\alpha(t) + u. $$
>>2. Luego, $\bar{\alpha}'(t) = C\alpha'(t)$ para todo $t$ y así, $\|\bar{\alpha}'\| = \|C\alpha'\| = \|\alpha'\| = 1$, con lo cual $\bar{\alpha}$ tiene rapidez unitaria.
>>3. Ademas $\bar{\alpha}''(t) = C\alpha''(t)$. Entonces, si $I(x, y) = (-y, x)$, $$ \bar{k}(t) = \langle I(\bar{\alpha}'(t)), \bar{\alpha}''(t) \rangle = \langle I(C\alpha'(t)), C\alpha''(t) \rangle. \quad (7) $$
>>4. Como $C$ es ortogonal tiene la forma $$ \begin{pmatrix} \cos \theta & -\varepsilon \sin \theta \\ \sin \theta & \varepsilon \cos \theta \end{pmatrix}. $$ con $\varepsilon=\det(C)=\pm 1$ 
>>5. Ahora verificamos que $I$ conmuta o anticonmuta con $C$, dependiendo de si $\varepsilon = 1$ o $-1$. En efecto, $$ IC = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} \cos \theta & -\varepsilon \sin \theta \\ \sin \theta & \varepsilon \cos \theta \end{pmatrix} = \begin{pmatrix} -\sin \theta & -\varepsilon \cos \theta \\ \cos \theta & -\varepsilon \sin \theta \end{pmatrix}, $$ $$ CI = \begin{pmatrix} \cos \theta & -\varepsilon \sin \theta \\ \sin \theta & \varepsilon \cos \theta \end{pmatrix} \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} -\varepsilon \sin \theta & -\cos \theta \\ \varepsilon \cos \theta & -\sin \theta \end{pmatrix}. $$
>>6. Luego $IC = \varepsilon CI$.
>>7. De 3. y usando que $C$ es rotar, si rotamos las dos componentes el producto interno no cambia. Resulta que $$ \bar{k}(t) = \langle I(C\alpha'(t)), C\alpha''(t) \rangle = \varepsilon \langle C(I\alpha'(t)), C\alpha''(t) \rangle = \varepsilon \langle I\alpha'(t), \alpha''(t) \rangle = \varepsilon k(t). $$

>[!Theorem]
>Sea $T : \mathbb{R}^n \to \mathbb{R}^n$ una función que preserva distancias, o sea,
>$$ \|Tx - Ty\| = \|x - y\| $$
>para todo $x, y \in \mathbb{R}^n$. Entonces $T$ es euclidiana, o sea, de la forma
>$$ T(x) = Cx + u, $$
>donde $C$ es ortogonal, y en particular, lineal.
>>[!Proof]-
>>8. Supongamos primero que $T(0) = 0$ y es una funcion que preserva distancias. Veamos que
>>	- $T$ Preserva normas
>>		1. $\|T(x)\| = \|T(x) - 0\| = \|T(x) - T(0)\| = \|x - 0\| = \|x\|$ (en la penúltima igualdad usamos que $T$ preserva distancias).
>>	- $T$ Preserva productos internos
>>		1. Sabemos que $\|Tx - Ty\|^2 = \|x - y\|^2$, o sea, $$\langle Tx - Ty, Tx - Ty \rangle = \langle x - y, x - y \rangle$$
>>		2. Distribuyendo, $$ \|Tx\|^2 + \|Ty\|^2 - 2\langle Tx, Ty \rangle = \|x\|^2 + \|y\|^2 - 2\langle x, y \rangle. $$
>>		3. Pero por preservar normas sabemos que $\|Tx\|^2 = \|x\|^2$ y $\|Ty\|^2 = \|y\|^2$, con lo cual, $\langle Tx, Ty \rangle = \langle x, y \rangle$.
>>	- $T$ es lineal
>>		1. Basta mostrar que para todo $x, y, \lambda$ se cumple que $$ \|T(x + y) - (Tx + Ty)\|^2 = 0 \quad \text{y} \quad \|T(\lambda x) - \lambda Tx\|^2 = 0. $$
>>		2. Verificamos la primera identidad y dejamos la segunda como ejercicio. 
>>		3. Usamos (1) y (2) repetidas veces. $$ \begin{align} \|T(x + y) - (Tx + Ty)\|^2 & = \|T(x + y)\|^2 - 2\langle T(x + y), Tx + Ty \rangle + \|Tx + Ty\|^2 \\ & = \|x + y\|^2 - 2\langle T(x + y), Tx \rangle - 2\langle T(x + y), Ty \rangle \\ & \quad + \|Tx\|^2 + 2\langle Tx, Ty \rangle + \|Ty\|^2 \\ & = \|x\|^2 + 2\langle x, y \rangle + \|y\|^2 - 2\langle x + y, x \rangle - 2\langle x + y, y \rangle \\ & \quad + \|x\|^2 + 2\langle x, y \rangle + \|y\|^2 \\ & = \|x\|^2 + 2\langle x, y \rangle + \|y\|^2 \\ & \quad - 2(\|x\|^2 + \langle y, x \rangle) - 2(\langle x, y \rangle + \|y\|^2) \\ & \quad + \|x\|^2 + 2\langle x, y \rangle + \|y\|^2 \\ & = 0. \end{align} $$
>>4. Así, $T$ es ortogonal. 
>>5. Ahora tratamos el caso general. Sea $T(0) = u \in \mathbb{R}^n$. Definimos $C(x) = T(x) - u$. 
>>6. Luego, $C(0) = T(0) - u = u - u = 0$ y es fácil ver que $C$ preserva distancias. 
>>7. Por lo anterior, $C$ es ortogonal y en consecuencia, $T(x) = C(x) + u$ con $C$ ortogonal
>>8. Osea $T$ es euclidea 

>[!Remark]
>Veamos a continuacion que como era de esperar la definicion de transformacion euclideana le da al origen un protagonismo que no tiene

>[!Proposition] Caso $n=1$
>Las transformaciones euclidianas de la recta real son traslaciones o reflexiones respecto de puntos en $\mathbb{R}$.
>> [!Proof]-
>> 1. Sabemos que $T(x) = \varepsilon x + u$, con $\varepsilon = \pm 1$ y $u \in \mathbb{R}$.
>> 2. Si $\varepsilon = 1$, $T$ es una traslación en $u$. 
>> 3. Veamos que si $\varepsilon = -1$, entonces $T$ es la reflexión en $u/2$. 
>> 4. En efecto notemos que $$ -\left(x - \frac{u}{2}\right) + \frac{u}{2} = -x + \frac{u}{2} + \frac{u}{2} = -x + u=T(x) $$
>> 5. Pero $-\left( x-\frac{u}{2} \right)+\frac{u}{2}$ es mover el origen a $\frac{u}{2}$ $x\mapsto x-\frac{u}{2}$ compuesto con hacer reflexion respecto del origen $x\mapsto -x$ compuesta con mover el origen a su punto original nuevamente $x\mapsto x+\frac{u}{2}$. Entonces esto es una reflexion respecto de $\frac{u}{2}$ 

>[!Definition] Caso $n=2$
>Denotamos por $R_{z, \theta}$ la rotación en ángulo $\theta$ alrededor del punto $z \in \mathbb{R}^2$. Se obtiene de conjugar $R_\theta$ por la traslación $x \mapsto x + z$, o sea,
> $$ R_{z, \theta}(x) = R_\theta(x - z) + z = R_{\theta}(x)+z-R_{\theta}(z) =R_{\theta}(x)+b$$
> Osea rotar alrededor del punto $z$ es una transformacion euclidea 

>[!Remark]
> En el práctico se ve que toda transformación rígida del plano es una traslación o una rotación alrededor de algún punto.

>[!Definition] Caso $n=3$
>Un **tirabuzón** es la composición de una rotación alrededor de una recta fija en $\mathbb{R}^3$ con una traslación a lo largo de esa recta.
>1) Esas transformaciones conmutan.
>2) Tanto la rotación como la traslación pueden ser la identidad. En el primer caso, el tirabuzón es una traslación y en el segundo, una rotación.

>[!Theorem] Teorema de Chasles
>Toda transformación rígida de $\mathbb{R}^3$ es un tirabuzón.
>>[!Proof]-
>>6. Supongamos que la transformación rígida es $T$, dada por $T(x) = Cx + u$, donde $C$ es una rotación, es decir una transformación ortogonal con $\det C = 1$.
>>7. Consideramos solo el caso particular en que $$ C = \begin{pmatrix} R_\theta & 0 \\ 0 & 1 \end{pmatrix}, $$ donde $R_\theta$ es la rotación en ángulo $\theta$ en el plano $x$-$y$. En cierto sentido se trata del caso general, pues vimos que cualquier rotación tiene esa forma en cierta base ortonormal.
>>8. Escribimos $$ x = \begin{pmatrix} x' \\ a \end{pmatrix} \quad \text{y} \quad u = \begin{pmatrix} u' \\ b \end{pmatrix}, $$ donde $x', u' \in \mathbb{R}^2$ y $a, b \in \mathbb{R}$.
>>9. Si $R_\theta$ es la identidad, entonces $T$ es la traslación en $u$.
>>10. Si no, tenemos que $$ T(x) = \begin{pmatrix} R_\theta & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} x' \\ a \end{pmatrix} + \begin{pmatrix} u' \\ b \end{pmatrix} = \begin{pmatrix} R_\theta x' + u' \\ a + b \end{pmatrix}. $$
>>11. Luego, $x' \mapsto R_\theta x' + u'$ es una transformación rígida del plano que no es una traslación. Sabemos que es la rotación en el mismo ángulo $\theta$ alrededor de cierto $z \in \mathbb{R}^2$. Entonces $$ T(x) = \begin{pmatrix} R_{z, \theta} x' \\ a + b \end{pmatrix} = \begin{pmatrix} R_\theta (x' - z) + z \\ a \end{pmatrix} + \begin{pmatrix} 0 \\ b \end{pmatrix}. $$
>>12. El primer término representa la rotación alrededor de la recta vertical $\{z\} \times \mathbb{R}$ y el segundo, la traslación vertical en $b$. $\square$

# Repaso de cálculo en varias variables

>[!Remark]
>Sea $\varphi : U \to \mathbb{R}^3$, donde $U$ es un abierto en $\mathbb{R}^2$,
>$$ \varphi(u, v) = (x(u, v), y(u, v), z(u, v)). $$
>Denotamos
>$$ \varphi_u(u, v) = \frac{\partial \varphi}{\partial u}(u, v) = \left. \frac{d}{dt} \right|_0 \varphi(u + t, v) $$
>y $\varphi_v(u, v)$ de manera análoga. Diremos que $\varphi$ es **suave** si las derivadas parciales de orden 3 de $\varphi$ existen y son continuas (esto es, si $\varphi$ es de clase $C^3$). Si $\varphi$ es de clase $C^1$ existe
>$$ d\varphi_{(u,v)} : \mathbb{R}^2 \to \mathbb{R}^3, $$
>llamada la **diferencial** de $\varphi$ en $(u, v)$, que es la única transformación lineal tal que
>$$ \lim_{h \to 0} \frac{\varphi(p + h) - \varphi(p) - d\varphi_p(h)}{\|h\|} = 0, $$
>donde $p = (u, v)$. La matriz de $d\varphi_p$ en la base canónica es
>$$ \begin{pmatrix} \left. \frac{\partial x}{\partial u} \right|_p & \left. \frac{\partial x}{\partial v} \right|_p \\ \left. \frac{\partial y}{\partial u} \right|_p & \left. \frac{\partial y}{\partial v} \right|_p \\ \left. \frac{\partial z}{\partial u} \right|_p & \left. \frac{\partial z}{\partial v} \right|_p \end{pmatrix}. $$
>
>**Comentarios.** Si $h \in \mathbb{R}^2$, $h \approx 0$, tenemos
>$$ \varphi(p + h) \approx \varphi(p) + d\varphi_p(h). $$
>La existencia de las derivadas parciales en $p$ no asegura la existencia de $d\varphi_p$.

# Superficies regulares

>[!Remark]
>Antes de dar la definición precisa, comentamos que una superficie regular es un subconjunto de $\mathbb{R}^3$ que localmente se puede mapear de manera suave a abiertos de $\mathbb{R}^2$.
>La definición de superficie regular está inspirada en la superficie de la Tierra y sus mapas.
>Un mapeo $\varphi$ lleva un abierto $U$ del plano (mapa) en un “abierto de la superficie”. Requeriremos que $\varphi : U \to \varphi(U)$ sea biyectiva, suave “con inversa continua”.

>[!Definition] Superficie regular
>Un subconjunto $S$ de $\mathbb{R}^3$ es una **superficie regular** si para todo $p \in S$ existe una función suave $\varphi : U \to \mathbb{R}^3$ definida en un abierto $U$ de $\mathbb{R}^2$ tal que:
>1) Se cumple que $p \in \varphi(U) \subset S$, $\varphi$ es inyectiva y $d\varphi_q : \mathbb{R}^2 \to \mathbb{R}^3$ es inyectiva para todo $q \in U$.
>2) Existe un conjunto abierto $\mathcal{V}$ de $\mathbb{R}^3$ tal que $\varphi(U) = \mathcal{V} \cap S$ y una función suave $\Phi : \mathcal{V} \to \mathbb{R}^2$ que satisface
>$$ \Phi(\varphi(q)) = q $$
>para todo $q \in U$.

^2d9e1d

>[!Remark]
>**Notación.** Las aplicaciones $\varphi : U \to \mathbb{R}^3$ como arriba se llaman **sistemas coordenados** o **cartas coordenadas**. Dada una superficie regular $S$, una función $\varphi : U \to \mathbb{R}^3$, con $U$ abierto en $\mathbb{R}^2$, y $\varphi(U) \subset S$ se dice una **parametrización** de $S$ si $d\varphi_q : \mathbb{R}^2 \to \mathbb{R}^3$ es inyectiva para todo $q \in U$.

>[!Proposition]
>Sean $U$ un abierto en $\mathbb{R}^2$ y $\varphi : U \to \mathbb{R}^3$ una función suave. Son equivalentes:
>- (a) Para toda curva regular $\alpha : (a, b) \to U$ se cumple que $\varphi \circ \alpha$ es una curva regular.
>- (b) La diferencial $d\varphi_q : \mathbb{R}^2 \to \mathbb{R}^3$ es inyectiva para todo $q \in U$.
>
>O sea, $\varphi$ preserva la regularidad de curvas si y solo si $\varphi$ es infinitesimalmente inyectiva.
>>[!Proof]-
>>- b) $\Rightarrow$ a) 
>>	1. Sea $\alpha : (a, b) \to U$ una curva regular entonces $\alpha '\neq0$ . 
>>	2. Por la regla de la cadena (considerando que la diferencial es una matriz y por hipotesis inyectiva entonces su nucleo es el 0) tenemos que $$ (\varphi \circ \alpha)'(t) = d\varphi_{\alpha(t)}(\alpha'(t)) \ne 0 $$ para todo $t$.
>>- a) $\Rightarrow$ b) 
>>	1. Sean $q \in U$ y $z \in \mathbb{R}^2$, $z \ne 0$. Basta mostrar $d\varphi_q(z) \ne 0$.
>>	2. Sea $\alpha(t) = q + tz$ una curva en $U$ (entonces es regular) , definida para $t$ suficientemente pequeño, así $\alpha(t) \in U$. 
>>	3. Por hipótesis $\varphi \circ \alpha$ es regular. Entonces $$ 0 \ne (\varphi \circ \alpha)'(0) = d\varphi_{\alpha(0)}(\alpha'(0)) = d\varphi_{q}(z), $$ como deseábamos.

>[!Remark]
>En general tendremos $\varphi(u, v) = (x(u, v), y(u, v), z(u, v))$. Si $q = (u, v)$,
>$$ [d\varphi_q]_{\text{can}} = \begin{pmatrix} x_u(q) & x_v(q) \\ y_u(q) & y_v(q) \\ z_u(q) & z_v(q) \end{pmatrix}. $$
>Las siguientes afirmaciones son equivalentes:
>- La transformación lineal $d\varphi_q$ es inyectiva.
>- La matriz $[d\varphi_q]_{\text{can}}$ tiene rango 2, es decir, las columnas son linealmente independientes.
>- El producto cruz de las columnas es distinto de cero, o sea, $\varphi_u(q) \times \varphi_v(q) \ne 0$.
>- Alguna submatriz $2 \times 2$ de $[d\varphi_q]_{\text{can}}$ tiene determinante no nulo.

>[!Proposition] Grafico de funcion es superficie
>Sea $A$ un abierto de $\mathbb{R}^2$ y sea $f : A \to \mathbb{R}$ una función suave. Sea $S$ el gráfico de $f$, es decir,
>$$ S = \{(x, y, f(x, y)) \mid (x, y) \in A\}. $$
>El subconjunto $S$ está cubierto por una sola carta coordenada. 
>>[!Proof]-
>>4. Sean $U = A$ y $$ \varphi : U \to \mathbb{R}^3, \quad \varphi(u, v) = (u, v, f(u, v)). $$
>>5. Verificamos (1): $\varphi$ es inyectiva pues $(u, v, f(u, v)) = (x, y, f(x, y))$ solo si $(u, v) = (x, y)$. Calculamos $$ [d\varphi_{(u,v)}]_{\text{can}} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \\ f_u(u, v) & f_v(u, v) \end{pmatrix}, $$que tiene rango 2 porque, por ejemplo, $\det \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = 1 \ne 0$.
>>6. Para verificar (2) podemos tomar $\mathcal{V} = U \times \mathbb{R}$, que es un subconjunto abierto de $\mathbb{R}^3$, y $\Phi(x, y, z) = (x, y)$. 
>>7. Se cumple que $$ \Phi(\varphi(u, v)) = \Phi(u, v, f(u, v)) = (u, v). $$
>>8. La comprobación del siguiente hecho queda como ejercicio: $$ \varphi(U) = \mathcal{V} \cap S. $$
>>9. Como $U=A$ entonces $S\subseteq \mathcal{V}$ entonces es ver que $\varphi(U)=S$ que es evidente por definicion  

>[!Remark]
>El punto (2) de la definición de superficie regular requiere la existencia de inversas a derecha continuas locales $\Phi$. Las necesitamos para excluir subconjuntos como el siguiente:
>![[Pasted image 20251122145538.png]]

>[!Example] 
>Veamos un ejemplo de aplicacion suave, inyectiva y con diferencial inyectiva pero que no llega a ser carta por que no es inversible localmente 
>Sean $\alpha : (-\pi, \pi) \to \mathbb{R}^2$ y $\varphi : U = (-\pi, \pi) \times \mathbb{R} \to \mathbb{R}^3$ definidas por
>$$ \alpha(s) = \sin s (\cos s, 1) \quad \text{y} \quad \varphi(s, t) = (\alpha(s), t). $$
>a) La aplicación $\varphi$ es suave, inyectiva y $d\varphi_q$ es inyectiva para todo $q \in U$.
>b) Dado cualquier entorno abierto $\mathcal{V}$ del origen en $\mathbb{R}^3$, no existe una función continua $\Phi : \mathcal{V} \to \mathbb{R}^2$ tal que
>$$ \Phi(\varphi(s, t)) = (s, t) $$
>para todo $(s, t)$ en un entorno abierto del origen en $\mathbb{R}^2$.
>![[Pasted image 20251122150201.png]]
>>[!Proof]-
>>- a) 
>>	1. La aplicación $\varphi$ es suave e inyectiva pues $\alpha$ lo es. La diferencial $d\varphi_q$ es inyectiva para todo $q \in U$ pues $\alpha$ es regular. (Verificarlo.)
>>- b) 
>>	1. Calculamos $\varphi(0, 0) = (\alpha(0), 0) = ((0, 0), 0)$. 
>>	2. Consideramos la sucesión $$ p_n = \varphi\left(-\pi + \frac{1}{n}, 0\right) = \left(\alpha\left(-\pi + \frac{1}{n}\right), 0\right) = \left(\sin\left(-\pi + \frac{1}{n}\right) \left(\cos\left(-\pi + \frac{1}{n}\right), 1\right), 0\right). $$
>>	3. Tenemos que $$ \lim_{n \to \infty} p_n = \lim_{n \to \infty} \varphi\left(-\pi + \frac{1}{n}, 0\right) = (\sin(-\pi) (\cos(-\pi), 1), 0) = ((0, 0), 0) = \varphi(0, 0). $$
>>	4. Suponemos que existen $\mathcal{V}$ y $\Phi$ como en el enunciado (osea una inversa local). Como $\Phi$ es continua, resulta $$ \lim_{n \to \infty} \Phi(p_n) = \Phi(\varphi(0, 0)) = (0, 0). $$
>>	5. Por otro lado $$ \lim_{n \to \infty} \Phi(p_n) = \lim_{n \to \infty} \Phi\left(\varphi\left(-\pi + \frac{1}{n}, 0\right)\right) = \lim_{n \to \infty} \left(-\pi + \frac{1}{n}, 0\right) = (-\pi, 0), $$con lo cual llegamos a un absurdo.

>[!Theorem] Teorema de la superficie implícita
>Sea $F : A \to \mathbb{R}$ una función suave, donde $A$ es un subconjunto abierto de $\mathbb{R}^3$. Sea $y \in \text{Imagen}(F)$ y sea
>$$ S = F^{-1}(\{y\}) = \{q \in A \mid F(q) = y\} $$
>el conjunto de nivel $y$ de $F$. Si $(\nabla F)(q) \ne 0$ para todo $q \in S$, entonces $S$ es una superficie regular.
>>[!Proof]-
>>6. Sea $q \in S$. Por hipótesis, $$ (\nabla F)(q) = (F_x(q), F_y(q), F_z(q)) \ne 0. $$
>>7. Luego, al menos una de las derivadas parciales de $F$ en $q$ es no nula, digamos, $F_z(q) \ne 0$.
>>8. Por el Teorema de la Función Implícita existen un subconjunto abierto $U$ de $\mathbb{R}^2$, una función suave $f : U \to \mathbb{R}$ y $\varepsilon > 0$ tales que si $\mathcal{V} = U \times (q_3 - \varepsilon, q_3 + \varepsilon)$ (subconjunto abierto de $\mathbb{R}^3$), entonces se cumple que $$ S \cap \mathcal{V} = \{(x, y, f(x, y)) \mid (x, y) \in U\}. $$ Y ademas $(q_{1},q_{2},q_{3})=(q_{1},q_{2},f(q_{1},q_{2}))\in S\cap\mathcal{V}$ 
>>9. Si $F_x(q) \ne 0$ o $F_y(q) \ne 0$, se cambian los roles de $x, y, z$ y $S$, cerca de $q$, resulta el gráfico de una función de $(y, z)$ o $(x, z)$.
>>10. Para mostrar que $S$ es una superficie regular, para cada $q \in S$ tomamos $$ \varphi : U \to \mathbb{R}^3, \quad \varphi(u, v) = (u, v, f(u, v)), $$ con $U$ y $f$ como arriba.
>>11. La verificación de los apartados (1) y (2) de la definición de superficie regular es la misma de que los gráficos de funciones son superficies regulares, con $\mathcal{V}$ también como arriba.
>>12. Osea que para cada $q\in S$ tengo un entorno donde puedo armar una carta. Entonces $S$ es superficie 

^14271e

>[!Proposition]
>Sea $S$ una superficie regular y sea $p \in S$. Si una función $\varphi : U \to \mathbb{R}^3$ satisface las condiciones del apartado (1) de la definición de superficie regular, entonces satisface también las del (2).
>>[!Proof]
>>No damos la prueba.

>[!Remark]
>- Se usa para obtener cartas coordenadas cuando por alguna razón ya sabemos que el subconjunto es una superficie regular, por ejemplo, a través del Teorema de la Superficie Implícita, o porque ya hemos hemos encontrado algunas cartas que cubren toda la superficie y para ellas hemos verificado (1) y (2).
>- “Un subconjunto bueno no puede tener cartas malas”.

>[!Definition]
>Una superficie regular $S$ se dice **conexa** si para todo par de puntos $p$ y $q$ de $S$ existe una curva suave a trozos $\alpha : [a, b] \to S$ con $\alpha(a) = p$ y $\alpha(b) = q$.

>[!Example]
>Sea $S$ le hiperboloide de dos hojas,
>$$ S = \{(x, y, z) \in \mathbb{R}^3 \mid z^2 - x^2 - y^2 = 1\}, $$
>que es una superficie regular. Esto se puede mostrar de dos maneras:
>- Cubriendo $S$ con las cartas coordenadas $\varphi_{\pm}(u, v) = (u, v, \pm\sqrt{1 + u^2 + v^2})$.
>- O mediante el Teorema de la Superficie Implícita, considerando
>$$ F(x, y, z) = z^2 - x^2 - y^2, \quad (\nabla F)(x, y, z) = (-2x, -2y, 2z), $$
>que no se anula en $S$.
>Sin embargo la superficie $S$ no es conexa.
>>[!Proof]-
>>13. Sean $p = (0, 0, -1)$ y $q = (0, 0, 1)$. Supongamos que existe una curva $\alpha$ como en la definición de superficie conexa. Tenemos que $$ \alpha(t) = (x(t), y(t), z(t)), $$ para ciertas funciones continuas $x, y, z : [a, b] \to \mathbb{R}$.
>>14. Como $z$ es continua, $z(a) = -1$ y $z(b) = 1$, por el Teorema de los Valores Intermedios existe $t_o \in [a, b]$ tal que $z(t_o) = 0$.
>>15. Entonces $\alpha(t_o) = (x(t_o), y(t_o), 0)$.
>>16. Como $\alpha(t_o) \in S$ resulta que $0 - x(t_o)^2 - y(t_o)^2 = 1$, con lo que llegamos a un absurdo.

# Funciones suaves definidas en superficies


>[!Remark]
>Las funciones suaves del cálculo de varias variables están definidas en subconjuntos abiertos de $\mathbb{R}^n$.

>[!Lemma] Lema del diagrama triangular
>Sea $S$ una superficie regular y sea $\varphi : U \to \mathbb{R}^3$ una carta coordenada de $S$. Sean $A$ un subconjunto abierto de $\mathbb{R}^m$ y $f : A \to \mathbb{R}^3$ una función suave tal que $f(A) \subset \varphi(U)$. Entonces $\varphi^{-1} \circ f : A \to \mathbb{R}^2$ es suave.
>![[Pasted image 20251122172334.png]]
>>[!Proof]-
>>1. Recordemos [[Definiciones#^2d9e1d]] nos dice que $\varphi(U)=\mathcal{V}\cap S$ y que $\Phi$ está definida en $\mathcal{V}$ entonces esta definida en $\varphi(U)$ con lo cual es logico hablar de $\varphi^{-1}$ en $f(A)\subseteq \varphi(U)$       
>>2. Como $\varphi : U \to \mathbb{R}^3$ es una carta coordenada, existen un abierto $\mathcal{V}$ de $\mathbb{R}^3$ y una función suave $\Phi : \mathcal{V} \to \mathbb{R}^2$ tal que $\Phi \circ \varphi = \text{id}_U$.
>>3. Veamos que $$ \varphi^{-1} \circ f = \Phi \circ f $$ con lo cual $\varphi^{-1} \circ f$ es suave, por ser composición de funciones suaves.
>>4. En efecto, debemos ver que $$ \varphi^{-1}(f(z)) = \Phi(f(z)) $$ para todo $z \in A$.
>>5. Como $f(A) \subset \varphi(U)$, tenemos que $f(z) = \varphi(q)$ para cierto $q \in U$.
>>6. Entonces la igualdad anterior equivale a $\varphi^{-1}(\varphi(q)) = \Phi(\varphi(q))$, que es verdadera para todo $q \in U$ (pues ambas son iguales a $q$).

^408c1f

>[!Remark]
>- Como $\varphi^{-1}$ no está definida en un abierto de $\mathbb{R}^3$, no tiene sentido decir que $\varphi^{-1}$ sea suave.
>- El lema del diagrama triangular no vale para el cilindro sobre el ocho. 

>[!Proposition] Cambio de coordenadas
>Sean $\varphi : U \to \mathbb{R}^3$ y $\psi : V \to \mathbb{R}^3$ dos sistemas coordenados de una superficie regular $S$ tal que $W := \varphi(U) \cap \psi(V) \ne \emptyset$. Entonces
>$$ U' := \varphi^{-1}(W) \quad \text{y} \quad V' :=\psi^{-1}(W) $$
>son subconjuntos abiertos de $\mathbb{R}^2$ y $\psi^{-1} \circ \varphi : U' \to V'$ es una función suave, llamada el **cambio de coordenadas** de $\varphi$ a $\psi$.
>![[Pasted image 20251122173149.png]]
>>[!Proof]-
>>1. Comenzamos mencionando que en el práctico se ve que si $A$ es un subconjunto abierto de $\mathbb{R}^n$ y $f : A \to \mathbb{R}^m$ es continua, entonces $f^{-1}(B)$ es abierto en $\mathbb{R}^n$ para todo subconjunto abierto $B$ de $\mathbb{R}^m$.
>>2. Sabemos que $\varphi(U) = S \cap \mathcal{U}$ y $\psi(V) = S \cap \mathcal{V}$ para ciertos subconjuntos abiertos $\mathcal{U}$ y $\mathcal{V}$ de $\mathbb{R}^3$. Luego
>>$$ W = S \cap (\mathcal{U} \cap \mathcal{V}), $$
>>donde $\mathcal{U} \cap \mathcal{V}$ es abierto en $\mathbb{R}^3$.
>>3. Así resulta que $U' = \varphi^{-1}(\mathcal{U} \cap \mathcal{V})$ y que este es un subconjunto abierto de $\mathbb{R}^2$. Notar que $\varphi ^{-1}(\mathcal{U}\cap\mathcal{V})=\varphi ^{-1}(S\cap\mathcal{U}\cap\mathcal{V})$ por que $\varphi(U)\subseteq S$ 
>>4. Con $V'$ se procede análogamente.
>>5. Finalmente, $\psi^{-1} \circ \varphi$ es suave por [[Definiciones#^408c1f]] recordando que $\varphi$ es suave por ser carta de coordenadas 

>[!Definition] Suavidad para funciones con superficie en dominio
>Sea $S\subseteq \mathbb{R}^{3}$ una superficie regular y sea $p \in S$. Una función $f : S \to \mathbb{R}^n$ se dice **suave en** $p$ si existe una carta coordenada $\varphi : U \to \mathbb{R}^3$ de $S$ con $p \in \varphi(U)$ tal que $f \circ \varphi : U \to \mathbb{R}^n$ es suave en $\varphi^{-1}(p)$.
>La función $f$ se dice **suave** si es suave en $p$ para todo $p \in S$.

>[!Example]-
>- Sea $S$ una superficie regular contenida en un subconjunto abierto $A$ de $\mathbb{R}^3$ y sea $F : A \to \mathbb{R}^n$ una función suave. Entonces $F|_S : S \to \mathbb{R}^n$ es suave. En efecto, sea $p \in S$ y sea $\varphi$ un sistema coordenado cuya imagen lo contenga. Como $S \subset A$,
>$$ F|_S \circ \varphi = F \circ \varphi, $$
>que es la composición de funciones suaves.
>Un caso particular se da cuando $A = \mathbb{R}^3$ y $F$ es la **función altura** respecto de un vector unitario $u \in \mathbb{R}^3$, es decir $F(q) = \langle q, u \rangle$.
>
>- Sea $S$ una superficie regular y sea $\varphi : U \to \mathbb{R}^3$ una carta coordenada de $S$. Tenemos que $\varphi(U)$ también es una superficie regular (en el práctico se ve que la intersección de una superficie regular con un abierto de $\mathbb{R}^3$ es una superficie regular). Resulta que $\varphi^{-1} : \varphi(U) \to \mathbb{R}^2$ es suave. En efecto, $\varphi^{-1} \circ \varphi = \text{id}|_U : U \to U \subset \mathbb{R}^2$ es suave. Resumiendo: Las funciones coordenadas son suaves.

>[!Proposition]
>Supongamos que existe una carta coordenada $\varphi$ como en la definición (osea que cumple $f\circ \varphi$ es suave) y que $\psi : V \to \mathbb{R}^3$ es una carta coordenada de $S$ con $p \in \psi(V)$. Entonces $f \circ \psi$ es suave en $\psi^{-1}(p)$.
>>[!Proof]-
>>6. Se deduce de que el cambio de coordenadas es suave. En algún abierto de $\mathbb{R}^2$ que contiene a $\varphi^{-1}(p)$ se cumple que
>>$$ f \circ \psi = f \circ (\varphi \circ \varphi^{-1}) \circ \psi = (f \circ \varphi) \circ (\varphi^{-1} \circ \psi), $$
>>que es la composición de funciones suaves.

^1bccd0

>[!Definition] Restriccion de funcion suave es suave
>Sea $L:\mathbb{R}^{3}\rightarrow \mathbb{R}^{n}$ suave entonces y sea $F=L|_{S}:S\rightarrow \mathbb{R}^{n}$ con $S$ una superficie entonces $F$ es suave.
>>[!Proof]-
>>1. Sea $\varphi :\mathbb{R}^{n}\rightarrow S$ cualquier carta de $S$ entonces $F\circ \varphi =L\circ\varphi$
>>2. Pero $L$ y $\varphi$ son suaves entonces $F\circ\varphi$ lo es. Mostrando que $F$ es suave

>[!Proposition]
>Sean $M$ y $N$ dos superficies regulares y sea $F : M \to \mathbb{R}^3$ una función suave tal que $F(M) \subset N$. Entonces para todo $p \in M$ existen sistemas coordenados $\varphi : U \to M$ y $\psi : V \to N$ de $M$ y $N$ respectivamente tales que $p \in \varphi(U)$, $F(\varphi(U)) \subset \psi(V)$ y $\psi^{-1} \circ F \circ \varphi$ es suave.
>>[!Proof]- Idea de la prueba
>>3. Como $\psi$ es un sistema coordenado, tenemos que $\psi(V) = N \cap \mathcal{V}$, donde $\mathcal{V}$ es un subconjunto abierto de $\mathbb{R}^3$. 
>>4. Sea $\bar{\varphi} : \bar{U} \to M$ un sistema coordenado con $p \in \bar{\varphi}(\bar{U})$. Como $F$ es suave, la composicion con cualquier carta es suave [[Definiciones#^1bccd0]]
>>5. Entonces $F \circ \bar{\varphi} : \bar{U} \to \mathbb{R}^3$ es suave, y en particular es continua, resulta que $U :=(F \circ \bar{\varphi})^{-1}(\mathcal{V})$ es abierto en $\bar{U}$. 
>>6. Podemos tomar $\varphi = \bar{\varphi}|_U$, que es un sistema coordenado de $M$ que va a cumplir que $F(\varphi(U)) \subset \psi(V)$ y satisfacer que $\psi^{-1} \circ F \circ \varphi$ es suave, por el lema del diagrama triangular.

>[!Definition]
>Sean $M$ y $N$ dos superficies regulares, decimos que $F:M\rightarrow N$ es suave en $p \in M$ si existen cartas $\varphi:U\rightarrow M$ con $p \in \varphi(U)$ y $\psi: V\rightarrow N$ con $F(p)\in \psi (V)$ tales que $$\psi ^{-1}\circ F\circ \varphi: U\rightarrow V$$ es suave como funcion entre abiertos de $R_{2}$ 

>[!Definition]
>Sean $M$ y $N$ superficies regulares. Una función suave $F : M \to N$ se dice **difeomorfismo** si tiene inversa $F^{-1} : N \to M$ y esta es suave. En este caso, $M$ y $N$ se dicen **difeomorfas**.

>[!Example]- Ejemplos de difeomorfismos
>- La esfera $S^2$ y el elipsoide $N = \{(x, y, z) \in \mathbb{R}^3 \mid \frac{x^2}{9} + \frac{y^2}{4} + z^2 = 1\}$ son superficies difeomorfas.
>>[!Proof]-
>>7. Consideremos la aplicación $F: S^2 \to N$ dada por $F(x, y, z) = (3x, 2y, z)$.
>>8. Esta función es suave pues es la restricción de la aplicación lineal (y por tanto suave) $L: \mathbb{R}^3 \to \mathbb{R}^3$, $L(x, y, z) = (3x, 2y, z)$.
>>9. Su inversa es $G: N \to S^2$ dada por $G(u, v, w) = (u/3, v/2, w)$, que también es suave por ser restricción de una lineal.
>>10. Verifiquemos que $F$ envía $S^2$ en $N$: Si $x^2 + y^2 + z^2 = 1$, entonces $$ \frac{(3x)^2}{9} + \frac{(2y)^2}{4} + z^2 = x^2 + y^2 + z^2 = 1. $$
>>11. Verifiquemos que $G$ envía $N$ en $S^2$: Si $\frac{u^2}{9} + \frac{v^2}{4} + w^2 = 1$, entonces $$ (u/3)^2 + (v/2)^2 + w^2 = \frac{u^2}{9} + \frac{v^2}{4} + w^2 = 1. $$
>>12. Por lo tanto, $F$ es un difeomorfismo.
>- El cuadrado $M = \{(x, y, 0) \mid |x| < \pi/2, |y| < \pi/2\}$ y el plano $N = \mathbb{R}^2 \times \{0\}$ son difeomorfos.
>>[!Proof]-
>>13. Consideremos la aplicación $F : M \to N$ dada por $F(x, y, z) = (\tan x, \tan y, 0)$.
>>14. Esta función es suave pues es la restricción de la función $\tilde{F}(x, y, z) = (\tan x, \tan y, 0)$ definida en el abierto $(-\pi/2, \pi/2) \times (-\pi/2, \pi/2) \times \mathbb{R}$ de $\mathbb{R}^3$.
>>15. Su inversa es $G : N \to M$ dada por $G(u, v, w) = (\arctan u, \arctan v, 0)$.
>>16. La función $G$ es suave pues es la restricción de $\tilde{G}(u, v, w) = (\arctan u, \arctan v, 0)$ definida en todo $\mathbb{R}^3$.
>>17. Claramente $F$ y $G$ son inversas una de la otra debido a que $\tan(\arctan t) = t$ para todo $t \in \mathbb{R}$ y $\arctan(\tan s) = s$ para todo $s \in (-\pi/2, \pi/2)$.
>- Sea $S^2$ la esfera de radio 1 centrada en el origen y sean $p_n = (0, 0, 1)$ y $p_s = (0, 0, -1)$ los polos sur y norte, respectivamente. Sean $M = S^2 - \{p_n, p_s\}$ y $C$ el cilindro $\{(x, y, z) \in \mathbb{R}^3 \mid x^2 + y^2 = 1\}$. Veamos que $M$ y $C$ son difeomorfas. 
>>[!Proof]-
>>18. Buscamos un difeomorfismo $f : C \to M$. Sea $$ f : C \to M, \quad f(q) = \frac{q}{\|q\|}, $$cuya imagen está contenida en $S^2$ y no contiene ninguno de los polos. 
>>19. La función $f$ es suave porque es la restricción al cilindro de la función $F : \mathbb{R}^3 - \{(0, 0, 0)\} \to \mathbb{R}^3$ definida por la misma fórmula (que es suave en ese dominio).
>>20. Veamos que $f$ tiene inversa suave. La proponemos de la forma $$ g : M \to C, \quad g(x, y, z) = \lambda(x, y, z)(x, y, z). $$Para que llegue a $C$ necesitamos que $$ (\lambda(x, y, z)x)^2 + (\lambda(x, y, z)y)^2 = 1. $$Equivalentemente, $\lambda(x, y, z) = 1/\sqrt{x^2 + y^2}$. 
>>21. Así, consideramos$$ g(x, y, z) = \frac{1}{\sqrt{x^2 + y^2}}(x, y, z). $$
>>22. Dejamos como ejercicio verificar que $g$ es suave (por ser la restricción de la función suave $G : A \to \mathbb{R}^3$ definida por la misma fórmula en un abierto $A$ de $\mathbb{R}^3$, ¿quién es $A$?) y que es la inversa de $f$.
>- Dado un cilindro como el del ejemplo anterior tenemos $\varphi:\mathbb{R}^{2}\rightarrow\mathbb{R}^{3}$ dada por $$\varphi(s,t)=(\cos s,\sin s,t)$$ es parametrizacion suryectiva del cilindro $C$. A partir de esto tenemos que $F:C\rightarrow C$ dada por $$F(\varphi(s, t)) = \varphi(s + t, t). $$ es un difeomorfismo entre cilindros.
>>[!Proof]-
>>23. Notemos que como $\varphi$ esta definida en todo $\mathbb{R}^{2}$ tenemos muchos valores repetidos en el dominio que van a una misma imagen. Entonces debemos ver que $F$ manda esos valores reptidos en la imagen a un mismo valor
>>24. Veamos $F$ está bien definida. Notar $\varphi(\mathbb{R}^2) = C$ y se verifica que $\varphi(s, t) = \varphi(s', t')$ esto implica que $\varphi(s + t, t) = \varphi(s' + t', t')$. En efecto, $\varphi(s, t) = \varphi(s', t')$ solo si $t' = t$ y $s' = s + 2k\pi$ con $k \in \mathbb{Z}$, con lo cual $$ \varphi(s' + t', t') = (\cos(s' + t'), \sin(s' + t'), t') = (\cos(s + 2k\pi + t), \sin(s + 2k\pi + t), t) = \varphi(s + t, t). $$
>>25. La función $F$ es suave pues $F \circ \varphi$ es suave pues $\varphi$ es suave por ser carta y $\varphi(s+t,t)$ es $\varphi$ compuesta con desplazar en primera coordenada que es suave 
>>26. (para estar más ajustados a la definición, se puede restringir $\varphi$ a franjas verticales de ancho menor que $2\pi$, con el fin de que resulte inyectiva).
>>27. La inversa está dada por $F^{-1}(\varphi(s, t)) = \varphi(s - t, t)$. Los mismos argumentos que se aplicaron para $\varphi$ sirven para mostrar que $F^{-1}$ está bien definida y es suave. Se verifica fácilmente que $F \circ F^{-1} = F^{-1} \circ F = \text{id}_C$.

# Plano Tangente

>[!Definition]
>Sea $S$ una superficie regular y sea $p \in S$. El **plano tangente** a $S$ o **espacio tangente** a $S$ en el punto $p$ se define mediante
>$$ T_pS = \{\alpha'(0) \mid \alpha \text{ es una curva suave en } S \text{ con } \alpha(0) = p\}. $$

>[!Proposition]
>Sea $\varphi : U \to \mathbb{R}^3$ un sistema coordenado de la superficie $S$ con $p \in \varphi(U)$, $p = \varphi(q)$. Entonces $T_pS$ es la imagen de la transformación lineal $d\varphi_q : \mathbb{R}^2 \to \mathbb{R}^3$, es decir
>$$ T_pS = d\varphi_q(\mathbb{R}^2). $$
>En particular, $T_pS$ es un subespacio vectorial de dimensión dos de $\mathbb{R}^3$ y $\{\varphi_u(q), \varphi_v(q)\}$ es una base de $T_pS$.
>>[!Proof]-
>>- $\subset$ 
>>	1. Sea $x \in T_pS$. Sea $\alpha : (-\varepsilon, \varepsilon) \to S$ una curva suave tal que $\alpha(0) = p$, $\alpha(-\varepsilon, \varepsilon) \subset \varphi(U)$ y $\alpha'(0) = x$. 
>>	2. Tenemos que $$ \varphi^{-1}(\alpha(t)) = (u(t), v(t)) $$para ciertas funciones suaves $u, v : (-\varepsilon, \varepsilon) \to \mathbb{R}$ [[Definiciones#^408c1f]]
>>	3. Así $$ \alpha(t) = \varphi(u(t), v(t)). $$
>>	4. Por la regla de la cadena (multiplicando la matriz $D\varphi$ con el vector $(u'(0),v'(0))$) , $$ \alpha'(0) = \varphi_u(u(0), v(0))u'(0) + \varphi_v(u(0), v(0))v'(0). $$ (notar $\varphi_{u}$ es un vector)(esto prueba tambien que es base) 
>>	5. Ademas por 1. $\varphi(q)=p=\alpha (0)=\varphi(u(0),v(0))$ entonces $q=(u(0),v(0))$  $$x = \alpha'(0) = \varphi_u(q)u'(0) + \varphi_v(q)v'(0)$$que pertenece a la imagen de $d\varphi_q$, pues $\varphi_u(q) = d\varphi_q(e_1)$ y $\varphi_v(q) = d\varphi_q(e_2)$.
>>- $\supset$
>>	1. Dado $(a, b) \in \mathbb{R}^2$, escribimos $$ d\varphi_q(a, b) = d\varphi_q\left(\frac{d}{dt}\Big|_0 (q + t(a, b))\right) = \frac{d}{dt}\Big|_0 \varphi(q + t(a, b)) = \alpha'(0), $$donde $\alpha(t) = \varphi(q + t(a, b))$, que es una curva suave en $S$ con $\alpha(0) = \varphi(q) = p$ (Notar $d\varphi_{q}$ es la diferencial y usamos regla de cadena notar que diferencial de $\varphi$ evaluada $q+t(a,b)=\alpha (t)$ evaluada en $0$ que es $q$ todo eso multiplicado por $\frac{d}{dt}\Big|_0 (q + t(a, b))$   pero multiplicar matriz por vector es lo mismo que evaluar la transformacion lineal dada por la matriz)  

>[!Remark]
>A pesar de que $T_pS$ es un subespacio de $\mathbb{R}^3$, se acostumbra dibujarlo con el cero apoyado en $p$.

>[!Definition]
>El **plano tangente afín** a $S$ en $p$ es $p + T_pS = \{p + u \mid u \in T_pS\}$.

>[!Definition] Valor regular
>Antes de la siguiente proposición, decimos que $y$ es un **valor regular** de una función
>$$F : A \to \mathbb{R}$$
>definida en un subconjunto abierto $A$ de $\mathbb{R}^3$ si $F^{-1}(\{y\}) \ne \emptyset$ (es decir, $y$ pertenece a la imagen de $F$) y $dF_q \ne 0$ (equivalentemente, $(\nabla F)(q) \ne 0$) para todo $q \in F^{-1}(\{y\})$.
>
>También, dado $v \in \mathbb{R}^3$, definimos
>$$ v^{\perp} = \{u \in \mathbb{R}^3 \mid \langle v, u \rangle = 0\}. $$

>[!Proposition] Espacio tangente de una superficie implícita
>Sea $A$ un subconjunto abierto de $\mathbb{R}^3$, sea $F : A \to \mathbb{R}$ una función suave con valor regular $y$, y sea $S$ la superficie $F^{-1}(\{y\})$ [[Definiciones#^14271e]]. Entonces, para todo $p \in S$,
>
>$$ T_pS = \ker(dF_p) = \big( (\nabla F)_p \big)^{\perp}. $$
>Notar $dF_{p}=\nabla F_{p}:\mathbb{R}^{3}\rightarrow \mathbb{R}$ osea es un vector en $\mathbb{R}^{3}$ tambien una transformacion lineal y se evalua con un vector de $\mathbb{R}^{3}$ que es lo mismo que hacer el producto interno (evaluar una "matriz" (vector) es multiplicar la matriz)       
>>[!Proof]-
>>- $\subset$) 
>>	1. Sea $x \in T_pS$. Sea $\alpha : (-\varepsilon, \varepsilon) \to S$ una curva suave tal que $\alpha(0) = p$, y $\alpha'(0) = x$. 
>>	2. Veamos que $x \in \ker(dF_p)$.Por la regla de la cadena,$$ dF_p(x) = dF_p(\alpha'(0)) = \frac{d}{dt}\Big|_0 F(\alpha(t)) = \frac{d}{dt}\Big|_0 y = 0. $$
>>- $\supset$) 
>>	1. Sabemos de la proposición anterior que $T_pS$ es un subespacio de dimensión 2.
>>	2. Además, acabamos de mostrar que está contenido en $\ker(dF_p)$. Entonces resta solo mostrar que $\ker(dF_p)$ tiene dimensión 2.
>>	3. Como $y$ es un valor regular, $dF_p : \mathbb{R}^3 \to \mathbb{R}$ es una transformación lineal no nula, en particular su imagen es $\mathbb{R}$. 
>>	4. Así,
>>$$ \dim(\ker(dF_p)) = 3 - \dim(\text{Imagen}(dF_p)) = 3 - 1 = 2, $$

>[!Example]-
>Sea $S$ la esfera de radio 1 centrada en el origen y sea $p \in S$. Entonces $$ T_pS = p^{\perp}. $$
>>[!Proof]
>>1. En efecto, $S = F^{-1}(\{1\})$, donde 1 es un valor regular de $F(x, y, z) = x^2 + y^2 + z^2$.
>>2. Calculamos $$ \nabla F(x, y, z) = (2x, 2y, 2z). $$
>>3. Luego $(\nabla F)_p = 2p \ne 0$ para todo $p \in S$ y así, $(\nabla F)_p^{\perp} = (2p)^{\perp} = p^{\perp}$.

>[!Definition]
>Sea $f : S \to \mathbb{R}^n$ una función suave y sea $p \in S$. Se define $df_p : T_pS \to \mathbb{R}^n$ mediante
>$$ df_p(\alpha'(0)) = (f \circ \alpha)'(0) = \frac{d}{dt}\Big|_0 f(\alpha(t)), $$
>donde $\alpha : (-\varepsilon, \varepsilon) \to S$ es una función suave con $\alpha(0) = p$.

>[!Proposition]
>La definición es buena y $df_p$ es lineal; se llama la **diferencial** de $f$ en $p$.
>>[!Proof]-
>>1. Sean $\alpha, \beta : (-\varepsilon, \varepsilon) \to S$ dos curvas suaves con $$ \alpha(0) = \beta(0) = p \quad \text{y} \quad \alpha'(0) = \beta'(0). $$
>>2. Debemos mostrar que $$ (f \circ \alpha)'(0) = (f \circ \beta)'(0). $$
>>3. Sea $\varphi : U \to \mathbb{R}^3$ un sistema coordenado de $S$ con $p \in \varphi(U)$, digamos, $p = \varphi(u_o, v_o)$.
>>4. Achicando $\varepsilon$ si fuera necesario, tenemos que las trayectorias de $\alpha$ y $\beta$ están contenidas en $\varphi(U)$ y $$ \alpha(t) = \varphi(u(t), v(t)), \quad \beta(t) = \varphi(x(t), y(t)), $$donde $u, v, x, y : (-\varepsilon, \varepsilon) \to \mathbb{R}$ son funciones suaves, por el lema del diagrama triangular, y satisfacen $x(0) = u(0) = u_o$ e $y(0) = v(0) = v_o$. 
>>5. Calculamos $$ \alpha'(0) = \varphi_u(u_o, v_o)u'(0) + \varphi_v(u_o, v_o)v'(0), $$ $$ \beta'(0) = \varphi_u(u_o, v_o)x'(0) + \varphi_v(u_o, v_o)y'(0). $$
>>6. Como $\alpha'(0) = \beta'(0)$, resulta que $$ u'(0) = x'(0) \quad \text{y} \quad v'(0) = y'(0). \quad (9) $$
>>7. Ahora calculamos $$ (f \circ \alpha)'(0) = \frac{d}{dt}\Big|_0 (f \circ \varphi)(u(t), v(t)) = (f \circ \varphi)_u(u_o, v_o)u'(0) + (f \circ \varphi)_v(u_o, v_o)v'(0), $$que por (9) es igual a $(f \circ \beta)'(0)$, como deseábamos. Así, $df_p$ está bien definida.
>>8. Veamos ahora que $df_p$ es lineal. Llamando $a = u'(0)$ y $b = v'(0)$, tenemos por lo anterior que $$ df_p(a\varphi_u(u_o, v_o) + b\varphi_v(u_o, v_o)) = a(f \circ \varphi)_u(u_o, v_o) + b(f \circ \varphi)_v(u_o, v_o), $$con lo cual $df_p$ es lineal.

>[!Proposition]
>Sea $M$ superficie y $f : M \to \mathbb{R}^3$ una función suave tal que $f(M)$ está contenida en una superficie $N$ y sea $p \in M$. Entonces
>$$ df_p : T_pM \to T_{f(p)}N $$
>y si $\varphi : U \to \mathbb{R}^3$ y $\psi : V \to \mathbb{R}^3$ son sistemas coordenados de $M$ y $N$, alrededor de $p$ y $f(p)$ respectivamente, con $f(\varphi(U)) \subset \psi(V)$, se cumple que
>$$ [df_p]_{\{\varphi_u(\bar{p}), \varphi_v(\bar{p})\}, \{\psi_x(\bar{q}), \psi_y(\bar{q})\}} = \left[ d(\psi^{-1} \circ f \circ \varphi)_{\bar{p}} \right]_{\text{can}}, \quad (10) $$
>donde $\varphi(\bar{p}) = p$ y $\psi(\bar{q}) = f(p)$.
>O sea, la matriz de la diferencial de una función entre superficies, en un punto de la superficie de partida, respecto de bases formadas por vectores coordenados, es igual a la matriz jacobiana de la función puesta en coordenadas, en el punto correspondiente del mapa de partida.
>>[!Proof]-
>>1. La primera afirmación se deja como ejercicio.
>>2. Para mostrar la segunda, escribimos $$ (\psi^{-1} \circ f \circ \varphi)(u, v) = (x(u, v), y(u, v)). \quad (11) $$
>>3. Como $\varphi_u(\bar{p}) = \frac{\partial \varphi}{\partial u}(\bar{p}) = \frac{d}{dt}\Big|_0 \varphi(\bar{p} + te_1)$, tenemos que $$ df_p(\varphi_u(\bar{p})) = \frac{d}{dt}\Big|_0 (f(\varphi(\bar{p} + te_1))) = (f \circ \varphi)_u(\bar{p}). $$
>>4. Pero $f(\varphi(u, v)) = \psi(x(u, v), y(u, v))$ por $(11)$ luego, por la regla de la cadena en varias variables, $$ df_p(\varphi_u(\bar{p})) = \psi_x(\bar{q})x_u(\bar{q}) + \psi_y(\bar{q})y_u(\bar{q}). $$
>>5. Entones en paso 3. tomamos $df_{p}$ y lo evaluamos en la primera coordenada de entrada de la base $\varphi_{u}(\bar{p})$ y en el paso 4. escribimos ese resultado en la base de salida. 
>>6. Por lo tanto la primera columna de $[df_p]_{\{\varphi_u(\bar{p}), \varphi_v(\bar{p})\}, \{\psi_x(\bar{q}), \psi_y(\bar{q})\}}$ es igual a $(x_u(\bar{q}), y_u(\bar{q}))^t$. 
>>7. Pero $(x_u(\bar{q}), y_u(\bar{q}))^t$ es trivialmente la primera columna de $\left[ d(\psi^{-1} \circ f \circ \varphi)_{\bar{p}} \right]_{\text{can}}$
>>8. Con argumentos similares se ve que las segundas columnas de las matrices en (10) también coinciden

>[!Definition]
>Sea $f : S \to \mathbb{R}$ una función suave definida en una superficie $S$. Un punto $p \in S$ se dice **crítico** para $f$ si $df_p = 0$ (o sea, $df_p$ es la transformación lineal nula).

>[!Example]
>Sea $h : S \to \mathbb{R}$ la función altura respecto del vector unitario $u \in \mathbb{R}^3$, definida por
>$$ h(q) = \langle q, u \rangle. $$
>Un punto $p \in S$ es crítico para $h$ si y solo si $T_pS \perp u$. Esto resulta de que
>$$ dh_p(X) = \langle X, u \rangle $$
>para todo $X \in T_pS$: Si $X = \alpha'(0)$ para una curva suave $\alpha : (-\varepsilon, \varepsilon) \to S$ con $\alpha(0) = p$, tenemos que
>$$ dh_p(X) = dh_p(\alpha'(0)) = \frac{d}{dt}\Big|_0 h(\alpha(t)) = \frac{d}{dt}\Big|_0 \langle \alpha(t), u \rangle = \langle \alpha'(0), u \rangle = \langle X, u \rangle. $$

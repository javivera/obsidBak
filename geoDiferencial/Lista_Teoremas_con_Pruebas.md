# Lista de Teoremas y Resúmenes de Pruebas

Este archivo contiene los enunciados de los teoremas (copiados textualmente de la lista) y una síntesis de los pasos principales de su demostración basada en el archivo de definiciones.

---

> [!Theorem] Teorema 3
> Demostrar que una curva de rapidez unitaria en $\mathbb{R}^3$ y curvatura nunca nula tiene torsión nula si y sólo si su trayectoria está contenida en un plano.
> > [!Proof]- Resumen
> > 1. **(⇐)** Se asume que la curva está en un plano con normal $n$. Esto implica que $\langle \alpha(t) - \alpha(t_o), n \rangle = 0$. Derivando sucesivamente, se ve que $T$ y $N$ son ortogonales a $n$, por lo que el binormal $B$ es constante (igual a $\pm n$), lo que implica $B'=0$ y $\tau = 0$.
> > 2. **(⇒)** Se asume $\tau = 0$. De las ecuaciones de Frenet, $B' = -\tau N = 0$, luego $B$ es un vector constante $n$. Se define la función $f(t) = \langle \alpha(t) - \alpha(t_o), n \rangle$ y se muestra que su derivada es $\langle T, B \rangle = 0$. Al ser constante y anularse en $t_o$, la curva está contenida en el plano.

> [!Theorem] Teorema 4
> Definir hélice y probar que si $\alpha : (a,b) \to \mathbb{R}^3$ es una hélice con curvatura $\kappa : (a,b) \to \mathbb{R}$ y torsión $\tau : (a,b) \to \mathbb{R}$, entonces $\tau/\kappa$ es constante.
> > [!Proof]- Resumen
> > 1. **(⇒)** Por definición, existe $u$ unitario tal que $\langle T, u \rangle = \cos \theta$. Derivando se obtiene $\kappa \langle N, u \rangle = 0$, por lo que $N \perp u$. Derivando nuevamente: $-\kappa \langle T, u \rangle + \tau \langle B, u \rangle = 0$. Esto relaciona $\kappa \cos \theta$ con $\tau \text{sen } \theta$, resultando en $\tau/\kappa = \cot \theta = \text{cte}$.
> > 2. **(⇐)** Si $\tau/\kappa = c$, se define $\theta$ tal que $\cot \theta = c$. Se construye el vector $u = (\cos \theta) T + (\text{sen } \theta) B$. Al derivar $u$ usando las ecuaciones de Frenet, se obtiene $u' = (\kappa \cos \theta - \tau \text{sen } \theta) N$. La hipótesis $\tau/\kappa = \cot \theta$ hace que este paréntesis sea cero, luego $u$ es constante y la curva es una hélice.

> [!Theorem] Teorema 7
> Enunciar con precisión y demostrar el Teorema Fundamental de las curvas planas.
> > [!Proof]- Resumen
> > 1. **Existencia:** Dada $\tilde{k}(s)$, se construye la función ángulo $\theta(s) = \theta_o + \int_a^s \tilde{k}(t) dt$. Luego se define la curva integrando el vector velocidad: $\alpha(s) = p + \int_a^s (\cos \theta(t), \sin \theta(t)) dt$.
> > 2. **Verificación:** Por construcción $\alpha(a)=p$ y $\alpha'(s)$ es unitario con ángulo $\theta(s)$. La curvatura signada es $\theta'(s)$, que por el TFC es exactamente $\tilde{k}(s)$.

> [!Theorem] Teorema 8
> Probar que la longitud de cualquier curva suave $\alpha : [a,b] \to \mathbb{R}^n$ con $\alpha(a)=0$ y $\alpha(b)=q$ cumple que $L[\alpha] \ge |q|$.
> > [!Proof]- Resumen
> > 1. Se parte de la identidad $q = \alpha(b) - \alpha(a) = \int_a^b \alpha'(t) dt$.
> > 2. Se toma el producto escalar de $q$ contra sí mismo: $\|q\|^2 = \langle \int \alpha'(t) dt, q \rangle = \int \langle \alpha'(t), q \rangle dt$.
> > 3. Aplicando la desigualdad de Cauchy-Schwarz: $\langle \alpha'(t), q \rangle \le \|\alpha'(t)\| \|q\|$.
> > 4. Integrando y simplificando $\|q\|$, se obtiene $\|q\| \le \int \|\alpha'(t)\| dt = L[\alpha]$.

> [!Theorem] Teorema 10
> Sea $C : \mathbb{R}^n \to \mathbb{R}^n$ una transformación lineal. Mostrar que son equivalentes: a) $C$ es ortogonal, b) $C$ preserva producto interno, c) $C$ preserva normas.
> > [!Proof]- Resumen
> > 1. **(a ⇒ b):** Se usa la notación matricial $\langle Cx, Cy \rangle = (Cx)^T Cy = x^T (C^T C) y$. Si $C$ es ortogonal, $C^T C = I$, luego queda $x^T y = \langle x, y \rangle$.
> > 2. **(b ⇒ c):** Directo tomando $x=y$.
> > 3. **(c ⇒ b):** Se utiliza la identidad de polarización que expresa el producto escalar en términos exclusivos de la norma de sumas y restas.
> > 4. **(b ⇒ a):** Si preserva productos internos, envía la base canónica (ortonormal) a otra base ortonormal, lo cual es la definición de matriz ortogonal.

> [!Theorem] Teorema 11
> Mostrar que si $C$ es una matriz ortogonal $3 \times 3$, entonces para todo par de vectores $x,y \in \mathbb{R}^3$ vale que $C x \times C y = (\det C) C(x \times y)$.
> > [!Proof]- Resumen
> > 1. Se utiliza el hecho de que $\langle u \times v, w \rangle = \det(u, v, w)$. 
> > 2. Se prueba que $\langle Cx \times Cy, Cz \rangle = \det(Cx, Cy, Cz) = \det(C(x, y, z)) = \det C \det(x, y, z)$.
> > 3. Esto es igual a $\det C \langle x \times y, z \rangle$, que por ser $C$ ortogonal ($\langle u, v \rangle = \langle Cu, Cv \rangle$) es igual a $\langle \det C \cdot C(x \times y), Cz \rangle$.
> > 4. Como esto vale para todo $z$, los vectores deben ser iguales.

> [!Theorem] Teorema 18
> Mostrar que el gráfico de una función suave es una superficie regular.
> > [!Proof]- Resumen
> > 1. Se define la carta $\varphi(u, v) = (u, v, f(u, v))$.
> > 2. La diferencial $d\varphi$ tiene como columnas a $(1, 0, f_u)$ y $(0, 1, f_v)$, que son linealmente independientes por la submatriz identidad superior; luego $d\varphi$ es inyectiva.
> > 3. La condición de homeomorfismo se verifica usando la proyección $\Phi(x, y, z) = (x, y)$ como inversa continua local.

> [!Theorem] Teorema 22
> Enunciar con precisión el teorema de la superficie implícita y demostrarlo.
> > [!Proof]- Resumen
> > 1. **Enunciado:** Si $F: A \subseteq \mathbb{R}^3 \to \mathbb{R}$ es suave y $y$ es un valor regular ($\nabla F \neq 0$ en $S=F^{-1}(y)$), entonces $S$ es una superficie regular.
> > 2. **Prueba:** Para $p \in S$, si $\nabla F(p) \neq 0$, alguna derivada parcial no es nula (ej. $F_z(p) \neq 0$). Por el Teorema de la Función Implícita del cálculo avanzado, existe localmente una función $z=f(x, y)$ tal que $S$ coincide con el gráfico de $f$, lo cual ya se probó que es una superficie regular.

> [!Theorem] Teorema 31
> a) Definición de $T_p S$. b) Probar que $T_p S$ es la imagen de $d\phi_q$.
> > [!Proof]- Resumen
> > 1. **Definición:** $T_p S = \{\alpha'(0) \mid \alpha \text{ curva en } S, \alpha(0)=p\}$. 
> > 2. **Prueba (⊂):** Si $\alpha$ está en $S$, se puede escribir en coordenadas como $\varphi(u(t), v(t))$. Por regla de la cadena: $\alpha'(0) = \varphi_u u' + \varphi_v v'$, que es una combinación de las columnas de $d\varphi_q$.
> > 3. **Prueba (⊃):** Cualquier vector en la imagen de $d\varphi_q$ es de la forma $d\varphi_q(a, b)$. Se construye la curva $\alpha(t) = \varphi(q + t(a, b))$, cuya derivada en 0 es precisamente $d\varphi_q(a, b)$.

> [!Theorem] Teorema 46
> Probar que $A_p$ diagonaliza en una base ortonormal de $T_p M$.
> > [!Proof]- Resumen
> > 1. El operador de forma $A_p = -dn_p$ es autoadjunto: $\langle A_p(u), v \rangle = \langle u, A_p(v) \rangle$.
> > 2. Para probar la simetría, se evalúa en la base $\{\varphi_u, \varphi_v\}$. La condición se reduce a $\langle n_u, \varphi_v \rangle = \langle \varphi_u, n_v \rangle$.
> > 3. Derivando las identidades de ortogonalidad $\langle n, \varphi_u \rangle = 0$ y $\langle n, \varphi_v \rangle = 0$, se obtiene que ambos términos son iguales a $-\langle n, \varphi_{uv} \rangle$, gracias a que $\varphi_{uv} = \varphi_{vu}$.
> > 4. Un operador autoadjunto en un espacio con producto interno siempre diagonaliza en base ortonormal.

> [!Theorem] Teorema 60
> Probar que si todos los puntos de una superficie regular conexa $M$ son umbílicos, entonces $M$ es una esfera o un plano.
> > [!Proof]- Resumen
> > 1. La condición umbílica implica que el operador de forma es escalar: $dn_q(Z) = k(q) Z$.
> > 2. Derivando las relaciones $n_u = k \varphi_u$ y $n_v = k \varphi_v$ y usando la igualdad de derivadas cruzadas, se demuestra que $\nabla k = 0$, luego $k$ es constante (por conexidad).
> > 3. Si $k=0$, $n$ es constante y la superficie es un plano.
> > 4. Si $k \neq 0$, se muestra que el centro $C = \varphi - \frac{1}{k} n$ es constante, por lo que la superficie está contenida en una esfera centrada en $C$.

> [!Theorem] Teorema 61
> Sea $M$ una superficie regular con orientación $n$. Definir el concepto de geodésica y mostrar que tienen rapidez constante.
> > [!Proof]- Resumen
> > 1. **Definición:** $\gamma$ es geodésica si $\gamma''(t) = \lambda(t) n(\gamma(t))$ (aceleración normal).
> > 2. **Prueba:** Se deriva la rapidez al cuadrado: $\frac{d}{dt} \langle \gamma', \gamma' \rangle = 2 \langle \gamma'', \gamma' \rangle$. Como $\gamma''$ es múltiplo de $n$ y $\gamma'$ es tangente al plano $(\gamma' \perp n)$, el producto escalar es 0. La rapidez es constante.

> [!Theorem] Teorema 73
> Enunciar con precisión el Teorema de Clairaut y demostrarlo.
> > [!Proof]- Resumen
> > 1. **Enunciado:** En una superficie de revolución, $\rho \cos \theta = \text{constante}$ para cualquier geodésica ($\rho$ distancia al eje, $\theta$ ángulo con el paralelo).
> > 2. **Prueba:** Se escribe la ecuación diferencial de las geodésicas en la carta de revolución. Una de las ecuaciones resulta ser $((r(v))^2 u')' = 0$, donde $r(v)$ es el radio ($\rho$) y $u$ es el ángulo azimutal.
> > 3. Se demuestra geométricamente que $\rho \cos \theta$ es exactamente igual a $(r(v))^2 u'$, por lo que su derivada es nula y el valor es constante.

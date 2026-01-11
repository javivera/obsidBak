# Soluciones — Geometría Diferencial — Práctico 5

---

>[!Example] Ejercicio 1
>Sea $S$ la esfera de centro cero y radio uno y sea $\psi : (-\pi, \pi) \times \mathbb{R} \to \mathbb{R}^3$,
>$$ \psi(s, t) = (\cos t (\cos s, \text{sen } s), \text{sen } t). $$
>Hallar las funciones de cambio de coordenadas de $\phi_1^+$ a $\psi$, y de $\phi_1^-$ a $\phi_3^+$, incluyendo la descripción de los dominios.
>>[!Proof]-
>>- **Contexto:** $\psi$ es la parametrización por coordenadas esféricas (con $t$ latitud y $s$ longitud).$$\psi(s, t) = (\cos t \cos s, \cos t \text{sen } s, \text{sen } t)$$Las cartas $\phi_i^\pm$ suelen denotar las proyecciones canónicas sobre los planos coordenados (parametrizaciones gráficas).
>>$\phi_1^+(u, v) = (\sqrt{1-u^2-v^2}, u, v)$ (hemisferio $x > 0$).
>>$\phi_1^-(u, v) = (-\sqrt{1-u^2-v^2}, u, v)$ (hemisferio $x < 0$).
>>$\phi_3^+(u, v) = (u, v, \sqrt{1-u^2-v^2})$ (hemisferio $z > 0$).
>>- **1. Cambio de coordenadas $\phi_1^+ \to \psi$:**
>>	1. Queremos calcular $(\psi^{-1} \circ \phi_1^+)(u, v)$.
>>	2. Sea $p = \phi_1^+(u, v) = (x, y, z) = (\sqrt{1-u^2-v^2}, u, v)$.
>>	3. Buscamos $(s, t)$ tal que $\psi(s, t) = p$.
>>	4. $z = \text{sen } t \implies v = \text{sen } t \implies t = \text{arcsen } v$.
>>	5. $x = \cos t \cos s \implies x = \sqrt{1-v^2} \cos s$ (reemplazando con el paso 4.) 
>>	6. Entonces como $x>0$ (y $\sqrt{1-v^{2} }>0$) tenemos que $cos(s)>0$ osea $s\in \left( -\frac{\pi}{2}, \frac{\pi}{2} \right)$    
>>	7. $y = \cos t \text{sen } s \implies u = \cos(\text{arcsen } v) \text{sen } s = \sqrt{1-v^2} \text{sen } s$. 
>>	8. Entonces $\text{sen } s = \frac{u}{\sqrt{1-v^2}}$ osea $s = \text{arcsen}\left( \frac{u}{\sqrt{1-v^2}} \right)$ que esta bien definida por que $s\in \left( -\frac{\pi}{2}, \frac{\pi}{2} \right)$ 
>>	9. Finalmente la función de cambio de coordenadas es: $$ T(u, v) = \left( \text{arcsen}\left( \frac{u}{\sqrt{1-v^2}} \right), \text{arcsen } v \right) $$
>>- **Dominio:** 
>>	1. Ahora necesito asegurarme que el dominio de $\phi_{1}^{+}$ este bien para que su imagen este en el dominio de $\psi$ 
>>	2. La imagen de $\phi_1^+$ es el hemisferio $x>0$. Para $\psi$, esto corresponde a $s \in (-\pi/2, \pi/2)$ y $t \in (-\pi/2, \pi/2)$.
>>	3. El punto de esto es que no hace falta restringir el dominio de $\phi_{1}^{+}$ 
>>	4. Por lo tanto el dominio el cambio de coordeandas es el de $\phi_{1}^{+}$ que es en el plano $uv$ es el disco unitario abierto $u^2+v^2 < 1$.
>>- **2. Cambio de coordenadas $\phi_1^- \to \phi_3^+$:**
>>	1. Queremos calcular $(\phi_3^+)^{-1} \circ \phi_1^-$.
>>	2. Sea $p = \phi_1^-(u, v) = (-\sqrt{1-u^2-v^2}, u, v)$.
>>	3. Para que $p$ esté en la imagen de $\phi_3^+$, debe cumplir $z > 0$.
>>	4. Aquí $z = v$, por lo tanto necesitamos $v > 0$.
>>	5. Aplicamos $(\phi_3^+)^{-1}$ a $p=(x, y, z)$. Esta inversa es la proyección al plano $xy$: $(x, y) \to (x, y)$.
>>	6. Entonces: $$ (\phi_3^+)^{-1}(-\sqrt{1-u^2-v^2}, u, v) = (-\sqrt{1-u^2-v^2}, u) $$
>>- **Dominio:** 
>>	1. Originalmente $(u, v)$ está en el disco $u^2+v^2 < 1$.
>>	2. La intersección de las imágenes de las cartas es $\{x < 0\} \cap \{z > 0\}$.
>>	3. En coordenadas de $\phi_1^-$, $x<0$ ya se cumple en todo el dominio. Para que la 3era coordenada sea mayor que $0$ por definicion es lo mismo que pedir $v > 0$.
>>	4. Por tanto el dominio de la composicion es el semi-disco $$\{(u, v) : u^2+v^2 < 1, v > 0\}$$

---

>[!Example] Ejercicio 2
>Sea $S$ una superficie regular y sea $\pi : S \to \mathbb{R}^2$ la función que lleva a cada punto $(x, y, z) \in S$ al punto $(x, y)$. ¿Es la función $\pi$ diferenciable?
>>[!Proof]-
>>Sí.
>>La función $\Pi : \mathbb{R}^3 \to \mathbb{R}^2$ dada por $\Pi(x, y, z) = (x, y)$ es una función lineal, y por tanto infinitamente diferenciable ($C^\infty$).
>>La función $\pi$ es la restricción de $\Pi$ a la superficie $S$ ($\pi = \Pi|_S$).
>>Por definición, la restricción de una función diferenciable definida en un abierto de $\mathbb{R}^3$ (en este caso todo $\mathbb{R}^3$) a una superficie regular es diferenciable.

---

>[!Example] Ejercicio 3
>Consideremos la esfera $S^2 = \{x \in \mathbb{R}^3 : |x| = 1\}$ y el elipsoide $E = \{(x, y, z) \in \mathbb{R}^3 : x^2/a^2 + y^2/b^2 + z^2/c^2 = 1\}$. Probar que $S^2$ y $E$ son difeomorfas.
>>[!Proof]-
>>Consideremos la aplicación $F : \mathbb{R}^3 \to \mathbb{R}^3$ definida por $F(x, y, z) = (ax, by, cz)$.
>>Esta es una transformación lineal invertible (su matriz es diagonal con entradas $a, b, c \neq 0$). Por tanto es un difeomorfismo global de $\mathbb{R}^3$.
>>Si restringimos $F$ a la esfera $S^2$:
>>Sea $(x, y, z) \in S^2$, entonces $x^2+y^2+z^2=1$.
>>La imagen es $(u, v, w) = (ax, by, cz)$.
>>Verificamos si está en $E$:
>>$\frac{u^2}{a^2} + \frac{v^2}{b^2} + \frac{w^2}{c^2} = \frac{(ax)^2}{a^2} + \frac{(by)^2}{b^2} + \frac{(cz)^2}{c^2} = x^2 + y^2 + z^2 = 1$.
>>Por tanto $F(S^2) = E$.
>>La restricción $f = F|_{S^2} : S^2 \to E$ es una biyección suave con inversa suave (la restricción de $F^{-1}(u, v, w) = (u/a, v/b, w/c)$).
>>Por lo tanto, $f$ es un difeomorfismo.

---

>[!Example] Ejercicio 4
>Sea $S$ una superficie regular y $f : S \to \mathbb{R}$. Un punto $p \in S$ se dice crítico para $f$ si $df|_p = 0$.
>Sea $f(p) = |p - p_0|$ con $p_0$ fuera de $S$ fijo. Mostrar que $p$ es crítico para $f$ si y sólo si la recta que pasa por $p$ y $p_0$ es perpendicular a $S$ en $p$.
>>[!Proof]-
>>Consideremos la función cuadrado de la distancia $g(p) = |p - p_0|^2 = \langle p - p_0, p - p_0 \rangle$.
>>Los puntos críticos de $f$ son los mismos que los de $g$ (pues $f = \sqrt{g}$ y $g > 0$, $df = \frac{1}{2\sqrt{g}} dg$, así que $df=0 \iff dg=0$).
>>Extendemos $g$ a todo $\mathbb{R}^3$ como $G(x) = |x - p_0|^2$.
>>El diferencial de $G$ en $p$ actuando sobre un vector $v \in \mathbb{R}^3$ es:
>>$dG_p(v) = 2 \langle p - p_0, v \rangle$.
>>Para la función restringida $g = G|_S$, el diferencial $dg_p$ es la restricción de $dG_p$ al espacio tangente $T_pS$.
>>$p$ es punto crítico de $g$ si $dg_p(v) = 0$ para todo $v \in T_pS$.
>>Esto equivale a:
>>$2 \langle p - p_0, v \rangle = 0 \quad \forall v \in T_pS$.
>>Esto significa que el vector $p - p_0$ es ortogonal a todo vector tangente a $S$ en $p$.
>>Es decir, $p - p_0$ es normal a $S$ en $p$.
>>Geométricamente, esto significa que la recta que une $p_0$ y $p$ (que tiene dirección $p - p_0$) es perpendicular al plano tangente $T_pS$.

---

>[!Example] Ejercicio 5
>Sean $M$ y $N$ dos superficies regulares y sea $F : \mathbb{R}^3 \to \mathbb{R}^3$ una función suave tal que $F(M) \subset N$. Mostrar que la función suave $f = F|_M : M \to N$ satisface $df_p = dF_p|_{T_pM}$ para todo $p \in M$. 
>En particular, si $F$ es lineal, entonces $df_p(w) = F(w)$, para todo $p \in M$ y $w \in T_pM$.
>>[!Proof]-
>>1. Sea $w \in T_pM$. Por definición, existe una curva suave $\alpha : (-\epsilon, \epsilon) \to M$ tal que $\alpha(0) = p$ y $\alpha'(0) = w$.
>>2. El diferencial de $f$ se calcula como:$$df_p(w) = \frac{d}{dt}\Big|_{0}f(\alpha (t))$$
>>3. Como $f$ es la restricción de $F$, y $\alpha(t)\in M$ tenemos $f(\alpha(t)) = F(\alpha(t))$.
>>4. Entonces:$$df_p(w) = \frac{d}{dt}\Big|_{0} (F(\alpha(t)))$$
>>5. Por la regla de la cadena y por definicion de matriz diferencial para funciones de $\mathbb{R}^{n}$ en $\mathbb{R}^{m}$ esto es: $$\frac{d}{dt}\Big|_{0} (F(\alpha(t)))=dF_{\alpha(0)}(\alpha'(0)) = dF_p(w)$$
>>6. Por lo tanto, $df_p(w)$ coincide con la aplicación lineal $dF_p$ evaluada en $w$.
>>- **Caso lineal:**
>>	1. Si $F$ es lineal, su diferencial en cualquier punto es la misma transformación lineal $F$ (es decir, $dF_p(v) = F(v)$).
>>	2. Entonces $df_p(w) = dF_p(w) = F(w)$.

---

>[!Example] Ejercicio 6
>Mostrar que el paraboloide $z = x^2 + y^2$ es difeomorfo a un plano.
>>[!Proof]-
>>1. Sea $P$ el paraboloide y $\pi : P \to \mathbb{R}^2$ la proyección $\pi(x, y, z) = (x, y)$. Esta función es suave (restricción de proyección lineal).
>>2. Su inversa es la parametrización global $\varphi : \mathbb{R}^2 \to P$ dada por $\varphi(u, v) = (u, v, u^2+v^2)$. (Una composicion es trivial la otra sale usando que $(x,y,z)\in Dm(\pi)$ entonces $z=x^{2}+y^{2}$) 
>>3. Ademas $\varphi$ es suave (sus componentes son polinomios osea es diferenciable en el sentido tradicional en $\mathbb{R}^{2}$).
>>4. Como $\pi \circ \varphi = \text{id}_{\mathbb{R}^2}$ y $\varphi \circ \pi = \text{id}_P$, $\pi$ es una biyección con inversa suave.
>>5. Por tanto, $P$ es difeomorfo a $\mathbb{R}^2$ (un plano).

---

>[!Example] Ejercicio 7
>Sea $A : S \to S, A(q) = -q$, la aplicación antipodal de la esfera y sea $p \in S$. Mostrar que $A$ es un difeomorfismo, $T_pS = T_{A(p)}S$ y calcular $dA_p$ sin recurrir a sistemas coordenados de $S$.
>>[!Proof]-
>>- **Difeomorfismo:** $A$ es la restricción a $S$ de la aplicación lineal $L(x) = -x$ en $\mathbb{R}^3$. Como $L$ es suave e invertible (su inversa es ella misma, $L^{-1} = L$), su restricción a una subvariedad invariante ($L(S)=S$) es un difeomorfismo.
>>- **Espacios tangentes:**
>>   1. El espacio tangente $T_pS$ es el conjunto de vectores ortogonales a $p$ (pues $S$ es la esfera unitaria).$$T_pS = \{v \in \mathbb{R}^3 : \langle p, v \rangle = 0\}$$
>>   2. El espacio tangente en $A(p) = -p$ es por la misma razon: $$T_{-p}S = \{v \in \mathbb{R}^3 : \langle -p, v \rangle = 0\}$$
>>   3. Como $\langle -p, v \rangle = -\langle p, v \rangle$, la condición es idéntica.
>>   4. Por tanto, $T_pS = T_{-p}S$ (como subespacios de $\mathbb{R}^3$).
>>- **Cálculo de $dA_p$:**
>>	1. Usando el resultado del Ejercicio 5, como $A$ es la restricción de la lineal $L(x) = -x$ entonces $dA_{p}=dL_{p}|_{T_{p}S}=L|_{T_{p}S}$ 
>>	2. Esto es $$dA_p(w) = L(w) = -w$$ para todo $w \in T_pS$.
>>	3. Es decir, $dA_p = -\text{Id}|_{T_pS}$.

---

>[!Example] Ejercicio 8
>Sean $F : M \to N$ y $G : N \to P$ funciones suaves entre superficies y sea $p \in M$. Mostrar que $d(G \circ F)_p = dG_{F(p)} \circ dF_p$ (regla de la cadena).
>>[!Proof]-
>>1. Sea $w \in T_pM$. Sea $\alpha : (-\epsilon, \epsilon) \to M$ una curva suave tal que $\alpha(0) = p$ y $\alpha'(0) = w$.
>>2. Por definición de diferencial:$$d(G \circ F)_p(w) = \frac{d}{dt} (G \circ F \circ \alpha)(t) \big|_{t=0}$$
>>3. Sea $\beta(t) = (F \circ \alpha)(t)$. Entonces $\beta$ es una curva en $N$ con $\beta(0) = F(p)$ y $\beta'(0) = dF_p(w)$ (por definición de $dF_p$).
>>4. Entonces reemplazando y por definicion de diferencial: $$\frac{d}{dt} (G \circ F \circ \alpha)(t) \big|_{t=0}=\frac{d}{dt} (G(\beta(t))) \big|_{t=0} = dG_{\beta(0)}(\beta'(0))$$
>>5. Sustituyendo:$$dG_{\beta(0)}(\beta'(0))= dG_{F(p)}(dF_p(w))$$
>>6. Como vale para todo $w$, $d(G \circ F)_p = dG_{F(p)} \circ dF_p$.

---

>[!Example] Ejercicio 9
>Sean $S^2$ la esfera de radio 1 y centro en el origen, y $M = \{(x, y, z) : x^2 + y^2 - z^2 = 1\}$. Denotamos con $N$ y $S$ respectivamente los puntos $(0, 0, 1)$ y $(0, 0, -1)$ y definimos $F : S^2 - \{N, S\} \to M$ de la siguiente manera: para cada $p \in S^2$ distinto de $N$ y $S$, $F(p)$ es el punto donde corta a $M$ la semirrecta que pasa por $p$ perpendicular al eje $z$, que parte desde dicho eje. Demostrar que $F$ es diferenciable. Mostrar que $F$ es un difeomorfismo de dos maneras: primero, calculando la inversa de $F$; después, sin hallar la inversa, usando el teorema de la función inversa.
>>[!Proof]-
>>- **Diferenciabilidad**
>>	1. La semirrecta perpendicular al eje $z$ que pasa por $p=(x, y, z)$ y parte del eje $z$ es el rayo radial en coordenadas cilíndricas a altura $z$.
>>	2. Parametrización del rayo: $R(t) = (0, 0, z) + t(x, y, 0)$ con $t > 0$.
>>	3. Como $p \in S^2$, $x^2+y^2+z^2=1$, así que $x^2+y^2 = 1-z^2$. El radio de $p$ al eje es $\rho_p = \sqrt{1-z^2}$.
>>	4. El punto $p$ está en el rayo para $t=1$.
>>	5. Buscamos la intersección con $M: x^2+y^2-z^2=1$. Punto del rayo: $Q = (tx, ty, z)$. Queremos encontrar $t$ para que $Q$ cumpla la ecuacion $M$  
>>	6. Reemplazando $(tx)^2 + (ty)^2 - z^2 = 1 \implies t^2(x^2+y^2) - z^2 = 1$.
>>	7. Entonces $t^2(1-z^2) = 1+z^2 \implies t = \sqrt{\frac{1+z^2}{1-z^2}}$.
>>	8. Obteniendo $F(x, y, z) = \left( x\sqrt{\frac{1+z^2}{1-z^2}}, y\sqrt{\frac{1+z^2}{1-z^2}}, z \right)$. Que seria la interseccion del rayo con $M$ 
>>	9. Esta función es diferenciable en $\mathbb{R}^3$ siempre que $z \neq \pm 1$. Por lo tanto es diferenciable en $S^{2}$ por ser restriccion de diferenciable 
>>	10. Los puntos con $z=\pm 1$ son los polos $(0, 0, \pm 1)$ que estan excluidos del dominio. 
>>- **Calculando la inversa:**
>>	1. Sea $Q = (X, Y, Z) \in M$. Queremos recuperar $p \in S^2$.
>>	2. La operación inversa es proyectar radialmente hacia el eje $z$ hasta tocar la esfera.
>>	3. La altura no cambia al invertir osea $z = Z$. 
>>	4. Radio en $M$: $$\rho_M = \sqrt{X^2+Y^2} = \sqrt{1+Z^2}$$Radio en $S^2$: $$\rho_S = \sqrt{1-z^2} = \sqrt{1-Z^2}$$Por lo tanto tenemos un factor de escala $k = \frac{\rho_S}{\rho_M} = \sqrt{\frac{1-Z^2}{1+Z^2}}$.
>>	5. Finalmente $$F^{-1}(X, Y, Z) = (kX, kY, Z)$$
>>	6. Para que $k$ esté bien definido necesitamos $1-Z^2 > 0 \implies |Z| < 1$. Pero esto es asi por que la imagen de $F$ es la parte de $M$ con $|z| < 1$. (Por que la esfera de centro $0$ y radio $1$ a lo sumo tiene altura $z=\pm 1$ y pero le sacamos el polo sur/norte) 
>>	7. $F^{-1}$ es trivialmente suave en ese dominio.
>>	8. Entonces $F|_{S^{2}}$ es difeomorfismo
>>- **Teorema de la función inversa:**
>>	1. Para calcular $dF$. Miramos a $F$ como $F(x,y,z)=(h(z)x,h(z)y,z)$ con $h(z) = \sqrt{\frac{1+z^2}{1-z^2}}$ que es nunca nula 
>>	2. Entonces $$dF_{p}=\begin{pmatrix}h(p_{3}) & 0 & h'(p_{3})p_{1} \\ 0 & h(p_{3}) & h'(p_{3})p_{2}\\0&0&1 \end{pmatrix}$$ (aca hice un poco de abuso por que esta seria la diferencial de $F$ sin restringir al dominio adecuado la esfera). Si restringimos $d\tilde{F}:=dF|_{T_{p}(S^{2})}:T_{p}S^{2}\rightarrow T_{F(p)}M$ y ambos viven en $\mathbb{R}^{2}$ 
>>	3. Supongo existe $(u,v,w)\in T_{p}S^{2}$ tal que $d\tilde{F}_{p}(u,v,w)=0$ entonces $$(h(p_{3})u+h'(p_{3})p_{1}w,h(p_{3})v+h'(p_{3})wp_{2},w)=0$$  
>>	4. Entonces $w=0$ por lo tanto $h(p_{3})u=0=h(p_{3})v$ pero $h(x)\neq0$ por lo tanto $u=0=v$ 
>>	5. Por lo tanto $(u,v,w)=0$ osea $Ker(dF_{p})=\{ 0 \}$ entonces $dF_{p}$ es isomorfismo  
>>	6. Y en realidad aca para terminarlo deberiamos ver que $F$ es biyectiva (ya sabemos que es suave por ser restriccion de suave a la esfera) y usar [[Definiciones#^409ff8]] que nos asegura que $F^{-1}$ es suave concluyendo que es difeomorfismo

---

>[!Example] Ejercicio 10
>Mostrar que si todos los puntos de una superficie conexa son puntos críticos de una función $f$, entonces $f$ es constante.
>>[!Proof]-
>>Si todos los puntos son críticos, $df_p = 0$ para todo $p \in S$.
>>Sea $p, q \in S$. Como $S$ es conexa (y por ser variedad, conexa por caminos), existe una curva suave $\alpha : [0, 1] \to S$ tal que $\alpha(0)=p$ y $\alpha(1)=q$.
>>Consideremos la función compuesta $g(t) = f(\alpha(t))$.
>>$g'(t) = df_{\alpha(t)}(\alpha'(t))$.
>>Como $df$ es idénticamente nulo, $g'(t) = 0$ para todo $t$.
>>Por cálculo elemental, $g(t)$ es constante.
>>Entonces $f(p) = g(0) = g(1) = f(q)$.
>>Como vale para cualesquiera $p, q$, $f$ es constante.

---

>[!Example] Ejercicio 11
> **Superficies de revolución.**
> Sea $I$ un intervalo abierto y sea $\gamma : I \subseteq \mathbb{R} \to \mathbb{R}^2$ una curva regular suave de la forma $\gamma(t) = (r(t), h(t))$, con $r(t) > 0$ para todo $t \in I$ y sea $\phi : \mathbb{R} \times I \to \mathbb{R}^3$,
> $$ \phi(s, t) = (r(t) \cos s, r(t) \text{sen } s, h(t)). $$
> Si $\gamma$ satisface condiciones de inyectividad (o periodicidad simple), $S = \text{Im}(\phi)$ es una superficie regular.
> - Mostrar que el toro $T(R, r)$ es un ejemplo de $S$ como arriba. ¿Con cuál $\gamma$?
> - Verificar que $\phi$ es una parametrización de $S$.
> - Definir paralelos y meridianos.
>>[!Proof]-
>>- **Parametrizacion:**
>>	1. El toro de revolución se genera rotando un círculo de radio $r$ centrado en $(R, 0)$ alrededor del eje $z$.
>>	2. La curva generatriz en el plano $xz$ (o $rz$) es: $$\gamma(t) = (R + r \cos t, r \text{sen } t)\quad t\in (0, 2\pi)$$
>>	3. Aquí $r(t) = R + r \cos t$ y $h(t) = r \text{sen } t$.
>>	4. Notar $R > r$, $r(t) > 0$ siempre.
>>	5. Ahora usando la parametrizacion para una supericie de revolucion tenemos $$\phi(s, t) = ((R + r \cos t)\cos s, (R + r \cos t)\text{sen } s, r \text{sen } t)$$
>>- **Verificacion:**
>>	1. Jacobiana: $\phi_s = (-r(t)\text{sen } s, r(t)\cos s, 0)$ y $\phi_t = (r'(t)\cos s, r'(t)\text{sen } s, h'(t))$
>>	2. Producto cruz: $\phi_s \times \phi_t = (r(t)h'(t)\cos s, r(t)h'(t)\text{sen } s, -r(t)r'(t))$.
>>	3. Norma al cuadrado: $\lVert \phi_s \times \phi_t  \rVert =r(t)^2 (h'(t)^2 + r'(t)^2) = r(t)^2 \|\gamma'(t)\|^2$.
>>	4. Como $r(t) > 0$ y $\gamma$ es regular ($\|\gamma'\| \neq 0$), el producto cruz nunca es cero.
>>	5. Entonces con las restricciones de dominio adecuadas la diferencial es inyectividad, ósea $\phi$ es una parametrización.
>>- **Paralelos:** Curvas con $t = \text{cte}$. Son circunferencias horizontales generadas por la rotación de un punto fijo de la generatriz.
>>- **Meridianos:** Curvas con $s = \text{cte}$. Son copias de la curva generatriz $\gamma$ (rotadas un ángulo $s$).

---

>[!Example] Ejercicio 12
>Sea $S$ una superficie dada implícitamente por $f(x, y, z) = 0$ (0 valor regular de $f$). Mostrar que el plano tangente afín en $(x_0, y_0, z_0)$ está dado por:
>$$ f_x(x_0, y_0, z_0)(x - x_0) + f_y(x_0, y_0, z_0)(y - y_0) + f_z(x_0, y_0, z_0)(z - z_0) = 0. $$
>Notar que la misma demo vale para $f(x,y,z)=c$ con $c$ valor regular 
>>[!Proof]-
>>1. Sea $p=(x_0,y_0,z_0)\in S$. Como $0$ es un valor regular de $f$, se tiene $\nabla f(p)\neq 0$.
>>2. Veamos que el gradiente es normal a la superficie. Sea $\alpha:(-\varepsilon,\varepsilon)\to S$ una curva $C^1$ tal que $\alpha(0)=p$. 
>>3. Como $\alpha(t)\in S$ para todo $t$, se cumple $f(\alpha(t))=0$ para todo $t$. Derivando respecto de $t$ en $t=0$ y usando la regla de la cadena se obtiene $$0=\frac{d}{dt}\Big|_{t=0}f(\alpha(t))=df_p(\alpha'(0)).$$ En coordenadas vale $df_p(v)=\langle \nabla f(p), v\rangle$, luego $$\nabla f(p)\cdot\alpha'(0)=0.$$
>>4. Como $\alpha'(0)$ es un vector tangente arbitrario a $S$ en $p$, se concluye que $$T_pS\subset\{v\in\mathbb{R}^3:\nabla f(p)\cdot v=0\}.$$
>>5. El conjunto $$H=\{v\in\mathbb{R}^3:\nabla f(p)\cdot v=0\}$$ es un subespacio vectorial de dimensión $2$, ya que $\nabla f(p)\neq 0$. 
>>6. Como $S$ es una superficie regular, el espacio tangente $T_pS$ también tiene dimensión $2$. Por inclusión y por igualdad de dimensiones se obtiene $$T_pS=H.$$
>>7. El plano tangente afín a $S$ en $p$ es $$p+T_pS=\{p+v:v\in T_pS\}.$$ Un punto $q=(x,y,z)$ pertenece a este plano si y solo si $q-p\in T_pS$, lo cual equivale a $$\nabla f(p)\cdot(q-p)=0.$$
>>8. Escribiendo $\nabla f(p)=(f_x(p),f_y(p),f_z(p))$ y $q-p=(x-x_0,y-y_0,z-z_0)$ se obtiene $$f_x(p)(x-x_0)+f_y(p)(y-y_0)+f_z(p)(z-z_0)=0,$$ que es la ecuación del plano tangente buscado. 

^a4f8a9

---

>[!Example] Ejercicio 13
>Mostrar que los planos tangentes de $x^2 + y^2 - z^2 = 1$ en los puntos $(x, y, 0)$ son todos paralelos al eje $z$.
>>[!Proof]-
>>1. Sea $f(x, y, z) = x^2 + y^2 - z^2$. Entonces la superficie esta dada implicitamente por $f(x,y,z)=1$
>>2. Usando un razonamiento analogo al [[GD - Pr5#^a4f8a9]] sabemos que el gradiente de $f$ es normal al plano tangente
>>3. Luego $\nabla f = (2x, 2y, -2z)$. En un punto $p = (x_0, y_0, 0)$ (intersección con plano $xy$), el gradiente es: $$\nabla f(p) = (2x_0, 2y_0, 0)$$
>>4. Luego $T_{p}S\subseteq \{ x\in \mathbb{R}^{3}:\langle x,(x_{0},y_{0},0)\rangle=0 \}$. Por lo tanto, el plano tangente es vertical, es decir, paralelo al eje $z$. 

---

>[!Example] Ejercicio 14
>- (a) Mostrar que si todas las rectas normales a una superficie conexa pasan por un punto, entonces la superficie está contenida en una esfera.
>- (b) Más en general, probar que si todas las rectas normales a una superficie regular conexa pasan por una recta fija, entonces $S$ es una superficie de revolución.
>>[!Proof]-
>>- **(a)** 
>>	1. Notar que la recta normal es $\{ p+tN(p):t \in \mathbb{R} \}$ 
>>	2. Supongamos que todas las normales pasan por el origen $O$ (sin pérdida de generalidad).
>>	3. Esto significa que para todo $p \in S$, el vector normal $N(p)$ es colineal con el vector posición $p$.
>>	4. Consideremos la función $f(x) = \|x\|^2 = \langle x, x \rangle$. Entonce si $v \in T_pS$ tenemos $df_p(v) = 2 \langle p, v \rangle$. 
>>	5. Como $p$ es colineal a la normal, $p$ es ortogonal al plano tangente. Por tanto $\langle p, v \rangle = 0$. Entonces $df \equiv 0$ en $S$.
>>	6. Por lo tanto $f$ es localmente constante  
>>	7. Como $S$ es conexa y  $f$ es constante. $\|p\|^2 = R^2$.
>>	8. Finalmente $S$ está contenida en una esfera de radio $R$.
>>- **(b)** 
>>	1. Supongamos que las normales cortan al eje $z$.
>>	2. Esto implica que la normal $N(p)$ no tiene componente "azimutal" que la saque del plano formado por $p$ y el eje $z$. O más formalmente, la normal es coplanar con el eje $z$ y el punto $p$.
>>	3. Esto sugiere simetría rotacional.
>>	4. Consideremos la función $g(p)$ que rota $p$ alrededor del eje $z$. El campo vectorial generado por rotaciones infinitesimales es $V(x, y, z) = (-y, x, 0)$ (tangente a los paralelos).
>>	5. Si la normal corta al eje $z$, entonces la normal está en el plano generado por $(0,0,1)$ y $p$. El vector $V(p)$ es perpendicular a este plano.
>>	6. Por tanto $V(p)$ es perpendicular a la normal $N(p)$.
>>	7. Esto implica que $V(p)$ es tangente a la superficie ($V(p) \in T_pS$).
>>	8. Como el campo de rotación es tangente a la superficie, la superficie es invariante bajo rotaciones (el flujo del campo preserva la superficie).
>>	9. Por tanto es una superficie de revolución.

---

>[!Example] Ejercicio 15
>Demostrar que si una superficie regular $S$ intersecta a un plano $P$ únicamente en un punto $p$, entonces dicho plano es el plano tangente a $S$ en $p$. 
>Hint: Sea $n$ un vector normal al plano $P$ y estudiar la función altura $h$ de $S$ con respecto de $n$. Mostrar que la hipótesis implica que el punto $p$ debe ser un punto donde $h$ tiene un máximo/mínimo local.
>>[!Proof]-
>>1. Sea $P$ definido por $\langle x - p, n \rangle = 0$ y $h(q) = \langle q - p, n \rangle$ la función altura
>>2. Obviamente $P = \{x : h(x) = 0\}$.
>>3. La intersección es $S \cap P = \{p\}$. Esto significa que $h(p) = 0$ y $h(q) \neq 0$ para todo $q \in S, q \neq p$.
>>4. Por continuidad de $h$ ($h:S\rightarrow\mathbb{R}$) y conexidad local (por ser superficie regular es localmente arco conexa que implica localmente conexa) de $S$ alrededor de $p$, $h$ debe tener signo constante en un entorno de $p$ (si tomara valores positivos y negativos, por valor intermedio habría más puntos donde $h=0$ no es dificil de probar).
>>5. Supongamos $h(q) \ge 0$ cerca de $p$. Entonces $p$ es un mínimo local de $h$.
>>6. En un extremo local, el diferencial debe anularse osea $dh_p = 0$. Por lo tanto $0=dh_p(v) = \langle v, n \rangle$ para $v \in T_pS$.
>>7. Que sea cero implica que $n$ es ortogonal a todo $v \in T_pS$. Por tanto, $n$ es normal a $S$ en $p$.
>>8. El plano $P$ (normal a $n$) coincide con el plano tangente $T_pS$.

---

>[!Example] Ejercicio 16
>Sea $T$ el toro $T(2, 1)$ con su parametrización usual $\phi : \mathbb{R}^2 \to T \subseteq \mathbb{R}^3$. 
>Dados $a, b, c, d \in \mathbb{Z}$, considerar $F : T \to T$ definida por
>$$ F(p) = \phi(as + ct, bs + dt), $$
>si $p = \phi(s, t)$.
>- Mostrar que $F$ está bien definida y es suave.
>- Probar que si $\det \begin{pmatrix} a & c \\ b & d \end{pmatrix} = 1$, entonces $F$ es un difeomorfismo. Para $a=b=c=1, d=2$ se tiene la transformación del gato de Arnold.
>- Hallar la matriz de $dF_{\phi(0,0)}$ en la base $\{\phi_s(0,0), \phi_t(0,0)\}$.
>>[!Proof]-
>>- **Bien definida:**
>>	1. La parametrización $\phi$ es $2\pi$-periódica en $s$ y $t$. Por lo tanto $p = \phi(s, t) = \phi(s', t')$ si y solo si $s' - s = 2\pi k$ y $t' - t = 2\pi l$ con $k, l \in \mathbb{Z}$.
>>	2. Veamos si la imagen es independiente del representante: $$\begin{align}F(\phi(s+2\pi k, t+2\pi l)) & = \phi(a(s+2\pi k) + c(t+2\pi l), b(s+2\pi k) + d(t+2\pi l))\\ & = \phi(as+ct + 2\pi(ak+cl), bs+dt + 2\pi(bk+dl))\\&=\phi(as+ct,bs+dt)\\&=F(\phi(s,t))\end{align}$$ Esto ultimo por que $a, b, c, d$ son enteros entonces los términos $ak+cl$ y $bk+dl$ son enteros.
>>	3. Entonces por la periodicidad de $\phi$, el valor en $T$ es el mismo.
>>- **Suavidad**
>>	1. Sea $L(s,t)=(as+ct,bs+dt)$ esto es obviamente lineal
>>	2. Notar que $F\circ \phi =\phi\circ L$ por que $$F(\phi(s,t))=F(p)=\phi(as+ct,bs+dt)=\phi(L(s,t))$$  
>>	3. Entonces $\phi ^{-1}\circ F\circ \phi=L$ como $L$ lineal entonces es suave
>>	4. Luego por [[Definiciones#^477389]] $F$ es suave
>>- **Difeomorfismo:**
>>	1. Notar que $1=\det \begin{pmatrix} a & c \\ b & d \end{pmatrix} = det(L)$ (coordenadas canonicas) entonces $L$ es inversible
>>	2. Definimos $F^{-1}(\phi(s,t))=F^{-1}(p)=\phi(L^{-1}(s,t))$ que es claramente la inversa por que $$F(F^{-1}(p))=F(\phi(L^{-1}(s,t)))=\phi(L(L^{-1}(s,t)))=\phi(s,t)=p$$
>>	3. Ademas $\phi ^{-1}\circ F^{-1}\circ\phi(s,t)=\phi ^{-1}(\phi(L^{-1}(s,t)))=L^{-1}(s,t)$ 
>>	4. Con loa cual $F^{-1}$ es suave.
>>- **Matriz del diferencial:**
>>	1. Matriz diferencial Derivando en $(0,0)$ y usando la regla de la cadena, $$d(\phi^{-1})_{\phi(0,0)} \circ dF_{\phi(0,0)} \circ d\phi_{(0,0)} = dL_{(0,0)}.$$
>>	2. Por lo tanto $$dF_{\phi(0,0)}=d\phi_{(0,0)} \circ L \circ d(\phi ^{-1})_{\phi(0,0)}$$  
>>	3. Como $L$ es lineal, se cumple $$dL_{(0,0)} = L.$$
>>	4. Además, notar $$d\phi_{(0,0)}(e_1)=\phi_s(0,0), \qquad d\phi_{(0,0)}(e_2)=\phi_t(0,0)$$ $$d(\phi ^{-1})_{_{\phi(0,0)}}(\phi_{s}(0,0))=e_{1}\qquad d(\phi ^{-1})_{_{\phi(0,0)}}(\phi_{v}(0,0))=e_{2}$$
>>	5. Entonces $$[dF_{\phi(0,0)}]_{\{ \phi_{s},\phi_{t} \}}=[d\phi_{(0,0)} \circ L \circ d(\phi ^{-1})_{\phi(0,0)}]_{\{ \phi_{s},\phi_{t}\}}=\begin{pmatrix} a & b \\ c & d \end{pmatrix}$$  

---
  

>[!Example] Ejercicio 17
>Sea $S$ una superficie regular y sea $f : S \to \mathbb{R}$ una función suave con un punto crítico $p$. Mostrar que el hessiano $H_p$ de $f$ en $p$ está bien definido por
>$$ H_p : T_pS \to \mathbb{R}, \quad H_p(\alpha'(0)) = (f \circ \alpha)''(0), $$
>donde $\alpha$ es una curva suave en $S$ con $\alpha(0) = p$.
>>[!Proof]-
>>1. Debemos mostrar que el valor $(f \circ \alpha)''(0)$ depende solo del vector tangente $v = \alpha'(0)$ y no de la curva elegida.
>>2. Sea $\varphi : U \to S$ una carta local alrededor de $p$. Sea $\alpha(t) = \varphi(u(t))$. Entonces $f(\alpha(t)) = (f \circ \varphi)(u(t))$.
>>3. Primera derivada: $$\begin{align}df_{\alpha (t)}(\alpha '(t))& =(f \circ \alpha)'(t) \\ & =(f\circ\varphi)'(u(t)).u'(t)\\ & = \nabla(f\circ\varphi)_{u(t)}.u'(t) \\ & =\sum_i \frac{\partial (f \circ \varphi)}{\partial u_i}(u(t)) u_i'(t)\end{align}$$En $t=0$, esto es $df_p(\alpha'(0))$. 
>>4. Como $p$ es punto crítico, $df_p = 0$, así que la primera derivada es $0$ (esto es consistente).
>>5. Entonces podemos calcular la segunda derivada: $$(f \circ \alpha)''(t) = \sum_{i,j} \frac{\partial^2 (f \circ \varphi)}{\partial u_i \partial u_j}(u(t)) u_i'(t) u_j'(t) + \sum_i \frac{\partial (f \circ \varphi)}{\partial u_i}u(t) u_i''(t)$$
>>6. Evaluando en $t=0$: El segundo término contiene $\frac{\partial (f \circ \varphi)}{\partial u_i}|_{u(0)}$. Estas son las componentes de $df_p$.
>>Como $p$ es punto crítico, $df_p = 0$, por lo que el segundo término desaparece.
>>Queda:
>>$(f \circ \alpha)''(0) = \sum_{i,j} \frac{\partial^2 (f \circ \varphi)}{\partial u_i \partial u_j} u_i'(0) u_j'(0)$.
>>Esta expresión es una forma cuadrática en las componentes del vector velocidad $u'(0)$ (que son las coordenadas de $v = \alpha'(0)$ en la base de la carta).
>>Por lo tanto, el valor depende únicamente de $v$ y no de la aceleración $u''(0)$ de la curva.
>>Está bien definido.

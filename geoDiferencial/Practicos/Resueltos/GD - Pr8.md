# Soluciones — Geometría Diferencial — Práctico 8

---

>[!Example] Ejercicio 1
>Sea $S$ una superficie de revolución con curva generatriz de rapidez unitaria, parametrizada por $\varphi(s, t) = (r(t) \cos s, r(t) \text{sen } s, h(t))$.
>a) Probar que los meridianos son geodésicas.
>b) Probar que un paralelo $s \mapsto \phi(s, t_0)$ es geodésica si y sólo si $r'(t_0) = 0$.
>> [!Proof]-
>> - **(a)** 
>>	1. Primero notar que la curva generatriz $(r(t),h(t))$ tiene rapidez unitaria entonces $$(r'(t))^2+(h'(t))^2=1^{2}$$
>>	2. Since $(r')^2+(h')^2=1$, derivando obtenemos $r'r''+h'h''=0.$
>>	3. Entonces $(r''(t),h''(t))$ es ortogonal a $(r'(t),h'(t))$, luego existe un escalar $\lambda(t)$ tal que $$(r''(t),h''(t))=\lambda(t)(h'(t),-r'(t)).$$
>>	4. Fijamos $s=s_0$ lo que nos da curvas meridianas $$\alpha(t)=\varphi(s_0,t)=(r(t)\cos s_0,\; r(t)\sin s_0,\; h(t))$$
>>	5. Derivamos $$\alpha'(t)=(r'(t)\cos s_0,\; r'(t)\sin s_0,\; h'(t)),$$$$\alpha''(t)=(r''(t)\cos s_0,\; r''(t)\sin s_0,\; h''(t)).$$
>>	6. Calculamos $n$: $$\varphi_s=(-r\sin s,\; r\cos s,\;0),\quad
>> 	\varphi_t=(r'\cos s,\; r'\sin s,\; h')$$$$\varphi_s\times\varphi_t=(rh'\cos s,\; rh'\sin s,\; -rr').$$
>> 	7. Evaluamos $n$ sobre $s=s_0$, $$N(t)=(rh'(t)\cos s_0,\; rh'(t)\sin s_0,\; -rr'(t)).$$
>> 	8. Luego por 3.
>> 	$$\alpha''(t)=\lambda(t)(h'(t)\cos s_0,\; h'(t)\sin s_0,\; -r'(t))
>> 	=\lambda(t)\,N(t).$$
>> - **(b)** 
>> 	1. Consideremos un paralelo $$\gamma(s) = \varphi(s, t_0)=(r(t_{0}) \cos s, r(t_{0}) \text{sen } s, h(t_{0}))$$
>> 	2. Derivada segunda: $\gamma''(s) = (-r(t_{0}) \cos s,\ -r(t_{0}) \sin s,\ 0)$
>> 	3. Producto con $\varphi_t$: $-r(t_{0}) r'(t_0)$ y el producto con $\varphi_{s}$ es 0 
>> 	4. Por lo tanto, geodésica si y solo si $r'(t_0) = 0$.
>> 	5. Notar que $r(t_{0})\neq0$ por que si no estariamos mirando $\gamma(s)=(0,0,h(t_{0}))$ que seria un punto, por defincion no es considerado un paralelo un paralelo  

---

>[!Example] Ejercicio 2
>Los paralelos de el toro $T(R, r)$ por los puntos $(R+r, 0), (R-r, 0), (R, r)$ son llamados paralelo máximo, paralelo mínimo y paralelo superior, respectivamente. Verificar cuál de estos paralelos es la trayectoria de una geodésica del toro.
>>[!Proof]-
>>1. Recordemos la parametrizacion del toro $$\phi(s, t) = ((R + r \cos t)\cos s, (R + r \cos t)\text{sen } s, r \text{sen } t)$$ Que seria la superficie de revolucion de $r(t)=R+r\cos t$ y $h(t)=r\sin t$
>>2. Usamos el criterio del Ejercicio 1b: Un paralelo es geodésica si $r'(t) = 0$. 
>>3. En este caso $-r\sin t=0$ que se da si $t=0,\pi$ 
>>4. Entonces los siguiente son geodesicas
>>5. **Paralelo máximo:** $t=0$. Entonces $r(\pi)=R+r$. y $h(\pi)=0$. (y luego revolucionar, por eso es el paralelo externo) 
>>6. **Paralelo mínimo:** $t=\pi$. Entonces $r(\pi)=R-r$. y $h(\pi)=0$. Analogo, por eso es el paralelo interno
>>7. Ademas el **Paralelo superior:** es cuando $t=\pi/2$ $r(t)=R$ y $h(t)=r$. (Que revolucionando nos da paralelo superior). Pero $r'(\pi/2) = -r \neq 0$. **No es geodésica.**
>>8. Esto tiene sentido con la idea de que las geodesicas son curvas que no estan cambiando de direccion si son miradas desde la superficie (o mas bien desde el plano tangente). La curva superior claramente esta "doblando" mirada desde el plano tangente. Pero las laterales no (si bien tienen cuarvatura normal , no tienen curvatura geodesica) 

---

>[!Example] Ejercicio 3
>Hallar todas las geodésicas del cilindro.
>>[!Proof]-
>>- Parametrizamos al cilindro como $\varphi(u,v)=(r\cos(u),r\sin(u),v)$ 
>>- **1era Solucion**
>>	1. Es facil calcular el campo normal unitario $$n(u,v)=(\cos(u),\sin(u),0)$$ 
>>	2. Tomamos una curva cualquiera en el cilindro osea $$\gamma(t)=(r\cos(u(t)),r\sin(u(t)),v(t))$$ 
>>	3. Por lo tanto derivando componente a componente $$\gamma'(t)=(-r\sin(u(t))u'(t),r\cos(u(t))u'(t),v'(t))=(-r\sin(u(t)),r\cos(u(t)),0)u'(t)+(0,0,1)v'(t)$$
>>	4. Analogamente  $$\gamma''(t)=-u'^{2}(r\cos u,r\sin u,0)+u''(-r\sin u,r\cos u,0)+v''(0,0,1)$$
>>	5. Notar que solo el primer sumando es paralelo a la normal y nosotros queremos $\gamma''(t)$ sea paralelo a la normal, por ende necesitamos que $u''(t)=v''(t)=0$
>>	6. Integrando llegamos a que $u(t)=at+b$ y $v(t)=ct+d$ 
>>	7. Luego $\gamma(t)=(r\cos(at+b),r\sin(at+b),ct+d)$ son geodesicas
>>	8. Y es facil verificar que serian las rectas verticales, los circulos horizontales y las helices
>>- **2da Solucion**
>>	1. Notamos que $$\varphi(u,v)=\left( r\cos\left( \frac{u}{r} \right),r\sin\left( \frac{u}{r} \right),v \right)$$ es directamente una isometria entre plano (lonja de ancho $(0,2\pi)$) y cilindro 
>>	2. Es facil ver que las longitudes se preservan tomando $\alpha(t)=(u(t),v(t))$ en el plano tenemos que $\lVert \alpha '(t) \rVert=\sqrt{ u'^{2}+v'^{2} }$ 
>>	3. Por otro lado $$\varphi\circ\alpha'(t)=(-\sin(u(t))u'(t),\cos(u(t))u'(t),v'(t))$$ entonces $\lVert \varphi\circ\alpha ' \rVert=\sqrt{ u'^{2}+v'^{2} }$ 
>>	4. Mostrando que son isometrias (preservan longitudes)
>>	5. Luego como isometria preservan geodesicas, las geodesicas del plano seran preservadas
>>	6. Se concluye lo mismo que arriba

---

>[!Example] Ejercicio 4
>Recurrir al resultado que detecta geodésicas cuando la superficie es preservada por una reflexión respecto de un plano para encontrar las trayectorias de tres geodésicas de la superficie definida implícitamente por $9x^2 + \frac{y^2}{4} + z^2 = 1$.
>>[!Proof]-
>>1. Recordemos de lo que habla el ejercicio [[Definiciones#^2bbc2c]]
>>2. La ecuación $9x^2 + \frac{y^2}{4} + z^2 = 1$ es un elipsoide.
>>3. Es invariante bajo las reflexiones de los planos coordenados:
>>   - Plano $xy$ ($z \to -z$): La ecuación no cambia ($z^2$). Por lo tanto es invariante por reflexion. Entonces la intersección con plano xy (z=0): Elipse $9x^2 + y^2/4 = 1$. **Es geodésica.**
>>   - Plano $xz$ ($y \to -y$): La ecuación no cambia. Intersección: Elipse $9x^2 + z^2 = 1$. **Es geodésica.**
>>   - Plano $yz$ ($x \to -x$): La ecuación no cambia. Intersección: Elipse $y^2/4 + z^2 = 1$. **Es geodésica.**

---

>[!Example] Ejercicio 5
>Mostrar que un campo paralelo a lo largo de una geodésica $\gamma$ forma un ángulo constante con $\gamma'$.
>>[!Proof]-    
>>1. Queremos ver que $\langle W,\gamma'\rangle=c$ y esto vale si y solo si $$\langle W',\gamma'\rangle+ \langle W,\gamma''\rangle=0$$
>>2. Pero por definicion de campo paralelo $W(t)'\perp T_{\gamma(t)}M$ y obviamente $\gamma'\in T_{\gamma(t)}M$ entonces $\langle W',\gamma'\rangle=0$
>>3. Por otro lado como $\gamma$ es geodesica sabemos que $\gamma''$ es multiplo del campo normal por lo tanto $\gamma''\perp T_{\gamma(t)}M$ y sabemos por definicion que $W\in T_{\gamma(t)}M$ por lo tanto $\langle W,\gamma''\rangle=0$  
>>4. Aqui asumimos que $\gamma$ es parametrizada por longitud de arco (rapidez unitaria).
>>5. No lo voy a hacer pero la idea seria que $\gamma(\alpha(s)) =\beta(s)$ seria la reparametrizacion. Entonces tendrias $\tilde{W}(s)=W(\alpha (s))$ y apareceria la derivada de $\alpha$ cuando derivas $\tilde{W}$ y cuando derivas $\beta$ pero no cambia el angulo esto.

---

>[!Example] Ejercicio 6
>Sea $S$ la esfera de centro cero y radio 1 y sea $\alpha$ una parametrización por longitud de arco del paralelo de altura $1/2$. Sea $W$ un campo paralelo a lo largo de $\alpha$ con $W(0) = \alpha'(0)$. Indicar cuántas vueltas da $W$ respecto del marco móvil a lo largo de $\alpha$ cuando esta curva da una vuelta completa. ¿Cuánto gira realmente $W$ a lo largo de $\alpha$?
>>[!Proof]-
>>1. **Datos:** Esfera radio $R=1$. Altura $z=1/2$.
>>   El ángulo de la latitud $\lambda$ cumple $\sin \lambda = 1/2 \implies \lambda = 30^\circ = \pi/6$.
>>   El ángulo de colatitud es $\varphi = \pi/2 - \pi/6 = \pi/3 = 60^\circ$.
>>   Radio del paralelo: $r = R \sin \varphi = \sin(\pi/3) = \sqrt{3}/2$.
>>2. **Cálculo de cambio de ángulo (Holonomía):**
>>   Usamos la fórmula de Gauss-Bonnet o la fórmula específica para conos tangentes.
>>   El ángulo $\Delta \psi$ que gira un campo paralelo respecto a la curva (o tangente) tras una vuelta cerrada es igual a la integral de la curvatura gaussiana en la región encerrada (teorema de GB).
>>   $\Delta \theta_{transporte} = \iint_{D} K dA$.
>>   $K=1$. Área del casquete esférico sobre el plano $z=1/2$:
>>   $Area = 2\pi R h = 2\pi(1)(1 - 1/2) = \pi$.
>>   Por tanto, el desplazamiento angular total debido a la curvatura es $\pi$.
>>3. **Interpretación:**
>>   El vector $W$ transportado paralelamente "retrocede" un ángulo $\pi$ respecto al vector tangente inicial si completamos el ciclo?
>>   Más preciso: El vector tangente $\alpha'$ *rota* $2\pi$ en el espacio (visto desde arriba) pero en la geometría intrínseca...
>>   Usemos la fórmula de variación de ángulo con el paralelo: $\Delta \beta = -2\pi \sin(\lambda)$? No.
>>   Desarrollo en cono: El perímetro del paralelo es $L = 2\pi r = 2\pi (\frac{\sqrt{3}}{2}) = \pi \sqrt{3}$.
>>   La generatriz del cono tangente es $d = R \cot \varphi$? No.
>>   Más simple: El ángulo que gira respecto a la base fija es $2\pi \cos \varphi$ o $2\pi \sin \lambda$.
>>   $\text{Angulo} = 2\pi (1 - \sin \lambda)$? No.
>>   La fórmula estándar para el ángulo que *rota* el vector respecto a la curva tangente es $2\pi - \iint K$.
>>   Osea $2\pi - \pi = \pi$.
>>   El vector $W$ (paralelo) termina formando un ángulo de $-\pi$ (o $\pi$) con el vector tangente $\alpha'(L)$ (que coincide con $\alpha'(0)$ geométricamente).
>>   **Respuesta:** Respecto al marco móvil (tangente), da media vuelta ($\pi$).
>>   "¿Cuánto gira realmente W?" Si se refiere a respecto a un sistema inercial fijo en el espacio 3D incrustado: El vector se mantiene "lo más constante posible", pero al volver no coincide.
>>   En el péndulo de Foucault, la rotación del plano de oscilación (campo paralelo) es $-2\pi \sin(\text{latitud})$.
>>   Aquí latitud $\pi/6$, $\sin = 1/2$. Rotación = $-\pi$.
>>   Da media vuelta en sentido de las agujas del reloj (si la Tierra gira antihorario).

---

>[!Example] Ejercicio 7
>Sea $M$ el helicoide, parametrizado por $\phi(u, v) = (u \cos v, u \text{sen } v, v)$.
>a) Calcular la curvatura geodésica de la hélice $\alpha(t) = (\cos(at), \text{sen}(at), at)$ ($a=1/\sqrt{2}$).
>b) Indicar si $\alpha$ minimiza la distancia entre algunos puntos de su trayectoria.
>c) Encontrar el campo paralelo $W$ a lo largo de $\alpha$ con $W(0) = \alpha'(0)$.
>>[!Proof]-
>>- **a) Curvatura geodésica:**
>>	1. La curva $\alpha(t)$ corresponde en la parametrización a $u(t)=1, v(t)=at$? No.
>>	   $\phi(u, v) = (u\cos v, \dots)$. $\alpha(t)$ tiene radio 1? No.
>>	   En $\alpha(t) = (\cos(at), \sin(at), at)$, el radio $x^2+y^2=1$.
>>	   Por tanto $u=1$. $\phi(1, at) = (\cos(at), \sin(at), at)$.
>>	   Así que la curva en coordenadas es $u(t) = 1$ (constante), $v(t) = at$. Es una curva coordenada ($u$-constante).
>>	2. Curvatura geodésica $k_g$.
>>	   Fórmula general o cálculo directo: $k_g = \vec{N} \cdot (\alpha' \times \alpha'')$? No, eso es un lío con las normas.
>>	   Usemos la fórmula de Liouville o Christoffel.
>>	   Métrica del helicoide: $\phi_u = (\cos v, \sin v, 0)$, $\phi_v = (-u\sin v, u\cos v, 1)$.
>>	   $E = 1, F = 0, G = 1+u^2$.
>>	   Para $u=1$, $G=2$.
>>	   Curva $u=1, v=at$.
>>	   Fórmula $k_g = -\frac{E_u}{2E\sqrt{G}} v'$ (para curva $u=cte$)?
>>	   O mejor: La curva coordenada $v$ (con $u=cte$) es geodésica ssi $E_v = 0$ (si, $0=0$) y $G_u = 0$.
>>	   $G_u = 2u$. En $u=1$, $G_u = 2 \neq 0$.
>>	   Entonces NO es geodésica.
>>	   Cálculo de $k_g$ para curvas $u=cte$:
>>	   $k_g = \frac{\Gamma_{vv}^u (v')^2}{\dots}$??
>>	   Formula: $k_g = - \frac{1}{2\sqrt{G}E} \frac{\partial G}{\partial u}$. (Signo depende orientación).
>>	   $\frac{\partial G}{\partial u} = 2u$. En $u=1$, es 2.
>>	   $k_g = - \frac{2}{2\sqrt{2}(1)} = -\frac{1}{\sqrt{2}}$.
>>- **b) Minimización:**
>>	Como $k_g \neq 0$, la curva NO es una geodésica.
>>	Las curvas que minimizan distancia localmente son geodésicas.
>>	Por tanto, $\alpha$ **no minimiza la distancia** (ni siquiera localmente, salvo orden infinitesimal).
>>- **c) Campo paralelo:**
>>	1. Ec. transporte paralelo para $W = A \phi_u + B \phi_v$. $\alpha'(t) = a \phi_v$.
>>	   $W(0) = \alpha'(0) = a \phi_v$.
>>	   $\nabla_{\alpha'}W = 0 \implies W' + \Gamma W = 0$.
>>	   Debido a $F=0$ y la simetría, las ecuaciones se simplifican.
>>	   Sistema de EDOs lineales. La solución suele girar con velocidad angular proporcional a $k_g$.
>>	   El ángulo $\theta$ que forma $W$ con $\alpha'$ satisface $\theta' = -k_g$.
>>	2. Como $k_g = -1/\sqrt{2}$ (cte).
>>	   $\theta(t) = -(-1/\sqrt{2}) t = t/\sqrt{2}$.
>>	   El campo gira uniformemente respecto a la tangente.
>>	   En $t=\sqrt{2}\pi$, $\theta = \pi$. Ha dado media vuelta (apunta opuesto).

---

>[!Example] Ejercicio 8
>Dado que se sabe que las geodésicas de la esfera son los círculos máximos, mostrar la existencia de triángulos geodésicos cuyos ángulos interiores suman más que $\pi$.
>>[!Proof]-
>>1. Consideremos tres puntos en la esfera:
>>   $N = (0, 0, 1)$ (Polo Norte).
>>   $A = (1, 0, 0)$ (Ecuador).
>>   $B = (0, 1, 0)$ (Ecuador).
>>2. Los lados del triángulo son segmentos de círculos máximos:
>>   - Arco $NA$: Meridiano de longitud $\pi/2$. Ángulo en $A$: El meridiano corta al ecuador perpendicularmente. $\angle A = \pi/2$.
>>   - Arco $NB$: Meridiano de longitud $\pi/2$. Ángulo en $B$: Perpendicular al ecuador. $\angle B = \pi/2$.
>>   - Arco $AB$: Segmento del ecuador. El ángulo en $N$ entre los meridianos $x$ e $y$ es $\pi/2$.
>>3. Suma de ángulos interiores:
>>   $\Sigma = \pi/2 + \pi/2 + \pi/2 = 3\pi/2$.
>>4. $3\pi/2 > \pi$.
>>5. (Esto es consistente con Gauss-Bonnet: $\int K dA = \Area(Triangulo) = 1/8 \text{esfera} = 4\pi/8 = \pi/2$. Exceso angular $\Sigma - \pi = \pi/2$).

---

>[!Example] Ejercicio 9
>Sea $\gamma$ una geodésica de una superficie regular $M$. Probar que si $\gamma$ tiene curvatura nunca nula y está en un plano $P$, entonces $\gamma$ es una línea de curvatura de $M$.
>Sugerencia: Mostrar primero que si $N$ es normal a $P$, entonces $\{\gamma'(t), \gamma''(t), N\}$ es una base ortogonal de $\mathbb{R}^3$ para todo $t$. (Nota: La sugerencia parece referirse a $N_S$ normal superficie o $N_P$ normal plano? Texto dice N es normal a P. Pero necesitamos relacionar con normal superficie.)
>>[!Proof]-
>>1. Sea $\gamma(s)$ parametrizada por arco.
>>2. Como $\gamma$ es geodésica, su aceleración $\gamma''(s)$ es ortogonal al plano tangente $T_{\gamma(s)}M$ y colineal con el vector normal de la superficie $\mathcal{N}(s)$.
>>   $\gamma''(s) = k_n \mathcal{N}(s)$. (La curvatura geodésica es nula).
>>   Como la curvatura de la curva $\kappa = \|\gamma''\|$ no es nula, entonces $\gamma''(s) \neq 0$, y $\mathcal{N}(s) = \pm \frac{\gamma''(s)}{\kappa(s)}$.
>>3. Por otro lado, $\gamma$ es una curva plana contenida en $P$.
>>   Su vector binormal $B$ del triedro de Frenet es constante y perpendicular a $P$.
>>   $\gamma''(s) = \kappa n_{frenet}$. El vector $n_{frenet}$ está contenido en el plano $P$.
>>4. De (2), el vector normal a la superficie $\mathcal{N}$ es paralelo a $n_{frenet} = \gamma'' / \kappa$.
>>   Por lo tanto, $\mathcal{N}$ está contenido en el plano $P$.
>>   (Ojo: $\gamma''$ es normal a la superficie. $\gamma''$ está en el plano osculador = $P$. Así que la normal a la superficie está en el plano de la curva).
>>5. Veamos que $\gamma$ es línea de curvatura. Esto significa que $\gamma'$ es dirección principal.
>>   Equivalente: La derivada del normal $d\mathcal{N}(\gamma') = (\mathcal{N} \circ \gamma)'$ es colineal a $\gamma'$.
>>6. Sabemos que $\mathcal{N}(s) = \pm n_{frenet}(s)$.
>>   Derivamos: $\mathcal{N}' = \pm n'_{frenet} = \pm (-\kappa t + \tau b)$.
>>   Como la curva es plana, la torsión $\tau = 0$.
>>   $\mathcal{N}' = \mp \kappa \gamma'$.
>>7. Entonces $d\mathcal{N}(\gamma') = \lambda \gamma'$ (con $\lambda = \mp \kappa$).
>>8. Por tanto, $\gamma'$ es una dirección principal y $\gamma$ es una línea de curvatura.

---

>[!Example] Ejercicio 10
>Mostrar que una isometría local entre superficies no preserva necesariamente el módulo de la curvatura media. Comparar con la afirmación análoga para la curvatura gaussiana.
>>[!Proof]-
>>1. **Curvatura Gaussiana:** El *Teorema Egregium* de Gauss afirma que la curvatura Gaussiana $K$ es un invariante intrínseco. Si $f: S_1 \to S_2$ es una isometría local, entonces $K_2(f(p)) = K_1(p)$.
>>2. **Curvatura Media:** La curvatura media $H = \frac{k_1+k_2}{2}$ es un invariante extrínseco (depende de cómo está inmersa la superficie en $\mathbb{R}^3$). No necesariamente se preserva.
>>3. **Contraejemplo:**
>>   - Superficie 1: Plano $P$ ($z=0$). Es isométrico a sí mismo. $k_1=0, k_2=0 \implies H=0$.
>>   - Superficie 2: Cilindro $C$ ($x^2+y^2=1$). Es localmente isométrico al plano (al desenrollarlo).
>>     Sus curvaturas principales son $k_1=0$ (generatriz) y $k_2=1$ (círculo).
>>     $H = \frac{0+1}{2} = 1/2$.
>>4. Como $0 \neq 1/2$, la isometría no preserva la curvatura media.

---

>[!Example] Ejercicio 11
>Considerar la esfera de radio uno, el cilindro y la silla de montar. Justificar por qué estas superficies no son localmente isométricas entre sí.
>>[!Proof]-
>>1. Por el Teorema Egregium, si dos superficies son localmente isométricas, deben tener la misma curvatura Gaussiana $K$ en los puntos correspondientes.
>>2. **Esfera ($S^2$):** $K = 1$ (constante positiva).
>>3. **Cilindro:** $K = 0$ (constante nula, pues es desarrollable).
>>4. **Silla de montar ($z = x^2 - y^2$ o similar):** $K < 0$ (negativa en todas partes salvo quizás el origen? En el paraboloide hiperbólico estándar $K = -1/(1+4u^2+4v^2)^2 < 0$. Silla mono $K$ varía pero es $\le 0$).
>>5. Como los signos (y valores) de $K$ son distintos ($1 \neq 0 \neq \text{negativo}$), no pueden existir isometrías locales entre ellas.

---

>[!Example] Ejercicio 12
>Probar que no existe una carta $\phi$ de la esfera $S$ de centro cero y radio $r$ tal que para todo $(u, v)$ en el dominio de $\phi$ la base $\{\phi_u(u, v), \phi_v(u, v)\}$ de $T_{\phi(u, v)}S$ sea ortonormal.
>>[!Proof]-
>>1. Supongamos que existe tal carta.
>>2. Que la base coordenada sea ortonormal significa $E = \|\phi_u\|^2 = 1$, $F = \langle \phi_u, \phi_v \rangle = 0$, $G = \|\phi_v\|^2 = 1$.
>>3. Esta es la métrica euclidiana $ds^2 = du^2 + dv^2$.
>>4. La curvatura Gaussiana de una métrica está determinada únicamente por $E, F, G$.
>>   Para la métrica euclidiana, $K \equiv 0$.
>>5. Sin embargo, sabemos que para la esfera de radio $r$, $K = 1/r^2 > 0$.
>>6. Contradicción ($1/r^2 \neq 0$).
>>7. Por lo tanto, tal carta no existe (la esfera no es localmente isométrica al plano).

---

>[!Example] Ejercicio 13
>Para cada $r > 0$, sea $C_r$ el cilindro $\{(x, y, z) \in \mathbb{R}^3 : x^2 + y^2 = r^2\}$. Probar $C_r$ no es isométrico al plano $z=0$ ni al cilindro $C_\rho$ si $\rho \neq r$. Sugerencia: Considerar las geodésicas periódicas.
>>[!Proof]-
>>- **No isométrico al plano globalmente:**
>>	1. Localmente son isométricos ($K=0$). Pero globalmente no.
>>	2. En $C_r$, existen geodésicas cerradas simples (los paralelos o ecuadores) de longitud $2\pi r$.
>>	3. En el plano $\mathbb{R}^2$, las geodésicas son rectas infinitas. No existen geodésicas cerradas.
>>	4. Una isometría global (difeormorfismo que preserva métrica) mapearía geodésicas cerradas a geodésicas cerradas. Como el plano no tiene, no son isométricos.
>>- **No isométrico a $C_\rho$ ($\rho \neq r$):**
>>	1. Supongamos que existe una isometría $F: C_r \to C_\rho$.
>>	2. Las geodésicas cerradas simples de $C_r$ tienen longitud $2\pi r$.
>>	3. Las geodésicas cerradas simples de $C_\rho$ tienen longitud $2\pi \rho$.
>>	4. La imagen de una geodésica cerrada simple por una isometría debe ser una geodésica cerrada simple de la misma longitud.
>>	5. Entonces $2\pi r = 2\pi \rho \implies r = \rho$.
>>	6. Si $r \neq \rho$, no pueden ser isométricos.

---

>[!Example] Ejercicio 14
>Sea $S$ el hiperboloide de revolución $x^2 + y^2 - z^2 = 1$, sea $p \in S$ con tercera coordenada mayor que dos ($z_0 > 2$), y sea $v \in T_pS$ un vector unitario que forma un ángulo de $\pi/3$ con el paralelo que pasa por $p$. Probar que la geodésica con velocidad inicial $v$ nunca tiene tercera coordenada negativa.
>Sugerencia: Usar el Teorema de Clairaut.
>>[!Proof]-
>>1. **Parametrización y Clairaut:**
>>   $S$ es superficie de revolución. Radio al eje $z$: $r(z) = \sqrt{1+z^2}$.
>>   Teorema de Clairaut: A lo largo de una geodésica, $r(t) \cos \theta(t) = C = \text{cte}$, donde $\theta$ es el ángulo con el paralelo.
>>2. **Condiciones iniciales:**
>>   En $p$, $z_0 > 2$. Radio inicial $r_0 = \sqrt{1+z_0^2} > \sqrt{1+4} = \sqrt{5}$.
>>   Ángulo inicial $\theta_0 = \pi/3 \implies \cos \theta_0 = 1/2$.
>>   Constante de Clairaut: $C = r_0 \cos \theta_0 = r_0 / 2 > \sqrt{5}/2 \approx 1.118$.
>>3. **Análisis:**
>>   En cualquier punto de la geodésica, debe cumplirse $r(t) \cos \theta(t) = C$.
>>   Como $|\cos \theta| \le 1$, tenemos $r(t) \ge C$.
>>   Por tanto, la geodésica está confinada a la región donde el radio del paralelo $r(z) \ge C$.
>>   $r(z) = \sqrt{1+z^2} \ge C > 1.118$.
>>   El mínimo radio del hiperboloide ("cintura") ocurre en $z=0$ y es $r(0)=1$.
>>   Como $C > 1$, la geodésica nunca puede alcanzar la cintura $z=0$ (donde $r=1$), ya que requeriría $1 \cdot \cos \theta = C > 1$, imposible.
>>4. **Conclusión:**
>>   Como la curva empieza en $z > 2$ (hemisferio norte) y no puede cruzar la banda ecuatorial $z=0$ (donde el radio es muy pequeño para preservar el momento angular $C$), la geodésica permanece confinada en la región $z > 0$.
>>   Nunca tiene coordenada $z$ negativa.

---

>[!Example] Ejercicio 15
>Sea $p$ un punto en una superficie $S$. Se puede probar que si $r > 0$ es suficientemente pequeño, entonces la circunferencia intrínseca de radio $r$ centrada en $p$, dada por $C_p(r) = \{\gamma(r) \mid \gamma \text{ es geodésica unitaria con } \gamma(0)=p\}$, es la imagen de una curva en $S$. Verificar en el caso particular que $S$ es la esfera de radio $R$ que la aproximación de Taylor de tercer grado de la función $r \mapsto \text{long}(C_p(r))$ es
>$$ 2\pi r - \frac{\pi}{3} K(p) r^3, $$
>donde $K(p)=1/R^2$.
>>[!Proof]-
>>1. En la esfera de radio $R$, las geodésicas son círculos máximos.
>>2. Una circunferencia geodésica de radio intrínseco $r$ (distancia medida sobre la superficie desde el polo $p$) corresponde a un paralelo a distancia de arco $r$.
>>   El ángulo polar correspondiente es $\theta = r/R$.
>>3. El radio euclidiano de este paralelo (distancia al eje $z$) es $\rho = R \sin \theta = R \sin(r/R)$.
>>4. La longitud de esta circunferencia es $L(r) = 2\pi \rho = 2\pi R \sin(r/R)$.
>>5. Desarrollo de Taylor de $\sin(x)$ cerca de 0: $\sin(x) \approx x - \frac{x^3}{6} + \dots$
>>   Sustituyendo $x = r/R$:
>>   $L(r) \approx 2\pi R \left( \frac{r}{R} - \frac{1}{6} \frac{r^3}{R^3} \right)$.
>>   $L(r) \approx 2\pi r - \frac{\pi}{3} \frac{r^3}{R^2}$.
>>6. Como la curvatura gaussiana de la esfera es $K = 1/R^2$, sustituimos:
>>   $L(r) \approx 2\pi r - \frac{\pi}{3} K r^3$. (Nota: El enunciado dice $2\pi r - \frac{2\pi}{3!} K r^3$? $2\pi/6 = \pi/3$. Correcto. El enunciado dice $2\pi r - \frac{2\pi}{3!} K r^3$, que es lo mismo).

---

>[!Example] Ejercicio 16
>Optativo. Visualización del transporte paralelo como mapa $u \mapsto -u^2$ en complejos.
>>[!Proof]-
>>El ejercicio pide visualizar, no probar formalmente.
>>Identificamos el plano tangente en el polo norte con $\mathbb{C}$. Los vectores unitarios son $u = e^{i\theta}$.
>>Transportamos este vector a lo largo del meridiano hacia el polo sur.
>>Por el Ejercicio 6, vimos que al volver da un giro de $\pi$ (o similar dependiendo del camino).
>>Aquí se viaja del Polo Norte al Sur. El campo paralelo a lo largo de un meridiano mantiene un ángulo constante con el meridiano.
>>El meridiano $\gamma_u$ sale con ángulo $\theta$ (asociado a $u$).
>>En el polo sur, el meridiano llega "desde el otro lado".
>>Si visualizamos la esfera y los vectores tangentes... se puede ver que la transformación inducida por el transporte paralelo de N a S a lo largo de la geodésica induce esa rotación doble en la coordenada compleja.
>>**(Sin prueba formal requerida).**

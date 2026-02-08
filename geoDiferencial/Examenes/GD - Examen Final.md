# Examen de Geometría Diferencial - 2 de diciembre de 2024

## Parte práctica

>[!Example] Ejercicio 1 (10 puntos)
>Sea $\alpha: (a, b) \to \mathbb{R}^3$ una curva suave de rapidez unitaria y curvatura nunca nula, con aparato de Frenet $\{T, N, B\}$. Una función suave $v: (a, b) \to \mathbb{R}^3$ con $\|v(t)\| = 1$ para todo $t$ se llama campo normal relativamente paralelo (c.n.r.p.) a lo largo de $\alpha$ si $$\langle v(t), \alpha'(t) \rangle = 0 \quad \text{y} \quad v'(t) = \lambda(t) \alpha'(t)$$para todo $t$, para cierta función $\lambda: (a, b) \to \mathbb{R}$. 
>Suponiendo que $$v(t) = \cos(\theta(t)) N(t) + \sin(\theta(t)) B(t)$$para cierta función $\theta: (a, b) \to \mathbb{R}$, encontrar condiciones sobre $\theta'$ en términos de la curvatura y la torsión de $\alpha$ para que $v$ sea un c.n.r.p. a lo largo de $\alpha$.
>>[!Proof]-
>>1. Usando las ecuaciones de Frenet–Serret $T'=\kappa N$, $N'=-\kappa T+\tau B$, $B'=-\tau N$ y la expresión $v=\cos\theta\,N+\sin\theta\,B$, derivamos: $$\begin{align} v'& =( \cos\theta\,N+\sin\theta\,B)'\\ & = \cos\theta\,N' + (\cos\theta)'N + \sin\theta\,B' + (\sin\theta)'B \\&= \cos\theta(-\kappa T+\tau B) - \theta'\sin\theta\,N + \sin\theta(-\tau N) + \theta'\cos\theta\ B\end{align}$$
>>2. Las componentes en $N$ y $B$ son $-(\tau+\theta')\sin\theta$ en $N$ y $(\tau+\theta')\cos\theta$ en $B$. 
>>3. Para que $v'$ sea colineal con $T$ (i.e., $v' = \lambda T$) y por tanto sin componente normal, debe cumplirse $\tau+\theta'\equiv 0$.
>>4. Bajo esta condición, $v'= -\kappa\cos\theta\,T$, luego $v' = \lambda T$ con $\lambda = -\kappa\cos\theta$.
>>5. Conclusión: $v$ es c.n.r.p. si y solo si $\theta'(t) = -\tau(t)$.
	
> [!Example] Ejercicio 2 (34 puntos)
> Sea $U = \{(x, y) \in \mathbb{R}^2 \mid x > 0\}$ y sea $M$ el gráfico de la función $f: U \to \mathbb{R}$, $f(x, y) = (\log x)^2$, que es una superficie regular.
> - **(a)** Mostrar que $\psi: U \to \mathbb{R}^3, \psi(u, v) = (e^{\sqrt{u}}, v, u)$ es un sistema coordenado de $M$
> - **(b)** Calcular la curvatura gaussiana y la curvatura media de $M$ en el punto $(1, 0, 0)$.
> - **(c)** Sea $A = \{(x, y, z) \in \mathbb{R}^3 \mid x > 0\}$ y $F : A \to A, F(x, y, z) = (\frac{1}{x}, y, z)$. Mostrar que $F$ lleva $M$ en $M$ y que la restricción de $F$ a $M$ es un difeomorfismo. ¿Es una isometría de $M$?
>> [!Proof]-
>>- (a) 
>>	1. Tenemos $\psi(u,v)=(e^{\sqrt{u}},\ v,\ u)$ y notamos que $f(e^{\sqrt{ u }},v)=u$, con lo cual $(e^{\sqrt{ u }},v,u)\in M$. Entonces $\psi$ parametriza correctamente
>>	2. Sea $\phi(x,y,z)=((\log x)^{2},y)$ es directo verificar que es inversa de $\psi$ (considerando que $x>0$) 
>>	3. Derivadas: $\psi_u=\big(\tfrac{e^{\sqrt{u}}}{2\sqrt{u}},\ 0,\ 1\big)$, $\psi_v=(0,1,0)$; son LI en todo $U$. Por su segunda coordenada 
>>	4. Luego es sistema coordenado
>>- (b) 
>>	1. Use la parametrización del gráfico $\varphi(x,y)=(x,y,f(x,y))$ con $f(x,y)=(\log x)^2$; la base tangente es $\{\varphi_x,\varphi_y\}$ con $\varphi_x=(1,0,f_x)$, $\varphi_y=(0,1,f_y)$.
>>	2. Calcule derivadas: $f_x=\tfrac{2\log x}{x}$, $f_y=0$, $f_{xx}=\tfrac{2(1-\log x)}{x^2}$, $f_{xy}=0$, $f_{yy}=0$
>>	3. Luego como queremos ver el punto $\varphi(1,0)=(1,0,0)$ evaluamos en $(1,0)$ entonces se tiene $f_x=0$, $f_y=0$, $f_{xx}=2$, $f_{xy}=0$, $f_{yy}=0$.
>>	4. El normal unitario para un gráfico es $n=\dfrac{(-f_x,-f_y,1)}{\sqrt{1+f_x^2+f_y^2}}$ por [[GD - Pr7#^5a9dfd]] 
>>	5. 
>>	6. Calcule $n_x$ y $n_y$ a mano. Con $n=\dfrac{(-f_x,-f_y,1)}{\sqrt{1+f_x^2+f_y^2}}$, se tiene en general: $$n_x=\dfrac{(-f_{xx},-f_{xy},0)}{(1+f_x^2+f_y^2)^{3/2} }+\dfrac{(-f_x,-f_y,1)(f_xf_{xx}+f_yf_{yx})}{(1+f_x^2+f_y^2)^{5/2}}$$ y $$n_y=\dfrac{(-f_{xy},-f_{yy},0)}{(1+f_x^2+f_y^2)^{3/2} }+\dfrac{(-f_x,-f_y,1)(f_xf_{xy}+f_yf_{yy})}{(1+f_x^2+f_y^2)^{5/2}}$$
>>	7. En $(1,0)$, usando 3. llegamos a $$n_x(1,0)=(-2,0,0)\qquad n_y(1,0)=(0,0,0)$$
>>	8. Entonces $-dn_{(1,0,0)}=\begin{pmatrix}-2&0\\0&0\end{pmatrix}$.
>>	9. La curvatura gaussiana es: $$K=\det S=2\cdot 0-0^2=0$$Y la curvatura media es $$H=\tfrac{1}{2}\operatorname{tr} S=\tfrac{1}{2}(-2+0)=-1$$
>>- (c)
>>	1. $F(x,y,z)=(1/x,\ y,\ z)$ mantiene $z=(\log x)^2=(\log(1/x))^2$, por lo que $F(M)\subset M$.
>>	2. $F|_M$ es claramente la restriccion de una funcion suave, por ende suave, lo mismo para su inversa. Entonces es un diferomorfismo
>>	3. Notemos que  $$dF_{(1,0,0)}=\begin{pmatrix} -\frac{1}{2} & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{pmatrix}$$ no es una isometria. Por que si tomamos la parametrizacion dada por el grafico $\varphi(u,v)=(u,v,f(u,v))$ tenemos que $\varphi_{u}(u,v)=\left( 1,v,\frac{2\log u}{u} \right)$ luego como estamos mirando la diferencial en el punto $(1,0,0)=\varphi(1,0)$ entonces $\varphi_{u}(1,0)=(1,0,0)\in T_{(1,0,0)}M$ 
>>	4. Pero $$\lVert dF_{(1,0,0)}.\varphi_{u}(1,0) \rVert=\left\lVert  -\frac{1}{2}  \right\rVert=\frac{1}{2}\neq1=\lVert \varphi_{u}(1,0) \rVert$$
>>	5. Como $dF$ no es isometria entonces $F$ no es isometria
>>
 
> [!Example] Ejercicio 3 (16 puntos)
> - **(a)** Sean $w$ y $z$ dos puntos de $\mathbb{R}^2$. ¿Qué transformación rígida del plano se obtiene si se compone la rotación en $180^\circ$ alrededor de $z$ con la rotación en $180^\circ$ alrededor de $w$? Justificar la respuesta.
> - **(b)** Mostrar que un campo paralelo a lo largo de una geodésica $\gamma$ forma un ángulo constante con $\gamma'$
>>[!Proof]-
>>- (a)
>>	1. Rotar 180 a un vector $x$ con respecto al $0$ seria hacer $-x$
>>	2. Ahora notamos que el vector que va desde $p$ hasta $x$ si lo trasladamos al origen seria $x-p$ 
>>	3. A ese lo queremos rotar 180 entonces $-(x-p)$ 
>>	4. Luego lo queremos trasladar para que su centro sea $p$ entonces $-(x-p)+p$  
>>	5. Por lo tanto $$R_{p}(x)=-(x-p)+p=2p-x$$
>>	6. Luego $$R_{w}(R_{p}(x))=R_{w}(2p-x)=2w-(2p-x)=2(w-p)+x$$ pero esto no es mas que una traslacion de $x$.
>>- (b) 
>>	1. Queremos ver que $\langle W,\gamma'\rangle=cte$
>>	2. Tomamos derivada $$\langle W,\gamma'\rangle'=\langle W',\gamma'\rangle+\langle W,\gamma''\rangle$$
>>	3. Pero ahora notamos como $W$ es campo paralelo entonces $W'\perp T_{p}S$ y obviamente $\gamma'\in T_{p}S$ luego $\langle W',\gamma'\rangle=0$ 
>>	4. Y $\gamma$ es geodesica entonces $\gamma''=\lambda n$ osea $\gamma\perp T_{p}S$ pero $W\in T_{p}S$ por definicion de campo paralelo. Por lo tanto $\langle W,\gamma''\rangle=0$ 
>>	5. Luego $\langle W,\gamma'\rangle'=0$ mostrando que $\langle W,\gamma'\rangle=cte$  

## Parte teórica

> [!Example] Ejercicio 4 (10 puntos)
> Sea $\alpha: [a, b] \to \mathbb{R}^3$ una curva regular (no necesariamente de rapidez unitaria). Definir la función curvatura $\kappa_\alpha : [a, b] \to \mathbb{R}$ y probar que
> $$\kappa_\alpha = \frac{\|\alpha' \times \alpha''\|}{\|\alpha'\|^3}.$$
>>[!Proof]-
>>1. Reparametrizamos y llegamos a $\beta(\sigma(t))=\alpha(t)$ 
>>2. Luego $\alpha '=\beta'(\sigma)\sigma'$ y $\alpha ''=\beta''(\sigma)\sigma'^{2}+\beta'(\sigma)\sigma''$ 
>>3. Ahora tenemos $$\alpha'\times\alpha''=\sigma'^{3}(\beta'\times\beta'')$$
>>4. Como $\lVert \beta' \rVert=1$ entonces $\langle \beta',\beta''\rangle=0$ entonces el angulo entre ellos es 90. Entonces recordando que $\sigma'=\lVert \alpha ' \rVert$ tenemos $$\lVert \alpha '\times\alpha '' \rVert=\lVert \alpha'  \rVert^{3}\lVert \beta'\times\beta'' \rVert=\lVert \alpha ' \rVert ^{3} \lVert \beta '' \rVert \lVert \beta ' \rVert \sin(90)=\lVert \alpha ' \rVert ^{3}\kappa_{\beta } $$
>>5. Finalmente (por definicion $\kappa_{\alpha }(t)=\kappa_{\beta}(\sigma(t))$) $$\kappa_{\alpha }(t)=\kappa_{\beta}(\sigma(t))=\frac{\lVert \alpha '\times\alpha '' \rVert}{\lVert \alpha ' \rVert^{3}}$$ 

> [!Example] Ejercicio 5 (10 puntos)
> Probar que si una función suave $f : M \to N$ entre dos superficies regulares es una isometría local, entonces $df_p : T_pM \to T_{f(p)}N$ es una isometría lineal para todo $p \in M$. Mostrar que, en particular, las isometrías locales son difeomorfismos locales.
>>[!Proof]-
>>6. Si $f$ es isometría local, existe vecindario de $p$ con $I_M = f^* I_N$.
>>7. Para $v,w\in T_pM$, se cumple $\langle v,w\rangle_M = \langle df_p(v), df_p(w)\rangle_N$; por tanto, $df_p$ preserva el producto interno y es isometría lineal.
>>8. En particular, $df_p$ es inyectivo; por el teorema de la función inversa, $f$ es difeomorfismo local.

> [!Example] Ejercicio 6 (10 puntos)
> Sea $M$ una superficie regular conexa $M$ tal que todos sus puntos son umbílicos. Dar por sabido que la función curvatura principal $k$ es constante y positiva en cada abierto coordenado conexo de $M$. Mostrar que cada abierto coordenado conexo está contenido en una esfera.
>>[!Proof]-
>>9. En cada abierto coordenado conexo $U$, $II = k\,I$ con $k>0$ constante, luego el operador de forma $S$ satisface $S=k\,\mathrm{Id}$.
>>10. Por Weingarten, $dn = -S = -k\,\mathrm{Id}$ en direcciones tangentes.
>>11. Defina $\Phi(p)=p+\tfrac{1}{k}n(p)$; para todo vector tangente $X$, $d\Phi(X)=X+\tfrac{1}{k}dn(X)=X-\tfrac{1}{k}kX=0$, así $\Phi$ es constante en $U$.
>>12. Sea $\Phi(p)=c$ constante; entonces $\|p-c\|=\|\tfrac{1}{k}n(p)\|=\tfrac{1}{k}$ y $U$ está contenido en la esfera de centro $c$ y radio $1/k$.

> [!Example] Ejercicio 7 (10 puntos)
> Enunciar con precisión el Teorema de Clairaut.
>>[!Proof]-
>>13. Sea $S$ una superficie de revolución con métrica $g=ds^2 + r(s)^2 d\theta^2$.
>>14. Para cualquier geodésica $\gamma$, el momento angular $r(s)^2\,\theta'(s)$ es constante.
>>15. Equivalentemente, el producto $r(s)\sin\varphi(s)$ es constante, donde $\varphi$ es el ángulo entre $\gamma'$ y la dirección meridiana.


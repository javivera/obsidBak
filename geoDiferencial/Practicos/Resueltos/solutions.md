# Soluciones — Geometría Diferencial — Práctico 2

A continuación se dan soluciones compactas y claras de los ejercicios 1–13.

---

## Ejercicio 1

Curva: $\alpha(t)=\dfrac{e^{t}}{\sqrt{3}}(\cos t,\,\sin t,\,1)$. 

1) Reparametrización por longitud de arco.

Calculemos la velocidad:

$\displaystyle \alpha'(t)=\frac{e^{t}}{\sqrt{3}}(\cos t-\sin t,\;\sin t+\cos t,\;1)$.

Su norma:

$\|\alpha'(t)\|=\frac{e^{t}}{\sqrt{3}}\sqrt{(\cos t-\sin t)^2+(\sin t+\cos t)^2+1}=\frac{e^{t}}{\sqrt{3}}\sqrt{2+1}=e^{t}.$

Por tanto la longitud desde $0$ a $t$ es

$\displaystyle s(t)=\int_{0}^{t} e^{u}\,du=e^{t}-1$ (tomamos $s(0)=0$). Invirtiendo, $t=\ln(s+1)$.

La reparametrización por longitud de arco es

$\displaystyle \beta(s)=\alpha(\ln(s+1))=\frac{s+1}{\sqrt{3}}\big(\cos(\ln(s+1)),\,\sin(\ln(s+1)),\,1\big).$

2) Tiedro de Frenet, curvatura y torsión.

Es conveniente trabajar con el parámetro $t$ y luego pasar a $s$. El vector tangente unitario es

$\displaystyle T(t)=\frac{\alpha'(t)}{\|\alpha'(t)\|}=\frac{1}{\sqrt{3}}(\cos t-\sin t,\;\sin t+\cos t,\;1).$

Derivando

$\displaystyle T'(t)=\frac{1}{\sqrt{3}}\big(-(\sin t+\cos t),\;\cos t-\sin t,\;0\big)$,

por lo que

$\|T'(t)\|=\sqrt{\tfrac{2}{3}}$.

Como $\dfrac{d}{ds}=\dfrac{1}{\|\alpha'(t)\|}\dfrac{d}{dt}=e^{-t}\dfrac{d}{dt}$, la curvatura es

$\displaystyle \kappa(t)=\Big\|\frac{dT}{ds}\Big\|=\frac{1}{e^{t}}\|T'(t)\|=\frac{\sqrt{2}}{\sqrt{3}\,e^{t}}.$

En la parametrización por arco $s$ (recuerde $e^{t}=s+1$) se tiene

$\displaystyle \kappa(s)=\frac{\sqrt{2}}{\sqrt{3}\,(s+1)}.$

Para la normal y la binormal (unidad) obtenemos

$\displaystyle N(t)=\frac{T'(t)}{\|T'(t)\|}=\frac{1}{\sqrt{2}}\big(-(\sin t+\cos t),\;\cos t-\sin t,\;0\big),$

$\displaystyle B(t)=T(t)\times N(t)=\frac{1}{\sqrt{6}}\big(\sin t-\cos t,\;-(\sin t+\cos t),\;2\big).$

Para la torsión usamos la fórmula general (o el triple producto). Calculando explícitamente se obtiene

$\displaystyle \tau(t)=\frac{1}{\sqrt{3}}e^{-t},$

y por tanto en función de $s$:

$\displaystyle \tau(s)=\frac{1}{\sqrt{3}(s+1)}.$

Observación: $\tau/\kappa=1/\sqrt{2}$ es constante.

---

## Ejercicio 2

Pregunta: si una curva parametrizada por longitud de arco se recorre en sentido opuesto, ¿cambian la curvatura y la torsión?

Sea $\alpha(s)$ unit-speed y sea $\beta(s)=\alpha(-s)$. Entonces

$\beta'(s)=-\alpha'(-s)=-T(-s)$, y por tanto $T_{\beta}(s)=-T_{\alpha}(-s)$. La curvatura se define como $\kappa=\|dT/ds\|$, por lo que

$\kappa_{\beta}(s)=\Big\|\frac{d}{ds}T_{\beta}(s)\Big\|=\Big\|\frac{d}{ds}(-T_{\alpha}(-s))\Big\|=\|T'_{\alpha}(-s)\|=\kappa_{\alpha}(-s)$.

En particular, en el mismo punto geométrico la curvatura no cambia (valor absoluto).

En cambio la torsión, que involucra la orientación del triedro, cambia de signo: si $B_{\beta}(s)=-B_{\alpha}(-s)$ entonces

$\tau_{\beta}(s)=-\tau_{\alpha}(-s)$. Conclusión: curvatura invariante, torsión cambia de signo.

---

## Ejercicio 3

Curva: $\alpha(s)=(a\cos(s/c),\;a\sin(s/c),\;b s/c)$ con $c^{2}=a^{2}+b^{2}$ y $s$ ya es la longitud de arco.

(a) Rapidez unitaria: derivando

$\alpha'(s)=\Big(-\frac{a}{c}\sin\frac{s}{c},\;\frac{a}{c}\cos\frac{s}{c},\;\frac{b}{c}\Big)$,

por tanto

$\|\alpha'(s)\|^{2}=\frac{a^{2}}{c^{2}}(\sin^{2}+\cos^{2})+\frac{b^{2}}{c^{2}}=\frac{a^{2}+b^{2}}{c^{2}}=1$.

(b) Triedro de Frenet, curvatura y torsión.

Como la curva es unit-speed, $T=\alpha'$. La segunda derivada es

$\alpha''(s)=\Big(-\frac{a}{c^{2}}\cos\frac{s}{c},\; -\frac{a}{c^{2}}\sin\frac{s}{c},\;0\Big)$,

por tanto la curvatura es

$\displaystyle \kappa=\|\alpha''(s)\|=\frac{a}{c^{2}}.$

La torsión clásica de la hélice vale

$\displaystyle \tau=\frac{b}{c^{2}}.$

Normal y binormal se pueden escribir explícitamente:

$\displaystyle N(s)=\frac{\alpha''(s)}{\kappa}=\big(-\cos\tfrac{s}{c},\; -\sin\tfrac{s}{c},\;0\big),$

$\displaystyle B(s)=T(s)\times N(s)=\Big(\frac{b}{c}\sin\tfrac{s}{c},\; -\frac{b}{c}\cos\tfrac{s}{c},\;\frac{a}{c}\Big).$

(c) Plano osculador en $s=\pi$.

El plano osculador en $s_{0}$ es el plano afín generado por $T(s_{0})$ y $N(s_{0})$; su vector normal es $B(s_{0})$. Por tanto la ecuación del plano osculador en $s=\pi$ es

$\displaystyle (x-\alpha(\pi))\cdot B(\pi)=0,$

es decir el conjunto de $x\in\mathbb{R}^{3}$ que satisfacen esa igualdad. El plano osculador afín es exactamente ese plano.

---

## Ejercicio 4

Consideremos la hélice canónica (en el parámetro "ángulo") $\gamma(t)=(a\cos t,\;a\sin t,\;b t)$. Para la familia de hélices los parámetros relevantes son el radio en el plano $xy$ (a) y el paso sobre el eje $z$ (b). Si $c^{2}=a^{2}+b^{2}$ entonces, en la parametrización por arco, $\kappa=a/c^{2}$ y $\tau=b/c^{2}$.

(a) Si comprimimos o dilatamos en la dirección del eje $z$ por un factor $\lambda$ (esto cambia $b\mapsto \lambda b$), las nuevas curvatura y torsión son

$\displaystyle \kappa_{\lambda}=\frac{a}{a^{2}+\lambda^{2}b^{2}},\qquad \tau_{\lambda}=\frac{\lambda b}{a^{2}+\lambda^{2}b^{2}}.$

Si la dilatación se hace en la dirección ortogonal al eje $z$ (factor $\mu$ en $(x,y)$), entonces $a\mapsto \mu a$ y

$\displaystyle \kappa_{\mu}=\frac{\mu a}{\mu^{2}a^{2}+b^{2}},\qquad \tau_{\mu}=\frac{b}{\mu^{2}a^{2}+b^{2}}.$

Conclución: la curvatura y la torsión cambian según los factores de escala; en particular la relación $\tau/\kappa=b/a$ cambia si se escala selectivamente.

(b) Reflejar respecto del plano $xz$ equivale a la isometría $(x,y,z)\mapsto (x,-y,z)$, que tiene determinante $-1$ (es una reflexión, altera la orientación). Bajo una isometría impropia la curvatura (como magnitud) se conserva, pero la torsión cambia de signo. Por tanto la torsión de la hélice reflejada es $-\tau$.

---

## Ejercicio 5

Sea $\alpha:(a,b)\to\mathbb{R}^{3}$ regular y supóngase que existe $t_{0}$ tal que $\|\alpha(t)\|$ alcanza un máximo en $t_{0}$. Denotemos $r=\|\alpha(t_{0})\|$.

Reparametricemos por longitud de arco cerca de $t_{0}$ y trabajemos con $\alpha(s)$ unit-speed y con $s_{0}$ correspondiente a $t_{0}$. Defina $f(s)=\|\alpha(s)\|^{2}$. En $s_{0}$ se tiene

$f'(s_{0})=2\langle\alpha(s_{0}),\alpha'(s_{0})\rangle=0$ y

$f''(s_{0})=2\big(\|\alpha'(s_{0})\|^{2}+\langle\alpha(s_{0}),\alpha''(s_{0})\rangle\big)=2\big(1+\kappa(s_{0})\langle\alpha(s_{0}),N(s_{0})\rangle\big)\le 0.$

De aquí se obtiene

$1+\kappa(s_{0})\langle\alpha(s_{0}),N(s_{0})\rangle\le 0\ \Longrightarrow\ \kappa(s_{0})(-\langle\alpha(s_{0}),N(s_{0})\rangle)\ge 1.$

Como $-\langle\alpha(s_{0}),N(s_{0})\rangle\le\|\alpha(s_{0})\|=r$ (por desigualdad de Cauchy), se sigue

$\kappa(s_{0})\ge\dfrac{1}{r}=\dfrac{1}{\|\alpha(t_{0})\|}.$

Esto demuestra la desigualdad solicitada.

---

## Ejercicio 6

Sea $\alpha$ unit-speed con curvatura $\kappa>0$ y torsión $\tau$.

(a) Si $\dfrac{\tau}{\kappa}$ es constante (digamos $\lambda$), entonces consideremos el vector

$\displaystyle v(t)=\frac{\tau(t)}{\kappa(t)}T(t)+B(t).$

Derivando y usando las ecuaciones de Frenet $T'=\kappa N$, $N'=-\kappa T+\tau B$, $B'=-\tau N$, obtenemos

$\displaystyle v'(t)=\Big(\frac{\tau}{\kappa}\Big)'T(t)+\frac{\tau}{\kappa}\kappa N(t)-\tau N(t)=\Big(\frac{\tau}{\kappa}\Big)'T(t).$

Si $\tau/\kappa$ es constante, $v'(t)=0$ y $v$ es un vector fijo en el espacio. Entonces $\langle T(t),v\rangle$ es constante, lo que significa que el ángulo entre la tangente y un vector fijo es constante: por definición, $\alpha$ es una hélice.

(b) Supongamos que existe un plano que contiene a $N(t)$ para todo $t$. Sea $u$ un vector normal a dicho plano. Entonces $\langle N(t),u\rangle=0$ para todo $t$. Diferenciando $\langle T(t),u\rangle'$ obtenemos

$\frac{d}{dt}\langle T,u\rangle=\langle T',u\rangle=\kappa\langle N,u\rangle=0,$

por tanto $\langle T,u\rangle$ es constante y la curva es una hélice. Recíprocamente, si $\alpha$ es una hélice existe $u$ tal que $\langle T,u\rangle$ es constante; diferenciando se obtiene $\kappa\langle N,u\rangle=0$, por lo que $\langle N,u\rangle=0$ para todo $t$, esto es, $N(t)$ está contenido en el plano ortogonal a $u$. Así se tiene la caracterización buscada.

---

## Ejercicio 7

$\alpha(t)=(t,\cosh t)$. Calculamos la curvatura de dos maneras.

(a) Reparametrización por longitud de arco: la velocidad es

$\|\alpha'(t)\|=\sqrt{1+\sinh^{2}t}=\cosh t$. La longitud desde $0$ a $t$ es

$\displaystyle s(t)=\int_{0}^{t}\cosh u\,du=\sinh t.$

Invirtiendo, $t=\operatorname{arsinh}(s)$, y la curvatura en función de $s$ será

$\kappa(s)=\frac{1}{\cosh^{2}t}=\frac{1}{1+\sinh^{2}t}=\frac{1}{1+s^{2}}.$

(b) Fórmula para curva no unit-speed en $\mathbb{R}^{2}$:

$\displaystyle \kappa(t)=\frac{|x'(t)y''(t)-x''(t)y'(t)|}{(x'(t)^{2}+y'(t)^{2})^{3/2}}.$

Aquí $x(t)=t$, $y(t)=\cosh t$, por lo que $x'=1$, $x''=0$, $y'=\sinh t$, $y''=\cosh t$. Entonces

$\kappa(t)=\dfrac{|1\cdot\cosh t-0\cdot\sinh t|}{(1+\sinh^{2}t)^{3/2}}=\dfrac{\cosh t}{\cosh^{3}t}=\dfrac{1}{\cosh^{2}t},$

coincidiendo con (a).

---

## Ejercicio 8

Sea $\alpha$ de rapidez unitaria en $\mathbb{R}^{2}$. Denotemos por $\kappa$ la curvatura geométrica (positiva) y por $k$ la curvatura signada. Para unit-speed se tiene $\alpha''(t)=\kappa(t)N(t)$ y la curvatura signada se define por

$k(t)=\langle \alpha''(t),J\,\alpha'(t)\rangle$ (o equivalentemente por el determinante $(x'y''-x''y')$). En el plano, $J\alpha'(t)=\pm N(t)$ según la orientación; en cualquier caso, $|k(t)|=\|\alpha''(t)\|=\kappa(t)$. Luego $\kappa=|k|$.

---

## Ejercicio 9

Sea $\alpha:I\to\mathbb{R}^{2}$ unit-speed con curvatura signada $k$ nunca nula. Una circunferencia de centro $p$ y radio $r$ es osculatriz en $0$ si la función $f(s)=\|\alpha(s)-p\|^{2}$ cumple $f(0)=r^{2}$ y $f'(0)=f''(0)=0$.

Calculemos condiciones sobre $p$.

$f'(s)=2\langle\alpha'(s),\alpha(s)-p\rangle$, luego $f'(0)=0$ implica $\langle T(0),\alpha(0)-p\rangle=0$, es decir, $\alpha(0)-p$ es ortogonal a $T(0)$, por tanto

$\alpha(0)-p=\lambda N(0)$ para algún escalar $\lambda$.

Ahora

$f''(s)=2(\|\alpha'(s)\|^{2}+\langle\alpha''(s),\alpha(s)-p\rangle)=2(1+\kappa(s)\langle N(s),\alpha(s)-p\rangle).$

En $s=0$ se requiere $f''(0)=0$, por tanto

$1+\kappa(0)\langle N(0),\lambda N(0)\rangle=1+\kappa(0)\lambda=0$, de donde $\lambda=-1/\kappa(0)$.

Así el centro debe ser

$\displaystyle p=\alpha(0)-\frac{1}{\kappa(0)}N(0).$

Si en lugar de usar la normal unitaria se usa la convención de curvatura signada $k(0)$ y la rotación $I$ de $90^{\circ}$ aplicada a $\alpha'(0)$, se obtiene la fórmula equivalente

$\displaystyle p=\alpha(0)+\frac{1}{k(0)}I(\alpha'(0)),$

y el radio es $r=1/|k(0)|$. La condición $f(0)=r^{2}$ se verifica automáticamente y la unicidad viene de que las ecuaciones lineales anteriores determinan $\lambda$ de forma única.

---

## Ejercicio 10

(a) Sea $\alpha(t)=(x(t),y(t))$ regular. La curvatura signada viene dada por

$\displaystyle k(t)=\frac{x'(t)y''(t)-x''(t)y'(t)}{(x'(t)^{2}+y'(t)^{2})^{3/2}}.$

Esta fórmula se obtiene aplicando la definición en coordenadas y usando la expresión del determinante que da el área orientada del paralelogramo formado por $\alpha'$ y $\alpha''$.

(b) Para la elipse $\alpha(t)=(a\cos t,\,b\sin t)$ con $a,b>0$ la curvatura (no signada, o signada según orientación) es

$\displaystyle k(t)=\frac{ab}{\big(a^{2}\sin^{2}t+b^{2}\cos^{2}t\big)^{3/2}}.$

Derivando y simplificando se obtiene

$\displaystyle k'(t)\propto (a^{2}-b^{2})\sin 2t,$

luego $k'(t)=0$ cuando $\sin 2t=0$, es decir en $t=0,\,\frac{\pi}{2},\,\pi,\,\frac{3\pi}{2}$ (al menos cuatro puntos críticos en $[0,2\pi)$). Esto ilustra el Teorema de los Cuatro Vértices para la elipse.

---

## Ejercicio 11

Sea $\alpha(t)=(\alpha_{1}(t),\alpha_{2}(t),0)$ una curva regular en el plano $z=0$ y sea $T:\mathbb{R}^{3}\to\mathbb{R}^{3}$ una transformación lineal inyectiva.

(a) Regularidad: como $\alpha'$ no es 0 en todo $t$ y $T$ es inyectiva (lineal), $T(\alpha'(t))\neq 0$ para todo $t$, por lo que $\tilde{\alpha}=T\circ\alpha$ es regular.

(b) Torsiones: la curva original está contenida en el plano $z=0$, por tanto su torsión es $0$ en todos los puntos. Como $T$ es lineal e inyectiva (en $\mathbb{R}^{3}$ esto implica invertible), la imagen del subespacio plano $z=0$ será otro subespacio de dimensión $2$ (un plano). Luego $\tilde{\alpha}$ queda contenida en un plano y por tanto su torsión también es $0$.

---

## Ejercicio 12

Si $\alpha:[a,b]\to\mathbb{R}^{n}$ tiene longitud igual a $\|\alpha(b)-\alpha(a)\|$, entonces hay igualdad en la desigualdad triangular integral

$\displaystyle L(\alpha)=\int_{a}^{b}\|\alpha'(t)\|\,dt\ge\Big\|\int_{a}^{b}\alpha'(t)\,dt\Big\|=\|\alpha(b)-\alpha(a)\|.$

La igualdad en la desigualdad de Cauchy-Schwarz (o en la desigualdad integral) ocurre si y sólo si los vectores $\alpha'(t)$ son todos colineales y en la misma dirección para casi todo $t$. De esta propiedad se sigue que la imagen de $\alpha$ está contenida en un segmento rectilíneo y que la parametrización es monótona a lo largo del segmento. En consecuencia, $\alpha$ es una reparametrización creciente del segmento que une $\alpha(a)$ y $\alpha(b)$.

---

## Ejercicio 13

Probar: una curva regular está contenida en una recta si y sólo si existe un punto $p$ tal que cada recta tangente a la curva pasa por $p$.

($\Rightarrow$) Si la curva está contenida en una recta $L$, entonces cada recta tangente coincide con $L$, por lo que tomando cualquier punto $p\in L$ todas las rectas tangentes pasan por $p$.

($\Leftarrow$) Supongamos que existe $p$ tal que para todo $t$ la recta tangente en $\alpha(t)$ pasa por $p$. Entonces $\alpha(t)-p$ es colineal con $\alpha'(t)$, es decir existe una función escalar $\lambda(t)$ tal que

$\alpha(t)-p=\lambda(t)\alpha'(t)$.

Derivando,

$\alpha'(t)=\lambda'(t)\alpha'(t)+\lambda(t)\alpha''(t)$,

de donde $(\lambda'(t)-1)\alpha'(t)+\lambda(t)\alpha''(t)=0$. Como $\alpha'$ no es nulo, esto implica que $\alpha''(t)$ es colineal con $\alpha'(t)$ para todo $t$, es decir la curvatura es cero y la trayectoria es una recta.

Si se quita la hipótesis de regularidad, la implicación recíproca puede fallar (por ejemplo en una curva con cuspide o punto estacionario la recta tangente puede no estar bien definida en todos los puntos o pueden existir puntos singulares que rompan la argumentación anterior).

---

Si quieres, puedo:

- Ejecutar comprobaciones simbólicas o numéricas de alguna de las fórmulas (por ejemplo comprobar las expresiones de curvatura/torsión de la Ej.1),
- Añadir diagramas o trazados para algunas curvas (hélice, catenaria, etc.),
- Formatear el documento con más detalles o pasos intermedios para alguno de los ejercicios.

Dime si quieres que commiteé el archivo o que haga alguna modificación en el formato o en el nivel de detalle.
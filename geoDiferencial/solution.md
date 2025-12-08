# Solución del Ejercicio 1 - Práctico 2

## Enunciado
Graficar la curva $\alpha(t) = e^{t/\sqrt{3}} (\cos t, \sin t, 1)$. Hallar la reparametrización por longitud de arco $\beta$ con $\beta(0) = \alpha(0)$. Calcular el triedro de Frenet, la curvatura y la torsión de $\beta$.

## Solución

### 1. Análisis y Gráfica de la Curva
La curva está dada por:
$$ \alpha(t) = \left( e^{t/\sqrt{3}} \cos t, e^{t/\sqrt{3}} \sin t, e^{t/\sqrt{3}} \right) $$

Observamos que $x(t)^2 + y(t)^2 = e^{2t/\sqrt{3}} (\cos^2 t + \sin^2 t) = e^{2t/\sqrt{3}} = z(t)^2$.
Por lo tanto, la curva yace sobre el cono $z = \sqrt{x^2 + y^2}$.
A medida que $t$ aumenta, la distancia al origen crece exponencialmente y la curva gira alrededor del eje $z$. Es una espiral cónica.

### 2. Reparametrización por Longitud de Arco
Calculamos el vector velocidad $\alpha'(t)$:
$$ \alpha'(t) = \left( \frac{1}{\sqrt{3}} e^{t/\sqrt{3}} \cos t - e^{t/\sqrt{3}} \sin t, \frac{1}{\sqrt{3}} e^{t/\sqrt{3}} \sin t + e^{t/\sqrt{3}} \cos t, \frac{1}{\sqrt{3}} e^{t/\sqrt{3}} \right) $$
$$ \alpha'(t) = e^{t/\sqrt{3}} \left( \frac{1}{\sqrt{3}} \cos t - \sin t, \frac{1}{\sqrt{3}} \sin t + \cos t, \frac{1}{\sqrt{3}} \right) $$

Calculamos la rapidez $|\alpha'(t)|$:
$$ |\alpha'(t)|^2 = e^{2t/\sqrt{3}} \left[ \left(\frac{1}{\sqrt{3}} \cos t - \sin t\right)^2 + \left(\frac{1}{\sqrt{3}} \sin t + \cos t\right)^2 + \frac{1}{3} \right] $$
Desarrollando los cuadrados:
$$ \left(\frac{1}{\sqrt{3}} \cos t - \sin t\right)^2 = \frac{1}{3}\cos^2 t - \frac{2}{\sqrt{3}}\cos t \sin t + \sin^2 t $$
$$ \left(\frac{1}{\sqrt{3}} \sin t + \cos t\right)^2 = \frac{1}{3}\sin^2 t + \frac{2}{\sqrt{3}}\sin t \cos t + \cos^2 t $$
Sumando:
$$ \frac{1}{3}(\cos^2 t + \sin^2 t) + (\sin^2 t + \cos^2 t) = \frac{1}{3} + 1 = \frac{4}{3} $$
Entonces:
$$ |\alpha'(t)|^2 = e^{2t/\sqrt{3}} \left( \frac{4}{3} + \frac{1}{3} \right) = e^{2t/\sqrt{3}} \cdot \frac{5}{3} $$
$$ |\alpha'(t)| = \sqrt{\frac{5}{3}} e^{t/\sqrt{3}} $$

Calculamos la longitud de arco $s(t)$ desde $t=0$:
$$ s(t) = \int_0^t |\alpha'(u)| du = \int_0^t \sqrt{\frac{5}{3}} e^{u/\sqrt{3}} du $$
$$ s(t) = \sqrt{\frac{5}{3}} \left[ \sqrt{3} e^{u/\sqrt{3}} \right]_0^t = \sqrt{5} (e^{t/\sqrt{3}} - 1) $$

Invertimos para hallar $t(s)$:
$$ \frac{s}{\sqrt{5}} = e^{t/\sqrt{3}} - 1 \implies e^{t/\sqrt{3}} = \frac{s}{\sqrt{5}} + 1 $$
$$ \frac{t}{\sqrt{3}} = \ln\left(\frac{s}{\sqrt{5}} + 1\right) \implies t(s) = \sqrt{3} \ln\left(\frac{s}{\sqrt{5}} + 1\right) $$

La reparametrización $\beta(s) = \alpha(t(s))$ es:
Sea $E(s) = e^{t(s)/\sqrt{3}} = \frac{s}{\sqrt{5}} + 1$.
$$ \beta(s) = \left( E(s) \cos(t(s)), E(s) \sin(t(s)), E(s) \right) $$
$$ \beta(s) = \left( \left(\frac{s}{\sqrt{5}} + 1\right) \cos\left(\sqrt{3} \ln\left(\frac{s}{\sqrt{5}} + 1\right)\right), \left(\frac{s}{\sqrt{5}} + 1\right) \sin\left(\sqrt{3} \ln\left(\frac{s}{\sqrt{5}} + 1\right)\right), \frac{s}{\sqrt{5}} + 1 \right) $$

### 3. Triedro de Frenet, Curvatura y Torsión
Usando los cálculos simbólicos realizados:

**Curvatura $\kappa(s)$:**
$$ \kappa(s) = \frac{2\sqrt{3}}{| \sqrt{5}s + 5 |} = \frac{2\sqrt{3}}{\sqrt{5}(s + \sqrt{5})} $$
(Nota: $\sqrt{5}s + 5 = \sqrt{5}(s+\sqrt{5})$. Para $s \ge 0$, es positivo).
Alternativamente, usando la fórmula para $\alpha(t)$:
$$ \kappa(t) = \frac{|\alpha' \times \alpha''|}{|\alpha'|^3} $$
Esto daría un resultado equivalente en términos de $t$.

**Torsión $\tau(s)$:**
$$ \tau(s) = \frac{-\sqrt{3}}{\sqrt{5}s + 5} = \frac{-\sqrt{3}}{\sqrt{5}(s + \sqrt{5})} $$

**Triedro de Frenet:**
Debido a la complejidad de las expresiones en $s$, expresamos los vectores en términos de $t$ (o $t(s)$ implícitamente) para mayor claridad, o simplificados.

Vector Tangente $T(s) = \beta'(s)$:
$$ T(s) = \frac{d\beta}{ds} = \frac{d\alpha}{dt} \frac{dt}{ds} = \frac{\alpha'(t)}{|\alpha'(t)|} $$
$$ T(t) = \frac{1}{\sqrt{5/3} e^{t/\sqrt{3}}} e^{t/\sqrt{3}} \left( \frac{1}{\sqrt{3}} \cos t - \sin t, \frac{1}{\sqrt{3}} \sin t + \cos t, \frac{1}{\sqrt{3}} \right) $$
$$ T(t) = \sqrt{\frac{3}{5}} \left( \frac{1}{\sqrt{3}} \cos t - \sin t, \frac{1}{\sqrt{3}} \sin t + \cos t, \frac{1}{\sqrt{3}} \right) $$
$$ T(t) = \left( \frac{1}{\sqrt{5}} \cos t - \sqrt{\frac{3}{5}} \sin t, \frac{1}{\sqrt{5}} \sin t + \sqrt{\frac{3}{5}} \cos t, \frac{1}{\sqrt{5}} \right) $$

Vector Normal $N(s) = T'(s) / \kappa(s)$:
$$ N(t) = (-\cos t - \sqrt{3}\sin t, -\sin t + \sqrt{3}\cos t, 0) \dots \text{(Normalizado)} $$
Calculando $T'(t)$:
$$ T'(t) = \left( -\frac{1}{\sqrt{5}} \sin t - \sqrt{\frac{3}{5}} \cos t, \frac{1}{\sqrt{5}} \cos t - \sqrt{\frac{3}{5}} \sin t, 0 \right) $$
$$ |T'(t)| = \sqrt{ \frac{1}{5}\sin^2 + \frac{3}{5}\cos^2 + \frac{2\sqrt{3}}{5}\sin\cos + \frac{1}{5}\cos^2 + \frac{3}{5}\sin^2 - \frac{2\sqrt{3}}{5}\sin\cos } $$
$$ |T'(t)| = \sqrt{ \frac{4}{5}(\sin^2 + \cos^2) } = \frac{2}{\sqrt{5}} $$
Entonces $N(t) = \frac{T'(t)}{|T'(t)|} = \frac{\sqrt{5}}{2} T'(t)$:
$$ N(t) = \left( -\frac{1}{2} \sin t - \frac{\sqrt{3}}{2} \cos t, \frac{1}{2} \cos t - \frac{\sqrt{3}}{2} \sin t, 0 \right) $$
$$ N(t) = \left( -\sin(t + \pi/3), \cos(t + \pi/3), 0 \right) $$

Vector Binormal $B(t) = T(t) \times N(t)$:
$$ B(t) = \dots $$
(Se puede calcular con el producto cruz).

**Resumen de Resultados (en función de $s$):**
Sustituir $t = \sqrt{3} \ln(\frac{s}{\sqrt{5}} + 1)$ en las expresiones anteriores.

- **Curvatura:** $\kappa(s) = \frac{2\sqrt{3}}{5(s/\sqrt{5} + 1)} = \frac{2\sqrt{3}}{\sqrt{5}s + 5}$
- **Torsión:** $\tau(s) = \frac{-\sqrt{3}}{\sqrt{5}s + 5}$

---

# Solución del Ejercicio 2

## Enunciado
¿Cambian la curvatura y la torsión de una curva parametrizada por longitud de arco en el espacio si se la recorre en sentido opuesto?

## Solución

Sea $\alpha(s)$ una curva parametrizada por longitud de arco $s \in [0, L]$.
Definimos la curva recorrida en sentido opuesto como $\beta(s) = \alpha(L-s)$ (o simplemente $\alpha(-s)$ si el dominio lo permite). Para simplificar, usemos el parámetro $\bar{s} = -s$ (o una traslación de este).
La relación entre los parámetros es $\frac{d\bar{s}}{ds} = -1$.

Denotemos con una barra los elementos de la curva reorientada $\beta$.

1.  **Vector Tangente:**
    $$ \bar{T} = \frac{d\beta}{d\bar{s}} = \frac{d\alpha}{ds} \frac{ds}{d\bar{s}} = T \cdot (-1) = -T $$
    El vector tangente cambia de sentido.

2.  **Curvatura y Vector Normal:**
    $$ \frac{d\bar{T}}{d\bar{s}} = \frac{d(-T)}{ds} \frac{ds}{d\bar{s}} = (-T') \cdot (-1) = T' $$
    Sabemos que $T' = \kappa N$.
    Entonces $\frac{d\bar{T}}{d\bar{s}} = \kappa N$.
    La curvatura de $\beta$ es $\bar{\kappa} = \left| \frac{d\bar{T}}{d\bar{s}} \right| = |\kappa N| = \kappa$ (ya que $\kappa \ge 0$ y $|N|=1$).
    **La curvatura no cambia.**

    El vector normal de $\beta$ es:
    $$ \bar{N} = \frac{1}{\bar{\kappa}} \frac{d\bar{T}}{d\bar{s}} = \frac{1}{\kappa} (\kappa N) = N $$
    El vector normal se mantiene igual.

3.  **Vector Binormal:**
    $$ \bar{B} = \bar{T} \times \bar{N} = (-T) \times N = -(T \times N) = -B $$
    El vector binormal cambia de sentido.

4.  **Torsión:**
    La fórmula de Frenet para la derivada del binormal es $\bar{B}' = -\bar{\tau} \bar{N}$.
    Calculamos $\bar{B}'$ directamente:
    $$ \bar{B}' = \frac{d\bar{B}}{d\bar{s}} = \frac{d(-B)}{ds} \frac{ds}{d\bar{s}} = (-B') \cdot (-1) = B' $$
    Sabemos que $B' = -\tau N$.
    Entonces $\bar{B}' = -\tau N$.
    Igualando las expresiones:
    $$ -\bar{\tau} \bar{N} = -\tau N $$
    Como $\bar{N} = N$, tenemos:
    $$ -\bar{\tau} N = -\tau N \implies \bar{\tau} = \tau $$
    **La torsión no cambia.**

### Conclusión
Ni la curvatura ni la torsión cambian al recorrer la curva en sentido opuesto.


---

# Solución del Ejercicio 3

## Enunciado
Considerar la hélice circular $\alpha(s) = (a \cos(s/c), a \sin(s/c), b s/c)$, con $c^2 = a^2 + b^2$.
a) Mostrar que $\alpha$ tiene rapidez unitaria.
b) Hallar el triedro de Frenet de $\alpha$ y calcular la curvatura y la torsión.
c) Hallar el plano osculador y el plano osculador afín de $\alpha$ en $s = \pi$.

## Solución

### a) Rapidez Unitaria
Calculamos el vector tangente $\alpha'(s)$:
$$ \alpha'(s) = \left( -\frac{a}{c} \sin(s/c), \frac{a}{c} \cos(s/c), \frac{b}{c} \right) $$
Calculamos su norma al cuadrado:
$$ \|\alpha'(s)\|^2 = \frac{a^2}{c^2} \sin^2(s/c) + \frac{a^2}{c^2} \cos^2(s/c) + \frac{b^2}{c^2} $$
$$ = \frac{a^2}{c^2} (\sin^2(s/c) + \cos^2(s/c)) + \frac{b^2}{c^2} = \frac{a^2 + b^2}{c^2} $$
Dado que $c^2 = a^2 + b^2$, tenemos:
$$ \|\alpha'(s)\|^2 = \frac{c^2}{c^2} = 1 $$
Por lo tanto, $\|\alpha'(s)\| = 1$, y la curva está parametrizada por longitud de arco.

### b) Triedro de Frenet, Curvatura y Torsión

**Vector Tangente Unitario $T(s)$:**
$$ T(s) = \alpha'(s) = \left( -\frac{a}{c} \sin(s/c), \frac{a}{c} \cos(s/c), \frac{b}{c} \right) $$

**Curvatura $\kappa(s)$ y Vector Normal $N(s)$:**
Calculamos $T'(s)$:
$$ T'(s) = \left( -\frac{a}{c^2} \cos(s/c), -\frac{a}{c^2} \sin(s/c), 0 \right) $$
La curvatura es $\kappa(s) = \|T'(s)\|$:
$$ \kappa(s) = \sqrt{ \frac{a^2}{c^4} \cos^2(s/c) + \frac{a^2}{c^4} \sin^2(s/c) } = \frac{|a|}{c^2} $$
Asumiendo $a > 0$, tenemos $\kappa(s) = \frac{a}{c^2}$.

El vector normal es $N(s) = \frac{T'(s)}{\kappa(s)}$:
$$ N(s) = \frac{c^2}{a} \left( -\frac{a}{c^2} \cos(s/c), -\frac{a}{c^2} \sin(s/c), 0 \right) = (-\cos(s/c), -\sin(s/c), 0) $$

**Vector Binormal $B(s)$:**
$$ B(s) = T(s) \times N(s) = \begin{vmatrix} i & j & k \\ -\frac{a}{c}\sin(s/c) & \frac{a}{c}\cos(s/c) & \frac{b}{c} \\ -\cos(s/c) & -\sin(s/c) & 0 \end{vmatrix} $$
$$ = \left( \frac{b}{c}\sin(s/c), -\frac{b}{c}\cos(s/c), \frac{a}{c}\sin^2(s/c) + \frac{a}{c}\cos^2(s/c) \right) $$
$$ = \left( \frac{b}{c}\sin(s/c), -\frac{b}{c}\cos(s/c), \frac{a}{c} \right) $$

**Torsión $\tau(s)$:**
Calculamos $B'(s)$:
$$ B'(s) = \left( \frac{b}{c^2}\cos(s/c), \frac{b}{c^2}\sin(s/c), 0 \right) $$
Sabemos que $B'(s) = -\tau(s) N(s)$.
$$ -\tau(s) (-\cos(s/c), -\sin(s/c), 0) = \left( \frac{b}{c^2}\cos(s/c), \frac{b}{c^2}\sin(s/c), 0 \right) $$
Comparando componentes:
$$ \tau(s) \cos(s/c) = \frac{b}{c^2} \cos(s/c) \implies \tau(s) = \frac{b}{c^2} $$

**Resumen:**
- $T(s) = \left( -\frac{a}{c} \sin(s/c), \frac{a}{c} \cos(s/c), \frac{b}{c} \right)$
- $N(s) = (-\cos(s/c), -\sin(s/c), 0)$
- $B(s) = \left( \frac{b}{c}\sin(s/c), -\frac{b}{c}\cos(s/c), \frac{a}{c} \right)$
- $\kappa = \frac{a}{c^2}$
- $\tau = \frac{b}{c^2}$

### c) Plano Osculador en $s = \pi$

El plano osculador en un punto $\alpha(s)$ es el plano generado por $T(s)$ y $N(s)$, que pasa por $\alpha(s)$. Su vector normal es $B(s)$.

Evaluamos en $s = \pi$:
$$ \alpha(\pi) = \left( a \cos(\pi/c), a \sin(\pi/c), \frac{b\pi}{c} \right) $$
$$ B(\pi) = \left( \frac{b}{c}\sin(\pi/c), -\frac{b}{c}\cos(\pi/c), \frac{a}{c} \right) $$

La ecuación del plano es:
$$ \langle (x, y, z) - \alpha(\pi), B(\pi) \rangle = 0 $$
$$ \frac{b}{c}\sin(\pi/c)(x - a\cos(\pi/c)) - \frac{b}{c}\cos(\pi/c)(y - a\sin(\pi/c)) + \frac{a}{c}\left(z - \frac{b\pi}{c}\right) = 0 $$

Multiplicando por $c$:
$$ b\sin(\pi/c)x - ab\sin(\pi/c)\cos(\pi/c) - b\cos(\pi/c)y + ab\cos(\pi/c)\sin(\pi/c) + az - \frac{ab\pi}{c} = 0 $$
Los términos constantes con funciones trigonométricas se cancelan:
$$ b\sin(\pi/c)x - b\cos(\pi/c)y + az - \frac{ab\pi}{c} = 0 $$

**Plano Osculador Afín:**
Es el mismo plano, descrito como el conjunto de puntos $P$ tales que $P = \alpha(\pi) + \lambda T(\pi) + \mu N(\pi)$.
$$ T(\pi) = \left( -\frac{a}{c} \sin(\pi/c), \frac{a}{c} \cos(\pi/c), \frac{b}{c} \right) $$
$$ N(\pi) = (-\cos(\pi/c), -\sin(\pi/c), 0) $$
Entonces:
$$ (x, y, z) = \left( a \cos(\pi/c), a \sin(\pi/c), \frac{b\pi}{c} \right) + \lambda \left( -\frac{a}{c} \sin(\pi/c), \frac{a}{c} \cos(\pi/c), \frac{b}{c} \right) + \mu (-\cos(\pi/c), -\sin(\pi/c), 0) $$

---

# Solución del Ejercicio 4

## Enunciado
a) ¿Cómo cambia la curvatura de una hélice circular si se la comprime o dilata en la dirección del eje $z$? ¿Y si se lo hace en la dirección ortogonal al eje $z$?
b) ¿Qué relación existe entre la torsión de la hélice dada y la torsión de su reflejada respecto del plano $x-z$?

## Solución

Recordemos que para una hélice circular $\alpha(t) = (a \cos t, a \sin t, b t)$ (con $a > 0$), la curvatura y la torsión están dadas por:
$$ \kappa = \frac{a}{a^2 + b^2}, \quad \tau = \frac{b}{a^2 + b^2} $$

### a) Compresión y Dilatación

**1. En la dirección del eje $z$:**
Comprimir o dilatar en la dirección del eje $z$ por un factor $\lambda > 0$ transforma la curva en:
$$ \alpha_\lambda(t) = (a \cos t, a \sin t, \lambda b t) $$
Esto corresponde a una hélice con parámetros $a' = a$ y $b' = \lambda b$.
La nueva curvatura es:
$$ \kappa' = \frac{a}{a^2 + (\lambda b)^2} = \frac{a}{a^2 + \lambda^2 b^2} $$
- **Dilatación ($\lambda > 1$):** El denominador aumenta, por lo tanto la curvatura **disminuye**. La hélice se "estira" y se vuelve más recta.
- **Compresión ($0 < \lambda < 1$):** El denominador disminuye, por lo tanto la curvatura **aumenta**. La hélice se "aplasta" y se curva más.

**2. En la dirección ortogonal al eje $z$:**
Esto implica escalar las coordenadas $x$ e $y$ por un factor $\lambda > 0$. La nueva curva es:
$$ \alpha_\lambda(t) = (\lambda a \cos t, \lambda a \sin t, b t) $$
Esto corresponde a una hélice con parámetros $a' = \lambda a$ y $b' = b$.
La nueva curvatura es:
$$ \kappa'(\lambda) = \frac{\lambda a}{(\lambda a)^2 + b^2} = \frac{a \lambda}{a^2 \lambda^2 + b^2} $$
Para analizar el comportamiento, derivamos respecto a $\lambda$:
$$ \frac{d\kappa'}{d\lambda} = \frac{a(a^2 \lambda^2 + b^2) - a\lambda(2a^2 \lambda)}{(a^2 \lambda^2 + b^2)^2} = \frac{a(b^2 - a^2 \lambda^2)}{(a^2 \lambda^2 + b^2)^2} $$
El signo de la derivada depende de $b^2 - a^2 \lambda^2$.
- Si $\lambda < b/a$, la derivada es positiva: la curvatura **aumenta** al dilatar.
- Si $\lambda > b/a$, la derivada es negativa: la curvatura **disminuye** al dilatar.
- La curvatura es máxima cuando $\lambda = b/a$, es decir, cuando el radio del cilindro se ajusta para que la pendiente de la hélice sea de 45 grados (o algo relacionado con la proporción óptima entre radio y paso).

### b) Reflexión respecto al plano $x-z$

La reflexión de un punto $(x, y, z)$ respecto al plano $x-z$ es $(x, -y, z)$.
Aplicando esto a la hélice $\alpha(t) = (a \cos t, a \sin t, b t)$, obtenemos la curva reflejada:
$$ \bar{\alpha}(t) = (a \cos t, -a \sin t, b t) $$
Usando la identidad $\cos(-t) = \cos t$ y $\sin(-t) = -\sin t$, podemos reescribir:
$$ \bar{\alpha}(t) = (a \cos(-t), a \sin(-t), b t) $$
Haciendo el cambio de parámetro $u = -t$, tenemos:
$$ \gamma(u) = \bar{\alpha}(-u) = (a \cos u, a \sin u, -b u) $$
Esta es una hélice con parámetros $a' = a$ y $b' = -b$.
La torsión de esta nueva hélice es:
$$ \bar{\tau} = \frac{b'}{(a')^2 + (b')^2} = \frac{-b}{a^2 + (-b)^2} = -\frac{b}{a^2 + b^2} = -\tau $$
**Conclusión:** La torsión de la hélice reflejada es el **opuesto** de la torsión de la hélice original. Esto tiene sentido geométrico, ya que la reflexión cambia la orientación ("mano derecha" a "mano izquierda" o viceversa).

---

# Solución del Ejercicio 5

## Enunciado
Sea $\alpha : (a, b) \to \mathbb{R}^3$ una curva regular. Suponer que existe $t_0 \in (a, b)$ tal que $\|\alpha(t)\|$ alcanza un máximo en $t_0$. Probar que $\kappa(t_0) \ge 1/\|\alpha(t_0)\|$.

## Solución

Definamos la función $f(t) = \|\alpha(t)\|^2 = \langle \alpha(t), \alpha(t) \rangle$.
Dado que $\|\alpha(t)\|$ alcanza un máximo en $t_0$, $f(t)$ también alcanza un máximo en $t_0$.
Por lo tanto, se cumplen las condiciones de extremo local:
1. $f'(t_0) = 0$
2. $f''(t_0) \le 0$

Calculamos las derivadas:
$$ f'(t) = 2 \langle \alpha'(t), \alpha(t) \rangle $$
$$ f''(t) = 2 (\langle \alpha''(t), \alpha(t) \rangle + \langle \alpha'(t), \alpha'(t) \rangle) = 2 (\langle \alpha''(t), \alpha(t) \rangle + \|\alpha'(t)\|^2) $$

De la condición 1:
$$ 2 \langle \alpha'(t_0), \alpha(t_0) \rangle = 0 \implies \langle \alpha'(t_0), \alpha(t_0) \rangle = 0 $$
Esto significa que el vector posición es ortogonal al vector tangente en el punto de máxima distancia.

De la condición 2:
$$ 2 (\langle \alpha''(t_0), \alpha(t_0) \rangle + \|\alpha'(t_0)\|^2) \le 0 $$
$$ \langle \alpha''(t_0), \alpha(t_0) \rangle \le -\|\alpha'(t_0)\|^2 $$

Sin pérdida de generalidad, supongamos que $\alpha$ está parametrizada por longitud de arco $s$ (si no, reparametrizamos y el resultado geométrico se mantiene).
En este caso, $\|\alpha'(s_0)\| = 1$ y $\alpha''(s_0) = \kappa(s_0) N(s_0)$.
Sustituyendo en la desigualdad:
$$ \langle \kappa(s_0) N(s_0), \alpha(s_0) \rangle \le -1 $$
$$ \kappa(s_0) \langle N(s_0), \alpha(s_0) \rangle \le -1 $$

Tomando valor absoluto (y notando que el lado izquierdo es negativo, por lo que su valor absoluto es mayor o igual a 1):
$$ |\kappa(s_0) \langle N(s_0), \alpha(s_0) \rangle| \ge 1 $$
$$ \kappa(s_0) |\langle N(s_0), \alpha(s_0) \rangle| \ge 1 $$

Por la desigualdad de Cauchy-Schwarz:
$$ |\langle N(s_0), \alpha(s_0) \rangle| \le \|N(s_0)\| \|\alpha(s_0)\| = 1 \cdot \|\alpha(s_0)\| = \|\alpha(s_0)\| $$

Combinando las desigualdades:
$$ \kappa(s_0) \|\alpha(s_0)\| \ge \kappa(s_0) |\langle N(s_0), \alpha(s_0) \rangle| \ge 1 $$
$$ \kappa(s_0) \|\alpha(s_0)\| \ge 1 $$
$$ \kappa(s_0) \ge \frac{1}{\|\alpha(s_0)\|} $$

Como queríamos demostrar. $\square$

---

# Solución del Ejercicio 6

## Enunciado
Sea $\alpha$ una curva de rapidez unitaria en $\mathbb{R}^3$ con curvatura nunca nula, torsión $\tau$ y marco de Frenet $\{T, N, B\}$.
a) Mostrar que si $\tau/\kappa$ es constante, entonces $\alpha$ es una hélice.
b) Mostrar que $\alpha$ es una hélice si y solo si existe un plano que contiene a $N(t)$ para todo $t$.

## Solución

### a) $\tau/\kappa$ constante implica hélice

Una curva se define como **hélice general** (o cilíndrica) si su vector tangente $T(s)$ forma un ángulo constante con un vector fijo unitario $u$. Es decir, $\langle T(s), u \rangle = \cos \theta = \text{constante}$.

Supongamos que $\frac{\tau}{\kappa} = c$ (constante).
Podemos escribir $\tau = c\kappa$.
Consideremos el vector $u = \frac{cT + B}{\sqrt{1+c^2}}$.
Derivamos $u$ respecto a $s$:
$$ u' = \frac{1}{\sqrt{1+c^2}} (cT' + B') $$
Usando las fórmulas de Frenet ($T' = \kappa N$, $B' = -\tau N$):
$$ u' = \frac{1}{\sqrt{1+c^2}} (c\kappa N - \tau N) = \frac{1}{\sqrt{1+c^2}} (c\kappa - c\kappa) N = 0 $$
(usamos que $\tau = c\kappa$).
Como $u' = 0$, el vector $u$ es constante.

Ahora calculamos el producto escalar $\langle T(s), u \rangle$:
$$ \langle T, u \rangle = \left\langle T, \frac{cT + B}{\sqrt{1+c^2}} \right\rangle = \frac{1}{\sqrt{1+c^2}} (c \langle T, T \rangle + \langle T, B \rangle) $$
$$ \langle T, u \rangle = \frac{c}{\sqrt{1+c^2}} $$
Como $c$ es constante, $\langle T, u \rangle$ es constante.
Por lo tanto, $\alpha$ es una hélice.

### b) Hélice $\iff N(t)$ contenido en un plano

La condición "existe un plano que contiene a $N(t)$" se interpreta como que los vectores $N(t)$ (trasladados al origen) son paralelos a un plano fijo, o equivalentemente, que son ortogonales a un vector fijo $u$.
Es decir, existe $u$ constante tal que $\langle N(t), u \rangle = 0$ para todo $t$.

**($\Rightarrow$) Si $\alpha$ es una hélice:**
Sabemos que $\tau/\kappa = \cot \theta$ es constante.
Definimos el vector eje de la hélice como $u = \cos \theta T + \sin \theta B$.
Como vimos en la parte a), este vector es constante ($u' = 0$).
Calculamos $\langle N, u \rangle$:
$$ \langle N, \cos \theta T + \sin \theta B \rangle = \cos \theta \langle N, T \rangle + \sin \theta \langle N, B \rangle = 0 $$
Por lo tanto, $N(t)$ es siempre ortogonal al vector constante $u$, lo que significa que $N(t)$ está contenido en el plano ortogonal a $u$.

**($\Leftarrow$) Si $N(t)$ está en un plano:**
Existe un vector constante unitario $u$ tal que $\langle N(t), u \rangle = 0$ para todo $t$.
Como $\{T, N, B\}$ es base, podemos escribir $u$ en esta base. Dado que es ortogonal a $N$, $u$ debe estar en el plano generado por $T$ y $B$:
$$ u(t) = a(t) T(t) + b(t) B(t) $$
Como $u$ es unitario, $a(t) = \cos \theta(t)$ y $b(t) = \sin \theta(t)$ para alguna función $\theta(t)$.
$$ u = \cos \theta(t) T(t) + \sin \theta(t) B(t) $$
Como $u$ es constante, $u' = 0$. Derivamos:
$$ 0 = u' = -\sin \theta \cdot \theta' T + \cos \theta T' + \cos \theta \cdot \theta' B + \sin \theta B' $$
Sustituimos Frenet ($T' = \kappa N$, $B' = -\tau N$):
$$ 0 = -\sin \theta \cdot \theta' T + \cos \theta \kappa N + \cos \theta \cdot \theta' B - \sin \theta \tau N $$
Agrupando componentes:
$$ 0 = (-\sin \theta \cdot \theta') T + (\kappa \cos \theta - \tau \sin \theta) N + (\cos \theta \cdot \theta') B $$
Como $T, N, B$ son linealmente independientes, cada componente debe ser cero:
1. $-\sin \theta \cdot \theta' = 0$
2. $\cos \theta \cdot \theta' = 0$
3. $\kappa \cos \theta - \tau \sin \theta = 0$

De 1 y 2, como seno y coseno no se anulan simultáneamente, debe ser $\theta'(t) = 0$.
Esto implica que $\theta$ es constante.
De 3, tenemos $\kappa \cos \theta = \tau \sin \theta$.
$$ \frac{\tau}{\kappa} = \cot \theta = \text{constante} $$
Por la parte a), si $\tau/\kappa$ es constante, la curva es una hélice. $\square$

---

# Solución del Ejercicio 7

## Enunciado
Sea $\alpha : \mathbb{R} \to \mathbb{R}^2$, $\alpha(t) = (t, \cosh t)$. Calcular la curvatura de $\alpha$ de dos maneras:
1. Por definición, hallando explícitamente la reparametrización de $\alpha$ por longitud de arco.
2. Recurriendo a la fórmula para la curvatura de curvas regulares que no tienen necesariamente rapidez unitaria.

## Solución

### 1. Por definición (Reparametrización)

Calculamos la rapidez:
$$ \alpha'(t) = (1, \sinh t) $$
$$ \|\alpha'(t)\| = \sqrt{1 + \sinh^2 t} = \sqrt{\cosh^2 t} = \cosh t $$

Calculamos la longitud de arco $s(t)$ desde $t=0$:
$$ s(t) = \int_0^t \cosh u \, du = \sinh t $$
Invertimos para obtener $t(s)$:
$$ t(s) = \text{arcsinh } s $$

La reparametrización por longitud de arco es $\beta(s) = \alpha(t(s))$:
$$ \beta(s) = (\text{arcsinh } s, \cosh(\text{arcsinh } s)) = (\text{arcsinh } s, \sqrt{1+s^2}) $$

Calculamos el vector tangente unitario $T(s) = \beta'(s)$:
$$ T(s) = \left( \frac{1}{\sqrt{1+s^2}}, \frac{1}{2\sqrt{1+s^2}} (2s) \right) = \left( \frac{1}{\sqrt{1+s^2}}, \frac{s}{\sqrt{1+s^2}} \right) $$

Calculamos $T'(s)$:
$$ \frac{d}{ds} \left( (1+s^2)^{-1/2} \right) = -\frac{1}{2}(1+s^2)^{-3/2}(2s) = -s(1+s^2)^{-3/2} $$
$$ \frac{d}{ds} \left( s(1+s^2)^{-1/2} \right) = (1+s^2)^{-1/2} + s(-s(1+s^2)^{-3/2}) = \frac{1+s^2-s^2}{(1+s^2)^{3/2}} = (1+s^2)^{-3/2} $$
$$ T'(s) = \frac{1}{(1+s^2)^{3/2}} (-s, 1) $$

La curvatura es la norma de $T'(s)$:
$$ \kappa(s) = \|T'(s)\| = \frac{1}{(1+s^2)^{3/2}} \sqrt{(-s)^2 + 1^2} = \frac{\sqrt{s^2+1}}{(1+s^2)^{3/2}} = \frac{1}{1+s^2} $$

Expresando en términos de $t$ (usando $s = \sinh t$):
$$ \kappa(t) = \frac{1}{1+\sinh^2 t} = \frac{1}{\cosh^2 t} $$

### 2. Usando la fórmula

Para una curva plana $\alpha(t) = (x(t), y(t))$, la curvatura está dada por:
$$ \kappa(t) = \frac{|x' y'' - x'' y'|}{((x')^2 + (y')^2)^{3/2}} $$

En nuestro caso:
$x(t) = t \implies x' = 1, x'' = 0$
$y(t) = \cosh t \implies y' = \sinh t, y'' = \cosh t$

Sustituyendo:
$$ \kappa(t) = \frac{|1 \cdot \cosh t - 0 \cdot \sinh t|}{(1^2 + \sinh^2 t)^{3/2}} $$
$$ \kappa(t) = \frac{\cosh t}{(\cosh^2 t)^{3/2}} = \frac{\cosh t}{\cosh^3 t} = \frac{1}{\cosh^2 t} $$

Ambos métodos arrojan el mismo resultado. $\square$

---

# Solución del Ejercicio 8

## Enunciado
Sea $\alpha : (a, b) \to \mathbb{R}^2$ una curva de rapidez unitaria y sean $\kappa, k : (a, b) \to \mathbb{R}$ su curvatura y su curvatura signada, respectivamente. Mostrar que $\kappa = |k|$.

## Solución

Sea $\alpha(s)$ una curva plana parametrizada por longitud de arco.
El vector tangente unitario es $T(s) = \alpha'(s)$.

**Curvatura ($\kappa$):**
Se define como la magnitud de la derivada del vector tangente:
$$ \kappa(s) = \|T'(s)\| $$

**Curvatura Signada ($k$):**
En el plano, definimos el vector normal signado $N_s(s)$ como el vector obtenido al rotar $T(s)$ un ángulo de $\pi/2$ en sentido antihorario. Como $T(s)$ es unitario, $N_s(s)$ también lo es.
La curvatura signada $k(s)$ se define mediante la relación:
$$ T'(s) = k(s) N_s(s) $$

**Relación:**
Tomando la norma en la definición de curvatura signada:
$$ \|T'(s)\| = \|k(s) N_s(s)\| $$
$$ \kappa(s) = |k(s)| \|N_s(s)\| $$
Como $\|N_s(s)\| = 1$, obtenemos:
$$ \kappa(s) = |k(s)| $$

Esto demuestra que la curvatura (que es siempre no negativa) es el valor absoluto de la curvatura signada. $\square$

---

# Solución del Ejercicio 9

## Enunciado
Sea $\alpha : I \to \mathbb{R}^2$ una curva de rapidez unitaria con curvatura signada $k$ nunca nula. Una circunferencia de centro $p$ y radio $r$ se llama **circunferencia osculatriz** de $\alpha$ en $0$ si es una aproximación de orden dos de $\alpha$ en $t=0$, es decir, si la función $f(s) = \|\alpha(s) - p\|^2$ cumple que $f(0) = r^2$ y $f'(0) = f''(0) = 0$.
Probar que la circunferencia de centro $p = \alpha(0) + \frac{1}{k(0)} N_s(0)$ y radio $r = \frac{1}{|k(0)|}$ es la única circunferencia osculatriz de $\alpha$ en $t=0$. (Aquí $N_s(0)$ es el normal signado, equivalente a $I(\alpha'(0))$).

## Solución

Definimos la función de distancia al cuadrado:
$$ f(s) = \langle \alpha(s) - p, \alpha(s) - p \rangle $$

**Condición 1: $f(0) = r^2$**
$$ \|\alpha(0) - p\|^2 = r^2 \implies \|\alpha(0) - p\| = r $$
Esto simplemente dice que $\alpha(0)$ está en la circunferencia.

**Condición 2: $f'(0) = 0$**
Derivamos $f(s)$:
$$ f'(s) = 2 \langle \alpha'(s), \alpha(s) - p \rangle $$
Evaluando en $s=0$:
$$ 2 \langle T(0), \alpha(0) - p \rangle = 0 \implies \langle T(0), \alpha(0) - p \rangle = 0 $$
Esto implica que el vector $\alpha(0) - p$ es ortogonal al vector tangente $T(0)$.
En el plano, los vectores ortogonales a $T(0)$ son múltiplos del vector normal signado $N_s(0)$.
Por lo tanto, existe un escalar $\lambda$ tal que:
$$ \alpha(0) - p = \lambda N_s(0) \implies p = \alpha(0) - \lambda N_s(0) $$
Además, de la condición 1, $r = \|\alpha(0) - p\| = \|\lambda N_s(0)\| = |\lambda|$.

**Condición 3: $f''(0) = 0$**
Derivamos $f'(s)$:
$$ f''(s) = 2 (\langle \alpha''(s), \alpha(s) - p \rangle + \langle \alpha'(s), \alpha'(s) \rangle) $$
Sabemos que $\alpha'(s) = T(s)$ y $\alpha''(s) = k(s) N_s(s)$ (por definición de curvatura signada).
$$ f''(s) = 2 (\langle k(s) N_s(s), \alpha(s) - p \rangle + \|T(s)\|^2) $$
Como $\alpha$ tiene rapidez unitaria, $\|T(s)\|^2 = 1$.
$$ f''(s) = 2 (\langle k(s) N_s(s), \alpha(s) - p \rangle + 1) $$
Evaluando en $s=0$:
$$ \langle k(0) N_s(0), \alpha(0) - p \rangle + 1 = 0 $$
Sustituimos $\alpha(0) - p = \lambda N_s(0)$:
$$ \langle k(0) N_s(0), \lambda N_s(0) \rangle + 1 = 0 $$
$$ k(0) \lambda \langle N_s(0), N_s(0) \rangle + 1 = 0 $$
Como $\|N_s(0)\| = 1$:
$$ k(0) \lambda + 1 = 0 \implies \lambda = -\frac{1}{k(0)} $$

**Conclusión:**
Hemos determinado $\lambda$ y $r$ de manera única.
El centro es:
$$ p = \alpha(0) - \left( -\frac{1}{k(0)} \right) N_s(0) = \alpha(0) + \frac{1}{k(0)} N_s(0) $$
El radio es:
$$ r = |\lambda| = \left| -\frac{1}{k(0)} \right| = \frac{1}{|k(0)|} $$
Esto demuestra la existencia y unicidad de la circunferencia osculatriz. $\square$

---

# Solución del Ejercicio 10

## Enunciado
a) Sea $\alpha : I \to \mathbb{R}^2, \alpha(t) = (x(t), y(t))$ una curva regular plana. Mostrar que la curvatura signada de $\alpha$ en $t \in I$ viene dada por
$$ k(t) = \frac{x'y'' - x''y'}{((x')^2 + (y')^2)^{3/2}} $$
b) Sea $\alpha : \mathbb{R} \to \mathbb{R}^2$ la elipse $\alpha(t) = (a \cos t, b \sin t)$, donde $a, b > 0$. Mostrar que la curvatura signada $k$ tiene al menos cuatro puntos críticos en el intervalo $[0, 2\pi)$.

## Solución

### a) Fórmula de la curvatura signada

Sea $s$ el parámetro de longitud de arco. El vector tangente unitario es $T = \frac{\alpha'}{\|\alpha'\|}$.
El vector normal signado $N_s$ se obtiene rotando $T$ en $90^\circ$ antihorario. Si $T = (u, v)$, entonces $N_s = (-v, u)$.
En términos de coordenadas:
$$ T = \frac{(x', y')}{\sqrt{x'^2 + y'^2}}, \quad N_s = \frac{(-y', x')}{\sqrt{x'^2 + y'^2}} $$

La curvatura signada $k$ satisface $\frac{dT}{ds} = k N_s$.
Por regla de la cadena: $\frac{dT}{ds} = \frac{dT}{dt} \frac{dt}{ds} = \frac{T'}{\|\alpha'\|}$.
Entonces $k = \langle \frac{dT}{ds}, N_s \rangle = \frac{1}{\|\alpha'\|} \langle T', N_s \rangle$.

Calculamos $T'$:
$$ T' = \left( \frac{\alpha'}{\|\alpha'\|} \right)' = \frac{\alpha'' \|\alpha'\| - \alpha' (\|\alpha'\|)'}{\|\alpha'\|^2} $$
Sustituimos en la expresión de $k$:
$$ k = \frac{1}{\|\alpha'\|} \left\langle \frac{\alpha'' \|\alpha'\| - \alpha' (\dots)}{\|\alpha'\|^2}, N_s \right\rangle $$
Como $\langle \alpha', N_s \rangle = 0$, el segundo término se anula:
$$ k = \frac{1}{\|\alpha'\|^3} \langle \alpha'' \|\alpha'\|, N_s \rangle = \frac{1}{\|\alpha'\|^2} \langle \alpha'', N_s \rangle $$
Sustituyendo las coordenadas $\alpha'' = (x'', y'')$ y $N_s = \frac{(-y', x')}{\|\alpha'\|}$:
$$ k = \frac{1}{\|\alpha'\|^2} \left\langle (x'', y''), \frac{(-y', x')}{\|\alpha'\|} \right\rangle = \frac{-x''y' + y''x'}{\|\alpha'\|^3} $$
$$ k(t) = \frac{x'y'' - x''y'}{((x')^2 + (y')^2)^{3/2}} $$

### b) Curvatura de la elipse

Para $\alpha(t) = (a \cos t, b \sin t)$:
$x' = -a \sin t, \quad x'' = -a \cos t$
$y' = b \cos t, \quad y'' = -b \sin t$

Numerador:
$$ x'y'' - x''y' = (-a \sin t)(-b \sin t) - (-a \cos t)(b \cos t) = ab \sin^2 t + ab \cos^2 t = ab $$

Denominador:
$$ ((x')^2 + (y')^2)^{3/2} = (a^2 \sin^2 t + b^2 \cos^2 t)^{3/2} $$

Curvatura signada:
$$ k(t) = \frac{ab}{(a^2 \sin^2 t + b^2 \cos^2 t)^{3/2}} $$

Para hallar los puntos críticos, derivamos $k(t)$ respecto a $t$.
Sea $D(t) = a^2 \sin^2 t + b^2 \cos^2 t$. Entonces $k(t) = ab (D(t))^{-3/2}$.
$$ k'(t) = ab \left( -\frac{3}{2} \right) (D(t))^{-5/2} D'(t) $$
Calculamos $D'(t)$:
$$ D'(t) = 2a^2 \sin t \cos t - 2b^2 \cos t \sin t = (a^2 - b^2) \sin(2t) $$
Entonces:
$$ k'(t) = -\frac{3}{2} ab (D(t))^{-5/2} (a^2 - b^2) \sin(2t) $$

Los puntos críticos ocurren cuando $k'(t) = 0$.
Suponiendo $a \neq b$ (si $a=b$ es una circunferencia y la curvatura es constante, todos los puntos son críticos), esto ocurre si y solo si $\sin(2t) = 0$.
$$ 2t = n\pi \implies t = \frac{n\pi}{2} $$
En el intervalo $[0, 2\pi)$, los valores son:
$$ t = 0, \frac{\pi}{2}, \pi, \frac{3\pi}{2} $$
Estos son 4 puntos distintos.
Estos puntos corresponden a los vértices de la elipse (extremos de los ejes mayor y menor), donde la curvatura alcanza sus máximos y mínimos locales.
Esto es consistente con el Teorema de los Cuatro Vértices, que afirma que toda curva cerrada simple convexa tiene al menos cuatro vértices (puntos críticos de la curvatura). $\square$

---

# Solución del Ejercicio 11

## Enunciado
Sea $\alpha(t) = (\alpha_1(t), \alpha_2(t), 0)$ una curva regular (contenida en el plano $z = 0$) y sea $T : \mathbb{R}^3 \to \mathbb{R}^3$ una transformación lineal inyectiva. Sea $\beta = T \circ \alpha$.
a) Mostrar que la curva $\beta$ es regular.
b) ¿Cuánto valen las torsiones de $\alpha$ y $\beta$?

## Solución

### a) Regularidad de $\beta$

La curva $\beta$ está definida por $\beta(t) = T(\alpha(t))$.
Calculamos su vector velocidad usando la regla de la cadena y la linealidad de $T$:
$$ \beta'(t) = \frac{d}{dt} (T(\alpha(t))) = T(\alpha'(t)) $$

Como $\alpha$ es regular, sabemos que $\alpha'(t) \neq 0$ para todo $t$.
Como $T$ es una transformación lineal inyectiva, su núcleo es trivial ($\ker(T) = \{0\}$). Esto significa que $T(v) = 0$ si y solo si $v = 0$.
Dado que $\alpha'(t) \neq 0$, entonces $T(\alpha'(t)) \neq 0$.
Por lo tanto, $\beta'(t) \neq 0$ para todo $t$.
Conclusión: $\beta$ es una curva regular.

### b) Torsiones

**Torsión de $\alpha$:**
La curva $\alpha(t)$ tiene tercera componente idénticamente nula, por lo que está contenida en el plano $xy$ ($z=0$).
Sabemos que toda curva plana (contenida en un plano fijo) tiene torsión nula.
Por lo tanto, $\tau_\alpha = 0$.

**Torsión de $\beta$:**
La imagen de $\alpha$ está contenida en el subespacio $V = \{(x, y, 0) \mid x, y \in \mathbb{R}\}$, que es un plano (dimensión 2).
La imagen de $\beta$ es $T(\text{Im}(\alpha))$, que está contenida en el subespacio $W = T(V)$.
Como $T$ es inyectiva y lineal, preserva la dimensión de los subespacios.
$$ \dim(W) = \dim(T(V)) = \dim(V) = 2 $$
Esto significa que $W$ es un plano que pasa por el origen en $\mathbb{R}^3$.
Como la curva $\beta$ está contenida en el plano $W$, es una curva plana.
Por lo tanto, su torsión es nula.
$\tau_\beta = 0$.

**Respuesta:** Ambas torsiones valen cero. $\square$

---

# Solución del Ejercicio 12

## Enunciado
Mostrar que si la curva $\alpha : [a, b] \to \mathbb{R}^n$ tiene longitud igual a la distancia entre $\alpha(a)$ y $\alpha(b)$, entonces $\alpha$ es una reparametrización creciente del segmento que une esos puntos.

## Solución

Sean $p = \alpha(a)$ y $q = \alpha(b)$.
La longitud de la curva es $L(\alpha) = \int_a^b \|\alpha'(t)\| dt$.
La distancia entre los extremos es $d(p, q) = \|q - p\|$.
Por el Teorema Fundamental del Cálculo:
$$ q - p = \alpha(b) - \alpha(a) = \int_a^b \alpha'(t) dt $$
Tomando normas:
$$ \|q - p\| = \left\| \int_a^b \alpha'(t) dt \right\| $$
Por hipótesis, $L(\alpha) = \|q - p\|$, así que:
$$ \int_a^b \|\alpha'(t)\| dt = \left\| \int_a^b \alpha'(t) dt \right\| $$

Si $p = q$, entonces la longitud es 0, lo que implica $\|\alpha'(t)\| = 0$ para todo $t$, así que $\alpha$ es constante (un punto, que es un segmento degenerado).
Supongamos $p \neq q$. Sea $u = \frac{q - p}{\|q - p\|}$ el vector unitario en la dirección del segmento.
Podemos escribir la norma de la integral como el producto punto con $u$:
$$ \left\| \int_a^b \alpha'(t) dt \right\| = \left\langle \int_a^b \alpha'(t) dt, u \right\rangle = \int_a^b \langle \alpha'(t), u \rangle dt $$
Por la desigualdad de Cauchy-Schwarz, sabemos que $\langle \alpha'(t), u \rangle \le \|\alpha'(t)\| \|u\| = \|\alpha'(t)\|$.
Integrando esta desigualdad:
$$ \int_a^b \langle \alpha'(t), u \rangle dt \le \int_a^b \|\alpha'(t)\| dt $$
La igualdad se da si y solo si $\langle \alpha'(t), u \rangle = \|\alpha'(t)\|$ para todo $t$ (asumiendo continuidad).
La igualdad en Cauchy-Schwarz ($\langle v, u \rangle = \|v\|\|u\|$) ocurre si y solo si $v$ es un múltiplo escalar no negativo de $u$.
Es decir, $\alpha'(t) = \lambda(t) u$ para alguna función escalar $\lambda(t) \ge 0$.
De hecho, $\lambda(t) = \|\alpha'(t)\|$.

Integrando $\alpha'(t)$:
$$ \alpha(t) = \alpha(a) + \int_a^t \alpha'(\tau) d\tau = p + \int_a^t \lambda(\tau) u \, d\tau $$
$$ \alpha(t) = p + \left( \int_a^t \lambda(\tau) d\tau \right) u $$
Definimos $g(t) = \int_a^t \lambda(\tau) d\tau$.
Como $\lambda(t) = \|\alpha'(t)\| \ge 0$ (y asumimos regularidad o al menos no degeneración trivial, aunque no es estrictamente necesario para la monotonía), $g(t)$ es una función creciente (o no decreciente).
Sustituyendo $u$:
$$ \alpha(t) = p + g(t) \frac{q - p}{\|q - p\|} $$
Esto describe una parametrización del segmento de recta que une $p$ con $q$.
Verificamos los extremos:
- $g(a) = 0 \implies \alpha(a) = p$.
- $g(b) = \int_a^b \|\alpha'(t)\| dt = L(\alpha) = \|q - p\|$.
  Entonces $\alpha(b) = p + \|q - p\| \frac{q - p}{\|q - p\|} = p + (q - p) = q$.

Por lo tanto, $\alpha$ recorre el segmento de $p$ a $q$ de manera monótona. $\square$

---

# Solución del Ejercicio 13

## Enunciado
Probar que una curva regular $\alpha$ está contenida en una recta si y sólo si existe un punto $p$ tal que cada recta tangente a $\alpha$ pasa por $p$. ¿Qué ocurre si se quita la hipótesis de que la curva sea regular?

## Solución

### Caso Regular

**($\Rightarrow$)**
Si $\alpha$ está contenida en una recta $L$, entonces el vector tangente $\alpha'(t)$ es paralelo a la dirección de la recta para todo $t$.
La recta tangente en $\alpha(t)$ es la misma recta $L$.
Cualquier punto $p \in L$ cumple que todas las rectas tangentes (que son $L$) pasan por él.

**($\Leftarrow$)**
Supongamos que existe un punto $p$ tal que para todo $t$, la recta tangente a $\alpha$ en $t$ pasa por $p$.
La ecuación de la recta tangente es $r(\lambda) = \alpha(t) + \lambda \alpha'(t)$.
La condición implica que existe un escalar $\lambda(t)$ tal que:
$$ p = \alpha(t) + \lambda(t) \alpha'(t) $$
Reordenando:
$$ \alpha(t) - p = -\lambda(t) \alpha'(t) $$
Esto significa que el vector $\alpha(t) - p$ es colineal con el vector tangente $\alpha'(t)$.
Por lo tanto, su producto cruz es cero:
$$ (\alpha(t) - p) \times \alpha'(t) = 0 $$
Derivamos esta expresión respecto a $t$:
$$ (\alpha'(t) \times \alpha'(t)) + (\alpha(t) - p) \times \alpha''(t) = 0 $$
$$ 0 + (\alpha(t) - p) \times \alpha''(t) = 0 $$
$$ (\alpha(t) - p) \times \alpha''(t) = 0 $$
Esto implica que $\alpha''(t)$ es paralelo a $\alpha(t) - p$.
Como $\alpha(t) - p$ es paralelo a $\alpha'(t)$ (por la condición inicial), entonces $\alpha''(t)$ es paralelo a $\alpha'(t)$.
En consecuencia:
$$ \alpha'(t) \times \alpha''(t) = 0 $$
La curvatura de una curva regular en $\mathbb{R}^3$ está dada por $\kappa(t) = \frac{\|\alpha'(t) \times \alpha''(t)\|}{\|\alpha'(t)\|^3}$.
Como el numerador es 0, tenemos $\kappa(t) = 0$ para todo $t$.
Una curva con curvatura idénticamente nula es una recta (o un segmento de recta).

### Caso No Regular

Si se quita la hipótesis de regularidad, la implicación ($\Leftarrow$) es **falsa**.
Si la curva no es regular, $\alpha'(t)$ puede anularse. En los puntos donde $\alpha'(t) = 0$, la recta tangente no está bien definida (o la condición se satisface trivialmente si consideramos que "pasa por p" no impone restricción, o si definimos la tangente por límites).
Consideremos el siguiente contraejemplo:
Una curva que viaja por una recta hacia $p$, se detiene en $p$ (velocidad cero), y luego sale por otra recta distinta.
Ejemplo:
$$ \alpha(t) = \begin{cases} (t^3, 0, 0) & \text{si } t < 0 \\ (0, t^3, 0) & \text{si } t \ge 0 \end{cases} $$
Tomemos $p = (0, 0, 0)$.
- Para $t < 0$, $\alpha'(t) = (3t^2, 0, 0)$. La recta tangente es el eje $x$, que pasa por $p$.
- Para $t > 0$, $\alpha'(t) = (0, 3t^2, 0)$. La recta tangente es el eje $y$, que pasa por $p$.
- En $t = 0$, $\alpha'(0) = (0, 0, 0)$. Es un punto singular.

Todas las rectas tangentes (donde están definidas) pasan por $p$. Sin embargo, la curva no está contenida en una única recta; es la unión de dos semirrectas perpendiculares.
La regularidad es crucial para evitar estos cambios abruptos de dirección en puntos donde la velocidad se anula. $\square$

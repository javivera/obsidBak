# Explicación: Condición Inicial en el Transporte Paralelo

Tienes razón en notar que $W(0) = \alpha'(0)$ parece una definición en un solo punto, pero en el contexto de **Transporte Paralelo**, esto funciona como una **condición inicial** para una ecuación diferencial.

### 1. El Campo $W(t)$ está definido por una EDO
Un campo $W(t)$ es **paralelo** si cumple la ecuación:
$$ \frac{DW}{dt} = 0 \iff W'(t) \perp T_{\alpha(t)}S $$
Esta es una Ecuación Diferencial Ordinaria (EDO) de primer orden de la forma $W'(t) = \Gamma(\alpha(t), \alpha'(t), W(t))$. Por el teorema de existencia y unicidad, una vez que fijas el valor en un punto (la **condición inicial**), el campo queda unívocamente definido para todo $t$ a lo largo de la curva.

### 2. ¿Por qué no $W(t) = \alpha'(t)$?
Para que $W(t) = \alpha'(t)$ fuera la solución, la curva $\alpha$ tendría que ser una **geodésica**. 
- En la esfera, las geodésicas son los círculos máximos (como el Ecuador).
- El paralelo de altura $1/2$ (latitud $30^\circ$) **no es una geodésica**. 
- Por lo tanto, su vector tangente $\alpha'(t)$ **no es un campo paralelo**. Si calculamos su derivada covariante, veremos que "dobla" respecto a la superficie: $\frac{D\alpha'}{dt} \neq 0$.

### 3. La intuición del Ejercicio 6
El ejercicio te dice:
1. Toma el vector tangente inicial $v = \alpha'(0)$.
2. Transpórtalo "sin girar" (paralelamente) a lo largo del paralelo.
3. Como el paralelo no es geodésica, el vector $W(t)$ se irá desfasando del vector tangente $\alpha'(t)$.
4. Al dar la vuelta, el ángulo entre $W(L)$ y $\alpha'(L)$ (que vuelve a ser el original) es la **holonomía**.

**En resumen:** $W(0) = \alpha'(0)$ no significa que sean iguales siempre; significa que el campo paralelo "nace" coincidiendo con la velocidad, pero luego cada uno sigue su propio camino debido a que la curva no es geodésica.

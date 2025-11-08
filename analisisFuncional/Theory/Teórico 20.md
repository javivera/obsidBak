---
dateCreated: 2024-11-10,20:16
---
>[!Remark]
>La representación $(7.10)$ (de [[Teórico 19#^e7a5da]]) del operador autoadjunto $T$ es una versión de dimensión infinita del conocido resultado en álgebra lineal de dimensión finita que un matriz autoadjunta puede ser diagonalizada eligiendo una base consistente de vectores propios de la matriz.
>El conjunto ortonormal de vectores propios $\{e_n\}_{n=1}^{r(T)}$ construido arriba es una base ortonormal para el espacio $\mathrm{Im} T$ pero no para todo el espacio $\mathcal{H}$, a menos que $\overline{ImT} = \mathcal{H}$. Por $(7.8)$ [[Teórico 19#^17c4c5]] y por $\{ 0 \}^{\perp}=\mathcal{H}$, esto ocurre cuando $\ker T = \{0\}$, es decir, cuando $T$ es inyectivo, por lo que tenemos el siguiente resultado.

>[!Corollary]
>Si $\ker T = \{ 0 \}$ entonces el conjunto de autovectores $\{ e_n \}_{n=1}^{r(T)}$ es una base ortonormal para $\mathcal{H}$. En particular, si $\mathcal{H}$ es de dimensión infinita y $\ker T = \{ 0 \}$, entonces $T$ tiene infinitos autovalores distintos.
>Si $\mathcal{H}$ es separable también podemos obtener una base de $\mathcal{H}$ formada por autovectores de $T$, incluso cuando $\ker T \neq \{ 0 \}$.
>>[!Proof]
>>1. $\overline{Im(T)}=\mathcal{H}\iff ker(T)=\overline{Im(T)}^{\perp}=\mathcal{H}^{\perp}=\{ 0 \}$ 

>[!Remark]
>Notar no puede ser $T$ comoacto y $T$ sobre. Pues $T$ sobre imolica $Im(T)=\mathcal{H}$ enticmed $\overline{ImT}=\mathcal{H}$ entonces $Ker(T)=\{ 0 \}$ entifnes $T$ imyectivo entonves $T$ inversible (por que son Hilbert entonces por aplicación abierta es biyectiva ) 

>[!Corollary]
>Supongamos que $\mathcal{H}$ es separable. Entonces existe una base ortonormal de $\mathcal{H}$ formada enteramente por autovectores de $T$. Esta base tiene la forma $\{ e_n \}_{n=1}^{r(T)} \cup \{ z_m \}_{m=1}^{n(T)}$, donde $\{ e_n \}_{n=1}^{r(T)}$ es una base ortonormal de $\text{Im}T$ y $\{ z_m \}_{m=1}^{n(T)}$ es una base ortonormal de $\ker T$.
>>[!Proof]
>>2. Como $\mathcal{H}$ es separable, $\ker T$ es un espacio de Hilbert separable (por el Lema 3.25 y el Ejercicio 3.25), por lo que, por el Teorema 3.52, existe una base ortonormal para $\ker T$, que escribimos en la forma $\{ z_m \}_{m=1}^{n(T)}$ (donde $n(T)$ puede ser finito o infinito).
>>3. Por definición, para cada $m$ tenemos que $T z_m = 0$, así que $z_m$ es un autovector de $T$ correspondiente al autovalor $\lambda = 0$. 
>>4. Ahora, la unión $E = \{ e_n \}_{n=1}^{r(T)} \cup \{ z_m \}_{m=1}^{n(T)}$ es un conjunto ortonormal en $\mathcal{H}$ pues $\overline{Im(T)}=(ker(T))^{\perp}$ 
>>5. De hecho, es una base para $\mathcal{H}$. Para ver esto, como $\{ e_{n} \}$ bon de $\overline{Im(T)}$ Y análogo $\{ z_{m} \}$ observamos que por el Teorema 3.47 tenemos
>>$$ x = P x + (I - P) x = \sum_{n=1}^{r(T)} \lambda_n (Px, e_n) e_n + \sum_{m=1}^{n(T)} ( (I - P) x, z_m ) z_m=\sum^{r(T)}_{n=1} (x,e_{n})e_{n}+\sum^{n(T)}_{n=1} (x,z_{m})z_{m}$$
>>6. usando (7.11) y, de forma similar, $((I - P) x, z_m) = (x, z_m)$ para cada $m$. 
>>7. Así que, por el Teorema 3.47 nuevamente, $E$ es una base ortonormal para $\mathcal{H}$.

>[!Remark]-
>En el Teorema 7.26 discutimos la existencia de soluciones de las ecuaciones (7.5) para el caso de un operador compacto general $T$. Cuando $T$ es auto-adjunto, podemos usar la representación de $T$ en (7.10) para dar una representación correspondiente de las soluciones.


>[!Theorem]
>Sean $\{\lambda_n\}_{n=1}^{r(T)}$ y $\{e_n\}_{n=1}^{r(T)}$ el conjunto de autovalores no nulos de $T$ y el correspondiente conjunto ortonormal de autovectores construido anteriormente. Entonces, para cualquier $\lambda \neq 0$, una de las siguientes alternativas se cumple para la ecuación
>$$ (T - \lambda I)x = p. \tag{7.12} $$
>- (a) Si $\lambda$ no es un autovalor, entonces la ecuación (7.12) tiene una solución única, y esta solución tiene la forma
>$$ x = \sum_{n=1}^{r(T)} \frac{(p, e_n)}{\lambda_n - \lambda} e_n - \frac{1}{\lambda}(I - P)p. \tag{7.13} $$
>- (b) Si $\lambda$ es un autovalor, sea $E$ el conjunto de enteros $n$ para los cuales $\lambda_n = \lambda$, la ecuación (7.12) tiene una solución si y solo si
>$$ (p, e_n) = 0, \quad n \in E. \tag{7.14} $$
>Si (7.14) se cumple, entonces el conjunto de soluciones de (7.12) tiene la forma
>$$ x = \sum_{n=1}^{r(T)} \frac{(p, e_n)}{\lambda_n - \lambda} e_n - \frac{1}{\lambda}(I - P)p + z, \tag{7.15} $$
>donde $z = \sum_{n \in E} \alpha_n e_n$ es un elemento arbitrario de $\ker(T - \lambda I)$.
>>[!Proof]
>>
>>8. La existencia de soluciones de (7.12) bajo las condiciones establecidas sigue del Teorema 7.26. 
>>9. Para mostrar que las soluciones tienen la forma indicada, notemos que, dado que $\{e_n\}_{n=1}^{r(T)}$ es una base ortonormal de $\text{Im}T = (\ker T)^\perp$, tenemos
>>$$ x = \sum_{n=1}^{r(T)} (x, e_n) e_n + (I - P)x, \quad p = \sum_{n=1}^{r(T)} (p, e_n) e_n + (I - P)p, $$
>>10. (usando (7.11)) y de (7.12) recordar $(x, e_n) = (Px + (I - P)x, e_n) = (Px, e_n)$
>>$$(T-\lambda I)x=\sum^{r(T)}_{n=1} (x,e_{n})(\lambda_{n}-\lambda)e_{n}-\lambda(I-P)x=\sum^{r(T)}_{n=1} (p,e_{n})e_{n}+(I-P)p$$    
>>11. tomando el producto interior de ambos lados de esta fórmula con $e_k$, para cualquier $1 \leq k \leq r(T)$, y asumiendo que $\lambda$ no es un autovalor, tenemos
>>$$ (x, e_k)(\lambda_k - \lambda) = (p, e_k), $$
>>12. por lo tanto
>>$$ (x, e_k) = \frac{(p, e_k)}{\lambda_k - \lambda}. \tag{7.16} $$
>>13. Además, tomando la proyección ortogonal de ambos lados de la fórmula anterior sobre $\ker T$ obtenemos
>>$$ -\lambda (I - P)x = (I - P)p. $$
>>14. La fórmula (7.13) sigue inmediatamente de estos dos resultados. 
>>15. Esto prueba la alternativa (a). La demostración de la alternativa (b) es similar. 
>>16. Nótese que cuando $k \in E$, las condiciones (7.14) aseguran que la primera ecuación en (7.16) es satisfecha por coeficientes arbitrarios $(x, e_k) = \alpha_k$ (y evitamos la dificultad causada por el término $\lambda_n - \lambda$ en el denominador). El término correspondiente $\alpha_k e_k$ contribuye al elemento arbitrario en $\ker(T - \lambda I)$ en la expresión para la solución $x$.
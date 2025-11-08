
> [!Exercise]-
> Decimos que una función $\varphi : \mathbb{R} \to \mathbb{R}$ es un homomorfismo de $\mathbb{R}$ si cumple que $$\varphi(x+y) = \varphi(x) + \varphi(y)$$ para todo $x,y \in \mathbb{R}$.
>
> **Proposición:** No todos los homomorfismos de $\mathbb{R}$ son continuos.
>
> **Explicación:**
>
> Existen homomorfismos aditivos que son discontinuos, especialmente cuando no se imponen condiciones de regularidad como continuidad, acotación o medibilidad.
>
> **Ejemplo de homomorfismo discontinuo:**
>
> 1. Consideramos $\mathbb{R}$ como un espacio vectorial sobre $\mathbb{Q}$.
> 2. Sea $B$ una base de Hamel de $\mathbb{R}$ sobre $\mathbb{Q}$. Esto significa que cualquier $x \in \mathbb{R}$ puede escribirse de forma única como:
>
> $$x = \sum_{i=1}^n q_i b_i,$$
>
> donde $q_i \in \mathbb{Q}$ y $b_i \in B$.
> 3. Definimos un homomorfismo $\varphi : \mathbb{R} \to \mathbb{R}$ asignando valores arbitrarios $c_b \in \mathbb{R}$ para cada $b \in B$, y está bien definida como se ha descrito:
>
> $$\varphi\left(\sum_{i=1}^n q_i b_i\right) = \sum_{i=1}^n q_i c_{b_i}.$$
>
> Este homomorfismo es aditivo (respeta la propiedad $\varphi(x+y) = \varphi(x) + \varphi(y)$), pero en general no es continuo, ya que depende de la elección arbitraria de los valores $c_b$.
>
> **¿Por qué no es continuo?**
>
> 1. **Base de Hamel y discontinuidad:** La base de Hamel $B$ de $\mathbb{R}$ sobre $\mathbb{Q}$ es una construcción puramente algebraica. No tiene ninguna relación con la topología de $\mathbb{R}$, es decir, no respeta la estructura de continuidad ni densidad de $\mathbb{Q}$ en $\mathbb{R}$.
> 2. **Dependencia de la base de Hamel:** Dado que $\mathbb{R}$ tiene una base de Hamel $B$, cualquier número real $x$ puede escribirse como una combinación lineal finita de elementos de $B$ con coeficientes racionales:
>
> $$x = \sum_{i=1}^n q_i b_i, \quad q_i \in \mathbb{Q}, \ b_i \in B.$$
> El homomorfismo $\varphi$ se define como:
>
> $$\varphi(x) = \sum_{i=1}^n q_i c_{b_i},$$
>
> donde $c_{b_i}$ son valores arbitrarios asignados a los elementos de $B$.
> 3. **Falta de continuidad:** La continuidad requiere que $\varphi(x)$ dependa de $x$ de manera suave, es decir, que pequeños cambios en $x$ produzcan pequeños cambios en $\varphi(x)$. En este caso, $\varphi(x)$ depende de los valores arbitrarios $c_b$ asignados a los elementos de $B$. No hay ninguna garantía de que $\varphi(x)$ varíe de manera continua cuando $x$ cambia, porque los valores $c_b$ no están relacionados de manera uniforme o suave.
> 4. **Ejemplo concreto de discontinuidad:** Supongamos que $x$ y $y$ son dos números reales muy cercanos, pero tienen representaciones diferentes en términos de la base de Hamel $B$:
>
> $$x = \sum_{i=1}^n q_i b_i, \quad y = \sum_{i=1}^m q'_i b'_i.$$
> Si los coeficientes $q_i$ y $q'_i$, o los valores $c_{b_i}$ y $c_{b'_i}$, son muy diferentes, entonces $\varphi(x)$ y $\varphi(y)$ pueden ser completamente distintos, incluso si $x$ y $y$ están muy cerca en $\mathbb{R}$.
>
> **Conexión con la parte (b):**
>
> La parte (b) establece que cualquier homomorfismo continuo debe ser de la forma $\varphi(x) = cx$, donde $c \in \mathbb{R}$. El ejemplo basado en la base de Hamel no es de esta forma, ya que depende de valores arbitrarios $c_b$ asignados a los elementos de $B$. Por lo tanto, este homomorfismo no puede ser continuo.
>
> **Condiciones para continuidad:**
>
> Un homomorfismo aditivo $\varphi : \mathbb{R} \to \mathbb{R}$ será continuo si cumple alguna de las siguientes condiciones:
>
> 1. **Es medible:** Si $\varphi$ es medible, entonces es continuo.
> 2. **Es acotado en algún intervalo:** Si existe un intervalo $[a, b]$ tal que $\varphi$ es acotado en $[a, b]$, entonces es continuo.
> 3. **Es monótono en algún intervalo:** Si $\varphi$ es monótono en algún intervalo, entonces es continuo.
>
> **Conclusión:**
>
> No todos los homomorfismos son continuos. Los homomorfismos discontinuos pueden construirse usando bases de Hamel, pero son altamente patológicos y no aparecen en aplicaciones prácticas donde se requiere continuidad o regularidad.

> [!Proposition] Homomorfismos aditivos de $\mathbb R$
> Sea $\varphi:\mathbb R\to\mathbb R$ un homomorfismo aditivo, es decir, $\varphi(x+y)=\varphi(x)+\varphi(y)$ para todo $x,y\in\mathbb R$. Entonces:
> - (a) Todas las soluciones (sin hipótesis extra) son exactamente las aplicaciones $\mathbb Q$-lineales, determinadas de manera arbitraria por sus valores en una base de Hamel de $\mathbb R$ sobre $\mathbb Q$.
> - (b) Si además $\varphi$ es continua (o medible, o acotada en algún intervalo no trivial, o monótona en algún intervalo), entonces existe $a\in\mathbb R$ tal que $\varphi(x)=a x$ para todo $x\in\mathbb R$.
>
>> [!Proof]
>> **Paso 1 — $\mathbb Q$-linealidad.**  
>> De $\varphi(x+y)=\varphi(x)+\varphi(y)$ se obtiene: $\varphi(0)=0$; por inducción $\varphi(nx)=n\varphi(x)$ para $n\in\mathbb Z$; y, para $p\in\mathbb Z,\; q\in\mathbb N$,  
>> $$
>> q\,\varphi\!\big(\tfrac{p}{q}x\big)=\varphi(px)=p\,\varphi(x)\ \Rightarrow\ \varphi\!\big(\tfrac{p}{q}x\big)=\tfrac{p}{q}\varphi(x).
>> $$  
>> Por tanto, $\varphi(qx)=q\varphi(x)$ para todo $q\in\mathbb Q$: $\varphi$ es $\mathbb Q$-lineal.
>>
>> **Paso 2 — Clasificación sin regularidad (bases de Hamel).**  
>> Consideremos $\mathbb R$ como $\mathbb Q$-espacio vectorial. Sea $B$ una base de Hamel. Todo $x\in\mathbb R$ se escribe **de modo único** como combinación finita $x=\sum_{i=1}^n q_i b_i$ con $q_i\in\mathbb Q,\; b_i\in B$.  
>> Si fijamos valores arbitrarios $c_b\in\mathbb R$ para cada $b\in B$ y definimos  
>> $$
>> \varphi\!\Big(\sum_{i=1}^n q_i b_i\Big)\ :=\ \sum_{i=1}^n q_i\,c_{b_i},
>> $$  
>> la unicidad de la descomposición garantiza que esta definición **está bien planteada**, y la $\mathbb Q$-linealidad muestra que $\varphi$ es aditiva.  
>> Recíprocamente, cualquier $\varphi$ aditiva queda determinada por sus valores en $B$. Concluimos (a).
>>
>> **Paso 3 — Caso continuo (y variantes).**  
>> Supongamos $\varphi$ continua en un punto (basta en $0$). Para $x\in\mathbb R$ elige una sucesión $(q_n)\subset\mathbb Q$ con $q_n\to x$. Como $\varphi(q_n)=q_n\varphi(1)$ por $\mathbb Q$-linealidad, usando continuidad:  
>> $$
>> \varphi(x)=\lim_{n\to\infty}\varphi(q_n)=\lim_{n\to\infty}q_n\varphi(1)=x\,\varphi(1)=:a x.
>> $$  
>> Por tanto, bajo continuidad (o, clásicamente, bajo medibilidad, acotación en un intervalo no trivial, o monotonicidad en un intervalo, que implican continuidad en un punto), se obtiene (b).
>>
>> **Conclusión.**  
>> Sin regularidad, las soluciones son todas las $\mathbb Q$-lineales (definidas arbitrariamente en una base de Hamel y extendidas por $\mathbb Q$-linealidad). Con regularidad mínima (continuidad/medibilidad/acotación/monotonicidad), necesariamente $\varphi(x)=ax$.
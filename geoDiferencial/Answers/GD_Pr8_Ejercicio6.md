>[!Example] Ejercicio 6
>Sea $S$ la esfera de centro cero y radio 1 y sea $\alpha$ una parametrización por longitud de arco del paralelo de altura $1/2$. Sea $W$ un campo paralelo a lo largo de $\alpha$ con $W(0) = \alpha'(0)$. Indicar cuántas vueltas da $W$ respecto del marco móvil a lo largo de $\alpha$ cuando esta curva da una vuelta completa. ¿Cuánto gira realmente $W$ a lo largo de $\alpha$?
>>[!Proof]-
>>1. **Datos:** Esfera de radio $R=1$. Altura $z=1/2$.
>>   Sabemos que si $y_0$ es la latitud del paralelo, entonces $\sin(y_0) = \text{altura} = 1/2$.
>>   De aquí deducimos que $y_0 = \pi/6$ ($30^\circ$).
>>   El radio del paralelo es $r = \cos(y_0) = \sqrt{3}/2$.
>>2. **Relación con el marco móvil:**
>>   Sea $\{e_1(t), e_2(t)\}$ un marco móvil ortonormal a lo largo de $\alpha$, donde $e_1(t) = \alpha'(t)$.
>>   La variación del ángulo $\theta$ de un campo paralelo $W$ respecto a este marco satisface:
>>   $$ \theta'(t) = -k_g(t) $$
>>   donde $k_g$ es la curvatura geodésica del paralelo.
>>3. **Cálculo de la curvatura geodésica:**
>>   Para un paralelo en la esfera a latitud $y_0$, la curvatura geodésica es constante:
>>   $$ k_g = \frac{\sin(y_0)}{r} = \frac{\sin(y_0)}{\cos(y_0)} = \tan(y_0) = \tan(\pi/6) = \frac{1}{\sqrt{3}} $$
>>4. **Variación del ángulo en una vuelta completa:**
>>   La longitud del paralelo es $L = 2\pi r = 2\pi \cos(y_0)$.
>>   El cambio total de ángulo $\Delta \theta$ al completar la curva ($t=L$) es:
>>   $$ \Delta \theta = \int_0^L \theta'(t) dt = \int_0^{2\pi \cos y_0} -\tan(y_0) dt = -2\pi \cos y_0 \tan y_0 = -2\pi \sin y_0 $$
>>   Como $\sin y_0 = 1/2$, tenemos:
>>   $$ \Delta \theta = -2\pi \left( \frac{1}{2} \right) = -\pi $$
>>5. **Interpretación:**
>>   - **Respecto al marco móvil:** El vector $W$ gira $-\pi$ radianes. Es decir, da **media vuelta** en sentido horario respecto a la dirección de marcha $\alpha'$.
>>   - **¿Cuánto gira realmente (rotación total)?**:
>>     El marco móvil (el vector tangente $\alpha'$) da una vuelta completa de $2\pi$ respecto a un sistema de coordenadas fijo al dar la vuelta al paralelo.
>>     Por lo tanto, el giro "real" (absoluto) del vector $W$ es:
>>     $$ \Delta \theta_{total} = \Delta \theta_{marco} + \Delta \theta_{curva} = -\pi + 2\pi = \pi $$
>>     O visto de otro modo, el vector ha rotado $\pi$ radianes en el espacio total (holonomía).

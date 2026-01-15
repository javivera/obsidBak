```markdown
[!Example] Ejercicio 7
- **(a)** Curvatura geodésica de la hélice $\alpha(t)=(\cos(at),\,\sin(at),\,at)$ sobre el helicoide $\phi(u,v)=(u\cos v,\,u\sin v,\,v)$ con $a=1/\sqrt{2}$.
- **(b)** Indicar si $\alpha$ minimiza distancia entre puntos de su traza.
- **(c)** Campo paralelo $W$ a lo largo de $\alpha$ con $W(0)=\alpha'(0)$.
>>[!Proof]-
>>- **(a)** Cálculo directo usando curvatura euclídea y curvatura normal (sin usar la segunda forma fundamental):

>1. Notación: $\phi(u,v)=(u\cos v,u\sin v,v)$. Tomamos la hélice con $u=1$, $v=at$, es decir
>   $$\alpha(t)=(\cos(at),\,\sin(at),\,at).$$

>2. Primera derivada y rapidez:
>   $$\alpha'(t)=(-a\sin(at),\,a\cos(at),\,a),\qquad \|\alpha'(t)\|^2=a^2(1+1)=2a^2.$$ Con $a=1/\sqrt2$ la curva es de unidad: $\|\alpha'\|=1$.

>3. Segunda derivada y curvatura euclídea:
>   $$\alpha''(t)=(-a^2\cos(at),\,-a^2\sin(at),\,0),\qquad k=\|\alpha''(t)\|=a^2=\tfrac12.$$ 

>4. Normal unitario de la superficie (en $u=1$):
>   $$\phi_u=(\cos v,\,\sin v,\,0),\quad \phi_v=(-\sin v,\,\cos v,\,1),$$
>   $$\phi_u\times\phi_v=(\sin v,\,-\cos v,\,1),\qquad N=\frac{1}{\sqrt2}(\sin v,\,-\cos v,\,1),\quad v=at.$$ 

>5. Curvatura normal (componente de $\alpha''$ en la dirección normal):
>   $$k_n=\langle\alpha'',N\rangle = \frac{1}{\sqrt2}\big(-a^2\cos v\sin v + a^2\sin v\cos v\big)=0.$$ 

>6. Curvatura geodésica: para curvas unitarias vale $k^2=k_g^2+k_n^2$, por tanto
>   $$k_g=\sqrt{k^2-k_n^2}=k=\tfrac12.$$ 

>>- **(b)** Dado que $k_g\neq0$, la curva no es geodésica en $M$ y por ello no minimiza localmente la distancia intrínseca entre sus puntos.

>>- **(c)** Campo paralelo: escribiendo $W=A(t)\phi_u+B(t)\phi_v$ y resolviendo $\nabla_{\alpha'}W=0$ (ecuaciones para $A,B$ con $u=1$ y $v'=a$) se obtiene
>   $$A'-aB=0,\qquad B'+\tfrac{a}{2}A=0,$$
>   con $A(0)=0$, $B(0)=a$. La solución es $A(t)=\sin(t/2),\;B(t)=a\cos(t/2)$, y por tanto
>   $$W(t)=\sin\tfrac{t}{2}\,(\cos at,\,\sin at,\,0)+\frac{1}{\sqrt2}\cos\tfrac{t}{2}\,(-\sin at,\,\cos at,\,1).$$

``` 
>[!Example] Ejercicio 7
>- **(a)** Curvatura geodésica de la hélice $\alpha(t)=(\cos(at),\,\sin(at),\,at)$ sobre el helicoide $\phi(u,v)=(u\cos v,\,u\sin v,\,v)$ con $a=1/\sqrt{2}$.
>- **(b)** Indicar si $\alpha$ minimiza distancia entre puntos de su traza.
>- **(c)** Campo paralelo $W$ a lo largo de $\alpha$ con $W(0)=\alpha'(0)$.
>>[!Proof]-
>>1. Métrica de $\phi$: $E=\langle\phi_u,\phi_u\rangle=1$, $F=0$, $G=1+u^2$. Segunda forma: $e=0$, $f=-1/\sqrt{1+u^2}$, $g=0$ (con normal $N=(\sin v,-\cos v,u)/\sqrt{1+u^2}$).
>>2. Curva en parámetros: $u(t)=1$, $v(t)=at$, $u'=0$, $v'=a$. Rapidez $\|\alpha'\|^2=E u'^2+G v'^2=2a^2=1$, luego es de arclength.
>>3. Curvatura euclídea: $T=\alpha'$, $T'=(-a^2\cos at,-a^2\sin at,0)$, $k=\|T'\|=a^2=\tfrac12$.
>>4. Curvatura normal: $k_n=\mathrm{II}(\gamma',\gamma')=e u'^2+2fu'v'+g v'^2=0$, porque $g=0$ y $u'=0$. Por tanto $k_g=\sqrt{k^2-k_n^2}=\tfrac12$ constante.
>>5. $\alpha$ no es geodésica ($k_g\ne0$), así que sus subarcos no minimizan la distancia intrínseca salvo coincidencia con el arco más corto de otra geodésica; en particular no es minimizante local.
>>6. Para $W=A\,\phi_u+B\,\phi_v$: ecuaciones de paralelo $A'+\Gamma^u_{vv}B v'=0$, $B'+\Gamma^v_{uv}A v'=0$. Con $\Gamma^u_{vv}=-u$, $\Gamma^v_{uv}=u/(1+u^2)$ y $u=1$, $v'=a$: $A'-aB=0$, $B'+\tfrac{a}{2}A=0$.
>>7. Condición inicial $W(0)=\alpha'(0)$: $\alpha'(t)=A\phi_u+B\phi_v$ da $A(0)=0$, $B(0)=a$. Sistema resuelto: $A(t)=\sin(t/2)$, $B(t)=a\cos(t/2)$.
>>8. Campo paralelo en coordenadas ambientas usando $v=at$ y $a=1/\sqrt2$:
>>   $$W(t)=\sin\tfrac{t}{2}\,(\cos at,\,\sin at,\,0)+\frac{1}{\sqrt2}\cos\tfrac{t}{2}\,(-\sin at,\,\cos at,\,1).$$

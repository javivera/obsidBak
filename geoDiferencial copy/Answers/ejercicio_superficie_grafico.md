>[!Example] Ejercicio 1
>- **(a)** Sea $U\subset\mathbb R^{2}$ abierto, $f:U\to\mathbb R$ y $S=\{(x,y,f(x,y)):(x,y)\in U\}$ el gráfico, parametrizado por $\varphi(x,y)=(x,y,f(x,y))$. Entonces $$\varphi_x=(1,0,f_x),\quad \varphi_y=(0,1,f_y).$$ El producto vectorial es $$\varphi_x\times\varphi_y=(-f_x,-f_y,1),\quad \|\varphi_x\times\varphi_y\|=\sqrt{1+f_x^2+f_y^2}.$$ Por lo tanto 
>  $$n(\varphi(x,y))=\frac{1}{\sqrt{1+f_x(x,y)^2+f_y(x,y)^2}}\,(-f_x(x,y),-f_y(x,y),1)$$
>  es normal unitario en $S$ (está ortogonal a $\varphi_x,\varphi_y$ y tiene norma $1$).
>
>- **(b)** En un gráfico $z=f(x,y)$, en un punto $p=(0,0,0)$ con $\nabla f(p)=0$, las direcciones principales se obtienen diagonalizando el Hessiano $Hf(p)$; las curvaturas principales son los autovalores $\lambda_1,\lambda_2$ de $Hf(p)$ y sus autovectores en el plano $xy$. Las direcciones asintóticas existen si y sólo si $K(p)<0$, equivalen a las direcciones donde la segunda forma es nula, esto es $\langle Hf(p)\,v,v\rangle=0$.
>
>  i) $f(x,y)=axy$.
>  - $f_x=ay$, $f_y=ax$, $f_{xx}=0$, $f_{yy}=0$, $f_{xy}=a$.
>  - $$Hf(0)=\begin{pmatrix}0&a\\ a&0\end{pmatrix},\ \text{autovalores }\lambda_{1}=a,\ \lambda_{2}=-a,$$ con autovectores $v_1=(1,1)$ y $v_2=(1,-1)$ en el plano $xy$.
>  - **Direcciones principales:** a lo largo de $x= y$ y $x= -y$.
>  - **Curvaturas principales:** $k_1=a$, $k_2=-a$.
>  - **Direcciones asintóticas:** cuando $a\neq 0$, existen dos (las mismas principales, pues una es positiva y la otra negativa, la segunda forma se anula sobre las bisectrices).
>  - **Tipo de punto:** $K<0$ si $a\neq 0$; punto hiperbólico (silla). Si $a=0$, la superficie es plana.
>
>  ii) $f(x,y)=(x+y)^2$.
>  - $f_x=2(x+y)$, $f_y=2(x+y)$. En $p$, $\nabla f=0$.
>  - $f_{xx}=2$, $f_{yy}=2$, $f_{xy}=2$; $$Hf(0)=\begin{pmatrix}2&2\\2&2\end{pmatrix}.$$
>  - Autovalores: $\lambda_1=4$ (autovector $(1,1)$), $\lambda_2=0$ (autovector $(1,-1)$).
>  - **Direcciones principales:** $x=y$ y $x=-y$.
>  - **Curvaturas principales:** $k_1=4$, $k_2=0$.
>  - **Direcciones asintóticas:** sí, existe una (la correspondiente a $k_2=0$), a lo largo de $x=-y$.
>  - **Tipo de punto:** $K=0$ y $H>0$; punto parabólico (cilíndrico en esa dirección).
>
>  iii) $f(x,y)=x^4+y^4$.
>  - $f_x=4x^3$, $f_y=4y^3$; en $p$, $\nabla f=0$.
>  - $f_{xx}=12x^2$, $f_{yy}=12y^2$, $f_{xy}=0$; en $p$: $$Hf(0)=\begin{pmatrix}0&0\\0&0\end{pmatrix}.$$
>  - **Direcciones principales:** el Hessiano se anula; todas las direcciones son "planas" al orden 2. No hay curvatura de segundo orden; la primera curvatura no lineal aparece al orden 3–4.
>  - **Curvaturas principales (cuadráticas):** $k_1=0$, $k_2=0$.
>  - **Direcciones asintóticas:** todas (la segunda forma es nula).
>  - **Tipo de punto:** punto plano–degenerado (orden superior), $K=0$ y $H=0$ en $p$.
>
>- **(c) Curvaturas en $p=(0,0,0)$** para gráficos con $\nabla f(p)=0$:
>  - Curvatura Gaussiana: $$\boxed{\,K(p)=\det Hf(p)=f_{xx}f_{yy}-f_{xy}^2\,}.$$
>  - Curvatura media: $$\boxed{\,H(p)=\tfrac12\operatorname{tr}Hf(p)=\tfrac12(f_{xx}+f_{yy})\,}.$$
>  Aplicando:
>  - i) $f=axy$: $K(0)=0\cdot0-a^2= -a^2<0$ si $a\neq 0$; $H(0)=\tfrac12(0+0)=0$.
>  - ii) $f=(x+y)^2$: $K(0)=2\cdot2-2^2=0$; $H(0)=\tfrac12(2+2)=2$.
>  - iii) $f=x^4+y^4$: $K(0)=0$, $H(0)=0$.

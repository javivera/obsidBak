> **Análisis Funcional I — 2024**
> **Práctico 5 — Soluciones parciales**
> 
> A continuación se dan las soluciones de los ejercicios 3, 4, 6 y 7.
> 
> [!Proof] Ejercicio 3
> > Sea $N$ un espacio normado.
> >
> > (a) Para $x\in N$, $x\neq 0$, aplicamos el Teorema de Hahn–Banach: existen funcionales lineales continuos $F\in N'$ que separan el vector $x$ del subespacio $\{0\}$. Más precisamente, existe $F\in N'$ tal que $F(x)=\|x\|$ y $\|F\|=1$. (Se toma la aplicación lineal definida sobre la recta $\operatorname{span}\{x\}$ por $f(\lambda x)=\lambda\|x\|$ y se extiende por Hahn–Banach manteniendo la norma.)
> >
> > (b) Dados $x_1\neq x_2$ en $N$ consideremos $x:=x_1-x_2$, que es no nulo. Por (a) existe $F\in N'$ con $\|F\|=1$ y $F(x)=\|x\|\neq 0$. Entonces $F(x_1)\neq F(x_2)$. Por tanto el dual $N'$ separa puntos de $N$.
> >
> > (c) Para cada $x\in N$ definimos $\widehat{x}:N'\to\mathbb{K}$ por $\widehat{x}(F)=F(x)$ para todo $F\in N'$. Es claro que $\widehat{x}$ es lineal. Además, para toda $F\in N'$, $|\widehat{x}(F)|=|F(x)|\le\|F\|\,\|x\|$, luego $\|\widehat{x}\|\le\|x\|$. Por otra parte, usando (a) existe $F\in N'$ con $\|F\|=1$ y $F(x)=\|x\|$, de donde $\|\widehat{x}\|\ge\|x\|$. Así $\|\widehat{x}\|=\|x\|$ y en particular $\widehat{x}\in N''$ (el bidual) y es continuo.
> >
> > (d) La aplicación canónica $J:N\to N'',\;J(x)=\widehat{x}$ es lineal por construcción y, por la igualdad de normas anterior, es isométrica: $\|J(x)\|_{N''}=\|x\|_N$ para todo $x\in N$.
> 
> [!Proof] Ejercicio 4
> > Sea $N$ un espacio normado y $S\subset N$ un subespacio vectorial cerrado. Sea $x_0\in N\setminus S$. Como $S$ es cerrado y lineal, la distancia $d:=\operatorname{dist}(x_0,S)>0$.
> >
> > Consideramos el subespacio $M=\operatorname{span}(S\cup\{x_0\})$. Definimos en la recta complementaria la forma lineal $f$ sobre $\operatorname{span}\{x_0-s_0\}$ (donde $s_0\in S$ es un punto que aproxima la distancia) por
> > $f(\lambda(x_0-s_0))=\lambda d$.
> >
> > Es inmediato que $|f(\lambda(x_0-s_0))|\le\|\lambda(x_0-s_0)\|$ (pues $\|x_0-s_0\|\ge d$), luego $\|f\|\le 1$ en esa recta. Por Hahn–Banach extendemos $f$ a un funcional $F\in N'$ con la misma norma. Para ese $F$ se tiene $F|_S=0$ (porque en la construcción se anulan los vectores de $S$) y $F(x_0)=d\neq 0$. Así existe $F\in N'$ que anula a $S$ pero no a $x_0$, como se quería.
> 
> [!Proof] Ejercicio 6
> > Sea $X$ un espacio vectorial real o complejo y $S\subset X$. La cápsula convexa (o envolvente convexa) de $S$ se define por
> > $$
> > S_c=\left\{\sum_{i=1}^n\alpha_i x_i:\;x_i\in S,\;\alpha_i>0,\;\sum_{i=1}^n\alpha_i=1,\;n\in\mathbb{N}\right\}.
> > $$
> >
> > (i) Primero probamos que $S_c$ es convexo. Sean $u=\sum_{i=1}^n\alpha_i x_i$ y $v=\sum_{j=1}^m\beta_j y_j$ dos combinaciones convexas (con $x_i,y_j\in S$, coeficientes positivos que suman 1). Para $t\in[0,1]$ tenemos
> > $t u+(1-t)v=\sum_{i=1}^n (t\alpha_i) x_i+\sum_{j=1}^m ((1-t)\beta_j)y_j$,
> > y los coeficientes $t\alpha_i$ y $(1-t)\beta_j$ son no negativos y suman
> > $t\sum_i\alpha_i+(1-t)\sum_j\beta_j=t+(1-t)=1$. Si alguno de los coeficientes fuese cero lo omitimos; por tanto $tu+(1-t)v$ es una combinación convexa finita de elementos de $S$, luego $tu+(1-t)v\in S_c$. Esto muestra la convexidad.
> >
> > (ii) Es el menor subconjunto convexo que contiene $S$. Evidentemente $S\subset S_c$. Si $C$ es convexo y contiene $S$, entonces cualquier combinación convexa finita de elementos de $S$ pertenece a $C$ por convexidad iterada, luego $S_c\subset C$. De aquí que $S_c$ es la envolvente convexa de $S$.
> 
> [!Proof] Ejercicio 7
> > Sea $S\subset X$ balanceado, es decir, $\lambda S\subset S$ para todo escalar $\lambda$ con $|\lambda|\le 1$. Queremos probar que su cápsula convexa $S_c$ es también balanceada.
> >
> > Tomemos $z=\sum_{i=1}^n\alpha_i x_i\in S_c$ con $x_i\in S$, $\alpha_i\ge0$, $\sum\alpha_i=1$. Para $\lambda$ con $|\lambda|\le1$ se tiene
> > $\lambda z=\sum_{i=1}^n\alpha_i (\lambda x_i)$.
> > Como $S$ es balanceado, $\lambda x_i\in S$ para todo $i$. Los coeficientes $\alpha_i$ siguen siendo no negativos y suman 1, por lo que $\lambda z$ es una combinación convexa de elementos de $S$. Por tanto $\lambda z\in S_c$. Esto prueba que $S_c$ es balanceado.
> >
> > Deducción para espacios topológicos vectoriales localmente convexos (EVTLC): si $U$ es un entorno de $0$ entonces existe un entorno equilibrado y convexo que lo contiene (basta tomar la intersección de un entorno convexo y uno balanceado, o bien tomar la cápsula convexa y el balanceado de $U$; por el resultado anterior la cápsula convexa de un conjunto balanceado es balanceada y convexa). En particular los entornoes de $0$ que son convexos, balanceados (y absorbentes por ser entorno del origen) forman una base de vecindades de $0$ en un EVTLC.
> 
> **Fin**

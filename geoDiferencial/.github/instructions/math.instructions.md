---
applyTo: '**'
---
- Always save answers to files in the Answers folder.
- If the file name is specified, use it. Otherwise, create a filename based on the prompt.
- Always surround latex in single or double $ depending on importance.

Here is a standard formatting you should follow for your answers:

>[!Example] Ejercicio 2
>- **(a)** Hallar las curvaturas principales y la curvatura gaussiana de la superficie de revolución $M$ con curva generatriz $\gamma(t) = (r(t), h(t))$, para los casos particulares en que $\gamma$ es de rapidez unitaria o $h(t) = t$ para todo $t$. Mostrar que los meridianos y paralelos son líneas de curvatura.
>- **(b)** Si $M$ tiene curva generatriz $\gamma(t) = \left(e^{-t^2}, t\right)$, determinar los puntos de $M$ con curvatura gaussiana positiva.
>>[!Proof]-
>>- **(a)**
>>	1. Sea la superficie de revolución parametrizada por $\phi(s,t)=(r(t)\cos s,r(t)\sin s,h(t))$.
>>	2. Derivadas parciales: $\phi_s=(-r\sin s,r\cos s,0)$ y $\phi_t=(r'\cos s,r'\sin s,h')$.
>>	3. El producto vectorial es $\phi_s\times\phi_t=(rh'\cos s,rh'\sin s,-rr')$ y su norma es $W=r\sqrt{r'^2+h'^2}$.
>>	4. Luego el campo normal unitario es $$N(s,t)=\frac{1}{\sqrt{r'^2+h'^2}}(h'\cos s,h'\sin s,-r')$$
>>	5. Derivando respecto de $s$ se obtiene $$N_s=\frac{h'}{\sqrt{r'^2+h'^2}}(-\sin s,\cos s,0)=\frac{h'}{r\sqrt{r'^2+h'^2}}\phi_s$$
>>	6. Derivando respecto de $t$ se obtiene $$N_t=\frac{1}{(r'^2+h'^2)^{3/2}}(r'h''-h'r'')(\cos s,\sin s,\frac{h'}{r'})$$ y en particular $N_t$ es proporcional a $\phi_t$.
>>	7. Esto implica que $\phi_s$ y $\phi_t$ son autovectores del operador de forma $A_{p}=-dN_{p}$.
>>	8. En consecuencia los paralelos (curvas $t=\text{cte}$) y los meridianos (curvas $s=\text{cte}$) son líneas de curvatura.
>>	9. Las curvaturas principales son $k_1=-\frac{h'}{r\sqrt{r'^2+h'^2}}$ y $k_2=\frac{r'h''-h'r''}{(r'^2+h'^2)^{3/2}}$.
>>	10. La curvatura gaussiana es $K=k_1k_2=-\frac{h'(r'h''-h'r'')}{r(r'^2+h'^2)^2}$.
>>	11. Si $\gamma$ es de rapidez unitaria, $r'^2+h'^2=1$ y ademas $2r'r''+2h'h''=(r'^{2}+h'^{2})'=0$ por lo tanto $h''=\frac{-r'r''}{h'}$ 
>>	12. Entonces $k_{1}=- \frac{h'}{r}$ y $k_{2}=r'h''-h'r''$ y $$K=-\frac{h'(r'h''-h'r'')}{r}= -h'\frac{(\frac{-r'^{2}r''}{h'}-h'r'')}{r}=\frac{r''}{r}$$  
>>	13. Si $h(t)=t$, entonces $h'=1$, $h''=0$ y $K=\frac{r''}{r(1+r'^2)^2}$.
>>- **b) $\gamma(t) = (e^{-t^2}, t)$:**
>>	1. Estamos en el caso $h(t)=t$. $r(t) = e^{-t^2}$.
>>	2. Calculamos $r' = -2t e^{-t^2}$ y ademas $r'' = -2 e^{-t^2} + (-2t)(-2t)e^{-t^2} = e^{-t^2}(4t^2 - 2)$.
>>	3. Entonces por (a) la **curvatura Gaussiana** es $$K = \frac{-r''}{r(1+r'^2)^2}$$
>>	4. El signo de $K$ es el signo de $-r''$ (pues $r>0$ entonces el denominador $>0$).Entonces  $$\begin{align}K > 0 & \iff -r'' > 0 \\ & \iff r'' < 0\\ & \iff e^{-t^2}(4t^2 - 2) < 0\\&\iff 4t^2 - 2 < 0\\& \iff  t^2 < 1/2 \\&\iff |t| < \frac{1}{\sqrt{2}}\end{align}$$
>>	5. **Puntos con $K > 0$:** La franja central de la superficie correspondiente a $t \in (-\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}})$.

- Remember to use [!Proof] for the answers to the exercises
- If the question is not a particular exercise. Just create a file to write the answer. If there is a follow up to the same question just add it to the bottom of that file else createa new file.
- Dont give the answer on the chat. Just create (or update) the corresponding file.
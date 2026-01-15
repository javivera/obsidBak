>[!Example] Ejercicio 2
>- **(a)** Hallar las curvaturas principales y la curvatura gaussiana de la superficie de revolución $M$ con curva generatriz $\gamma(t) = (r(t), h(t))$, para los casos particulares en que $\gamma$ es de rapidez unitaria o $h(t) = t$ para todo $t$. Mostrar que los meridianos y paralelos son líneas de curvatura.
>- **(b)** Si $M$ tiene curva generatriz $\gamma(t) = \left(e^{-t^2}, t\right)$, determinar los puntos de $M$ con curvatura gaussiana positiva.
>>[!Proof]-
>>- **(a)**
>>	1. Sea la superficie de revolución parametrizada por $\phi(s,t)=(r(t)\cos s,r(t)\sin s,h(t))$.
>>	2. Derivadas parciales: $\phi_s=(-r\sin s,r\cos s,0)$ y $\phi_t=(r'\cos s,r'\sin s,h')$.
>>	3. Coeficientes de la primera forma fundamental ($E, F, G$):
>>	   $\langle \phi_s, \phi_s \rangle = r^2$.
>>	   $\langle \phi_s, \phi_t \rangle = 0$.
>>	   $\langle \phi_t, \phi_t \rangle = r'^2 + h'^2$.
>>	4. El vector normal unitario es $N = \frac{\phi_s \times \phi_t}{\|\phi_s \times \phi_t\|}$.
>>	   $\phi_s \times \phi_t = (r h' \cos s, r h' \sin s, -r r')$.
>>	   $\|\phi_s \times \phi_t\| = r \sqrt{h'^2 + r'^2}$.
>>	   $N = \frac{1}{\sqrt{r'^2+h'^2}} (h' \cos s, h' \sin s, -r')$.
>>	5. Coeficientes de la segunda forma fundamental ($e, f, g$):
>>	   $e = \langle N, \phi_{ss} \rangle$. $\phi_{ss} = (-r\cos s, -r\sin s, 0)$.
>>	   $\langle N, \phi_{ss} \rangle = \frac{1}{\sqrt{r'^2+h'^2}} (-r h' \cos^2 s - r h' \sin^2 s) = \frac{-r h'}{\sqrt{r'^2+h'^2}}$.
>>	   $f = \langle N, \phi_{st} \rangle = 0$ (pues $\phi_{st} = (-r'\sin s, r'\cos s, 0)$ perpendicular a $N$).
>>	   $g = \langle N, \phi_{tt} \rangle$. $\phi_{tt} = (r''\cos s, r''\sin s, h'')$.
>>	   $\langle N, \phi_{tt} \rangle = \frac{1}{\sqrt{r'^2+h'^2}} (r''h' - r'h'')$.
>>	6. Como $F=f=0$, las curvas coordenadas (meridianos y paralelos) son líneas de curvatura.
>>	7. Curvaturas principales ($k_1 = e/E, k_2 = g/G$):
>>	   $k_1 = \frac{-r h' / \sqrt{r'^2+h'^2}}{r^2} = \frac{-h'}{r\sqrt{r'^2+h'^2}}$.
>>	   $k_2 = \frac{(r''h' - r'h'')/\sqrt{r'^2+h'^2}}{r'^2+h'^2} = \frac{r''h' - r'h''}{(r'^2+h'^2)^{3/2}}$.
>>	8. **Caso $\gamma$ rapidez unitaria:** $r'^2+h'^2=1$.
>>	   Derivando: $2r'r'' + 2h'h'' = 0 \implies r'r'' = -h'h''$.
>>	   $k_1 = \frac{-h'}{r}$.
>>	   $k_2 = r''h' - r'h''$. Usamos $h'h'' = -r'r''$. Si $h' \neq 0$, $h'' = -r'r''/h'$.
>>	      $k_2 = r''h' - r'(-r'r''/h') = \frac{r''h'^2 + r'^2r''}{h'} = \frac{r''(h'^2+r'^2)}{h'} = \frac{r''}{h'}$.
>>	      (Nota: Hay una identidad útil: $r''h' - r'h'' = \dots$. Alternativamente $k_2 = -r''/h'$ o similar.
>>	      Usando $r''h' - r'h''$: $r'r'' + h'h''=0$. Multiplicamos por $h'$: $r'r''h' + h'^2h'' = 0$.
>>	      Multiplicamos $k_2$ por $h'$: $h'k_2 = r''h'^2 - r'h'h'' = r''h'^2 - r'(-r'r'') = r''(h'^2+r'^2) = r''$.
>>	      Entonces $k_2 = r''/h'$ ??
>>	      Espera. $r'r'' = -h'h''$.
>>	      Numerator: $r''h' - r'h''$.
>>	      Si $r'' = -h'h''/r'$, entonces $(-h'h''/r')h' - r'h'' = -h'' (h'^2/r' + r') = -h''/r' (h'^2+r'^2) = -h''/r'$.
>>	      Entonces $k_2 = -h''/r'$.
>>	      Sustituyendo $h'' = -r'r''/h'$, queda $k_2 = -(-r'r''/h')/r' = r''/h'$.
>>	      Wait, let's look at Gaussian Curvature K directly.
>>	      $K = k_1 k_2 = (-h'/r) (r''/h') = -r''/r$.
>>	      Así que $K = -r''/r$.
>>	   
>>	   **Resultado Caso Rapidez Unitaria:**
>>	   $k_1 = -h'/r, k_2 = -h''/r'$. (O equivalentes).
>>	   $K = -\frac{r''}{r}$.
>>	   
>>	9. **Caso $h(t)=t$:**
>>	   $h'=1, h''=0$. $r'^2+h'^2 = 1+r'^2$.
>>	   $k_1 = \frac{-1}{r\sqrt{1+r'^2}}$.
>>	   $k_2 = \frac{r''(1) - r'(0)}{(1+r'^2)^{3/2}} = \frac{r''}{(1+r'^2)^{3/2}}$.
>>	   $K = k_1 k_2 = \frac{-1}{r\sqrt{1+r'^2}} \frac{r''}{(1+r'^2)^{3/2}} = \frac{-r''}{r(1+r'^2)^2}$.
>>	   
>>- **(b) $\gamma(t) = (e^{-t^2}, t)$:**
>>	1. Estamos en el caso $h(t)=t$. $r(t) = e^{-t^2}$.
>>	2. $K > 0 \iff \frac{-r''}{r(1+r'^2)^2} > 0$.
>>	3. Como $r > 0$ y el denominador es positivo, esto equivale a $-r'' > 0 \iff r'' < 0$.
>>	4. Calculamos $r''$:
>>	   $r'(t) = -2t e^{-t^2}$.
>>	   $r''(t) = -2 e^{-t^2} + (-2t)(-2t) e^{-t^2} = (4t^2 - 2)e^{-t^2}$.
>>	5. Condición $r'' < 0$:
>>	   $(4t^2 - 2)e^{-t^2} < 0 \iff 4t^2 - 2 < 0$ (pues exponencial positiva).
>>	   $4t^2 < 2 \iff t^2 < 1/2 \iff |t| < \frac{1}{\sqrt{2}}$.
>>	6. **Puntos con $K > 0$:** La franja central de la superficie correspondiente a $t \in (-\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}})$.

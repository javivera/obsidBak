>[!Definition] Topological manifold
>Let $M$ be a topological space. We say that $M$ is a **topological manifold of dimension $n$** (or **topological $n$-manifold**) if it satisfies:
>- (**Hausdorff**) For every pair of distinct points $p,q\in M$, there exist disjoint open sets $U,V\subseteq M$ such that $p\in U$ and $q\in V$.
>- (**Second-countable**) There exists a countable basis for the topology of $M$.
>- (**Locally Euclidean of dimension $n$**) For every $p\in M$, there exists a neighborhood of $p$ that is homeomorphic to an open subset of $\mathbb{R}^n$. More explicitly, for each $p\in M$ there exist:
>	1. An open set $U\subseteq M$ with $p\in U$,
>	2. an open set $\widehat U\subseteq\mathbb{R}^n$,
>	3. a homeomorphism $\varphi:U\to\widehat U$.

>[!Definition] Coordinate chart
>Let $M$ be a topological $n$-manifold. A **coordinate chart** (or just a **chart**) on $M$ is a pair $(U,\varphi)$, where $U$ is an open subset of $M$ and $\varphi:U\to\widehat U$ is a homeomorphism from $U$ to an open subset $\widehat U=\varphi(U)\subseteq\mathbb{R}^n$. By definition of a topological manifold, each point $p\in M$ is contained in the domain of some chart $(U,\varphi)$. If $\varphi(p)=0$, we say that the chart is centered at $p$. If $(U,\varphi)$ is any chart whose domain contains $p$, it is easy to obtain a new chart centered at $p$ by subtracting the constant vector $\varphi(p)$.
>Given a chart $(U,\varphi)$, we call the set $U$ a **coordinate domain**, or a **coordinate neighborhood** of each of its points. If, in addition, $\varphi(U)$ is an open ball in $\mathbb{R}^n$, then $U$ is called a **coordinate ball**; if $\varphi(U)$ is an open cube, $U$ is a **coordinate cube**. The map $\varphi$ is called a (local) **coordinate map**, and the component functions $(x^1,\ldots,x^n)$ of $\varphi$, defined by $\varphi(p)=(x^1(p),\ldots,x^n(p))$, are called **local coordinates** on $U$. We sometimes write things such as "$(U,\varphi)$ is a chart containing $p$" as shorthand for "$(U,\varphi)$ is a chart whose domain $U$ contains $p$". If we wish to emphasize the coordinate functions $(x^1,\ldots,x^n)$ instead of the coordinate map $\varphi$, we sometimes denote the chart by $(U,(x^1,\ldots,x^n))$ or $(U,(x^i))$.

>[!Example]- Graphs of continuous functions
>Let $U\subseteq\mathbb{R}^n$ be open, and let $f:U\to\mathbb{R}^k$ be continuous. The **graph** of $f$ is the subset of $\mathbb{R}^n\times\mathbb{R}^k$ defined by
>
>$$\Gamma(f)=\{(x,y)\in\mathbb{R}^n\times\mathbb{R}^k:\ x\in U\text{ and }y=f(x)\},$$
>
>with the subspace topology. Let $\pi_1:\mathbb{R}^n\times\mathbb{R}^k\to\mathbb{R}^n$ denote the projection onto the first factor, and let $\varphi: \Gamma(f)\to U$ be the restriction of $\pi_1$ to $\Gamma(f)$:
>
>$$\varphi(x,y)=x,\qquad (x,y)\in\Gamma(f).$$
>
>Because $\varphi$ is the restriction of a continuous map, it is continuous; and it is a homeomorphism with continuous inverse $\varphi^{-1}(x)=(x,f(x))$. Thus $\Gamma(f)$ is a topological manifold of dimension $n$, homeomorphic to $U$ itself. The pair $(\Gamma(f),\varphi)$ is a global coordinate chart, called **graph coordinates**. The same observation applies to any subset of $\mathbb{R}^{n+k}$ defined by setting any $k$ coordinates equal to a continuous function of the other $n$, which vary over an open subset of $\mathbb{R}^n$.
>

>[!Example]- Spheres
>For each integer $n\ge 0$, the unit $n$-sphere $\mathbb{S}^n$ is Hausdorff and second-countable as a topological subspace of $\mathbb{R}^{n+1}$. To show it is locally Euclidean, for each index $i=1,\ldots,n+1$ let $U_i^+$ denote the subset of $\mathbb{R}^{n+1}$ where the $i$th coordinate is positive:
>
>$$U_i^+=\{(x^1,\ldots,x^{n+1})\in\mathbb{R}^{n+1}: x^i>0\}.$$
>
>Similarly, let $U_i^- = \{x\in\mathbb{R}^{n+1}: x^i<0\}$. Let $f:\mathbb{B}^n\to\mathbb{R}$ be the continuous function
>
>$$f(u)=\sqrt{1-\lVert u\rVert^2},$$
>
>where $\mathbb{B}^n$ denotes the open unit ball in $\mathbb{R}^n$. Then for each $i=1,\ldots,n+1$, it is easy to check that $U_i^+\cap \mathbb{S}^n$ is the graph of the function
>
>$$x^i = f(x^1,\ldots,\widehat{x^i},\ldots,x^{n+1}),$$
>
>where the hat indicates that $x^i$ is omitted. Similarly, $U_i^-\cap \mathbb{S}^n$ is the graph of
>
>$$x^i = -\,f(x^1,\ldots,\widehat{x^i},\ldots,x^{n+1}).$$
>
>Thus, each subset $U_i^{\pm}\cap \mathbb{S}^n$ is locally Euclidean of dimension $n$, and the maps
>
>$$\varphi_i^{\pm}: U_i^{\pm}\cap S^n\to\mathbb{B}^n,\qquad \varphi_i^{\pm}(x^1,\ldots,x^{n+1})=(x^1,\ldots,\widehat{x^i},\ldots,x^{n+1}),$$
>
>are graph coordinates for $\mathbb{S}^n$.
>Since each point of $\mathbb{S}^{n}$ is in the domain of at least one of these $2n+2$ charts, $\mathbb{S}^{n}$ is a topological $n$-manifold.

>[!Example]- Projective spaces
>The **$n$-dimensional real projective space** $\mathbb{RP}^n$ (sometimes written $\mathbf{P}^n$) is the set of 1‑dimensional linear subspaces of $\mathbb{R}^{n+1}$, with the quotient topology determined by the natural map $\pi:\mathbb{R}^{n+1}\setminus\{0\}\to\mathbb{RP}^n$ sending a nonzero vector $x\in\mathbb{R}^{n+1}$ to the line $[x]$ spanned by $x$. For each $i=1,\ldots,n+1$, let $\widehat U_i\subset\mathbb{R}^{n+1}\setminus\{0\}$ be the set where $x^i\ne 0$, and let $U_i=\pi(\widehat U_i)\subset\mathbb{RP}^n$. Since $\widehat U_i$ is saturated, $U_i$ is open and $\pi\vert_{\widehat U_i}:\widehat U_i\to U_i$ is a quotient map. Define a map $\varphi_i:U_i\to\mathbb{R}^n$ by
>
>$$\varphi_i\big([x^1,\ldots,x^{n+1}]\big)=\left(\frac{x^1}{x^i},\ldots,\frac{x^{i-1}}{x^i},\frac{x^{i+1}}{x^i},\ldots,\frac{x^{n+1}}{x^i}\right).$$
>
>This is well defined (scaling $x$ by a nonzero constant does not change the ratios) and $\varphi_i\circ\pi$ is continuous, so $\varphi_i$ is continuous by the characteristic property of quotient maps. In fact, $\varphi_i$ is a homeomorphism with inverse
>
>$$\varphi_i^{-1}(u^1,\ldots,u^n)=[u^1,\ldots,u^{i-1},1,u^i,\ldots,u^n].$$
>
>Geometrically, $\varphi_i([x])=u$ means $(u,1)$ is the point where the line $[x]$ intersects the affine hyperplane $x^i=1$. Because the sets $U_1,\ldots,U_{n+1}$ cover $\mathbb{RP}^n$, this shows $\mathbb{RP}^n$ is locally Euclidean of dimension $n$. The Hausdorff and second‑countability properties are standard.

>[!Example]- Product manifolds
>Suppose $M_1,\ldots,M_k$ are topological manifolds of dimensions $n_1,\ldots,n_k$, respectively. The product space $M_1\times\cdots\times M_k$ is Hausdorff and second-countable; to check it is locally Euclidean of dimension $n_1+\cdots+n_k$, fix $(p_1,\ldots,p_k)\in M_1\times\cdots\times M_k$ and choose charts $(U_i,\varphi_i)$ of each $M_i$ with $p_i\in U_i$. The product map
>
>$$\varphi_1\times\cdots\times\varphi_k:\ U_1\times\cdots\times U_k\longrightarrow\mathbb{R}^{n_1+\cdots+n_k}$$
>
>is a homeomorphism onto its image, which is a product open subset of $\mathbb{R}^{n_1+\cdots+n_k}$. Thus $M_1\times\cdots\times M_k$ is a topological manifold of dimension $n_1+\cdots+n_k$, with charts of the form $(U_1\times\cdots\times U_k,\ \varphi_1\times\cdots\times\varphi_k)$.
>

>[!Example]- Tori
>For a positive integer $n$, the **$n$-torus** (plural: tori) is the product space $T^n=S^1\times\cdots\times S^1$ ($n$ copies). By the product-manifold discussion above, $T^n$ is a topological $n$-manifold. (The $2$-torus $T^2$ is usually called simply **the torus**.)
>

>[!Lemma]
>Every topological manifold has a countable basis of precompact coordinate balls.
>>[!Proof]-
>>Let $M$ be a topological $n$-manifold. First consider the special case in which $M$ can be covered by a single chart: suppose $\varphi:M\to \widehat U\subseteq\mathbb{R}^n$ is a global coordinate map, and let $\mathcal{B}$ be the collection of all open balls $B_r(x)\subseteq\mathbb{R}^n$ such that $r$ is rational, $x$ has rational coordinates, and $B_{r'}(x)\subseteq\widehat U$ for some $r'>r$. Each such ball is precompact in $\widehat U$, and $\mathcal{B}$ is a countable basis for the topology of $\widehat U$. Because $\varphi$ is a homeomorphism, it follows that the collection of sets of the form $\varphi^{-1}(B)$ for $B\in\mathcal{B}$ is a countable basis for the topology of $M$, consisting of precompact coordinate balls, with the restrictions of $\varphi$ as coordinate maps.
>>Now let $M$ be an arbitrary $n$-manifold. By definition, each point of $M$ is in the domain of a chart. Because every open cover of a second-countable space has a countable subcover, $M$ is covered by countably many charts $\{(U_i,\varphi_i)\}$. For each coordinate domain $U_i$, the same argument as above gives a countable basis of coordinate balls that are precompact in $U_i$. The union of these countable bases is a countable basis for the topology of $M$. If $V\subseteq U_i$ is one of these balls, then the closure of $V$ in $U_i$ is compact, and because $M$ is Hausdorff, it is closed in $M$. It follows that the closure of $V$ in $M$ equals its closure in $U_i$, so $V$ is precompact in $M$ as well


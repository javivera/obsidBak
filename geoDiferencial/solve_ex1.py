import sympy as sp

t = sp.symbols('t', real=True)
s = sp.symbols('s', real=True)

# Define the curve alpha(t)
# Assuming alpha(t) = e^(t/sqrt(3)) * (cos(t), sin(t), 1)
# This matches the text "et p 3 (cos t; sent; 1)" interpreted as e^{t/sqrt(3)}
expr = sp.exp(t/sp.sqrt(3))
alpha = sp.Matrix([expr * sp.cos(t), expr * sp.sin(t), expr])

print("Alpha(t):")
sp.pprint(alpha)

# 1. Calculate velocity vector alpha'(t)
d_alpha = alpha.diff(t)
print("\nAlpha'(t):")
sp.pprint(d_alpha)

# 2. Calculate speed |alpha'(t)|
speed_sq = d_alpha.dot(d_alpha)
speed = sp.sqrt(speed_sq).simplify()
print("\nSpeed |alpha'(t)|:")
sp.pprint(speed)

# 3. Arc length function s(t) from t=0
# s(t) = integral_0^t |alpha'(u)| du
u = sp.symbols('u', real=True)
speed_u = speed.subs(t, u)
arc_length = sp.integrate(speed_u, (u, 0, t))
print("\nArc length s(t):")
sp.pprint(arc_length)

# 4. Invert to find t(s)
# s = ... -> find t in terms of s
t_s = sp.solve(s - arc_length, t)[0] # Take the real solution
print("\nt(s):")
sp.pprint(t_s)

# 5. Reparametrize beta(s) = alpha(t(s))
beta = alpha.subs(t, t_s)
print("\nBeta(s):")
sp.pprint(beta)

# 6. Calculate Frenet frame for beta(s)
# Tangent T(s) = beta'(s)
T = beta.diff(s)
T.simplify()
print("\nTangent T(s):")
sp.pprint(T)

# Normal N(s) = T'(s) / |T'(s)|
dT = T.diff(s)
dT.simplify()
kappa = sp.sqrt(dT.dot(dT))
kappa = sp.simplify(kappa)
print("\nCurvature kappa(s):")
sp.pprint(kappa)

N = (dT / kappa)
N.simplify()
print("\nNormal N(s):")
sp.pprint(N)

# Binormal B(s) = T(s) x N(s)
B = T.cross(N)
B.simplify()
print("\nBinormal B(s):")
sp.pprint(B)

# Torsion tau(s) = -N'(s) . B(s)
dN = N.diff(s)
dN.simplify()
tau = -dN.dot(B)
tau = sp.simplify(tau)
print("\nTorsion tau(s):")
sp.pprint(tau)

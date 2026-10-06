"""Compare the displayed expansions of Q and J (relevant terms) with the exact model, n=2."""
import sympy as sp, itertools, random
random.seed(3)
n = 2; R = range(n)
Z = sp.symbols('z0:%d' % n); Zb = sp.symbols('zb0:%d' % n)
S = sp.symbols('s0:%d' % n); Sb = sp.symbols('sb0:%d' % n)
w, wb = sp.symbols('w wb')
swap = {}
for a, b in list(zip(Z, Zb)) + list(zip(S, Sb)) + [(w, wb)]:
    swap[a] = b; swap[b] = a
def conj(e):
    e = sp.expand(e)
    return sp.expand(sp.conjugate(e.xreplace(swap)).xreplace({sp.conjugate(x): x for x in swap}))
def rc(): return sp.Integer(random.randint(-3, 3)) + sp.I * random.randint(-3, 3)
Ilist = [I for I in itertools.product(range(4), repeat=n) if 2 <= sum(I) <= 3]
def mono(X, I): return sp.Mul(*[X[i] ** I[i] for i in R])
def minus(I, l):
    L = list(I); L[l] -= 1; return tuple(L)
cflat = {k: rc() for k in itertools.product(R, R, R, R)}
# Hermitian symmetry conj(c_jklm)=c_kjml
c = {}
for (j, k, l, m), val in cflat.items():
    if (j, k, l, m) in c: continue
    if (k, j, m, l) == (j, k, l, m): val = sp.re(val)
    c[(j, k, l, m)] = val; c[(k, j, m, l)] = sp.conjugate(val)
d = {(I, k, m): rc() for I in Ilist for k in R for m in R}
e = {(I, j, k, m): rc() for I in Ilist for j in R for k in R for m in R}
def trunc(ex):
    ex = sp.expand(ex)
    P = sp.Poly(ex, *Z, *Zb); res = 0
    for mon, coef in P.terms():
        if sum(mon[:n]) <= 1 and sum(mon[n:]) <= 1:
            res += coef * sp.Mul(*[x ** p for x, p in zip(list(Z) + list(Zb), mon)])
    return sp.expand(res)
xi = []
for m in R:
    ex = S[m]
    for I in Ilist:
        ex -= (sum(d[(I, k, m)] * Zb[k] for k in R) + sum(e[(I, j, k, m)] * Z[j] * Zb[k] for j in R for k in R)) * w ** (sum(I) - 1) * mono(S, I)
    xi.append(sp.expand(ex))
xib = [conj(x) for x in xi]
h = [[(1 if l == m else 0) - sum(c[(j, k, l, m)] * Z[j] * Zb[k] for j in R for k in R) for m in R] for l in R]
Q = trunc(sum(h[l][m] * xi[l] * xib[m] for l in R for m in R))
Jm = sp.Matrix(n, n, lambda m, l: sp.diff(xi[m], S[l]))
detJ = trunc(Jm.det()); deth = trunc(sp.Matrix(n, n, lambda l, m: h[l][m]).det())
J = trunc(deth * detJ * conj(detJ))
def RE2(x): return x + conj(x)
t = sum(S[i] * Sb[i] for i in R)
Qd = t - sum(c[(j, k, l, m)] * Z[j] * Zb[k] * S[l] * Sb[m] for j in R for k in R for l in R for m in R)
Qd -= RE2(sum(d[(I, k, m)] * w ** (sum(I) - 1) * mono(S, I) * Sb[m] * Zb[k] for I in Ilist for k in R for m in R))
Qd -= RE2(sum(e[(I, j, k, m)] * w ** (sum(I) - 1) * mono(S, I) * Sb[m] * Z[j] * Zb[k] for I in Ilist for j in R for k in R for m in R))
Qd += sum(d[(I, k, m)] * sp.conjugate(d[(J2, j, m)]) * w ** (sum(I) - 1) * wb ** (sum(J2) - 1) * mono(S, I) * conj(mono(S, J2)) * Z[j] * Zb[k]
          for I in Ilist for J2 in Ilist for j in R for k in R for m in R)
Jd = 1 - sum(c[(j, k, l, l)] * Z[j] * Zb[k] for j in R for k in R for l in R)
Jd -= RE2(sum(d[(I, k, m)] * w ** (sum(I) - 1) * I[m] * mono(S, minus(I, m)) * Zb[k] for I in Ilist for k in R for m in R if I[m] > 0))
Jd -= RE2(sum(e[(I, j, k, m)] * w ** (sum(I) - 1) * I[m] * mono(S, minus(I, m)) * Z[j] * Zb[k] for I in Ilist for j in R for k in R for m in R if I[m] > 0))
Jd += sum(d[(I, k, m)] * sp.conjugate(d[(J2, j, l)]) * w ** (sum(I) - 1) * wb ** (sum(J2) - 1) * I[m] * J2[l] * mono(S, minus(I, m)) * conj(mono(S, minus(J2, l))) * Z[j] * Zb[k]
          for I in Ilist for J2 in Ilist for j in R for k in R for m in R for l in R if I[m] > 0 and J2[l] > 0)
# relevant part: drop pure zz / zbzb terms (already truncated) -- compare all remaining
def relevant(ex):
    ex = sp.expand(ex); P = sp.Poly(ex, *Z, *Zb); res = 0
    for mon, coef in P.terms():
        dz = sum(mon[:n]); dzb = sum(mon[n:])
        if (dz, dzb) in [(0, 0), (1, 0), (0, 1), (1, 1)]:
            res += coef * sp.Mul(*[x ** p for x, p in zip(list(Z) + list(Zb), mon)])
    return sp.expand(res)
print('Q diff:', sp.expand(relevant(Q) - relevant(Qd)) == 0)
print('J diff:', sp.expand(relevant(J) - relevant(Jd)) == 0)

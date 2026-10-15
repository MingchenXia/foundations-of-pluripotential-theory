"""Check the identity eq:chern-kernel-square-identity in an exact finite-jet model.

Model at the center z=0: a(z,rho)=z+rho, metric h_{l mbar}=delta-sum c_{jklm} z_j zbar_k,
xi = s - sum_I (sum_k d_{Ikm} zbar_k + sum_{jk} e_{Ijkm} z_j zbar_k) w^{|I|-1} s^I  (exact),
Q=|xi|_h^2, J=det h |det d xi/ds|^2, weight chi(T)=(1-T)^4, chi_1=-(1-T)^5/5.
Psi_p(z,w)=int_{|s|<1} p(z+ws) chi(Q) J ds; compare its joint Levi form at z=0 with
 int P[v+eta s+r^2 Xi]^2 chi + r^2 int P[U - r^2 Xi Xi^*] chi .
"""
import sympy as sp, random, itertools, sys

n = int(sys.argv[1]) if len(sys.argv) > 1 else 1
seed = int(sys.argv[2]) if len(sys.argv) > 2 else 1
random.seed(seed)
K = 4
R = range(n)
Z = sp.symbols('z0:%d' % n); Zb = sp.symbols('zb0:%d' % n)
S = sp.symbols('s0:%d' % n); Sb = sp.symbols('sb0:%d' % n)
V = sp.symbols('v0:%d' % n); Vb = sp.symbols('vb0:%d' % n)
Y = sp.symbols('y0:%d' % n); Yb = sp.symbols('yb0:%d' % n)
w, wb, eta, etab = sp.symbols('w wb eta etab')
swap = {}
for a, b in list(zip(Z, Zb)) + list(zip(S, Sb)) + list(zip(V, Vb)) + list(zip(Y, Yb)) + [(w, wb), (eta, etab)]:
    swap[a] = b; swap[b] = a


def conj(e):
    e = sp.expand(e)
    return sp.expand(sp.conjugate(e.xreplace(swap)).xreplace({sp.conjugate(x): x for x in swap}))


def rc():
    return sp.Integer(random.randint(-3, 3)) + sp.I * random.randint(-3, 3)


# multi-indices with 2<=|I|<=3
Ilist = [I for I in itertools.product(range(4), repeat=n) if 2 <= sum(I) <= 3]
absI = sum


def mono(X, I):
    return sp.Mul(*[X[i] ** I[i] for i in R])


def minus(I, l):
    L = list(I); L[l] -= 1; return tuple(L)


# curvature with Hermitian and Kaehler symmetries: conj(c_jklm)=c_kjml, symmetric in (j,l) and (k,m)
c = {}
for j, k, l, m in itertools.product(R, R, R, R):
    key = (min(j, l), max(j, l), min(k, m), max(k, m))
    c.setdefault(key, None)
base = {}
for (j, l, k, m) in list(c.keys()):
    if (j, l, k, m) in base:
        continue
    conjkey = (k, m, j, l)
    val = rc()
    if conjkey == (j, l, k, m):
        val = sp.re(val)
    base[(j, l, k, m)] = val
    base[conjkey] = sp.conjugate(val)


def cc(j, k, l, m):
    return base[(min(j, l), max(j, l), min(k, m), max(k, m))]


d = {(I, k, m): rc() for I in Ilist for k in R for m in R}
e = {(I, j, k, m): rc() for I in Ilist for j in R for k in R for m in R}

t = sum(S[i] * Sb[i] for i in R)


def trunc(ex):
    ex = sp.expand(ex)
    if ex == 0:
        return ex
    P = sp.Poly(ex, *Z, *Zb)
    res = 0
    for mon, coef in P.terms():
        if sum(mon[:n]) <= 1 and sum(mon[n:]) <= 1:
            res += coef * sp.Mul(*[x ** p for x, p in zip(list(Z) + list(Zb), mon)])
    return sp.expand(res)


xi = []
for m in R:
    ex = S[m]
    for I in Ilist:
        coef = sum(d[(I, k, m)] * Zb[k] for k in R) + sum(e[(I, j, k, m)] * Z[j] * Zb[k] for j in R for k in R)
        ex -= coef * w ** (absI(I) - 1) * mono(S, I)
    xi.append(sp.expand(ex))
xib = [conj(x) for x in xi]
h = [[(1 if l == m else 0) - sum(cc(j, k, l, m) * Z[j] * Zb[k] for j in R for k in R) for m in R] for l in R]

z0 = {**{x: 0 for x in Z}, **{x: 0 for x in Zb}}
Qfull = sum(h[l][m] * xi[l] * xib[m] for l in R for m in R)
Jm = sp.Matrix(n, n, lambda m, l: sp.diff(xi[m], S[l]))
detJ = Jm.det(); deth = sp.Matrix(n, n, lambda l, m: h[l][m]).det()
Jfull = deth * detJ * conj(sp.expand(detJ))
T = sp.Symbol('T')
chi = (1 - T) ** K
chi1 = -(1 - T) ** (K + 1) / (K + 1)
def D0(f, *vs):
    g = f
    for x in vs: g = sp.diff(g, x)
    return sp.expand(g.subs(z0))
c0 = chi.subs(T, t); c1 = sp.diff(chi, T).subs(T, t); c2 = sp.diff(chi, T, 2).subs(T, t)
Qz = {j: D0(Qfull, Z[j]) for j in R}; Qzb = {j: D0(Qfull, Zb[j]) for j in R}
Jz = {j: D0(Jfull, Z[j]) for j in R}; Jzb = {j: D0(Jfull, Zb[j]) for j in R}
dW = {}
for j in R:
    dW[('z', j)] = sp.expand(c1 * Qz[j] + c0 * Jz[j])
    dW[('zb', j)] = sp.expand(c1 * Qzb[j] + c0 * Jzb[j])
    for k in R:
        Qjk = D0(Qfull, Z[j], Zb[k]); Jjk = D0(Jfull, Z[j], Zb[k])
        dW[('zzb', j, k)] = sp.expand(c2 * Qz[j] * Qzb[k] + c1 * Qjk + c1 * (Qz[j] * Jzb[k] + Qzb[k] * Jz[j]) + c0 * Jjk)
    dW[('zwb', j)] = sp.expand(c1 * D0(Qfull, Z[j], wb) + c0 * D0(Jfull, Z[j], wb))
    dW[('wzb', j)] = sp.expand(c1 * D0(Qfull, w, Zb[j]) + c0 * D0(Jfull, w, Zb[j]))
print('Q(0)=|s|^2:', sp.expand(Qfull.subs(z0) - t) == 0, ' w-derivs vanish:', D0(Qfull, w) == 0, D0(Jfull, w) == 0, D0(Qfull, w, wb) == 0, D0(Jfull, w, wb) == 0, flush=True)
W0 = c0
def integrate_ball(ex):
    ex = sp.expand(ex)
    if ex == 0:
        return 0
    P = sp.Poly(ex, *S, *Sb)
    res = 0
    for mon, coef in P.terms():
        a = mon[:n]; b = mon[n:]
        if a == b:
            res += coef * sp.pi ** n * sp.Mul(*[sp.factorial(x) for x in a]) / sp.factorial(n + sum(a))
    return sp.expand(res)


def levi(G):
    out = 0
    for j in R:
        for k in R:
            out += V[j] * Vb[k] * sp.diff(G, Z[j], Zb[k])
        out += V[j] * etab * sp.diff(G, Z[j], wb)
        out += eta * Vb[j] * sp.diff(G, w, Zb[j])
    out += eta * etab * sp.diff(G, w, wb)
    return sp.expand(out.subs({**{x: 0 for x in Z}, **{x: 0 for x in Zb}}))


def rhs(p, variant):
    sub = {**{Y[i]: w * S[i] for i in R}, **{Yb[i]: wb * Sb[i] for i in R}}
    P = [[sp.diff(p, Y[a], Yb[b]).subs(sub, simultaneous=True) for b in R] for a in R]  # P[a][b]=p_{a bbar}
    r2 = w * wb
    chit = chi.subs(T, t); chi1t = chi1.subs(T, t)
    Xi = []
    for m in R:
        val = 0
        for I in Ilist:
            if I[m] == 0:
                continue
            for j in R:
                for l in R:
                    sl = Sb[l] if variant == 'text' else S[l]
                    val += sp.Rational(I[m], absI(I)) * sp.conjugate(d[(I, j, l)]) * wb ** (absI(I) - 2) * sl * conj(mono(S, minus(I, m))) * V[j]
        Xi.append(sp.expand(val))
    Xib = [conj(x) for x in Xi]
    Yv = [V[i] + eta * S[i] + r2 * Xi[i] for i in R]
    Yvb = [conj(x) for x in Yv]
    first = integrate_ball(sum(P[a][b] * Yv[a] * Yvb[b] for a in R for b in R) * chit)
    # U_{ml}, contracted as sum_{m,l} p_{m lbar} U_{ml}; we store U*chi
    Uchi = [[0] * n for _ in R]
    for m in R:
        for l in R:
            val = sum(cc(j, k, l, m) * V[j] * Vb[k] for j in R for k in R)
            for I in Ilist:
                if I[l] == 0:
                    continue
                fl = sp.Rational(I[l], absI(I)) * mono(S, minus(I, l))
                val += 2 * sum(e[(I, j, k, m)] * V[j] * Vb[k] for j in R for k in R) * w ** (absI(I) - 1) * fl
                val += 2 * sum(d[(I, k, m)] * Vb[k] for k in R) * (absI(I) - 1) * w ** (absI(I) - 2) * fl * eta
            ex = -chi1t * val
            ex += chit * sum(d[(I, k, m)] * sp.conjugate(d[(I2, j, l)]) * w ** (absI(I) - 1) * wb ** (absI(I2) - 1)
                             * mono(S, I) * conj(mono(S, I2)) * V[j] * Vb[k]
                             for I in Ilist for I2 in Ilist for j in R for k in R)
            if variant == 'full':
                # extra term: 2 chi_1 * (sum_{k,I,q} v_k dbar_{Ikq} wbar^{|I|-2} (I_m/|I|)(I-1_m)_q sbar^{I-1_m-1_q}) * conj(v_l+eta s_l)
                extra = 0
                for I in Ilist:
                    if I[m] == 0:
                        continue
                    I1 = minus(I, m)
                    for q in R:
                        if I1[q] == 0:
                            continue
                        extra += sum(V[k] * sp.conjugate(d[(I, k, q)]) for k in R) * wb ** (absI(I) - 2) \
                            * sp.Rational(I[m], absI(I)) * I1[q] * conj(mono(S, minus(I1, q)))
                ex += 2 * chi1t * extra * (Vb[l] + etab * Sb[l])
            Uchi[m][l] = sp.expand(ex)
    UH = [[(Uchi[m][l] + conj(Uchi[l][m])) / 2 for l in R] for m in R]
    second = integrate_ball(r2 * sum(P[m][l] * (UH[m][l] - r2 * Xi[m] * Xib[l] * chit) for m in R for l in R))
    return sp.expand(first + second)


def realpoly(deg):
    p = 0
    for a in itertools.product(range(deg + 1), repeat=2 * n):
        if sum(a) > deg or sum(a) < 2:
            continue
        p += rc() * mono(Y, a[:n]) * mono(Yb, a[n:])
    return sp.expand(p + conj(p))



for trial in range(int(sys.argv[3])):
    p = realpoly(int(sys.argv[4]))
    sub = {**{Y[i]: w * S[i] for i in R}, **{Yb[i]: wb * Sb[i] for i in R}}
    ev = lambda e: sp.expand(e.subs(sub, simultaneous=True))
    p0 = ev(p); Py = [ev(sp.diff(p, Y[i])) for i in R]; Pyb = [ev(sp.diff(p, Yb[i])) for i in R]
    Pyyb = [[ev(sp.diff(p, Y[a], Yb[b])) for b in R] for a in R]
    LG = sum(V[j] * Py[j] for j in R) + eta * sum(S[j] * Py[j] for j in R)
    LbG = sum(Vb[j] * Pyb[j] for j in R) + etab * sum(Sb[j] * Pyb[j] for j in R)
    X = [V[a] + eta * S[a] for a in R]; Xb = [Vb[a] + etab * Sb[a] for a in R]
    LLbG = sum(Pyyb[a][b] * X[a] * Xb[b] for a in R for b in R)
    LW = sum(V[j] * dW[('z', j)] for j in R)
    LbW = sum(Vb[j] * dW[('zb', j)] for j in R)
    LLbW = sum(V[j] * Vb[k] * dW[('zzb', j, k)] for j in R for k in R) + sum(V[j] * etab * dW[('zwb', j)] for j in R) + sum(eta * Vb[j] * dW[('wzb', j)] for j in R)
    lhs = integrate_ball(LLbG * W0) + integrate_ball(LG * LbW) + integrate_ball(LbG * LW) + integrate_ball(p0 * LLbW)
    for variant in ['text', 'sfix', 'full']:
        diff = sp.expand(lhs - rhs(p, variant))
        print('n=%d trial %d %-5s' % (n, trial, variant), 'ZERO' if diff == 0 else 'nonzero (%d terms)' % len(sp.Add.make_args(diff)), flush=True)

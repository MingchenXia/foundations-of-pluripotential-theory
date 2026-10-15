# n=1: check that the value term int p(A) LLbar W ds equals r^2 int P [U_1..4] chi ds (text's four terms)
import sympy as sp, random, sys
exec(open(sys.argv[1]).read().split("trials = ")[0].replace("n = int(sys.argv[1]) if len(sys.argv) > 1 else 1","n=1").replace("seed = int(sys.argv[2]) if len(sys.argv) > 2 else 1","seed=5"))
for trial in range(2):
    p = realpoly(6)
    sub = {**{Y[i]: w * S[i] for i in R}, **{Yb[i]: wb * Sb[i] for i in R}}
    # value term: p(A) * LLbar W at z=0, A=z+ws
    A = [Z[i] + w * S[i] for i in R]; Ab = [Zb[i] + wb * Sb[i] for i in R]
    pA = p.subs({**{Y[i]: A[i] for i in R}, **{Yb[i]: Ab[i] for i in R}}, simultaneous=True).subs({Z[0]:0,Zb[0]:0})
    val = integrate_ball(sp.expand(pA*levi(Wt)))
    P = [[sp.diff(p, Y[a], Yb[b]).subs(sub, simultaneous=True) for b in R] for a in R]
    r2=w*wb; chit=chi.subs(T,t); chi1t=chi1.subs(T,t)
    m=l=0
    v_ = sum(cc(j,k,l,m)*V[j]*Vb[k] for j in R for k in R)
    for I in Ilist:
        fl = sp.Rational(I[l], sum(I))*mono(S, minus(I,l))
        v_ += 2*sum(e[(I,j,k,m)]*V[j]*Vb[k] for j in R for k in R)*w**(sum(I)-1)*fl
        v_ += 2*sum(d[(I,k,m)]*Vb[k] for k in R)*(sum(I)-1)*w**(sum(I)-2)*fl*eta
    U = -chi1t*v_ + chit*sum(d[(I,k,m)]*sp.conjugate(d[(I2,j,l)])*w**(sum(I)-1)*wb**(sum(I2)-1)*mono(S,I)*conj(mono(S,I2))*V[j]*Vb[k] for I in Ilist for I2 in Ilist for j in R for k in R)
    U = (U+conj(U))/2
    rhs = integrate_ball(r2*P[0][0]*U)
    print('value term == r^2 int P[U_1..4]:', sp.expand(val-rhs)==0)

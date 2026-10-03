# Remaining arbitrary-submanifold extension proof

Working proof architecture, not a completed theorem or review. Preserve Q07-05 drafting until every step is written and checked. The point/Bergman portion is independently proved; it does not need this larger interface.

## Route through gentle approximations

For an original strict singular metric, use Q06 decreasing gentle potentials Phi_j >= phi with the same strict lower bound up to epsilon_j. On Y, the restricted metric is defined because phi|Y is not identically minus infinity. The original weighted section f is integrable for every Phi_j|Y and the norms are bounded by the original norm. Prove extension first for each gentle analytic metric with one geometry-only curvature threshold N(X,omega,Y) and norm constant C(X,omega,Y). Then holomorphic compactness and Fatou give the original singular metric. This removes the need for a simultaneous perturbed regularization/error-index argument. No projectivity or Stein-complement theorem is imported.

For codimension q=0 the section extends itself. For q>=1 construct R_Y>0 off Y, zero exactly on Y, by a finite squared-cutoff sum of local normal-coordinate squared norms and a positive term away from Y. Normalize R_Y very small. It is comparable to squared normal distance, and on a principalization R_Y pulls back to a divisor monomial times a smooth strictly positive function. Generator comparisons and the Q06 cutoff Hessian calculation should prove both dd^c log R_Y >= -b omega and dd^c log(R_Y+epsilon) >= -b omega, uniformly in epsilon, with b depending only on fixed geometry. Use a squared partition sum equal to one, so addition of epsilon is represented by adding epsilon to every local kernel. The outside chart has a constant kernel and overlaps only where normal generators have a fixed positive lower bound.

## Twisted estimate to prove

For smooth metric h, let a,b be smooth positive functions bounded above/below for the fixed approximation parameter. Apply the proved Bochner identity to the metric a*h. Its adjoint is delta_(a*h)=delta_h-a^{-1}(barpartial a)^*. Expanding cancels the a^{-1} gradient square on the two sides, giving the Bochner inequality with curvature a*iTheta_h-i*partialbarpartial a and a cross term. Bound the cross term below by -b|delta_h v|²-b^{-1}|(barpartial a)^*v|². Thus

  integral <[a*iTheta_h-i*partialbarpartial a-i/b*partial a wedge barpartial a,Lambda]v,v>
  <= integral (a+b)|delta_h v|² + a|barpartial v|².

Use Hilbert spaces H0 with density h/(a+b), H1 with h, H2 with a*h. Then T*= (a+b)*delta_h. Boundedness for the fixed parameter and the existing complete cutoffs give graph density. The Q04 complex-solvability theorem yields correction norm integral |u|² h/(a+b) <= dual curvature energy of g. The (n,1) dual energy is independent of the auxiliary complete metric exactly as in the new Q07 bundle lemma. Do not omit the closed-complex projection step.

Set psi=log R_Y, psi_e=log(epsilon+R_Y), a_e=epsilon-psi_e+log(1-psi_e), b_e=(2-psi_e)², and use metric h*exp(-q*psi). The derivative chi'=-1-1/(1-psi_e), chi''=-1/(1-psi_e)² cancels the gradient loss with b_e. For sufficiently small epsilon, a_e>=1 and -chi' is between 1 and 2. The curvature form dominates a uniform positive omega term plus (epsilon/R_Y)*i*partial psi_e wedge barpartial psi_e if the original curvature exceeds (q+2)b plus the fixed inverse-canonical curvature cost. The rank-one dual estimate for barpartial psi_e wedge G is then <= R_Y/epsilon * |G|². Track the factor 2*pi from the book's dd^c convention.

## Local critical logarithmic gain

Prove on a relatively compact Euclidean product chart, Y={w=0}, for singular psh p and tangential holomorphic data f defined on a larger tangential chart:

  integral |F|² exp(-p) / (|w|^(2q) * (-log|w|²)²)
  <= C * integral_Y |f|² exp(-p).

For a smooth p obtained by radial convolution, add a fixed M|z|² to get sufficient curvature; that only changes bounded factors. Use G(z',w)=f(z'), which is holomorphic on the whole product and smooth on its closure. The cutoff rho(R/epsilon) gives g with no gluing-error term. Its annular dual energy has the smooth limit bounded by the data integral. Complete metrics/cutoffs on the product minus Y can be built from positive boundary potentials -log(r²-|z'|²), -log(r²-|w|²) and -log(-log|w|²); the sum of the positive boundary exhaustion and +log(-log|w|²) is proper, and each gradient is bounded in the chosen metric.

Important: F_e cannot be bounded in the correction's uncapped weight for fixed epsilon, since its nonzero trace makes that weight nonintegrable. Use the capped weight (epsilon+R)^(-q)*(-log(epsilon+R))^(-2). The cutoff G has capped norm O((log epsilon)^(-2)) for a fixed smooth metric. The correction's weight dominates this capped weight because a_e+b_e <= C*(-log(epsilon+R))². Let epsilon tend to zero first, then the convolution radius. Compactness and Fatou preserve the trace and give the singular critical-gain estimate with one geometric constant.

## Initial gluing

For a gentle analytic metric Phi and f integrable on compact Y, strong openness on Y provides one sigma>0 (depending on Phi and f, which is allowed) such that the finitely many local data are integrable for the strengthened local weights (1+sigma)*p. Apply the critical-gain result locally and glue the holomorphic extensions F_i with a smooth partition chi_i summing to one near Y. Set G=sum chi_i F_i, zero away from a neighborhood of Y. It is smooth globally, G|Y=f and barpartial G|Y=0. Both G and barpartial G have finite strengthened critical-gain norm. The derivative is O(sqrt(R_Y)) along Y.

Hölder gives finiteness and decay to zero of
  integral_{R_Y<epsilon} |barpartial G|² exp(-Phi)*R_Y^(-q).
The first Hölder factor is the strengthened critical/log² norm; the other is the unweighted integral |barpartial G|² R_Y^(-q)*|log R_Y|^(2/sigma), finite by first-order normal vanishing. This avoids the invalid assertion that ordinary weighted L2 plus normal vanishing is enough.

## Gentle weighted normal residue — key new proof

Prove that the main annular integral of G with the unstrengthened metric has limsup bounded by C_geometry * integral_Y |f|² h. Use resolution to justify this, rather than the smooth-source Taylor argument under a singular weight.

Blow up Y first (identity in codimension one), with exceptional divisor E and K_(BlY/X)=(q-1)E. Resolve the gentle weight and the ideal of Y with normal-crossing centers. On a final coordinate chart, write Phi=sum a_D log|s_D|²+smooth, R_Y=product |s_D|^(2b_D)*positive smooth, and the volume Jacobian has exponents A_D-1. Each local holomorphic F_i has orders e_D>=0. Strengthened critical/log² integrability forces
  e_D + A_D >= (1+sigma)*a_D + q*b_D if b_D>0,
and a strict inequality if b_D=0. The logarithmic denominator cannot repair a strictly negative power. For a_D>0 the unstrengthened critical density therefore has positive margin sigma*a_D. For a_D=0, every divisor other than the strict transform of E has positive margin as well.

Supply the latter geometric fact explicitly. Since A_D(X)-q*b_D = A_D(BlY)-ord_D(E), the smooth pair (BlY,E) has zero margin on E and strictly positive margin on every other divisor produced by the resolution. Prove this by the smooth-center blowup formula: for a center of codimension c contained in r boundary components, the new margin is c-r plus the sum of their margins. A nontrivial center contained only in E has c>=2; a center meeting previous exceptional components inherits a positive margin; r<=c. No general log-canonical-pair theorem is imported.

After factoring the finitely many active F_i, their smooth partition sum G has the same common monomial lower orders and a smooth remaining coefficient. All density powers except the strict E coordinate are integrable with a positive margin. Charts away from strict E have an integrable critical density, so their shrinking-annulus integral tends to zero. In a strict-E chart, the only borderline factor is |t|^(-2). Integrate it over a unit logarithmic annulus; the other positive-margin factors provide an integrable dominator. Dominated convergence gives the trace density on E. On the initial blowup that trace is |f|² h|Y times the projective normal-direction density. Its fiber integral is bounded by a fixed geometry constant, using R_Y's uniformly positive normal quadratic form. Subsequent resolutions change only a null set and the same trace integral. Treat f=0 separately, where the strict-E order is positive and the residue vanishes. Treat Y of dimension zero separately or use the previously proved point theorem.

## Global correction and final limit

For a gentle metric, solve on X minus its poles and Y, using the complete cutoffs from the sum of the gentle pole potential and log R_Y. Set G_e=rho(R_Y/epsilon)G. Split barpartial G_e into its annular rank-one term and rho*barpartial G. The first is bounded by the residue lemma; the second tends to zero by Hölder. The twisted estimate gives u_e with uniformly bounded correction norm. For fixed epsilon, a_e+b_e is bounded, so u_e has an uncapped critical normal-pole norm. L2 analytic removal makes F_e=G_e-u_e holomorphic across the removed sets. Since u_e=G_e-F_e is smooth after removal and critical-pole integrable, it vanishes on Y away from the analytic poles. Identity on connected Y gives F_e|Y=f everywhere.

The correction norm controls its ordinary h norm uniformly because R_Y^q*(-log R_Y)² is bounded and a_e+b_e <= C*(-log(epsilon+R_Y))². The ordinary h norm of G_e tends to zero. Holomorphic compactness yields a gentle-metric extension with C depending only on geometry. Then the Phi_j limit gives the original metric and the same C. The corollary for T tensor L^k has k0 determined by k*delta-b_T>=N, with the fixed canonical cost included in N. Convert factorial volumes if comparing with the sample's omega powers.

This route still needs every calculation, the residue lemma, constants and local scopes written and directly reviewed. It is not completion evidence.

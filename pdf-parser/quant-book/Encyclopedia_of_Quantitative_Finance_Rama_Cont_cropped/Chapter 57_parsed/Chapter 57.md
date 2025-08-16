# **Expectations Hypothesis**

If the attractiveness of an economic hypothesis is measured by the number of papers which statistically reject it, the expectations theory of the term structure is a knockout [43].

The term expectations hypothesis (EH) stands for numerous statements that link yields, returns on bonds, and forward rates of different maturities and periods. The EH has been the basis of empirical and theoretical work in fixed income following the work of Macaulay [54]. These hypotheses were developed for understanding the returns and yields on long- versus short-term bonds and the time series movements of the term structure. The literature distinguishes between the *pure expectations hypothesis* (PEH), which postulates that (i) expected excess returns on long-term over short-term bonds are zero, (ii) yield term premia are zero, or (iii) forward term premia are zero, from the EH, which postulates that (i) expected excess returns are constant over time, (ii) yield term premia are constant, or (iii) forward term premia are constant over time.

We review the literature related to the EH. We present the different forms of both the PEH and the less strong EH. We show that their mathematical expressions depend on the researchers' choice of model-continuous time versus discrete time-and their choice of frequency of compounding returns-continuous (log-return) *versus* discrete (simple return). Depending on these choices, we may or may not have equivalence among the several forms of the (pure) EH. In addition, we examine which of the statements can be derived from a no-arbitrage general equilibrium model. Lastly, we present empirical evidence against the EH mainly from the US data, and the less strong rejection of the hypotheses when using non-US data.

## Notation

To formulate the different forms of the EH, we need to introduce the basic fixed income assets and concepts associated with them. Even though all the empirical research is done using discrete time models, the theoretical literature predominantly uses continuous time models mainly for tractability

and simplicity reasons. In comparing the expected returns on two bonds of different maturities, however, the returns may be compounded in any of four natural ways: continuously, to the shorter bond's maturity, to the longer bond's maturity, or to the nearest available future date. For these reasons, in the following, we introduce notation that is flexible enough to accommodate the description of discrete as well as continuous time models and all possible ways that compounding may take place.

A zero-coupon bond or discount bond-the simplest fixed income security-promises a single fixed payment at a specified date in the future known as *maturity date.* The size of this payment is called *face* value of the bond. Example of such securities is the Treasury bills, which are bonds issued by the US government with maturities up to a year.

We denote the price of a zero-coupon bond that matures  $\tau \in \mathbb{R}^+$  periods from now and pays 1 unit at maturity as  $P_t^{(\tau)}$ . Call the yield to maturity-compounded once per period-for this zerocoupon bond as  $Y_t^{(\tau)}$ . Then prices and yields are connected through the following equation:

$$P_t^{(\tau)} = \frac{1}{(1 + Y_t^{(\tau)})^{\tau}} \tag{1}$$

It is common in the empirical finance literature to work with log or continuously compounded variables. This has the usual advantage of linearizing exponential affine equations that arise frequently in asset pricing and of defining comparable yield values independent of the remaining horizon value  $\tau$ . Using lowercase letters for logs, the relationship between log yield and log price is

$$y_t^{(\tau)} = -\frac{p_t^{(\tau)}}{\tau} \tag{2}$$

The collection of all these yields for different maturities is called the zero term structure of interest rates. Buying this bond at time  $t$  and reselling it at time  $t + s$  generate a holding period return of

$$R_{t \to t+s}^{(\tau)} = \frac{P_{t+s}^{(\tau-s)}}{P_t^{(\tau)}} = \frac{(1+Y_t^{(\tau)})^{\tau}}{(1+Y_{t+s}^{(\tau-s)})^{\tau-s}} \qquad (3)$$

and a log holding period return of

$$r_{t \to t+s}^{(\tau)} = p_{t+s}^{(\tau-s)} - p_t^{(\tau)}$$
  
=  $s \ y_t^{(\tau)} - (\tau - s)(y_{t+s}^{(\tau-s)} - y_t^{(\tau)})$  (4)

Clearly, the holding period  $s$  cannot exceed the time to maturity  $\tau$ ,  $s < \tau$ . The above equation shows that the holding period return on a zero-coupon bond is not known at time  $t$  unless the holding period coincides with the lifetime of the bond. In this case, the holding period return is the yield to maturity. Otherwise, the return is a random variable that depends on the future evolution of yields.

Even though returns are unknown, bonds can be combined to guarantee a fixed interest rate on an investment to be made in the future; the interest rate on this investment is called a *forward rate*. The forward and log forward rates guaranteed at time  $t$ for an investment made at time  $t + s$  until time  $t + \tau$ where  $s < \tau$  are given as

$$1 + F_t^{(s,\tau)} = \frac{1}{\tau - s} \frac{1}{(P_t^{(\tau)}/P_t^{(s)})}$$
$$= \frac{1}{\tau - s} \frac{(1 + Y_t^{(\tau)})^{\tau}}{(1 + Y_t^{(s)})^s} \tag{5}$$

$$f_t^{(s,\tau)} = \frac{p_t^{(s)} - p_t^{(s)}}{\tau - s} = y_t^{(s)} + \frac{\tau}{\tau - s} (y_t^{(\tau)} - y_t^{(s)})$$
(6)

Finally, the short-term interest rate is the limit of yields to maturity as maturity approaches,  $r_t =$  $\lim_{\tau \downarrow 0} y_t^{(\tau)}$ .

# **Bond Pricing**

Bonds are usually priced with the use of the socalled *risk-neutral probability measure*  $\mathbb{Q}$ , which is equivalent to the *true* or *physical* or *data-generating* measure  $\mathbb{P}^{a}$ . The pricing under  $\mathbb{P}$  is done with the use of a pricing kernel  $M$ , which is the result of the no-arbitrage assumption. For an asset that promises payoff  $S(T)$  at time T, its price now at time t is given by the expected discounted cash flows equation:

$$S(t) = \mathbb{E}_{t}^{\mathbb{P}} \left[ \frac{M(T)}{M(t)} S(T) \right] \tag{7}$$

It can be shown that given the shocks of the economy  $dz(t)$ , M takes the following form:

$$\frac{\mathrm{d}M(t)}{M(t)} = -r(t)\,\mathrm{d}t - \Lambda(t)^{\top}\mathrm{d}z(t) \tag{8}$$

and the two measures  $\mathbb{P}$  and  $\mathbb{Q}(\Lambda)$  are connected through the Radon-Nikodym derivative

$$\frac{\mathrm{d}\mathbb{Q}(\Lambda)}{\mathrm{d}\mathbb{P}} = \xi_T^{\Lambda} = \exp\left(-\frac{1}{2}\int_0^T \Lambda(s)^{\top} \Lambda(s) \mathrm{d}s - \int_0^T \Lambda(s) \mathrm{d}s\right) \tag{9}$$

This gives rise to the following pricing equation under both measures:

$$S(t) = \mathbb{E}_{t}^{\mathbb{P}}\left[\frac{M(T)}{M(t)}S(T)\right] = \mathbb{E}_{t}^{\mathbb{Q}}\left[e^{-\int_{t}^{T}r(s)\mathrm{d}s}S(T)\right]$$
(10)

Easy manipulations of the above equation can prove that under  $\mathbb{Q}$ , the instantaneous expected returns for all assets are equal to the risk-free rate. For this reason, the measure  $\mathbb{Q}$  is also called the *risk-neutral measure.* Specializing the above equation for a zerocoupon bond that matures at time  $t + \tau$  and promises a payoff of  $$1$  gives

$$P_t^{(\tau)} = \mathbb{E}_t^{\mathbb{P}} \left[ \frac{M(T)}{M(t)} \right] = \mathbb{E}_t^{\mathbb{Q}} \left[ e^{-\int_t^T r(s) \mathrm{d}s} \right] \tag{11}$$

From the above pricing equations, we observe that the key variables that govern the bond prices dynamics are (i) the interest rate  $r(t)$  and (ii) the prices of risk  $\Lambda(t)$ . Different assumptions about the functional form of these variables imply different data-generating processes for bond yields. A large part of the current fixed income literature is devoted to studying these different models and the goodness of fitting the raw bond yield data crossectionally and in time series. We examine below the features of the most representative bond pricing models.

## The Expectations Hypothesis

The term *expectations hypothesis* stands for numerous statements that link yields, returns on bonds, and forward rates of different maturities and periods. It is important to note that initially, starting with Hicks [49], Lutz [53], and Macaulay [54], these statements were not formally derived from any fully specified equilibrium model, but rather merely hypothesized. For this reason, the term *expectations hypothesis* is not associated with only one mathematical statement.

These hypotheses were developed for understanding the returns and yields on long- versus short-term bonds, and the time series movements of the term structure. Later, researchers developed theoretical models that give rise to some of the hypothesized equations associated with the EH [20, 21, 27, 57].

The literature distinguishes between the PEH, which postulates that (i) expected excess returns on long-term over short-term bonds are zero, (ii) yield term premia are zero, or that (iii) forward term premia are zero, from the EH, which postulates that (i) expected excess returns are constant over time, (ii) yield term premia are constant, or (iii) forward term premia are constant over time. In the following, all the forms of the PEH in discrete time with discrete and continuous compounding and in continuous time (continuous compounding) are presented. We will see that the PEH expressions derived in all these models are not equivalent across models as well as within each model.

# **Pure Expectations Hypothesis in Discrete** Time

## Discrete Compounding

The first form of the PEH equates the expected returns on one-period (short-term) and  $n$ -period (long-term) bonds, or equivalently, expected excess returns on long-term over short-term bonds are zero:

$$(1 + Y_t^{(1)}) = \mathbb{E}_t^{\mathbb{P}} \left[ 1 + R_{t \to t+1}^{(n)} \right]$$
  
=  $\left( 1 + Y_t^{(n)} \right)^n \cdot \mathbb{E}_t^{\mathbb{P}} \left[ \left( 1 + Y_{t+1}^{(n-1)} \right)^{-n+1} \right]$   
(12)

The second form of the PEH equates the  $n$ -period expected returns on the one-period and  $n$ -period bonds, or equivalently, yield term premia are zero<sup> $b$ </sup>:

$$\left(1 + Y_t^{(n)}\right)^n = \mathbb{E}_t^{\mathbb{P}} \left[ \left(1 + Y_t^{(1)}\right) \left(1 + Y_{t+1}^{(1)}\right) \cdots \left(1 + Y_{t+n-1}^{(1)}\right) \right] \tag{13}$$

The third form of the PEH equates the expected future one-period spot rate with the current forward rate of that future period, or equivalently, forward term premiag are zero $^{\rm c}$ :

$$1 + F_t^{(n-1,n)} = \frac{(1 + Y_t^{(n)})^n}{(1 + Y_t^{(n-1)})^{n-1}} = \mathbb{E}_t^{\mathbb{P}} \left[ 1 + Y_{t+n-1}^{(1)} \right]$$
(14)

The last form of the PEH equates the  $n$ -period bond return with the one-period bond and  $n-1$  period bond:

$$\left(1 + Y_t^{(n)}\right)^n = \left(1 + Y_t^{(1)}\right) \mathbb{E}_t^{\mathbb{P}} \left[ \left(1 + Y_{t+1}^{(n-1)}\right)^{n-1} \right] \tag{15}$$

Even though the above expressions describe different forms of the PEH, they are not mutually equivalent. Assuming that the above expressions are true for all  $t$  and  $n$ , it can be shown that (i) equation  $(13)$  is equivalent to equation  $(15)$ , (ii) equation (14) implies equation (13) (therefore equation (15)), but the opposite is not true unless we make the additional assumption that  $\left(1 + Y_{t+j}^{(1)}\right)_{j=1}^{\infty}$  are uncorrelated with each other, and (iii) equations (12) and  $(15)$  are inconsistent, because the expected value of the inverse of a random variable is not in general equal to the inverse of its expected value.

To summarize, the PEH cannot hold in both its one-period form and its  $n$ -period form, and, essentially there are three different (competing) forms of the PEH in discrete time, the excess return expression  $(12)$ , the yield premia expression  $(13)$ , and the forward premia expression  $(14)$ .

Imposing more structure in the term structure model by assuming that the interest rate is lognormal and homoscedastic, we can quantify the effect of Jensen's inequality. Under this additional assumption, the excess one-period bond returns under the different hypotheses can be shown to be of  $\frac{1}{2}\text{Var}[r_{t\rightarrow t+1}^{(n)}$  $y_t^{(1)}$ ] order. Therefore, the difference between the oneperiod excess bond returns of different PEH forms is Var[ $r_{t \to t+1}^{(n)} - y_t^{(1)}$ ]. Using sample means and standard deviations, we can get an estimate and a standard error of the above quantity. This magnitude is very small for short-term bonds and becomes significant only for long-term bonds; hence, the differences between different forms of the PEH are small except for very long term zero-coupon bonds. Thus, the data reject all forms of the PEH at the short end, but reject no forms of the PEH at the long end of the term structure. In this sense, the distinction between the different forms of the PEH is not critical for evaluating this hypothesis.

#### Continuous Compounding

Most empirical research, though, uses neither of the above PEH forms, but a log form of them. Once the PEH is formulated in logs, all the forms of the PEH become equivalent. Using log returns, the counterparts of equations  $(12)$ ,  $(13)$ , and  $(14)$  are

$$y_t^{(1)} = \mathbb{E}_t^{\mathbb{P}}[r_{t \to t+1}^{(n)}]$$
(16)

$$y_t^{(n)} = (1/n) \sum_{i=0}^{n-1} \mathbb{E}_t^{\mathbb{P}}[y_{t+i}^{(1)}]$$
 (17)

$$f_t^{(\tau-1,\tau)} = \mathbb{E}_t^{\mathbb{P}}[y_{t+\tau-1}^{(1)}]$$
(18)

The empirical literature uses equations  $(17)$  and  $(18)$  in order to construct two related notions of term premia that have played a prominent role in the literature of expected bond returns: the yield premium,

$$c_t^{(n)} \equiv y_t^{(n)} - \frac{1}{n} \sum_{i=0}^{n-1} \mathbb{E}_t^{\mathbb{P}}[y_{t+i}^{(1)}]$$
(19)

and the forward term premium,

$$p_t^{(n)} \equiv f_t^{(n,n+1)} - \mathbb{E}_t^{\mathbb{P}}[y_{t+n}^{(1)}]. \tag{20}$$

Derivations of PEH- and EH-tested formulas follow below.

# **Pure Expectations Hypothesis in Continuous Time**

 $\text{Cox } et al.$  [27] restate the PEH forms in continuous time and prove that the different forms are incompatible. The equivalent of expression  $(12)$  in continuous time is created by assuming that the holding period is the shortest possible, that is, infinitesimal. In this case, the PEH takes the following form:

$$\frac{\mathbb{E}_t^{\mathbb{P}}[dP_t^{(\tau)}]}{P_t^{(\tau)}} = r(t) \,\mathrm{d}t \tag{21}$$

This expression states that all bonds have the same expected infinitesimal return, equal to the shortterm interest rate. However, the above expression is

also known to hold under  $\mathbb{Q}$ ; under the risk-neutral measure, all assets have the same expected return, equal to the risk-free rate. This implies that this form of the PEH postulates that  $\mathbb{P} = \mathbb{Q}$ . The expression's  $(13)$  continuous time equivalent is

$$\frac{1}{P_t^{(\tau)}} = \mathbb{E}_t^{\mathbb{P}} \left[ e^{\int_t^{t+\tau} r(s) \, ds} \right] \tag{22}$$

This statement equates the guaranteed return from holding any zero-coupon bond to maturity with the total return expected from rolling over a series of short-term period bonds. The continuous time equivalent of equation  $(14)$  is

$$\frac{-\partial P_t^{(\tau)}/\partial \tau}{P_t^{(\tau)}} = \mathbb{E}_t^{\mathbb{P}} \left[ r(t+\tau) \right] \tag{23}$$

The left-hand side of the equation is the current infinitesimal forward rate at time  $t + \tau$ , and the right-hand side is the expected future spot rate at  $t + \tau$ . Integrating the last equation and applying the boundary condition  $P_t^{(0)} = 1$  gives

$$-\ln[P_t^{(\tau)}] = \int_t^{t+\tau} \mathbb{E}_t^{\mathbb{P}} \left[r(s)\right] \, \mathrm{d}s \tag{24}$$

Formulating the PEH in continuous time makes the pairwise incompatibility of equations  $(21)$ ,  $(22)$ , and  $(24)$  transparent. If we define the random variable  $\tilde{X} \equiv \exp\left(-\int_{t}^{t+\tau} r(s) \, ds\right)$ , then these equations can be rewritten as

$$P = \mathbb{E}_t^{\mathbb{P}}[\tilde{X}] \tag{25}$$

$$P^{-1} = \mathbb{E}^{\mathbb{P}}_{\cdot}[\tilde{X}^{-1}] \tag{26}$$

$$\ln(P) = \mathbb{E}_t^{\mathbb{P}}[\ln \tilde{X}] \tag{27}$$

By invoking Jensen's inequality, one can show that the yields to maturity implied from equations (21),  $(22)$ , and  $(24)$  satisfy the relationship (with some abuse of notation):

$$y_t^{(\tau)(21)} \le y_t^{(\tau)(22)} \le y_t^{(\tau)(24)} \tag{28}$$

In this model, it is also easy to see that the expected excess returns are positive in all hypotheses except in equation  $(21)$ .

Perhaps the most impacting result of Cox et al.  $[27]$  is the characterization of the PEH forms that can be the result of a (no-arbitrage) equilibrium model. They examine whether there exist pricing kernels (i.e., prices of risk) that can satisfy the resulting pricing PDE in the economy and at the same time satisfy the form of the PEH under examination. They conclude that only equation  $(21)$  can be sustained by an equilibrium model. By definition, equation (21) implies that  $\mathbb{Q} = \mathbb{P}$ ; therefore, selecting  $\Lambda(t) = \mathbf{0}$ gives rise to a valid pricing kernel. Cox et al. [27] prove that the other forms do not give rise to a valid pricing kernel. However, McCulloch [57] later showed that their claim is incorrect. Working in generalizing a preexisting discrete time model to continuous time, he shows that there exists an equilibrium economy that also gives rise to equation  $(23)$ .

## **Expectation Hypothesis**

As described above, the difference between the EH and the PEH is that the term premia under the PEH are assumed to be zero, whereas under the EH they are assumed to be constant. Therefore, to formulate the different forms of the EH we need to add in each form of the PEH a constant term that depends only upon the remaining time to maturity of the corresponding bond considered in each form of the EH.

Even though the different forms of the PEH are generally incompatible, Campbell [21] showed that the different forms of the EH are not incompatible and he derived a general equilibrium model that sustained several forms of the EH at the same time. His model is set up in continuous time. In addition, special cases of the models examined in  $[16]$  and  $[47]$ provide equilibrium models that give rise to constant term premia [36].

Next, we show the most commonly tested equations of the EH in the literature.

## **Tests of the Expectations Hypothesis**

The EH has been under scrutiny at least since the work of Macaulay [54]. In this study, Macaulay emphasizes the low (given the EH is true) correlation between forward rates and subsequent spot rates. Since then, the EH has been tested in hundreds of studies, and in all of them-with only few exceptions-has been rejected. Some of the early papers that test the EH are those of Sutch [74], Shiller [69, 70, 71], Modigliani and Shiller [59], Sargent [67, 68]. Fama [39, 40] and Fama and Bliss [41] also present challenges of the EH where they find evidence of rich patterns of variation in expected returns across time and maturities. Keim and Stambaugh [50], Fama and French [42], and Campbell and Ammer [23] show that yield spreads help to forecast excess return on bonds as well as on other long-term assets.

Perhaps the most widely cited tests of the EH are the Campbell and Shiller [24] regressions based on the equations:

$$\mathbb{E}_{t}^{\mathbb{P}}\left[y_{t+m}^{(n-m)} - y_{t}^{(n)}\right] = \alpha_{nm} + \frac{m}{n-m}(y_{t}^{(n)} - y_{t}^{(m)})\tag{29}$$

which are a more general form of the regressions in [30] based on the following equations:

$$\mathbb{E}_{t}^{\mathbb{P}}\left[y_{t+1}^{(n-1)} - y_{t}^{(n)}\right] = \alpha_{n1} + \frac{1}{n-1}(y_{t}^{(n)} - r_{t}) \quad (30)$$

that are used to assess the goodness of fit of the different term structure models. The derivations of the above equations are shown in detail in the above-mentioned papers and in [73]. In short, from equation  $(4)$  we have that the one-period excess bond continuously compounded return is equal to

$$\mathbb{E}_{t}^{\mathbb{P}}\left[r_{t \to t+1}^{(n)} - r_{t}\right] = -(n-1)\mathbb{E}_{t}^{\mathbb{P}}\left[y_{t+1}^{(n-1)} - y_{t}^{(n)}\right] + (y_{t}^{(n)} - r_{t}) \tag{31}$$

and, it can also be shown that it is equal to

$$\mathbb{E}_{t}^{\mathbb{P}}\left[r_{t \to t+1}^{(n)} - r_{t}\right] = -(n-1)\mathbb{E}_{t}^{\mathbb{P}}\left[c_{t+1}^{(n-1)} - c_{t}^{(n)}\right] + p_{t}^{(n-1)} \tag{32}$$

where  $c_t^{(n)}$  and  $p_t^{(n)}$  are the yield and forward premia defined in equations  $(19)$  and  $(20)$ , respectively. The last expression implies that if the PEH holds (i.e.,  $c_t^{(n)} = 0, p_t^{(n)} = 0$ ) then the expected excess returns are zero, whereas if the EH holds (i.e.,  $c_t^{(n)} = c(n)$ ,  $p_t^{(n)} = p(n)$ , then the expected excess returns are constants that depend on the time to maturity  $n$ . Combining equations (31) and (32) gives rise to equation (30), the well-known LPY regressions of Dai and Singleton [30].

Campbell and Shiller [24] and Dai and Singleton [30], among others, document the failure of both the regressions  $(31)$  and  $(32)$ , which are true under the EH. According to these equations, the coefficients of the nonconstant terms when regressing  $y_{t+m}^{(n-m)} - y_t^{(n)}$  onto  $\frac{m}{n-m}(y_t^{(n)} - y_t^{(m)})$ , or  $\frac{1}{n-1}(y_t^{(n)} - r_t)$  if  $m = 1$ , should be equal to unity. Not only are the estimated coefficients not unity but also they are often statistically significantly negative, particularly for large  $n$ . This means that the EH fails more significantly for long-term bonds. The intuition of the EH is that increases in the slope of term structure  $(y_t^{(n)} - r_t)$  reflect expectations of rising future short spot rates. For the "buy an  $n$ -period bond and hold it to maturity" investment strategy to match, on average, the returns from rolling over short rates in a rising short rate environment, the price of the long bond should decrease such that the yield increases  $(y_{t+1}^{(n-1)} > y_t^{(n)})$ . The regression results suggest that the slope of the yield curve does not even forecast correctly the direction of the changes in the long-bond yields. The underreaction of long rates to spread term changes has also been the study in [56]. Elaborating and further documenting this underreaction, Campbell [22] finds that yield spreads do not forecast short-run changes in long yields (against EH) but do forecast long-run changes in short yields (consistent with EH).

Backus *et al.* [7] tested the EH by running regressions based on analogous equations for the forward rates:

$$\mathbb{E}_{t}^{\mathbb{P}}\left[f_{t+1}^{(n-1,n)} - r_{t}\right] = \alpha + (f_{t}^{(n-1,n)} - r_{t}) \qquad (33)$$

They also find that the regression coefficients of  $(f_t^{(n-1,n)} - r_t)$  are not unity as the null hypothesis sets, but slightly less than one and significantly different than one. They also show that the small differences of the estimated coefficients with unity in the above regressions do not constitute separate or weaker findings against the EH than the deviations of the Campbell-Shiller coefficients from unity, but are actually the same. They constructed a one-factor model and showed that the small differences in the coefficients of the Backus *et al.*  $[7]$  regressions from their null value translate into large negative values for the Campbell–Shiller coefficients.

Similar to the above forward regressions are the forward term regressions tested in  $[43, 72]$  Shiller et al. [72] use a log-linearized model [70, 71] that allows them to test several models of the EH without having to use discount rates (which are easily available for maturities up to a year, but for longer maturities the rates have to be constructed using spline methods) but with the use of the easily observable coupon-bond yields. One of their regressions is based on the EH equation:

$$\mathbb{E}_{t}^{\mathbb{P}}\left[y_{t+m}^{(n-m)} - y_{t}^{(m)}\right] = \alpha_{n,m} + (f_{t}^{(m,n)} - y_{t}^{(m)}) \quad (34)$$

Using coupon-bond yields does not change the results that future bond yield changes cannot be predicted by the current term spread of forward spread. Still, even the direction cannot be predicted correctly. They suggest time-varying risk premia as a plausible solution to the failure of the EH. Froot [43] also tests the same equation trying to understand whether its failure is the result of time varying term premia or that expected future spot rates under- or overreact to changes in short rates. He finds that for short maturities its failure is due to variation in term premia, but this is not true for long maturities.

A recent paper that has received a lot of attention is Cochrane and Piazzesi [26]. Cochrane and Piazzesi [26] have revisited the forecasting regressions of Fama and Bilss using the term structure of forward rates instead of a single forward rate. Their most notable finding is that the coefficients from regressing excess bond returns over one year onto the one year forward rates for the next five years exhibit a tentlike shape for all maturity bonds. The tentlike shape similarities for all bond maturities suggest that a single common factor may be underlying the predictability of excess bond returns for all maturities. Another very interesting fact in [26] is the high  $R^2$ s generated in the above regressions. The  $R^2$ s range between 36% and 39%. This is substantially more predictability than in [41] using a single forward factor.

A series of other papers have also examined alternative reasons for the failure of the EH: Mankiew and Miron [55] find that interest rate movements were more predictable before the founding of the Federal Reserve in 1913, and the downward bias appears to be smaller in that period. Campbell and Ammer [23] emphasize that long-term bond yields vary primarily in response to changing expected inflation. Rudebusch [65] argues that contemporary Federal Reserve operating procedures lead to predictable interest rate movements in the very short run and the very long run, but tend to smooth away predictable movements in the medium run. Balduzzi et al. [8] argue that spreads between short-term rates and the overnight federal reserve funds rate are mainly driven by expectations of changes in the target, and not by the transitory dynamics of the overnight rate around the target. Hence, the bias in tests of the EH that they document can be mainly attributed to the erroneous anticipation of future changes in monetary policy.

Several studies have examined the small-sample bias of the regression coefficients. Bekaert and Hodrick [10] argue that the past use of large sample critical regions, instead of their small-sample counterparts, may have overstated the evidence against the expectations theory. They find that the evidence against the EH for these interest rates and exchange rates is much less strong than under asymptotic inference. Other studies, though, such as Backus *et al.* [7] and Bekaert, Hodrick, and Marshall [11], find that the small-sample properties of the regressions like the ones shown in this article are actually biased upward; this means the *true* Campbell–Shiller coefficients are more negative than the ones estimated in the regressions, heightening the puzzle related with the failure of the EH.

Researchers have also looked at the validity of the EH outside the United States. The tendency in these studies is to find Campbell–Shiller coefficients that are less than zero but less negative than the US data results. Some of those studies that are done primarily for European countries and show mixed results are Bekaert and Hodrick [10], Boero and Torricelli [14], Evans [37], Gerlach and Smets [44], Hardouvelis [48], Kugler [51].

# **Conclusion**

The EH constitutes several hypotheses that were generated to understand bond returns and their yields through the help of other maturity bond returns or investment strategies and forward rates. We showed that these hypotheses can be formulated in many different ways and using different models (continuous time *vs* discrete and continuous compounding *vs* discrete). The different hypotheses are not equivalent. Therefore to test the validity of the EH numerous different expressions have to be tested.

The consensus is that the EH fails in the US data. Its failure, though, is less strong or mixed for the non-US data. Researchers challenging and trying to understand the failure of the EH have hinted on different reasons that may give rise to time-varying expected excess returns on bonds. Even though the understanding of the failure of the EH is not complete, part of the literature is devoted to creating models that better capture this failure and that better replicate the data.

In this strand we can put the papers of reduced form (affine or nonaffine, with macro or without macrovariables) term structure models, such as Ahn *et al.* [1], Ang and Bekaert [2], Bansal and Zhou [9], Bikbov and Chernov [12, 13], Buraschi *et al.* [17], Dai and Singleton [29, 30, 32], Diebold *et al.* [33], Duarte [34], Evans [38], Leippold and Wu [52], and Naik and Lee [59], and, those of the structural form models with or without macrovariables, such as, Ang *et al.* [3, 6], Ang and Piazzesi [4, 5], Brandt and Wang [15], Buraschi and Jiltsov [18, 19], Dai [28], Greenwood and Vayanos [45], Guibaud *et al.* [46], Piazzesi [62], Piazzesi and Schneider [63], Rudebusch and Wu [65, 66], Vayanos and Vila [75], and Wachter [76].

# **Acknowledgments**

The author thanks Aggie Moon for providing research assistantship. The author takes the responsibility for errors if any.

# **End Notes**

a*.* Cochrane [25], Dai and Singleton [31], Duffie [35], Nielsen [60], Piazzesi [61], Singleton [73].

b*.* In the EH literature the term *yield premium* is used to denote the difference of the *n*th root of the terms in the left- and right-hand side of equation (13).

c*.* In the EH literature the term *forward premium* is used to denote the difference of the terms in the left- and right-hand side of equation (14).

# **References**

- [1] Ahn, D.-H., Dittmar, R.F. & Gallant, A.R. (2002). Quadratic term structure models: theory and evidence, *Review of Financial Studies* **15**, 243–288.
- [2] Ang, A. & Bekaert, G. (2002). Regime switches in interest rates, *Journal of Business and Economic Statistics* **20**, 163–182.
- [3] Ang, A., Dong, S. & Piazzesi, M. (2007). *No-Arbitrage Taylor Rules*, National Bureau of Economic Research.
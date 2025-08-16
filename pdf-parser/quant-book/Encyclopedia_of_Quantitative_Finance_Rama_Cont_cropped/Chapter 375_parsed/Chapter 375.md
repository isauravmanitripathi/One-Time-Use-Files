# **Modigliani-Miller** Theorem

The Modigliani-Miller theorem states that the value of a firm is invariant with respect to its leverage policy in an arbitrage-free market when there is no corporate income tax and no bankruptcy cost. Modigliani and Miller  $(M-M)$  [10] proved this "invariance" result using, for the first time, a "no-arbitrage" condition.

To present the M-M theorem, we consider a simple levered firm in which there are two basic claimants on the firm's income:

- debt holders, whose security allows them to claim the coupon  $C$  at each time  $t$  as long as default is not declared;
- equity holders (the owners of the firm), whose security allows them, once debt holders have been paid, to claim the residual cash flow (if positive) as dividends.

Debt holders are paid *before* equity holders, but their claim does not allow them to receive more than the coupon, no matter what the net result is. On the contrary, dividends received by equity holders may be very high when the net result is very high but can also be very low (and even null) when the net result is very low. Equity holders are frequently called the residual claimant since they own the residual income (i.e., the net result) of the firm, that is, what remains when employees, debt holders, and government have been paid.

Let  $E^l$  and B be the market value of equity and debt, respectively, of a given firm at some point in time. To become the owner of this (levered) firm, an investor must buy not only the equity  $E^l$  but also the debt of the firm, so that the total payment is equal to  $V^l = E^l + B$ , where  $V^l$  is called the *value of the* firm. It is thus tempting to think that if we increase B, the value of the firm  $V^l$  will also increase. Finding the conditions under which debt affects the value of the firm is the central question of  $M-M$  analysis: given a *fixed* investment policy, what are the condition(s) under which debt does not affect the value of the firm?

## **Basic Statement of the Theorem**

Consider a firm that has invested in some productive asset, which allows it to generate an operating income (i.e., the earning before interests and taxes  $(EBIT)$ )  $X_t$  at each time t. Roughly speaking,  $X_t$  is equal to the value of the sales minus production costs. When positive,  $X_t$  is used to pay debt holders (coupon), government (tax), and equity holders (dividends).

## Unlevered Firm

In this case, the value of the firm at time  $t$  is denoted by  $v_t$ , and is simply equal to the net result, that is,

$$v_t = X_t (1 - T_a) \tag{1}$$

where  $T_a$  is the corporate tax income.

Let  $C$  be the coupon of the corporate debt and  $T$ be the maturity of the debt. In what follows, we not only consider the case of a *perpetual debt* so that  $T$  is infinite but we also assume that each firm distributes all the residual income (or cash flow) as dividends to equity holders. This thus implies that the firm does not have any cash reserve that it can use when the EBIT is not enough to pay the coupon C. Let  $v^l$  be the value of the levered firm at a given time  $t$ . We now compute  $v_t^l$  under various scenarios.

#### Levered Firm-No Default Risk

We say that a perpetual corporate debt is risk-free if the coupon  $C$  is paid at each time  $t$  to debt holders with probability one. Since the debt is riskfree, the net result  $(X_t - C)(1 - T_a)$  is positive with probability one.<sup>a</sup> The value of the levered firm at time  $t$  is thus equal to

$$v_t^l = C + (X_t - C)(1 - T_a) = X_t(1 - T_a) + T_aC$$

$$= v_t + T_a C \tag{3}$$

The value of the levered firm is equal to the value of the unlevered firm  $v_t$ , plus the value of the taxshield  $T_aC$ , which comes from the fact that interest expenses are tax-deductible. In the particular case in which  $T_a = 0$ , we thus have the following equality:

$$v_t^l = v_t = X_t \tag{4}$$

When there is no corporate income tax, the value of the levered firm (at time  $t$ ) is equal to the value of the unlevered one (at time  $t$ ), that is, the value of the firm is invariant with respect to  $C$  as long as the coupon implies no default risk. This is the  $M-M$ theorem without default risk.

#### Levered Firm—Default Risk

We say that the corporate bond is risky if there is a positive probability that the coupon will not be paid to debt holders at some time  $t$ . Since all the residual income is distributed to equity holders as dividends, there are no available retained earnings so that default is declared at the first time for which  $X_t < C$ . Note importantly that in a default<sup> $b$ </sup> situation

- debt holders have an unconditional right to be paid before equity holders:
- the firm is not subject to corporate taxation;
- due to *limited liability* of equity holders, debt holders cannot force them to pay the difference  $C - X_t$ ; and
- the bankruptcy cost (i.e., lawyer cost, administrative costs, etc.) is a fraction  $\gamma$  of  $X_t$ .

It follows thus that

$$v_t^l = \min\{X_t, C\} (1 - \gamma \mathbf{1}_{X_t < C})$$
  
+  $\max\{(X_t - C)(1 - T_a \mathbf{1}_{X_t > C}); 0\}$  (5)

where  $\mathbf{1}_{X_t \geq C}$  and  $\mathbf{1}_{X_t < C}$  are indicator functions.<sup>c</sup> When there is no default, the value of the firm is given by equation (3). However, when there is default, the value of the firm is equal to  $X_t(1-\gamma)$ . In the particular case in which  $\gamma = 0$  and  $T_a = 0$ , it follows that

$$v_t^l = \min\{X_t, C\} + \max\{(X_t - C); 0\} = v_t = X_t$$
(6)

When there is no bankruptcy cost and no corporate income tax, the value of the levered firm is equal to the value of the unlevered one, that is, the value of the firm is invariant with respect to the coupon. This is the  $M-M$  theorem with default risk.

## **Classical Presentation**

In their original work, Modigliani and Miller [10] make the following assumptions.<sup>d</sup>

- Capital markets are perfectly competitive. 1.
- 2. Individuals and firms can borrow and lend at the risk-free rate  $r$ .
- 3. All firms are assumed to be in the same class risk.

Assumption 1 implies that market investors have full (and symmetric) information concerning the return of the firm, that there are no transaction costs, and that there are no restriction on asset trade, that is, long and short positions are possible. Assumption 2 means that when firms or households borrow, they are not subject to default risk so that they can borrow at the risk-free rate. Assumption 3 means that the stream of EBIT is the same for all firms in the same class risk; if two firms, one levered and one unlevered, belong to the same class risk, then, they differ only with respect to leverage.

In their original work, Modigliani and Miller [10] consider a discrete-time model in which the family of random variable  $\{X_t\}_{t\geq 1}$  is identically and independently distributed. Let  $\mathbb{E}(X_t) = \bar{X}$  be the expectation of  $X_t$  under the probability measure  $\mathbb{P}$ . In the present framework, the corporate debt is riskless if  $\mathbb{P}(X_t > C) = 1$ .

#### Cost of Capital and Valuation Principle

In  $M-M$  [10], the valuation principle is fairly simple: the present value of a stream of risky cash flow is equal to the *expected* sum over time of the *discounted* value of the cash flow. The expectation is taken under the probability measure  $\mathbb{P}$ , and the discount factor, also called risk adjusted rate of return or, more simply, the cost of capital incorporates a risk premium. Since, in general, investors are risk averse, the riskier the cash flow, the higher is the cost of capital. Let  $r$  be the cost of capital of a riskless cash flow and  $k_u > r$  be the cost of capital of a risky cash flow.

Using the above principle, the value of the unlevered firm is equal to the present value of the flow of  $v_t$ , that is,

$$V = E = \mathbb{E} \sum_{t=1}^{\infty} \frac{v_t}{(1 + k_u)^t} = \frac{\bar{X}(1 - T_a)}{k_u} \quad (7)$$

where  $V$  denotes the value of the unlevered firm, which is also equal to the value of equity  $E$ . To determine the value of the levered firm now, we have to compute the expected discounted value of the flow of  $v_t^l$ . Using equation (3), we just have to compute the value of the stream of tax shield. By assumption, the corporate debt is a perpetual risk-free one, so that the relevant cost of capital for the tax shield is  $r$ . It thus follows that

$$V^{l} = \mathbb{E} \sum_{t=1}^{\infty} \frac{X_{t}(1 - T_{a})}{(1 + k_{u})^{t}} + \sum_{t=1}^{\infty} \frac{T_{a} C}{(1 + r)^{t}}$$
$$= V + T_{a} \frac{C}{r} = V + T_{a} B \tag{8}$$

where  $B = \frac{C}{a}$  is the value of the perpetual corporate risk-free debt, and  $T_a B$  the value of the perpetual tax shield. The value of the levered firm is thus equal to the value of the unlevered firm plus the value of the tax shield. We can now state the famous invariance result when  $T_a = 0$ . Let  $\frac{B}{E^l}$  be the *debt–equity ratio* where  $E^l = V^l - B$  is the value of equity of the levered firm.

#### Modigliani–Miller Theorem with Risk-free Debt

In addition to the above assumptions, suppose that there is no arbitrage opportunity and no corporate income tax (i.e.,  $T_a = 0$ ); then,  $V = V^l$ , that is, the value of the firm is invariant with respect to the debt-equity ratio.

This result implies that when there are no taxes and no default risk, the value of the firm is *invariant* with respect to the "financing policy", which means that issuing only equity or issuing a mix of debt and equity does not affect the value of the firm. Fundamentally, the value of the firm is determined by the stream of EBIT, that is, by the investment policy; debt affects only the *split* of the value of the firm between debt holders and equity holders. As a consequence, different debt-equity ratios lead to different splits of the total value but have no impact on this total value.

From a mathematical point of view, the proof is trivial, since when  $T_a = 0$ , we immediately get that  $V = V^l$ . Actually, Modigliani and Miller became very famous not only for the result *per se*, but also because they offered, for the first time, a no-arbitrage

 $principle<sup>e</sup>$  for security valuation: they showed that if  $V^l > V$  when  $T_a = 0$ , then, there is an arbitrage opportunity.

While the proof is rather simple, it highlights their assumptions. Consider two firms that are in the same class risk. The first is unlevered while the second is levered. Since  $T_a = 0$ , the value of equity of the levered firm is equal to  $E^l = V - C/r$  while the value of equity of the unlevered firm is  $V = E$ . Consider now an equity holder who owns  $\kappa\%$  of the shares of the levered firm. At each time  $t$ , his/her claim  $D_t$  (i.e., dividend) is equal to

$$D_t = \kappa (X_t - C) \tag{9}$$

Suppose now that he/she sells his/her part of the levered firm for an amount  $\kappa E^l$  and borrows an amount equal to  $\kappa(C/r)$ . With that money, he/she buys a fraction  $\frac{\kappa(\dot{E}^l + (C/r))}{V}$  of the shares of the unlevered firm. Actually, the equity holder borrows an amount  $\kappa C/r$  to *replicate* the leverage of the firm, and this has been called a *homemade leverage*. Note importantly that by assumption 2, the investor borrows at the risk-free rate. He/she thus holds a portfolio in which he/she will not only perceive the dividends (in proportion of his/her part) of the unlevered firm at each time  $t$  but will also have to pay the interest expense equal to  $\kappa C$ . The return of his/her portfolio is thus equal to  $Y_t = \frac{\kappa (E^l + C/r)}{V} X_t - \kappa C$ . By definition,  $V^{l} = E^{l} + B$  so that  $Y_{t}$  is equal at each time  $t$  to

$$Y_t = \kappa \left(\frac{V^l}{V} X_t - C\right) \qquad t \ge 1 \tag{10}$$

Since  $V^l > V$  by assumption, it thus follows that  $Y_t > D_t$  with probability one, which is an arbitrage opportunity. If we rule out such an arbitrage opportunity, then,  $V^l = V$ .

As Duffie [2] remarks in his review on  $M-M$ theorem, the result follows because equity holders can undertake the same financial transaction as the firm in exactly the same condition. If an equity holder is considered as defaultable so that he/she must borrow at a rate higher than the risk-free rate, then, he/she cannot offset the financial decision of the firm at the same price.

#### The Cost of Equity and the Debt–equity Ratio

From equation (7), when  $T_a = 0$ , the cost of capital  $k_u = \bar{X}/E$  is the (expected) rate of return on equity. When the firm is levered, with  $T_a = 0$ , the (expected) rate of return of the levered firm  $k_e$  that we call *cost* of equity is equal to

$$k_e = \frac{\bar{X} - C}{E^l} \tag{11}$$

Since the firms are in the same class risk, the mean EBIT  $\bar{X}$  of the two firms are equal. As a consequence, by writing equation (11) as  $\bar{X} = E^l k_e + rB$  (recall that  $C = rB$ ), since  $\bar{X} = k_u E$ , it thus follows that

$$E^l k_e + r B = k_u E \tag{12}$$

The M-M theorem implies that  $V = V^l \equiv E^l + B$ . Since  $V = E$ , from equation (12), we easily obtain that

$$k_e = k_u + (k_u - r)\frac{B}{E^l}$$
 (13)

Equation (13) means that *ceteris paribus*, the higher the debt-equity ratio, the higher is the cost of equity of the levered firm. More precisely, the cost of equity is a *linear* increasing function of the debt-equity ratio, and is sometimes thought of as a pricing formula where  $(k_u - r)\frac{B}{E^l}$  is the premium for the *financial risk*. See [14] for a presentation of the various existing formulas of the cost of capital.

#### Contrast with Empirical Evidence

In contrast to the  $M-M$  theorem, the value of firms is actually influenced by their capital structure: the debt-equity ratio affects the value of the firm. To explain the observed debt-equity ratio, a large part of the recent theory of capital structure has been to explore the role of the conflicts, inexistent in the  $M-M$  analysis, that arise among managers, equity holders, and debt holders. Informational asymmetries play an important role. The article of Harris and Raviv [5] and the books of Milgrom [9] or Hillier *et al.* [7] contain a very readable presentation of many aspects of the recent theory of capital structure.

## **Modern Presentation**

We now present the  $M-M$  theorem in a continuoustime setting assuming that markets are arbitrage free

and complete<sup> $f$ </sup> so that there exists a *unique pricing measure* (also called risk-neutral measure) denoted by  $\mathbb{Q}$ . More precisely, we assume that under the unique risk-neutral measure  $\mathbb{Q}$ , the stochastic process  $X = (X_t)_{t>0}$  is given by

$$X_t = x \ e^{(\mu - 0.5\sigma^2)t + \sigma W_t} \Longleftrightarrow \frac{\mathrm{d}X_t}{X_t} = \mu \ \mathrm{d}t + \sigma \ \mathrm{d}W_t \tag{14}$$

where  $\mu$  is the risk-neutral drift,  $\sigma$  is the volatility,  $W_t$  is a standard Brownian motion under  $\mathbb{Q}$ , and x is the value of the EBIT at time  $t = 0$ . In what follows, the expectation is taken under the pricing measure  $\mathbb{Q}$ .

#### Valuation Principle

In the "modern" approach, one also values a stream of risky cash flow as the *expected* sum over time of the *discounted* value of the cash flow. The discount rate is now always equal to the risk-free rate  $r$ , whether the cash flow is risky or not, and, to prevent arbitrage,<sup>g</sup> the pricing measure  $\mathbb{Q}$  is such that the overall expected rate of return of the unlevered equity, that is, expected capital gain plus dividend yield, is equal to the risk-free rate  $r$ .

The value of the unlevered firm seen from  $t = 0$ , which is also the value of equity, is equal to the expected sum of discounted  $v_t$  (see equation 1) over time, that is

$$V(x) \equiv V = \mathbb{E} \int_0^\infty e^{-rt} v_t dt$$
  
= 
$$\mathbb{E} \int_0^\infty e^{-rt} X_t (1 - T_a) dt \quad (15)$$

$$= \frac{x(1 - T_a)}{r - \mu} \qquad \mu < r \tag{16}$$

Seen from a given time  $t > 0$ , the value of the unlevered firm (or equity) is equal to

$$V_t = \frac{X_t(1 - T_a)}{r - \mu} \tag{17}$$

We assume, as previously, that equity is a *traded* asset, whose price is  $V_t$  at time t. Since all the residual cash flow is distributed to equity holders as dividends, the dividend yield is equal to  $\frac{X_t(1-T_a)}{V_c}$  =

 $r - \mu$ , which means that  $\mu < r$ . As a consequence, the overall expected rate of return from holding the equity of the unlevered firm is equal to  $r$ , that is, the expected capital gain  $\mu$  plus the dividend yield  $r - \mu$ .

## Default Risk

The existence of default risk complicates the analysis of the preceding section, since the flow of  $v_t^l$  may be stopped at a random time  $\tau$ . Moreover, if default occurs at time  $\tau$ , a fraction  $\gamma V$  is lost due to bankruptcy costs. As a consequence, the value of the levered firm is equal to  $V$  plus the value of the taxshield  $TS$  minus the value of the bankruptcy costs BC. The value of the levered firm  $V^l$  at time  $t=0$ is thus equal to

$$V^{l} = V + TS - BC \tag{18}$$

To compute the value (at time  $t = 0$ ) of the taxshield  $TS$  and of the bankruptcy costs  $BC$ , we now have to specify the default declaration mechanism. It is assumed that default is triggered at the first time  $t > 0$  for which  $V_t \leq V_B$ , with  $V_B < C/r$ . Let  $\tau$ denote the default time. Since (almost all) the sample paths of the stochastic process  $V_t$  are continuous, default occurs at the first time for which  $V_t = V_B$ . It follows that

$$\tau = \inf\{t \in \mathbb{R}^+ : V_t = V_B\} \tag{19}$$

It can be shown<sup>h</sup> that, for a perpetual corporate debt, the risk-neutral default probability is equal to

$$\left(\frac{V_B}{V}\right)^{2(\mu - 0.5\sigma^2)/\sigma^2} \tag{20}$$

To determine  $TS$  and  $BC$ , we follow [3] and first compute the present value of a contingent claim that pays €1 if the firm defaults. Seen from  $t = 0$ , if the default time  $\tau$  were to be known, its value would be equal to  $e^{-r\tau}$ . Since  $\tau > 0$  is not known, the value of such a contingent claim is equal to its expected value. It can be shown<sup>i</sup> that

$$\lim_{T \to \infty} \mathbb{E} \left( e^{-r\tau} \mathbf{1}_{\tau < T} \right) = \left( \frac{V_B}{V} \right)^{\xi} \tag{21}$$

where  $\xi = \frac{1}{\sigma^2} \left[ (\mu - 0.5\sigma^2) + \sqrt{(\mu - 0.5\sigma^2)^2 + 2r\sigma^2} \right] >$ 0, and  $\mathbf{1}_{\tau < T}$  is the indicator function of the event  $\tau < T$  (recall that T is the maturity of the debt).

Consider now the value of the bankruptcy costs. Seen from  $t = 0$ , when default occurs at time  $\tau > 0$ , their value is  $e^{-r\tau}\gamma V_B$  while if default never occurs, their value is zero. Using equation (21), it thus follows that the value of the bankruptcy costs is equal to

$$BC = \lim_{T \to \infty} \mathbb{E} \left( \gamma \, V_B \mathrm{e}^{-r\tau} \mathbf{1}_{\tau < T} \right) = \gamma \, V_B \left( \frac{V_B}{V} \right)^{\xi} \tag{22}$$

In the same way, since the tax shield is positive as long as default is not declared, its value is equal to

$$TS = \left(1 - \left(\frac{V_B}{V}\right)^{\xi}\right) T_a(C/r) \tag{23}$$

The value of the levered firm, defined by equation  $(18)$ , is thus equal to

$$V^{I} = V + \left(1 - \left(\frac{V_{B}}{V}\right)^{\xi}\right) T_{a}(C/r) - \left(\frac{V_{B}}{V}\right)^{\xi} \gamma V_{B}$$
(24)

Note that when  $V$  (or  $x$ ) tends to infinity, equation (24) reduces to equation (8) since default risk vanishes. When  $T_a = 0$  and  $\gamma = 0$  in equation (24), it thus follows that  $V^l = V$ .

## *Modigliani–Miller theorem with risky debt*

Assume that markets are arbitrage free and complete and that there are no corporate income taxes (i.e.,  $T_a = 0$ ) and no bankruptcy costs (i.e.,  $\gamma = 0$ ). Then  $V = V<sup>l</sup>$ , that is, the value of the firm is invariant with respect to the debt-equity ratio.

Default risk does not invalidate the  $M-M$  theorem as long as there are no taxes and no bankruptcy costs. When there are both tax and bankruptcy costs, the debt-equity ratio that maximizes the value of the firm is an optimal trade-off between the value of the tax shield and the value of the bankruptcy costs.<sup>1</sup> However, it is assumed not only that there is no cash reserve (due to the particular dividend policy) but also that equity holders can *costlessly* issue new shares to avoid default if they want to do so.

Assume now that some fraction of the net income (when positive) is not distributed to equity holders as dividends, it goes on a cash reserve that capitalizes at a rate equal to *r* − *λ*. The parameter *λ* reflects inefficiencies of managerial expenses (agency costs) so that some fraction of the cash can be considered as lost. When there are both issuance and agency costs, it has been shown that the *optimal dividend policy*<sup>k</sup> is an optimal trade-off between these two costs.

# **End Notes**

a*.* This might not be the case if, for example, equity holders issue new equity to pay *C* − *Xt* to bondholders when *Xt < C*. <sup>b</sup>*.*

Here, we make no difference between default and liquidation.

c*.* Recall that the indicator function of an event *A* is such that **<sup>1</sup>***<sup>A</sup>* <sup>=</sup> 1 if *<sup>ω</sup>* <sup>∈</sup> *<sup>A</sup>* and 0 otherwise. <sup>d</sup>*.*

See [13] for a lucid discussion of their assumptions.

e*.* Their no-arbitrage proof was indeed misunderstood. See [6] and the reply in [11].

f*.* In a section entitled Arrow-Debreu Securities, [12] shows the M–M theorem in a (static) complete market setting. For a treatment of the incomplete market case, see [1] or [4].

g*.* See, for example, Kerry Back (2005). *A Course in Derivatives Securities*, Springer-Verlag, p. 42.

h*.* See, for example, Bielecki, T. & Rutkowski, M. (2001). *Credit Risk: Modeling, Valuation and Hedging*, Springer-Verlag, p. 68.

i*.* See Bielecki T. and Rutkowski M. (2001), p 81 for a probabilistic proof or [3], p 491 for an alternative proof. j*.*

This model has been developed by Leland [8].

k*.* See Decamps, J.P., Mariotti, T., Rochet, J.C. & Villeneuve, S. (2008). *Free Cash Flow, Issuance Costs, and Stock Price Volatility*, IDEI Working Paper, n*<sup>o</sup>* 518, September 2008.

# **References**

- [1] De Marzo, P. (1988). An extension of the Modigliani-Miller theorem to stochastic economies with incomplete markets, *Journal of Economic Theory* **45**(2), 261–286.
- [2] Duffie, D. (1992). Modigliani-Miller theorem, in *The New Palgrave Dictionary of Money and Finance*, M. Milgate, P. Newman, & J. Eatwell, eds, McMillan Press, London.

- [3] Goldstein, R., Ju, N. & Leland, H. (2001). An EBITbased model of dynamic capital structure, *Journal of Business* December, 483–512.
- [4] Gottardi, P. (1995). An analysis of the conditions for the validity of the Modigliani-Miller theorem with incomplete markets, *Economic Theory* **5**, 191–207.
- [5] Harris, A. & Raviv, A. (1991). The theory of capital structure, *Journal of Finance* March, 297–355.
- [6] Heins, J. & Sprenkle, C. (1969). A comment on the Modigliani-Miller cost of capital thesis, *American Economic Review* September, 590–592.
- [7] Hillier, D., Grinblatt, M. & Titman, S. (2008). *Financial Markets and Corporate Strategy*, European edition, Mac Graw Hill.
- [8] Leland, H. (1994). Corporate debt value, bond covenants, and optimal capital structure, *Journal of Finance* **49**, 1213–1252.
- [9] Milgrom, P. & Roberts, J. (1992). *Economics, Organization, and Management*, Prentice-Hall.
- [10] Modigliani, F. & Miller, M. (1958). The cost of capital, corporation finance, and the theory of investment, *American Economic Review* **48**, 261–297.
- [11] Modigliani, F. & Miller, M. (1969). Reply to Heins and Sprenkle, *American Economic Review* September, 592–595.
- [12] Stiglitz, J. (1969). A re-examination of the Modigliani-Miller theorem, *American Economic Review* **59**, 784–793.
- [13] Stiglitz, J. (1988). Why financial structure matters, *Journal of Economic Perspectives* **2**(4), 121–126.
- [14] Taggart, R. (1991). Consistent valuation and the cost of capital expressions with corporate and personal taxes, *Financial Management* Autumn, 8–20.

# **Further Reading**

- Hellwig, M. (1981). Bankruptcy, limited liability and the Modigliani-Miller theorem, *American Economic Review* **71**(1), 155–170.
- Modigliani, F. & Miller, M. (1961). Dividend policy, growth and the valuation of shares, *Journal of Business* **34**(4), 411–433.
- Stiglitz, J. (1974). On the irrelevance of corporate financial policy, *American Economic Review* December, 851–866.

# **Related Articles**

**Arbitrage Pricing Theory**; **Modigliani, Franco**.

YANN BRAOUEZEC
# Compensators

In probability theory, the *compensator* of a stochastic process designates a quantity that, once subtracted from a stochastic process, yields a martingale.

## Compensator of a Random Time

Let  $(\Omega, \mathbf{G}, \mathbb{P})$  be a filtered probability space and  $\tau$ a **G**-stopping time. The process  $H_t = \mathbb{1}_{\tau \leq t}$  is a **G**adapted increasing process, hence a **G**-submartingale and admits a Doob-Meyer decomposition as

$$H_t = M_t + \Lambda_t \tag{1}$$

where *M* is a **G**-local martingale and  $\Lambda$  a **G**predictable increasing process. The process  $\Lambda$ , called the **G**-compensator of  $H$ , is constant after  $\tau$ , that is,  $\Lambda_t = \Lambda_{t \wedge \tau}$ . The process  $\Lambda$  "compensates" *H* with the meaning that  $H - \Lambda$  is a martingale. If  $\tau$  is Gpredictable, then  $\Lambda_t = H_t$ . The continuity of  $\Lambda$  is equivalent to the fact that  $\tau$  is a **G**-totally inaccessible stopping time. If  $\Lambda$  is absolutely continuous with respect to the Lebesgue measure, that is, if  $\Lambda_t =$  $\int_0^t \lambda_s^{\mathbf{G}} ds$ , the nonnegative **G**-adapted process  $\lambda^{\mathbf{G}}$  is called the *intensity rate* of  $\tau$ . Note that  $\lambda_{\tau}^{\mathbf{G}}$  is null on the set  $\tau \leq t$ .

For any integrable random variable  $X \in \mathcal{G}_T$ , one has

$$\mathbb{E}(X\mathbbm{1}_{T<\tau}|\mathcal{G}_t) = \mathbbm{1}_{\{t<\tau\}} \left(V_t - \mathbb{E}(\Delta V_\tau \mathbbm{1}_{\tau\leq T}|\mathcal{G}_t)\right)$$
(2)

with  $V_t = e^{\Lambda_t} \mathbb{E}(X e^{-\Lambda_T} | \mathcal{G}_t).$ 

In the following examples,  $\tau$  is a given random time, that is, a nonnegative random variable, and  $\mathbf{H}$ the natural filtration of  $H$  (i.e., the smallest filtration satisfying the usual conditions such that the process H is adapted). The random time  $\tau$  is a **H**-stopping time.

# Elementary Case

Let  $\tau$  be an exponential random variable with constant parameter  $\lambda$ . Then, the **H**-compensator of *H* is  $\lambda(t \wedge \tau)$ . More generally, if  $\tau$  is a nonnegative random variable with cumulative distribution function  $F$ , taken continuous on the right  $(F(t) = \mathbb{P}(\tau \leq t))$  such

that  $\forall t, F(t) < 1$ , the **H**-compensator of  $\tau$  is  $\Lambda_t =$  $\int_{0}^{t \wedge \tau} \frac{\mathrm{d}F(s)}{1-F(s^{-})}$ . If *F* is continuous, the **H**-compensator is  $\Lambda_{t} = -\ln(1-F(t \wedge \tau))$ .

# Cox Processes

Let **F** be a given filtration,  $\lambda$  a given **F**-adapted nonnegative process,  $\Lambda_t^{\mathbf{F}} = \int_0^t \lambda_s \mathrm{d}s$ , and  $\Theta$  a random variable with exponential law, independent of  $\mathbf{F}$ . Let us define the random time  $\tau$  as

$$\tau = \inf \left\{ t \; : \; \Lambda_t^{\mathbf{F}} \ge \Theta \right\} \tag{3}$$

Then, the process

$$\mathbb{1}_{\tau \leq t} - \int_{0}^{t \wedge \tau} \lambda_{s} \, \mathrm{d}s = \mathbb{1}_{\tau \leq t} - \Lambda_{t \wedge \tau}^{\mathbf{F}} \tag{4}$$

is a martingale in the filtration  $\mathbf{G} = \mathbf{F} \vee \mathbf{H}$ , the smallest filtration that contains **F**, making  $\tau$  a stopping time (in fact a totally inaccessible stopping time). The Gcompensator of *H* is  $\Lambda_t = \Lambda_{t \wedge \tau}^{\mathbf{F}}$ , and the **G**-intensity rate is  $\lambda_t^{\mathbf{G}} = \mathbb{1}_{t < \tau} \lambda_t$ . In that case, for an integrable random variable  $X \in \mathcal{F}_T$ , one has

$$\mathbb{E}(X\mathbb{1}_{T<\tau}|\mathcal{G}_t) = \mathbb{1}_{t<\tau} \mathrm{e}^{\Lambda_t^{\mathbf{F}}} \mathbb{E}(X\mathrm{e}^{-\Lambda_T^{\mathbf{F}}}|\mathcal{F}_t) \tag{5}$$

and, for  $H$ , an **F**-predictable (bounded) process

$$\mathbb{E}(H_{\tau} \mathbb{1}_{\tau \leq T} | \mathcal{G}_{t}) = H_{\tau} \mathbb{1}_{\tau \leq t}$$
  
+ 
$$\mathbb{1}_{t < \tau} e^{\Lambda_{t}^{\mathbf{F}}} \mathbb{E}\left(\int_{t}^{T} H_{s} e^{-\Lambda_{s}^{\mathbf{F}}} \lambda_{s} \mathrm{d}s | \mathcal{F}_{t}\right) \qquad (6)$$

#### Conditional Survival Probability

Assume now that  $\tau$  is a nonnegative random variable on the filtered probability space  $(\Omega, \mathbf{F}, \mathbb{P})$  with conditional survival probability  $G_t := \mathbb{P}(\tau > t | \mathcal{F}_t),$ taken continuous on the right and let  $\mathbf{G} = \mathbf{F} \vee \mathbf{H}$ . The random time  $\tau$  is a **G**-stopping time.

If  $\tau$  is an **F**-predictable stopping time (hence a **G**-predictable stopping time), then  $G_t = \mathbb{1}_{\tau > t}$  and  $\Lambda = H.$ 

In what follows, we assume that  $G_t > 0$  and we introduce the Doob-Meyer decomposition of the **F**-supermartingale G, that is,  $G_t = Z_t - A_t$ , where  $Z$  is an **F**-martingale and  $A$  is an increasing **F**predictable process. Then, the G-compensator of  $\tau$  is  $\Lambda_t = \int_0^{t \wedge \tau} (G_{s^-})^{-1} dA_s$ . If  $dA_t = a_t dt$ , the **G**-<br>intensity rate is  $\lambda_t^{\mathbf{G}} = \mathbb{1}_{t < \tau} (G_{t^-})^{-1} a_t$ . Moreover, if G is continuous, then for an integrable random variable  $X \in \mathcal{F}_T$ , one has

$$\mathbb{E}(X\mathbb{1}_{T<\tau}|\mathcal{G}_t) = \mathbb{1}_{t<\tau}(G_t)^{-1}\mathbb{E}(XG_T|\mathcal{F}_t) \tag{7}$$

It is often convenient to introduce the F-adapted process  $\widetilde{\lambda}_t = (G_{t^-})^{-1} a_t$ , equal to  $\lambda_t^{\mathbf{G}}$  on the set  $t < \tau$ . We shall call this process the *predefault-intensity* process.

A particular case occurs when the process  $G$  is nonincreasing and absolutely continuous with respect to the Lebesgue measure, that is,  $G_t = \int_t^{\infty} g_s ds$ , where  $g \ge 0$ . In that case, the **G**-adapted intensity rate is  $\lambda_t^{\mathbf{G}} = (G_t)^{-1} g_t \mathbb{1}_{t < \tau}$ , the predefault intensity is  $\widetilde{\lambda}_t = (G_t)^{-1} g_t$  and, for an integrable random variable  $X \in \mathcal{F}_T$ ,

$$\mathbb{E}(X\mathbb{1}_{T<\tau}|\mathcal{G}_t) = \mathbb{1}_{t<\tau} e^{\Lambda_t^{\mathbf{F}}} \mathbb{E}(Xe^{-\Lambda_T^{\mathbf{F}}}|\mathcal{F}_t)$$
(8)

where  $\Lambda^{\mathbf{F}}$  is the **F**-adapted process defined as

$$\Lambda_t^{\mathbf{F}} = \int_0^t \widetilde{\lambda}_s \mathrm{d}s = \int_0^t (G_s)^{-1} g_s \mathrm{d}s \tag{9}$$

Aven's Lemma

The Aven lemma has the following form: let  $(\Omega, \mathcal{G}_t, \mathbb{P})$  be a filtered probability space and N be a counting process. Assume that  $E(N_t) < \infty$  for any t. Let  $(h_n, n \ge 1)$  be a sequence of real numbers converging to  $0$ , and

$$Y_t^{(n)} = \frac{1}{h_n} E(N_{t+h_n} - N_t | \mathcal{G}_t)$$
(10)

Assume that there exists  $\lambda_t$  and  $y_t$  nonnegative G-adapted processes such that

1. For any 
$$t$$
,  $\lim Y_t^{(n)} = \lambda_t$  (11)

2. For any *t*, there exists for almost all  $\omega$  an  $n_0 =$  $n_0(t,\omega)$  such that

$$|Y_s^{(n)} - \lambda_s(\omega)| \le y_s(\omega), \ s \le t, \ n \ge n_0(t, \omega)$$
(12)

3. 
$$\int_0^t y_s \, \mathrm{d}s < \infty, \forall t \tag{13}$$

Then,  $N_t - \int_0^t \lambda_s ds$  is a G-martingale.

For the particular case of a random time, we obtain the following: assume that  $\lim_{h\to 0} \frac{1}{h} \mathbb{P}(t < \tau \leq t +$ 

 $h|\mathcal{G}_t) = \lambda_t^{\mathbf{G}}$ , and that, there exists a Lebesgue integrable process y such that  $\left|\frac{1}{h}\right| \mathbb{P}(t < \tau \le t + h|\mathcal{G}_t)$  $|\lambda_t^{\mathbf{G}}| \le y_t$  for any h small enough. Then  $\lambda^{\mathbf{G}}$  is the **G**-intensity of  $\tau$ .

In the case of conditional survival probability model, the predefault intensity  $\lambda^G$  is

$$\widetilde{\lambda}_{t}^{\mathbf{G}} = \lim_{h \to 0} \frac{1}{h \mathbb{P}(t < \tau | \mathcal{F}_{t})} \mathbb{P}(t < \tau \le t + h | \mathcal{F}_{t}) \quad (14)$$

See  $[2]$  for an extensive study.

Shrinking

Assume that  $\mathbf{G}^*$  is a subfiltration of  $\mathbf{G}$  such that  $\tau$  is a  $G^*$  (and a  $G$ ) stopping time. Assume that  $\tau$  admits a **G**-intensity rate equal to  $\lambda^G$ . Then, the **G**<sup>\*</sup>-intensity of  $\tau$  is  $\lambda_t^* = \mathbb{E}(\lambda_t^{\mathbf{G}} | \mathbf{G}_t^*)$  (see [1]).

As we have seen above, in the survival probability approach, the value of the intensity can be given in terms of the conditional survival probability. Assume that  $G_t = \mathbb{P}(\tau > t | \mathcal{F}_t) = Z_t - \int_0^t a_s \text{d}s$ , where Z is an **F**-martingale and that  $\mathbf{G}^* = \mathbf{F}^* \vee \mathbf{H}$  where,  $\mathbf{F}^* \subset$  $\mathbf{F}$ . Then, the  $\mathbf{F}^*$ -conditional survival probability of  $\tau$  is

$$G_t^* = \mathbb{P}(\tau > t | \mathcal{F}_t^*) = \mathbb{E}(G_t | \mathcal{F}_t^*) = X_t^* - \int_0^t a_s^* \mathrm{d}s \tag{15}$$

where  $X^*$  is an  $\mathbf{F}^*$ -martingale and  $a_s^* = \mathbb{E}(a_s|\mathcal{F}_s^*)$ . It follows that the  $G^*$ -intensity rate of  $\tau$  writes as (we assume, for simplicity, that G and  $G^*$  are continuous)

$$\lambda_t^* = \mathbb{1}_{t < \tau} \frac{a_t^*}{G_t^*} = \mathbb{1}_{t < \tau} \frac{\mathbb{E}(\lambda_t^{\mathbf{G}} G_t | \mathcal{F}_t^*)}{\mathbb{E}(G_t | \mathcal{F}_t^*)} \tag{16}$$

It is useful to note that one can start with a model in which  $\tau$  is an **F**-predictable stopping time (hence  $G = F$ , and a G-intensity rate does not exist) and consider a smaller filtration (e.g., the trivial filtration) for which there exists an intensity rate, computed by means of the conditional survival probability.

## **Compensator of an Increasing Process**

The notion of interest in this section is that of *dual predictable projection*, which we define as follows:

**Proposition 1** Let  $A$  be an integrable increasing process (not necessarily F-adapted). There exists a unique F-predictable increasing process  $(A_t^{(p)}, t \ge 0)$ , called the **F**-dual predictable projection of A such that

$$\mathbb{E}\left(\int_0^\infty H_s \, \mathrm{d}A_s\right) = \mathbb{E}\left(\int_0^\infty H_s \, \mathrm{d}A_s^{(p)}\right) \qquad (17)$$

for any positive  $\mathbf{F}$ -predictable process  $H$ .

The definition of compensator of a random time can be interpreted in terms of dual predictable projection: if  $\tau$  is a random time, the *F*-predictable *compensator* associated with  $\tau$  is the dual predictable projection  $A^{\tau}$  of the increasing process  $\mathbb{1}_{\{\tau < t\}}$ . It satisfies  $\sim$ 

$$\mathbb{E}(k_{\tau}) = \mathbb{E}\left(\int_{0}^{\infty} k_{s} \mathrm{d}A_{s}^{\tau}\right) \tag{18}$$

for any positive, **F**-predictable process  $k$ .

#### Examples

Covariation Processes. Let  $M$  be a martingale and  $[M]$  its quadratic variation process. If  $[M]$  is integrable, its compensator is  $\langle M \rangle$ .

Standard Poisson Process. If  $N$  is a Poisson process,  $(M_t = N_t - \lambda t, t \ge 0)$  is a martingale, and  $\lambda t$  is the compensator of N; the martingale M is called the *compensated martingale*.

Compensated Poisson Integrals. Let  $N$  be a time inhomogeneous Poisson process with deterministic intensity  $\lambda$  and  $\mathbf{F}^N$  its natural filtration. The process

$$\left(M_t = N_t - \int_0^t \lambda(s) \mathrm{d}s, \ t \ge 0\right) \tag{19}$$

is an  $\mathbf{F}^N$ -martingale. The increasing function  $\Lambda(t)$  :=  $\int_0^t \lambda(s) ds$  is called the (deterministic) *compensator* of  $N$ .

# **Random Measures**

#### Definitions

The *compensator* of a random measure  $\mu$  is the unique random measure  $\nu$  such that

- 1. for every predictable process  $H$ , the process  $(H \star v)$  is predictable (the measure v is said to be predictable) and
- 2. for every predictable process  $H$  such that the process  $|H| \star \mu$  is increasing and locally integrable, the process  $(H \star \mu - H \star \nu)$  is a local martingale.

#### Examples

If N is a Lévy process with Lévy measure  $\nu$ 

$$\int_{\Lambda} f(x)N_{t}(\cdot, dx) - t \int_{\Lambda} f(x)\nu(dx)$$
$$= \sum_{0 < s \le t} \left( f(\Delta X_{s}) \mathbb{1}_{\Lambda}(\Delta X_{s}) \right) - t \int_{\Lambda} f(x)\nu(dx)$$
(20)

is a martingale, the compensator of  $\int_{\Lambda} f(x) N_t(\cdot, dx)$ is  $t \int_{\Lambda} f(x) \nu(\mathrm{d}x)$ .

For other examples see the article on point processes (see Point Processes).

## References

- [1] Brémaud, P. & Yor, M. (1978). Changes of filtration and of probability measures, Zeit Wahr and Verw Gebiete 45,  $269 - 295$
- [2] Zeng, Y. (2006). Compensators of Stopping Times, PhD thesis, Cornell University.

# **Further Reading**

Brémaud, P. (1981). Point Processes and Queues. Martingale Dynamics, Springer-Verlag, Berlin.

- Cinlar, E. (1975). Introduction to Stochastic Processes, Prentice Hall.
- Cont, R. & Tankov, P. (2004). Financial Modeling with Jump Processes, Chapman & Hall/CRC.
- Jeanblanc, M., Yor, M. & Chesney, M. (2009). Mathematical *Models for financial Markets*, Springer, Berlin.
- Karlin, S. & Taylor, H. (1975). A First Course in Stochastic Processes, Academic Press, San Diego.

## **Related Articles**

Doob-Meyer Decomposition; Filtrations; Intensity-based Credit Risk Models; Point Processes.

MONIQUE JEANBLANC
# **Duration Models**

Duration models appear when studying the moment in time that certain events occur. Next to general applications in economics and medical sciences, their financial applications are in the more specific field of market microstructure (transaction times of assets or derivatives in a given market), and also in corporate governance (tenure of management).

Denote the unknown times at which the events of interest occur as  $T_i$ ,  $i = 1, \ldots, n$ . Almost invariable in the literature, it is assumed that the times  $T_i$  form an *increasing* sequence of *stopping times*. The random times are increasing if  $T_{i+1} \geq T_i$  (almost surely (a.s.)). In that case, the *duration*  $D_i$  is defined by  $D_i = T_i - T_{i-1} \ge 0$ , with the usual convention  $T_0 = 0$ , which explains the name duration models. The stopping time property is with respect to a given underlying filtration  $(\mathcal{F}_t)_{t>0}$ . This filtration is supposed to model the information available to either the investigator (in order to perform inference) or an agent in a financial market (in order to take, e.g., investment decisions). Care is to be taken when extrapolating results on inference to actual financial market decisions if these information sets are different (where, often, the investigator's information set is smallest). Mathematically, the information structure is generally assumed to satisfy the so-called *usual* conditions [5].

The stopping-time property of  $T_i$  formally states that, for each  $t > 0$ , the event  $\{T_i < t\}$  belongs to  $\mathcal{F}_t$ . As the filtration is, by definition, increasing  $(\mathcal{F}_s \subset \mathcal{F}_t)$ for  $s \leq t$ ), we also have  $\{T_i \leq s\} \in \mathcal{F}_t$  for  $s \leq t$ . Thus, informally, if  $T_i$  is a stopping time denoting the occurrence of an event then, at each time  $t \ge 0$ , we know whether the event has occurred already. Also, in case the event has occurred by time  $t$ , we know at which time  $s \leq t$  it occurred.

#### Scale Models

A popular way to model the times  $T_i$  or, equivalently, the durations  $D_i$  is via a scale model. This method became popular in the financial econometrics literature because of its resemblance to volatility modeling (see, for instance, the *autoregressive* conditional duration (ACD) specification of [2]). In these models, we write the  $i$ th duration as the product of two positive random variables,  $D_i = \psi_i \varepsilon_i$ . Here  $(\varepsilon_i)_{i=1}^n$  is some *innovation sequence* and the properties of the model depend on the assumptions made on this innovation sequence. The scale factor  $\psi_i$  is assumed to be predetermined, meaning that  $\psi_i$  is measurable with respect to  $\mathcal{F}_{T_{i-1}}$ , the information available at time  $T_{i-1}$ . This information set allows the formalization of, for example, the expectation given the information at  $T_{i-1}$  and, in particular, leads to the optional stopping theorem [5]. Most of the literature identifies the scale of the innovation sequence by  $E\{\varepsilon_i | \mathcal{F}_{T_{i-1}}\} = 1$ . Such an assumption is innocuous insofar as the modeling is concerned, but may change the interpretation of parameters specifying  $\psi_i$  and thus inferential aspects as (semiparametric) adaptivity [1]. In the ACD specification, it is assumed that  $\mathcal{F}_{T_i}$  is observed by the investigator, so that  $\psi_i$  is observed as well (up to unknown parameters). An alternative is given by the stochastic volatility duration (SVD) model of [3], where the expected duration  $\psi_i$  is modeled using an unobserved factor allowing for unobserved heterogeneity.

#### **Point or Counting Process Models**

In the probabilistic literature, point processes refer to stochastic processes that generate random points in a set [4]. Applied to the positive half line, this leads to models for random times/durations. As describing the location of certain points is equivalent to count the number of points in general sets, these processes are also called *counting processes*. The distributional properties of these processes are characterized by, for instance, the (conditional) intensity measure, which essentially gives the (conditionally) expected number of events in a small (time) interval.

#### **Passage Time Models**

A structural approach to duration models can be obtained, using as a duration the time it takes for a stochastic process to pass a certain threshold. In particular, if the underlying process is a Brownian motion this leads to Brownian hitting times, which are well studied. In this simplest setting, these hitting times (durations) are distributed according to the inverse Gaussian distribution, which also explains the name for this distribution.

## **Proportional Hazard and Survival Models**

Survival analysis is used in (bio)statistics to model uncertain lifetimes and can be adopted to model other (financial) durations. This literature uses, in particular, the *hazard* rate to model the duration of an event. The hazard rate is the (instantaneous) probability that the event will occur in the next time instance, given that it has not occurred so far. Mathematically, the hazard rate equals the density of the duration distribution, divided by it survival function (one minus the cumulative distribution function). In particular, the proportional hazard model has been used a lot. In such a model, predetermined variables multiply the baseline hazard, to give a conditional hazard.

## **Multivariate Models**

In financial applications, there is much interest in jointly modeling several durations, for example, the transaction times for multiple assets. Owing to the nonsynchronous occurrence of events, this is a nontrivial exercise. In general, the point process approach is most suited in these circumstances, as the multivariate intensities can be modeled. Inference, though, is fairly involved.

Similarly, one is often interested in the joint behavior of durations and other quantities as volume or volatility. Such multivariate extensions can be complicated by possible subtle causality relations (both instantaneous and Granger) between the processes. Moment-based inference that takes these effects into account has been proposed in [6].

### **References**

- [1] Drost, F.C. & Werker, B.J.M. (2004). Semiparametric duration models, *Journal of Business and Economic Statistics* **22**, 40–50.
- [2] Engle, R.F. & Russell, J.R. (1998). Autoregressive conditional duration: a new model for irregularly spaced transaction data, *Econometrica* **66**, 1127–1162.
- [3] Ghysels, E., Gourieroux, C. & Jasiak, J. (2004). Stochastic ´ volatility duration models, *Journal of Econometrics* **119**, 413–433.
- [4] Last, G. & Brandt, A. (1995). *Marked Point Processes on the Real Line: The Dynamic Approach*, Springer-Verlag.
- [5] Protter, P.E. (1990). *Stochastic Integration and Differential Equations : A New Approach*, Springer-Verlag.
- [6] Renault, E. & Werker, B.J.M. (2009). Causality effects in return volatility measures with random times, *Journal of Econometrics* Forthcoming.

### **Related Articles**

**High-frequency Data**; **Order Flow**; **Point Processes**; **Poisson Process**.

BAS J.M. WERKER
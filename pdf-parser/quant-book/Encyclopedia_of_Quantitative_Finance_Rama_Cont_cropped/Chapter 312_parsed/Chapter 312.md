# **Model Validation**

One important way to mitigate model risk (*see* **Models**; for a more detailed discussion of model risk and how to mitigate model risk, see Crouhy *et al.* [1], chapter 14) is to invest in research to improve models and to develop better statistical tools, either internally at the bank or externally at a university (or at an analytically oriented consulting organization).

An even more vital way of reducing model risk is to establish a process for the independent vetting of how models are both selected and constructed. This should be complemented by independent oversight of the profit and loss (P&L) calculation. In this article, we address the *ex ante* validation of pricing models developed for the front office of a trading institution. *Ex post* validation of risk models, or back testing, is addressed in **Backtesting**.

The role of vetting is to offer assurance to the firm's management that any model proposed by, say, a trading desk for the valuation of a given security, is reasonable. In other words, the model offers a reasonable representation of how the market itself values the instrument, and that the model has been implemented correctly. Vetting should consist of the following phases:

#### **1. Documentation**

The vetting team should ask for a full documentation of the model, including both the assumptions underlying the model and its mathematical expression. This should be independent of any particular implementation, such as a spreadsheet or a C++ computer code, and should include the following:

- The term sheet or, equivalently, a complete description of the transaction.
- A mathematical statement of the model, which should include the following:
  - An explicit statement of all the components of the model: stochastic variables and their processes, parameters, equations, and so on.
  - The payoff function and/or any pricing algorithm for complex structured deals.
  - The calibration procedure for the model parameters.
  - The hedge ratios/sensitivities.

- Implementation features, that is, inputs, outputs, and numerical methods employed.
- A working version of the implementation.

#### **2. Soundness of model**

An independent model vetter needs to verify that the mathematical model is a reasonable representation of the instrument that is being valued. For example, the manager might reasonably accept the use of a particular model (e.g., the Black model) for valuing a short-term option on a long maturity bond, but reject (without even looking at the computer code) the use of the same model to value a two-year option on a three-year bond. At this stage, the risk manager should concentrate on the finance aspects, and not become overly focused on the mathematics.

#### **3. Independent access to financial rates**

The model vetter should check that the bank's middle office has independent access to an independent market risk management financial rates database (to facilitate independent parameter estimation).

#### **4. Benchmark modeling**

The model vetter should develop a benchmark model based on the assumptions that are being made and on the specifications of the deal. Here, the model vetter may use a different implementation from the implementation that is being proposed. A proposed analytical model can be tested against a numerical approximation technique or against a simulation approach. (For example, if the model to be vetted is based on a "tree" implementation, one may instead rely on the partial differential equation approach and use the finite element technique to derive the numerical results.) The results of the benchmark test can be then compared with those of the proposed model.

#### **5. Health check and stress test the model**

Also, make sure that the model possesses the basic properties that all derivatives models should possess, such as put–call parity and other nonarbitrage conditions. Finally, the vetter should stress-test the model. The model can be stress-tested by looking at some limit scenario, in order to identify the range of parameter values for which the model provides accurate pricing. This is especially important for implementations that rely on numerical techniques.

### **6. Build a formal treatment of model risk into the overall risk management procedures, and periodically reevaluate models**

Also, reestimate parameters using best-practice statistical procedures. Experience shows that simple, but robust models tend to work better than more ambitious, but fragile models. It is essential to monitor and control model performance over time.

## **Reference**

[1] Crouhy, M., Galai, D. & Mark, R. (2006). *The Essentials of Risk Management*, McGraw-Hill.

## **Related Articles**

#### **Backtesting**; **Models**.

MICHEL CROUHY, DAN GALAI & ROBERT MARK
# **Utility Theory: Historical** Perspectives

The first recorded mention of a concave utility function in the context of risk and uncertainty is in a manuscript of Daniel Bernoulli [4] in 1738, though credit should also be given to Gabriel Cramer, who, according to Bernoulli himself, developed a remarkably similar theory in 1728. Bernoulli proposes a resolution of a paradox posed in 1713 by his cousin Nicholas Bernoulli. Known as the St. Petersburg *paradox*, it challenges the idea that rational agents value random outcomes by their expected returns. Specifically, a game is envisioned in which a fair coin is tossed repeatedly and the payoff equals  $2^n$  ducats if the first *heads* appeared on the  $n$ th toss. The expected value of the payoff can be computed as

$$\frac{1}{2} \times 2 + \frac{1}{4} \times 4 + \frac{1}{8} \times 8 + \cdots$$
$$+ \frac{1}{2^n} \times 2^n + \cdots = +\infty \tag{1}$$

but, clearly, no one would pay an infinite, or even a large finite, amount of money for a chance to play such a game. Daniel Bernoulli suggests that the satisfaction or utility  $U(w)$  from a payoff of size w should not be proportional to  $w$  (as mandated by the then prevailing valuation by expectation), but should exhibit diminishing marginal returns; in contemporary language, the derivative  $U'$  of the function  $U$ should be decreasing (see Utility Function). Proposing a logarithmic function as a suitable  $U$ , Bernoulli suggests that the value of the game to the agent should be calculated as the expected utility

$$\frac{1}{2} \times \log(2) + \frac{1}{4} \times \log(4) + \frac{1}{8} \times \log(8) + \cdots$$
$$+ \frac{1}{2^n} \times \log(2^n) + \cdots = \log(4) \tag{2}$$

Bernoulli's theory was poorly accepted by his contemporaries. It was only a hundred years later that Herman Gossen [11] used Bernoulli's idea of diminishing marginal utility of wealth to formulate his "Laws of Economic Activity". Gossen's "Second law"—the idea that the ratio of exchange values of two goods must equal the ratio of marginal utilities of the traders-presaged, but did not directly influence, what will become known in economics as the "Marginalist revolution" led by William Jevons [13], Carl Menger [17], and Leon Walras [26].

## Axiomatization

The work of Gossen notwithstanding, another century passed before the scientific community took an interest in Bernoulli's ideas (with some notable exceptions such as Alfred Marshal [16] or Francis Edgeworth's entry on probability [8] in the celebrated 1911 edition of Encyclopedia Britannica). In 1936, Franz Alt published the first axiomatic treatment of decision making in which he deduces the existence of an implied utility function solely on the basis of a simple set of plausible axioms. Eight years later, Oskar Morgenstern and John von Neumann published the widely influential "Theory of Games and Economic Behavior" [25]. Along with other contributions—the most important representative being a mathematically rigorous foundation of game theory—they develop, at great length, a theory similar to Alt's. Both Alt's and the von Neumann-Morgenstern axiomatizations study a preference relation on the collection of all lotteries (probability distributions on finite sets of outcomes) and show that one lottery is preferred to the other if and only if the expected utility of the former is larger than the expected utility of the latter. The major conceptual leap accomplished by Alt, von Neumann, and Morgenstern was to show that the *behavior* of a rational agent necessarily coincides with the behavior of an agent who values uncertain payoffs using an expected utility.

### The Subjectivist Revolution and the **State-preference Approach**

All of the aforementioned derivations of the expected-utility hypothesis assumed the existence of a physical (objective) probability over the set of possible outcomes of the random payoff. An approach in which both the probability distribution and the utility function are determined jointly from simple behavioral axioms has been proposed by Leonard Savage [23], who was inspired by the work of Frank Ramsey [21] and Bruno de Finetti [5, 6].

One of the major features of the expected-utility theory is the separation between the utility function and the resolution of uncertainty, in that equal payoffs in different states of the world yield the same utilities. It has been argued that, while sometimes useful, such a separation is not necessary. An approach in which the utility of a payoff depends not only on its monetary value but also on the state of the world has been proposed. Such an approach has been popularized through the work of Kenneth Arrow [2] (*see* **Arrow, Kenneth**) and Gerard Debreu [7], largely because of its versatility and compatibility with general-equilibrium theory where the payoffs are not necessarily monetary. Further successful applications have been made by Roy Radner [20] and many others.

#### **Empirical Paradoxes and Prospect Theory**

With the early statistical evidence being mostly anecdotal, many empirical studies have found significant inconsistencies between the observed behavior and the axioms of utility theory. The most influential of these early studies were performed by George Shackle [24], Maurice Allais [1], and Daniel Ellsberg [9]. In 1979, Daniel Kahneman and Amos Tversky [14] proposed "prospect theory" as a psychologically more plausible alternative to the expected utility theory.

#### **Utility in Financial Theory**

The general notion of a numerical value associated with a risky payoff was introduced to finance by Harry Markowitz [15] (*see* **Markowitz, Harry**) through his influential "portfolio theory".

Markowitz's work made transparent the need for a precise measurement and quantitative understanding of the levels of "risk aversion" (degree of concavity of the utility function) in financial theory. Even though a similar concept had been studied by Milton Friedman and Leonard Savage [10] before that, the major contribution to this endeavor was made by John Pratt [19] and Kenneth Arrow [3].

With the advent of stochastic calculus (developed by Kiyosi Ito [12], ˆ *see* **Ito, Kiyosi (1915–2008) ˆ** ), the mathematical tools for continuous-time financial modeling became available. Paul Samuelson [22] (*see* **Samuelson, Paul A.**) introduced geometric Brownian motion as a model for stock evolution, and it was not long before it was combined with expected utility theory in the work of Robert Merton [18] (*see* **Merton, Robert C.**).

#### **References**

- [1] Allais, M. (1953). La psychologie de l'home rationnel devant le risque: critique des postulats et axiomes de l'ecole Am ´ ericaine, ´ *Econometrica* **21**(4), 503–546. Translated and reprinted in Allais and Hagen, 1979.
- [2] Arrow, K.J. (1953). Le Role des valeurs boursi ˆ eres pour ` la Repartition la meilleure des risques, ´ *Econom´etrie,* Colloques Internationaux du Centre National de la Recherche Scientifique, Paris **11**, 41–47; Published in English as (1964). The role of securities in the optimal allocation of risk-bearing, *Review of Economic Studies* **31**(2), 91–96.
- [3] Arrow, K.J. (1965). *Aspects of the Theory of Risk-Bearing*, Yrjo Jahnsson Foundation, Helsinki. ¨
- [4] Bernoulli, D. (1954). Exposition of a new theory on the measurement of risk, *Econometrica* **22**(1), 23–36. Translation from the Latin by Dr. Louise Sommer of work first published 1738.
- [5] de Finetti, B. (1931). Sul significato soggettivo della probabilita,` *Fundamenta Mathematicae* **17**, 298–329.
- [6] de Finetti, B. (1937). La prevision: ses lois logiques, ses ´ sources subjectives, *Annales de l'Institut Henri Poincar´e* **7**(1), 1–68.
- [7] Debreu, G. (1959). *Theory of Value—An Axiomatic Analysis of Economic Equilibrium*, Cowles Foundation Monograph # 17, Yale University Press.
- [8] Edgeworth, F.Y. (1911). *Probability and Expectation*, Encyclopedia Britannica.
- [9] Ellsberg, D. (1961). Risk, ambiguity and the Savage axioms, *Quarterly Journal of Economics* **75**, 643–69.
- [10] Friedman, M. & Savage, L.P. (1952). The expectedutility hypothesis and the measurability of utility, *Journal of Political Economy* **60**, 463–474.
- [11] Gossen, H.H. (1854). *The Laws of Human Relations and the Rules of Human Action Derived Therefrom*, MIT Press, Cambridge, 1983. Translated from 1854 original by Rudolph C. Blitz with an introductory essay by Nicholas Georgescu-Roegen.
- [12] Ito, K. (1942). On stochastic processes. I. (Infinitely ˆ divisible laws of probability), *Japan. Journal of Mathematics* **18**, 261–301.
- [13] Jevons, W.S. (1871). *The Theory of Political Economy*. History of Economic Thought Books, McMaster University Archive for the History of Economic Thought.
- [14] Kahneman, D. & Tversky, A. (1979). Prospect theory: an analysis of decision under risk, *Econometrica* **47**(2), 263–292.
- [15] Markowitz, H. (1952). Portfolio selection, *Journal of Finance* **7**(1), 77–91.
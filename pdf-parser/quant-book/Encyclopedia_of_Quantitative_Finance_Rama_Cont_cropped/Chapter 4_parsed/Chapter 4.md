# **Mandelbrot, Benoit**

![](_page_0_Picture_1.jpeg)

Benoit B. Mandelbrot, Sterling Professor Emeritus of Mathematical Sciences at Yale University and IBM Fellow Emeritus at the IBM Research Center, best known as the "father of fractal geometry", is a Polish-born French-American multidisciplinary scientist with numerous contributions to different fields of knowledge including mathematics, statistics, hydrology, physics, engineering, physiology, economics and, last but not least, quantitative finance. In this short text we will focus on Mandelbrot's contributions to the study of financial markets.

Benoit Mandelbrot was born in Warsaw, Poland, on November 20, 1924 in a family of scholars from Lituania. In 1936 Mandelbrot's family moved to Paris, where he was influenced by his mathematician uncle Szolem Mandelbrojt (1899–1983). He entered the Ecole Polytechnique in 1944. Among his professors at Polytechnique was Paul Levy, whose pioneering work on stochastic processes influenced Mandelbrot.

After two years in Caltech and after obtaining a doctoral degree in mathematics from University of Paris in 1952, he started his scientific career at the Centre National de la Recherche Scientifique in Paris, before moving on various scientific appointments which included those at Ecole Polytechnique, Universite de Lille, the University of Geneva MIT, Princeton, University of Chicago, and finally the IBM Thomas J. Watson Research Center in Yorktown Heights, New York and Yale University where he spent the longer part of his career.

A central thread in his scientific career is the "ardent pursuit of the concept of roughness" which resulted in a rich theoretical apparatus—fractal and multifractal geometry—whose aim is to describe and represent the order hidden in apparently wildly disordered and random phenomena ranging from the geometry of coastlines to the variation of foreign exchange rates. In his own words

The roughness of clusters in the physics of disorder, of turbulent flows, of exotic noises, of chaotic dynamical systems, of the distribution of galaxies, of coastlines, of stock price charts, and of mathematical constructions,—these have typified the topics I studied.

He formalized the notion of 'fractal process'—and later, that of multifractal [13]—which provided a tool for quantifying the "degree of irregularity" of various random phenomena in mathematics, physics, and economics.

Benoit Mandelbrot's numerous awards include the 1993 *Wolf Prize for Physics* and the 2003 *Japan Prize for Science and Technology*, the 1985 *F. Barnard Medal for Meritorious Service to Science* ("Magna est Veritas") of the US National Academy of Sciences, the 1986 *Franklin Medal for Signal and Eminent Service in Science* of the Franklin Institute of Philadelphia, the 1988 *Charles Proteus Steinmetz Medal* of IEEE, the 2004 *Prize of Financial Times/Deutschland,* and a *Humboldt Preis* from the Alexander von Humboldt Stiftung.

### **From Mild to Wild Randomness: The Noah Effect**

Mandelbrot developed an early interest in the stochastic modeling of financial markets. Familiar with the work of Louis Bachelier (*see* **Bachelier, Louis (1870–1946)**), Mandelbrot published a series of pioneering studies [6–8, 21] on the tail behavior of the distribution of price variations, where he advocated the use of heavy-tailed distributions and scale-invariant Levy processes for modeling price ´ fluctuations. The discovery of the heavy-tailed nature of price movements led him to coin the term "wild randomness" for describing market behavior, as opposed to the "mild randomness" represented by Bachelier's Brownian model, which later became the standard approach embodied in the Black–Scholes model. Mandelbrot likened the sudden bursts of volatility in financial markets to the "Noah effect", by analogy with the flood which destroys the world in Noah's biblical story:

In science, all important ideas need names and stories to fix them in the memory. It occurred to me that the market's first wild trait, abrupt change or discontinuity, is prefigured in the tale of Noah. As Genesis relates, in Noah's six-hundredth year God ordered the Great Flood to purify a wicked world. [*...*] The flood came and went, catastrophic but transient. Market crashes are like that : at times, even a great bank or brokerage house can seem like a little boat in a big storm.

### **Long-range Dependence: The Joseph Effect**

Another early insight of Mandelbrot's studies of financial and economic data was the presence of longrange dependence [9–11] in market fluctuations:

The market's second wild trait—almost cycles—is prefigured in the story of Joseph. The Pharaoh dreamed that seven fat cattle were feeding in the meadows, when seven lean kine rose out of the Nile and ate them. [*...*] Joseph, a Hebrew slave, called the dreams prophetic : Seven years of famine would follow seven years of prosperity. [*...*] Of course, this is not a regular or predictable pattern. But the appearance of one is strong. Behind it is the influence of long-range dependence in an otherwise random process or, put another way, a long-term memory through which the past continues to influence the random fluctuations of the present. I called these two distinct forms of wild behavior the Noah effect and the Joseph effect. They are two aspects of one reality.

Building on his earlier work Mandelbrot [22, 23] on long-range dependence in hydrology and fractional Brownian motion, he proposed the use of fractional processes for modeling long-range dependence and scaling properties of economic quantities (*see* **Long Range Dependence**).

## **Multifractal Models and Stochastic Time Changes**

In a series of papers [2, 4, 20] with Adlai Fisher and Laurent Calvet, Mandelbrot studied the scaling properties of the US/DEM foreign exchange rate at frequencies ranging from a few minutes to weeks and, building on earlier work by Clark [3] and Mandelbrot [12, 13], introduced a new family of stochastic models, where the (log) price of an asset is represented by a time-changed fractional Brownian motion, where the time change, representing market

activity, is given by a multifractal (*see* **Multifractals**) increasing process (*see* **Mixture of Distribution Hypothesis**; **Time Change**) [5, 15]:

The key step is to introduce an auxiliary quantity called *trading time*. The term is self-explanatory and embodies two observations. While price changes over fixed clock time intervals are long-tailed, price changes between successive transactions stay near-Gaussian over sometimes long period between discontinuities. Following variations in the trading volume, the time interval between successive transactions vary greatly. Thissuggests that trading time is related to volume.

The topic of multifractal modeling in finance was further developed in [1, 17–19]; a nontechnical account is given in [16].

Mandelbrot's work in quantitative finance has been generally 20 years ahead of its time: many of his ideas proposed in the 1960s—such as longrange dependence, volatility clustering, and heavy tails—became mainstream in financial modeling in the 1990s. If this is anything of a pattern, his more recent work in the field might deserve a closer look. Perhaps, one of the most important insights of his work on financial modeling is to *closely examine* the empirical features of data before axiomatizing and writing down complex equations, a timeless piece of advice which can be a useful guide for quantitative modeling in finance.

Mandelbrot's work in finance is summarized in the books [14, 15] and a popular account of this work is given in the book [5].

#### **References**

- [1] Barral, J. & Mandelbrot, B. (2002). Multifractal products of cylindrical pulses, *Probability Theory and Related Fields* **124**, 409–430.
- [2] Calvet, L., Fisher, A. & Mandelbrot, B. (1997). *Large Deviations and the Distribution of Price Changes*. Cowles Foundation Discussion Papers: 1165.
- [3] Clark, P.K. (1973). A subordinated stochastic process model with finite variance for speculative prices, *Econometrica* **41**(1), 135–155.
- [4] Fisher, A., Calvet, L.M. & Mandelbrot, B. (1997). *Multifractality of the Deutschmark/US Dollar exchange rates*. Cowles Foundation Discussion Papers: 1166.
- [5] Hudson, R.L. (2004). *The (Mis)behavior of Prices: A Fractal View of Risk, Ruin, and Reward*, Basic Books, New York, & Profile Books, London, pp. xxvi + 329.
- [6] Mandelbrot, B. (1962). Sur certains prix speculatifs: faits ´ empiriques et modele bas ` e sur les processus stables ´
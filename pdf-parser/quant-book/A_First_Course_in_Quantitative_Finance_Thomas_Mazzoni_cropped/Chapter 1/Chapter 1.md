✖

## **1 Introduction**

Modern financial markets have come a long way from ancient bartering. They are highly interconnected, the information is very dense, and reaction to external events is almost instantaneous. Even though organized markets have existed for a very long time, this level of sophistication was not realized before the second half of the last century. The reason is that sufficient computing power and broadband internet coverage is necessary to allow a market to become a global organic structure. It is not surprising that such a self-organizing structure reveals new rules like for example the no arbitrage principle. What is surprising is that not only the rules, but also the purpose of the whole market seems to have changed. Nowadays, one of the primary objectives of an operational and liquid financial market is risk transfer. There are highly sophisticated instruments like options, swaps, and so forth, designed to decouple all sorts of risks from the underlying contract, and trade them separately. That way market participants can realize their individually desired level of insurance by simply trading the risk. Such a market is certainly not dominated by gambling or speculation, as suggested by the news from time to time, but indeed obeys some very fundamental and deep mathematical principles and is best analyzed using tools from probability theory, econometrics, and engineering.

Unfortunately the required mathematical machinery is not part of the regular education of economists. So the better part of this fascinating field is often reserved to trained mathematicians, physicists, and statisticians. The tragedy is that economists have much to contribute, because they are usually the only ones trained in the economic background and the appropriate way of thinking. It is not easy to bridge the gap, because often economists and mathematicians speak a very different language. Nevertheless, the fundamental structures and principles generally possess more than one representation. They can be proved mathematically, described geometrically, and be understood economically. It is thus the goal of this book to navigate through the equivalent descriptions, avoiding unnecessary technicalities, to provide an unobstructed view on those deep and elegant principles, governing modern financial markets.

## **About This Book**

This book consists of four parts and an appendix, containing a short introduction to complex analysis. Part I provides some basics in probability theory, vector spaces, and utility theory, with strong reference to the geometrical view. The emphasis of those chapters is not on a fully rigorous exposition of measure theory or *Hilbert*-spaces, but on intuitive notation, visualization, and association with familiar concepts like length

**• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •**

## **2 Introduction**

and geometric forms. Part II deals with the fundamental structure of financial markets, the no arbitrage principle, and classical portfolio theory. A large number of scientists in this field received the Noble Prize for their pioneering work. Models like the capital asset pricing model (CAPM) and the arbitrage pricing theory (APT) are still cornerstones of portfolio management and asset pricing. Furthermore, some of the most famous puzzles in economic theory are discussed. In Part III, the reader enters the world of derivative pricing. There is no doubt that this area is one of the mathematically most intense in quantitative finance. The high level of sophistication is due to the fact that prices of derivative contracts depend on future prices of one or more underlying securities. Such an underlying may as well be another derivative contract. It is also in this area that one experiences the consequences of incomplete markets very distinctly. Thus, approaches to derivative pricing in incomplete markets are also discussed extensively. Finally, Part IV is devoted to fixed-income markets and their derivatives. This is in some way the supreme discipline of quantitative finance. In ordinary derivative pricing, the fundamental quantities are prices of underlying securities, which can be understood as single zero-dimensional objects. In pricing fixed-income derivatives, the fundamental quantities are the yield or forward curve, respectively. They are one-dimensional objects in this geometric view. That makes life considerably more complicated, but also more exciting.

This book is meant as an undergraduate introduction to quantitative finance. It is based on a series of lectures I have given at the University of Greifswald since 2012. In teaching economics students I learned very rapidly that it is of vital importance to provide a basis for the simultaneous development of technical skills and substantial concepts. Much of the necessary mathematical framework is therefore developed along the way to allow the reader to make herself acquainted with the theoretical background step by step.

To support this process, there are lots of short exercises called "quick calculations." Here is an example: Suppose we are talking about the binomial formulas you know from high school, in particular the third one

$$(a+b)(a-b) = a2 - b2.$$
 (1.1)

Now it's your turn.

**Quick calculation 1.1** Show that 899 is not a prime number.

If you are looking for factors by trial and error, this surely will be no quick calculation and you are on the wrong track. At least you missed something, in this case that 899 = 30<sup>2</sup> − 1 2 , and thus 31 and 29 have to be factors.

There are also more intense exercises at the end of each chapter. Their level of difficulty is varying and you should not feel bad if you cannot solve them all without stealing a glance at the solutions. Some of them are designed to train you in explicit computations. Others provide additional depth and background information on some topics in the respective chapter, and still others push the concepts discussed a little bit further, to give you a sneak preview of what is to come.

![](_page_2_Figure_1.jpeg)

**Fig. 1.1** 3D Stereoscopic image – Space of arbitrage opportunities *K* and complete market *M*

In a highly technical field like quantitative finance, it is often unavoidable that we work with three-dimensional figures and graphs. To preserve the spatial perception, these graphics are provided as stereoscopic images. You can visualize them without 3Dglasses or other fancy tools. All it takes is a little getting used to. Whenever you see the 3D icon in a caption, it means that the figure is a stereoscopic image. Figure 1.1 is such an image; I borrowed it from a later chapter. At first sight, you will hardly recognize any difference between the two graphs, and you can retrieve all the information from either one of them. But if you follow the subsequent steps, you can explore the third dimension:

- 1. Slightly increase your usual reading distance and concentrate on the center between the two images, while pretending to look straight through the book, focusing on an imaginary distant point. You will see both images moving towards each other and finally merging.
- 2. If you have achieved perfect alignment, you will see one image at the center and two peripheral ghost images, that your brain partially blends out. Try to keep the alignment, while refocusing your vision to see the details sharply.
- 3. If you have difficulties keeping the alignment, try to increase the distance to about half a meter until you get a feeling for it. Don't tilt your head or it is all over.

Your brain is probably not used to controlling ocular alignment and lens accommodation independently, so it may take a little bit of practice, but it is real fun. So give it a try.

My goal in writing this book was to make the sometimes strange, but always fascinating world of modern financial markets accessible to undergraduate students with a little bit of mathematical and statistical background. Needless to say that quantitative finance is such an extensive field that this first course can barely scratch the surface. But the really fundamental principles are not that hard to grasp and exploring them is like a journey through a century of most elegant ideas. So I hope you enjoy it.
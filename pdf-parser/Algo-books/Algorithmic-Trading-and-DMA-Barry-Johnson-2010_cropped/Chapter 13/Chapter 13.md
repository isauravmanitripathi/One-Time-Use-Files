## Addendum A: Covariance

Covariance is just a measure of how much two variables  $I$  and  $J$  vary together:

$$Cov (I, J) = E((I - \mu)(J - \nu))$$

where the function  $E()$  represents the expected value (or mean), and variables  $\mu$  and v are the respective mean values for variables  $I$  and  $J$ . A positive covariance means that the two items vary together, so if the value of  $I$  is more than its average then it is likely that  $J$  will also have a higher than normal value. Conversely, a negative covariance means that they behave in opposite fashions, so a high value for one implies a lower expected value for the other. A covariance of zero shows that the items are completely independent, so no inference may be made from either value.

Sometimes the relationship between variables is compared using the correlation coefficient ( $\rho$ ). Essentially, this is their covariance divided by the product of their standard deviations:

$$\rho_{i,j} = \frac{Cov(I,J)}{\sigma_i \sigma_j} = \frac{E((I - \mu_i)(J - \mu_j))}{\sigma_i \sigma_j}$$
(12-9)

where  $\mu_i$ ,  $\mu_j$  and  $\sigma_i$ ,  $\sigma_j$  are the means and standard deviations of variables I and J respectively.

**Example 12-3:** Let's determine the covariance between the four assets whose sample prices are shown in Table 12-8.

| i            | Price series |      |      |      |      |      |      |      |         | $\mu$ | σ    |      |
|--------------|--------------|------|------|------|------|------|------|------|---------|-------|------|------|
|              |              |      |      | 4    |      | 6    |      |      |         | 10    |      |      |
| Α            | 3.50         | 3.50 | 3.28 | 3.34 | 3.69 | 3.86 | 3.58 | 3.69 | 17<br>2 |       | 3.47 | 0.06 |
| $\mathbf{B}$ | 4.41         | 4.42 | 4.28 | 4.34 | 4.69 | 4.86 | 4.58 | 5.00 | 4.22    | 4.03  | 4.48 | 0.09 |
|              | 5.42         | 5.54 | 5.58 | 5.68 | 5.44 | 5.03 | 5.82 | 5.93 | 5.61    | 5.94  | 5.60 | 0.07 |
|              | 6.42         | 6.54 | 6.58 | 6.34 | 6.69 | 6.86 | 6,58 | 6.93 | 6.30    | 6.94  | 6.62 | 0.05 |

Table 12-8 Sample time series for covariance calculation

Table 12-9 shows the intermediate calculations for determining the covariance between the prices of assets A and B.  $\Delta_A$  corresponds to the series of differences to the mean ( $\mu$ ).

|                     | Series  |         |         |              |      |      |                         |      |                 |          |  |  |
|---------------------|---------|---------|---------|--------------|------|------|-------------------------|------|-----------------|----------|--|--|
|                     |         |         |         | $\mathbf{L}$ |      |      |                         |      |                 | 10       |  |  |
| $\Delta_A$          | 0.02    | 0.03    | $-0.19$ | $-0.13$      | 0.22 | 0.39 | A 11<br>$\upsilon$ . I. | 0.22 | .35<br>$\Omega$ | $-0.30$  |  |  |
| $\Delta_{\rm R}$    | $-0.07$ | $-0.07$ | $-0.20$ | $-0.14$      | 0.21 | 0.38 | 0.10                    | 0.52 | $-0.26$         | $-0.46$  |  |  |
| $\Delta_A \Delta_B$ | 0.00    | 0.00    | 0.04    | 0.02         | 0.05 | 0.15 | 0.01                    | 0.1  | 0.09            | 0.<br>14 |  |  |

Table 12-9 Sample intermediate calculations for covariance

The sample covariance for assets A and B is equal to the sum  $\Sigma(\Delta_A \Delta_B)$  adjusted by dividing by  $(n-1)$  where *n* is the sample size:

 $Cov(A,B) = \Sigma(\Delta_A \Delta_B) / (n-1)$  $=(0+0+0.04+0.02+0.05+0.15+0.01+0.11+0.09+0.14)/9$  $= 0.07$ 

This process is then repeated for all the other possible combinations.

Note that  $Cov(A, B) = Cov(B, A)$ , similarly  $Cov(A, A) = Variance(A)$  or  $\sigma^2$  as shown in Table 12-8. Hence, the covariance matrix  $(\Omega)$  for this example set may be defined as:

$$\Omega = \begin{pmatrix}\n0.06 & 0.07 & -0.03 & 0.02 \\
0.07 & 0.09 & -0.02 & 0.03 \\
-0.03 & -0.02 & 0.07 & 0.01 \\
0.02 & 0.03 & 0.01 & 0.05\n\end{pmatrix}$$
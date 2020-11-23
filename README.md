# Week 13 Assignment A

In class we have discussed the binomial distribution function 

<a href="https://www.codecogs.com/eqnedit.php?latex=b_{n,p}(k)=\begin{pmatrix}&space;n\\&space;k&space;\end{pmatrix}p^k\left(1-p\right)^{n-k}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?b_{n,p}(k)=\begin{pmatrix}&space;n\\&space;k&space;\end{pmatrix}p^k\left(1-p\right)^{n-k}" title="b_{n,p}(k)=\begin{pmatrix} n\\ k \end{pmatrix}p^k\left(1-p\right)^{n-k}" /></a>

where the two parameters of the function are <a href="https://www.codecogs.com/eqnedit.php?latex=p" target="_blank"><img src="https://latex.codecogs.com/gif.latex?p" title="p" /></a>, the probability of success in one trial, and <a href="https://www.codecogs.com/eqnedit.php?latex=n" target="_blank"><img src="https://latex.codecogs.com/gif.latex?n" title="n" /></a>, the number of trials, and the possible values of the integer argument <a href="https://www.codecogs.com/eqnedit.php?latex=k" target="_blank"><img src="https://latex.codecogs.com/gif.latex?k" title="k" /></a> go from 0 to <a href="https://www.codecogs.com/eqnedit.php?latex=n" target="_blank"><img src="https://latex.codecogs.com/gif.latex?n" title="n" /></a>. Remember that the notation 

<a href="https://www.codecogs.com/eqnedit.php?latex=\binom{n}{k}=\frac{n!}{k!\left(n-k&space;\right&space;)!}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\binom{n}{k}=\frac{n!}{k!\left(n-k&space;\right&space;)!}" title="\binom{n}{k}=\frac{n!}{k!\left(n-k \right )!}" /></a>

refers to the binomial coefficient.  

Tasks: 
1. Write a function to compute the binomial distribution for any possible value of the its parameters. 
2. Given the bins and frequencies of the distribution, compute the total sum of frequencies of the distribution: <a href="https://www.codecogs.com/eqnedit.php?latex=\sum_{k=0}^{n}b_{n,p}(k)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\sum_{k=0}^{n}b_{n,p}(k)" title="\sum_{k=0}^{n}b_{n,p}(k)" /></a>
3. Compute around which value of <a href="https://www.codecogs.com/eqnedit.php?latex=k" target="_blank"><img src="https://latex.codecogs.com/gif.latex?k" title="k" /></a> the distribution is centered (i.e. the average of the distribution): <a href="https://www.codecogs.com/eqnedit.php?latex=\bar{k}=\sum_{k=0}^{n}k\:b_{n,p}(k)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\bar{k}=\sum_{k=0}^{n}k\:b_{n,p}(k)" title="\bar{k}=\sum_{k=0}^{n}k\:b_{n,p}(k)" /></a>
4. Compute the spread of the distribution: <a href="https://www.codecogs.com/eqnedit.php?latex=\sigma^2=\sum_{k=0}^{n}\left(k-\bar{k}\right&space;)^2b_{n,p}(k)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\sigma^2=\sum_{k=0}^{n}\left(k-\bar{k}\right&space;)^2b_{n,p}(k)" title="\sigma^2=\sum_{k=0}^{n}\left(k-\bar{k}\right )^2b_{n,p}(k)" /></a>

Outcomes: Compare the results obtained on the binomial distribution with the ones of the stochastic process that follows the same distribution. Can you evaluate the results in tasks 2-4 analytically? 

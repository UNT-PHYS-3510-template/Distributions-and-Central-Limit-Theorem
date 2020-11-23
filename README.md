# Week 14 Assignment A
Consider a population that is uniformly distributed in the \[0,1\) interval (i.e. it follows the a constant distribution where every value in the interval is equally probable). The distribution function is thus

<a href="https://www.codecogs.com/eqnedit.php?latex=r(x)=\begin{matrix}&space;1&space;&&space;\text{for&space;}&space;x\in\left[0,1&space;\right)\\&space;0&space;&&space;\text{otherwise}&space;\end{matrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r(x)=\begin{matrix}&space;1&space;&&space;\text{for&space;}&space;x\in\left[0,1&space;\right)\\&space;0&space;&&space;\text{otherwise}&space;\end{matrix}" title="r(x)=\begin{matrix} 1 & \text{for } x\in\left[0,1 \right)\\ 0 & \text{otherwise} \end{matrix}" /></a>

Python has several modules that allow you to sample this distribution, i.e. to generate values of x with a probability given by the distribution function. Although the random module has its own function to sample the above distribution (can you find out which one?), you should be using the numpy.random.random() function. This is because this function has an optional argument that allows you to specify how many points you want to generate and the function will put its output directly into a numpy array.

Tasks: 
1. Write a python function that evaluates the given distribution function.
2. Derive the analytic expressions of the mean and standard deviation of the given distribution
function. Since the function is defined on a continuous variable in the \[0,1\) interval, you should be using the following formulas

<a href="https://www.codecogs.com/eqnedit.php?latex=\mu=\int_0^1r(x)\:x\:dx" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\mu=\int_0^1r(x)\:x\:dx" title="\mu=\int_0^1r(x)\:x\:dx" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\sigma^2=\int_0^1r(x)\:(x-\mu)^2\:dx" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\sigma^2=\int_0^1r(x)\:(x-\mu)^2\:dx" title="\sigma^2=\int_0^1r(x)\:(x-\mu)^2\:dx" /></a>

3. Plot the function in its relevant range
4. Use the numpy.random.random() function to sample points from the distribution. Generate one sample with n=10 points and plot its frequency distribution.
5. Generate 100 samples with n=10 points. For each sample compute its mean. Collect all the means of the different samples and compute (and plot) the frequency distribution of the means of the samples (i.e. the sampling distribution of the mean).
6. Compare the computed distribution with the result of the central limit theorem.
7. Using the one sample obtained in step 4, write the sample estimate of the mean of the population and the associated error (95% confidence).

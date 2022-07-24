# Chapter 2
# Distributions

#Make a PMF
#Make a PMF for year with normalize=False and display the result.
# Compute the PMF for year
pmf_year = Pmf(gss['year'], normalize=False)

# Print the result
print(pmf_year)

#Plot a PMF
#Select the 'age' column from the gss DataFrame and store the result in age.

#Make a normalized PMF of age. Store the result in pmf_age.
# Select the age column
age = gss['age']

# Make a PMF of age
pmf_age = Pmf(age)

#Plot pmf_age as a bar chart.
# Select the age column
age = gss['age']

# Make a PMF of age
pmf_age = Pmf(age)

# Plot the PMF
pmf_age.bar()

# Label the axes
plt.xlabel('Age')
plt.ylabel('PMF')
plt.show()

#Make a CDF
#Select the 'age' column. Store the result in age.
# Select the age column
age = gss['age']

# Compute the CDF of age
cdf_age = Cdf(age)

# Calculate the CDF of 30
print(cdf_age(30))

#Compute IQR
#Calculate the 75th percentile of income and store it in percentile_75th.
# Calculate the 75th percentile 
p = 0.75
percentile_75th = cdf_income.inverse(p)
print(percentile_75th)

#Calculate the 25th percentile of income and store it in percentile_25th.
# Calculate the 75th percentile 
percentile_75th = cdf_income.inverse(0.75)

#Calculate the interquartile range of income. Store the result in iqr.
# Calculate the 25th percentile
percentile_25th = cdf_income.inverse(0.25)

# Calculate the 75th percentile 
percentile_75th = cdf_income.inverse(0.75)

# Calculate the 25th percentile
percentile_25th = cdf_income.inverse(0.25)

# Calculate the interquartile range
iqr = percentile_75th - percentile_25th

# Print the interquartile range
print(iqr)

#Plot a CDF
''''
Select 'realinc' from the gss dataset.
Make a Cdf object called cdf_income.
Create a plot of cdf_income using .plot().
'''
# Select realinc
income = gss['realinc']

# Make the CDF
cdf_income = Cdf(income)

# Plot it
cdf_income.plot()

# Label the axes
plt.xlabel('Income (1986 USD)')
plt.ylabel('CDF')
plt.show()

#Extract education levels
# Select educ
educ = gss['educ']

# Bachelor's degree
bach = (educ >= 16)

# Associate degree
assc = (educ >= 14) & (educ < 16)

# High school
high = (educ <= 12)
print(high.mean())

#Plot income CDFs
#Fill in the missing lines of code to plot the CDFs.
income = gss['realinc']

# Plot the CDFs
Cdf(income[high]).plot(label='High school')
Cdf(income[assc]).plot(label='Associate')
Cdf(income[bach]).plot(label='Bachelor')

# Label the axes
plt.xlabel('Income (1986 USD)')
plt.ylabel('CDF')
plt.legend()
plt.show()

#Distribution of income
''''
Extract 'realinc' from gss and compute its logarithm using np.log10().
Compute the mean and standard deviation of the result.
Make a norm object by passing the computed mean and standard deviation to norm().
'''
# Extract realinc and compute its log
income = gss['realinc']
log_income = np.log10(income)

# Compute mean and standard deviation
mean = log_income.mean()
std = log_income.std()
print(mean, std)

# Make a norm object
from scipy.stats import norm
dist = norm(0, 1)

#Comparing CDFs
''''
Evaluate the normal cumulative distribution function using dist.cdf.
Use the Cdf() function to compute the CDF of log_income.
Plot the result.
'''
# Evaluate the model CDF
xs = np.linspace(2, 5.5)
ys = dist.cdf(xs)

# Plot the model CDF
plt.clf()
plt.plot(xs, ys, color='gray')

# Create and plot the Cdf of log_income
Cdf(log_income).plot()
    
# Label the axes
plt.xlabel('log10 of realinc')
plt.ylabel('CDF')
plt.show()

#Comparing PDFs
''''
Evaluate the normal PDF using dist, which is a norm object with the same mean and standard deviation as the data.
Make a KDE plot of the logarithms of the incomes, using log_income, which is a Series object.
'''
# Evaluate the normal PDF
xs = np.linspace(2, 5.5)
ys = dist.pdf(xs)

# Plot the model PDF
plt.clf()
plt.plot(xs, ys, color='gray')

# Plot the data KDE
sns.kdeplot(log_income)

# Label the axes
plt.xlabel('log10 of realinc')
plt.ylabel('PDF')
plt.show()
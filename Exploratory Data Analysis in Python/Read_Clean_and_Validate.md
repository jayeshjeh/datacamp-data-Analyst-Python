# Chapter 1
# Read, clean, and validate

#Exploring the NSFG data

#Calculate the number of rows and columns in the DataFrame nsfg.
nsfg.shape

#Display the names of the columns in nsfg.
nsfg.columns

#Select the column 'birthwgt_oz1' and assign it to a new variable called ounces.
# Select column birthwgt_oz1: ounces
ounces = nsfg['birthwgt_oz1']

#Display the first 5 elements of ounces.
# Print the first 5 elements of ounces
print(ounces.head())

#Clean a variable
''''
In the 'nbrnaliv' column, replace the value 8, in place, with the special value NaN.
Confirm that the value 8 no longer appears in this column by printing the values and their frequencies.
'''
# Replace the value 8 with NaN
nsfg['nbrnaliv'].replace(8, np.nan, inplace=True)

# Print the values and their frequencies
print(nsfg['nbrnaliv'].value_counts())

#Compute a variable
''''
Select 'agecon' and 'agepreg', divide them by 100, and assign them to the local variables agecon and agepreg.
'''
# Select the columns and divide by 100
agecon = nsfg['agecon'] / 100
agepreg = nsfg['agepreg'] / 100

#Compute the difference, which is an estimate of the duration of the pregnancy. Keep in mind that for each pregnancy, agepreg will be larger than agecon.
# Select the columns and divide by 100
agecon = nsfg['agecon'] / 100
agepreg = nsfg['agepreg'] / 100

# Compute the difference
preg_length = agepreg-agecon

#Use .describe() to compute the mean duration and other summary statistics.
# Select the columns and divide by 100
agecon = nsfg['agecon'] / 100
agepreg = nsfg['agepreg'] / 100

# Compute the difference
preg_length = agepreg - agecon

# Compute summary statistics
print(preg_length.describe())

#Make a histogram
#Plot a histogram of agecon with 20 bins.

# Plot the histogram
plt.hist(agecon.dropna(), bins = 20)

# Label the axes
plt.xlabel('Age at conception')
plt.ylabel('Number of pregnancies')

# Show the figure
plt.show()

#Adapt your code to make an unfilled histogram by setting the parameter histtype to be 'step'.
# Plot the histogram
plt.hist(agecon, bins=20, histtype='step')

# Label the axes
plt.xlabel('Age at conception')
plt.ylabel('Number of pregnancies')

# Show the figure
plt.show()

#Compute birth weight
''''
Make a Boolean Series called full_term that is true for babies with 'prglngth' greater than or equal to 37 weeks.
Use full_term and birth_weight to select birth weight in pounds for full-term babies. Store the result in full_term_weight.
Compute the mean weight of full-term babies.
'''
# Create a Boolean Series for full-term babies
full_term = nsfg['prglngth'] >= 37

# Select the weights of full-term babies
full_term_weight = birth_weight[full_term]

# Compute the mean weight of full-term babies
print(full_term_weight.mean())

#Filter
''''
Use the variable 'nbrnaliv' to make a Boolean Series that is True for single births (where 'nbrnaliv' equals 1) and False otherwise.
Use Boolean Series and logical operators to select single, full-term babies and compute their mean birth weight.
For comparison, select multiple, full-term babies and compute their mean birth weight.
'''
# Filter full-term babies
full_term = nsfg['prglngth'] >= 37

# Filter single births
single = nsfg['nbrnaliv'] == 1

# Compute birth weight for single full-term babies
single_full_term_weight = birth_weight[single & full_term]
print('Single full-term mean:', single_full_term_weight.mean())

# Compute birth weight for multiple full-term babies
mult_full_term_weight = birth_weight[~single & full_term]
print('Multiple full-term mean:', mult_full_term_weight.mean())

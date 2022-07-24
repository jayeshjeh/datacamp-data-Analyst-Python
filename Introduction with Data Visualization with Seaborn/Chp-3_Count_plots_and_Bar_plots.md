# Chapter 3
# Visualizing a Categorical and a Quantitative Variable

#Count plots
#Use sns.catplot() to create a count plot using the survey_data DataFrame with "Internet usage" on the x-axis.
# Create count plot of internet usage
sns.catplot(x="Internet usage",data=survey_data,kind="count")

# Show plot
plt.show()

#Make the bars horizontal instead of vertical.
# Change the orientation of the plot
sns.catplot(y="Internet usage", data=survey_data,
            kind="count")

# Show plot
plt.show()

#Create column subplots based on "Age Category", which separates respondents into those that are younger than 21 vs. 21 and older.
# Create column subplots based on age category
sns.catplot(y="Internet usage", data=survey_data,
            kind="count", col="Age Category")

# Show plot
plt.show()

#Bar plots with percentages
#Use the survey_data DataFrame and sns.catplot() to create a bar plot with "Gender" on the x-axis and "Interested in Math" on the y-axis.
# Create a bar plot of interest in math, separated by gender
sns.catplot(x="Gender",y="Interested in Math",data=survey_data,kind="bar")


# Show plot
plt.show()

#Customizing bar plots
#Use sns.catplot() to create a bar plot with "study_time" on the x-axis and final grade ("G3") on the y-axis, using the student_data DataFrame.

# Create bar plot of average final grade in each study category
sns.catplot(x="study_time",y="G3",data=student_data,kind="bar")

# Show plot
plt.show()

#Using the order parameter, rearrange the categories so that they are in order from lowest study time to highest.
# Rearrange the categories
study_time=["<2 hours", "2 to 5 hours", "5 to 10 hours", ">10 hours"]

sns.catplot(x="study_time", y="G3",
            data=student_data,
            kind="bar",
            order=category_order)

# Show plot
plt.show()

#Update the plot so that it no longer displays confidence intervals.
# Turn off the confidence intervals
sns.catplot(x="study_time", y="G3",
            data=student_data,
            kind="bar",
            order=["<2 hours", 
                   "2 to 5 hours", 
                   "5 to 10 hours", 
                   ">10 hours"],
                   ci=None)

# Show plot
plt.show()

#Create and interpret a box plot
#Use sns.catplot() and the student_data DataFrame to create a box plot with "study_time" on the x-axis and "G3" on the y-axis. Set the ordering of the categories to study_time_order.

# Specify the category ordering
study_time_order = ["<2 hours", "2 to 5 hours", 
                    "5 to 10 hours", ">10 hours"]

# Create a box plot and set the order of the categories
sns.catplot(x="study_time",y="G3",data=student_data,kind="box",order=study_time_order)

# Show plot
plt.show()

#Omitting outliers
''''
Use sns.catplot() to create a box plot with the student_data DataFrame, putting "internet" on the x-axis and "G3" on the y-axis.
Add subgroups so each box plot is colored based on "location".
Do not display the outliers.
'''
# Create a box plot with subgroups and omit the outliers
sns.catplot(x="internet", y="G3",
            data=student_data,
            kind="box",
            hue="location",
            sym="")

# Show plot
plt.show()

#Adjusting the whiskers
#Adjust the code to make the box plot whiskers to extend to 0.5 * IQR. Recall: the IQR is the interquartile range.
# Set the whiskers to 0.5 * IQR
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=0.5)

# Show plot
plt.show()

#Change the code to set the whiskers to extend to the 5th and 95th percentiles.
# Extend the whiskers to the 5th and 95th percentile
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=[5,95])

# Show plot
plt.show()

#Change the code to set the whiskers to extend to the min and max values.
# Set the whiskers at the min and max values
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=[0,100])

# Show plot
plt.show()

#Customizing point plots
#Use sns.catplot() and the student_data DataFrame to create a point plot with "famrel" on the x-axis and number of absences ("absences") on the y-axis.
# Create a point plot of family relationship vs. absences
sns.catplot(x="famrel",y="absences",data=student_data,kind="point")

# Show plot
plt.show()

#Add "caps" to the end of the confidence intervals with size 0.2.
# Add caps to the confidence interval
sns.catplot(x="famrel", y="absences",
			data=student_data,
            kind="point",
            capsize=0.2)
        
# Show plot
plt.show()

#Remove the lines joining the points in each category.
# Remove the lines joining the points
sns.catplot(x="famrel", y="absences",
			data=student_data,
            kind="point",
            capsize=0.2,
            join=False)
            
# Show plot
plt.show()

#Point plots with subgroups
#Use sns.catplot() and the student_data DataFrame to create a point plot with relationship status ("romantic") on the x-axis and number of absences ("absences") on the y-axis. Create subgroups based on the school that they attend ("school")
# Create a point plot with subgroups
sns.catplot(x="romantic",y="absences",data=student_data,hue="school",kind="point")

# Show plot
plt.show()

#Turn off the confidence intervals for the plot.
# Turn off the confidence intervals for this plot
sns.catplot(x="romantic", y="absences",
			data=student_data,
            kind="point",
            hue="school",
            ci=None)

# Show plot
plt.show()

#Since there may be outliers of students with many absences, import the median function from numpy and display the median number of absences instead of the average.
# Import median function from numpy
from numpy import median

# Plot the median number of absences instead of the mean
sns.catplot(x="romantic", y="absences",
			data=student_data,
            kind="point",
            hue="school",
            ci=None,
            estimator=median)

# Show plot
plt.show()

#Modify the code to use relplot() instead of scatterplot().
# Change to use relplot() instead of scatterplot()
sns.relplot(x="absences", y="G3", 
                data=student_data)

# Show plot
plt.show()

#Modify the code to create one scatter plot for each level of the variable "study_time", arranged in columns.
# Change to make subplots based on study time
sns.relplot(x="absences", y="G3", 
            data=student_data,
            kind="scatter",
            col="study_time")

# Show plot
plt.show()

#Adapt your code to create one scatter plot for each level of a student's weekly study time, this time arranged in rows.
# Change this scatter plot to arrange the plots in rows instead of columns
sns.relplot(x="absences", y="G3", 
            data=student_data,
            kind="scatter", 
            row="study_time")

# Show plot
plt.show()

#Creating two-factor subplots
#Use relplot() to create a scatter plot with "G1" on the x-axis and "G3" on the y-axis, using the student_data DataFrame.
# Create a scatter plot of G1 vs. G3
sns.relplot(x="G1",y="G3",data=student_data,kind="scatter")

# Show plot
plt.show()

# Adjust to add subplots based on school support
sns.relplot(x="G1", y="G3", 
            data=student_data,
            kind="scatter",
            col="schoolsup",
            col_order=["yes","no"])

# Show plot
plt.show()

#Add row subplots based on whether the student received support from the family ("famsup"), ordered so that "yes" comes before "no". This will result in subplots based on two factors.
# Adjust further to add subplots based on family support
sns.relplot(x="G1", y="G3", 
            data=student_data,
            kind="scatter", 
            col="schoolsup",
            col_order=["yes", "no"],
            row="famsup",
            row_order=["yes","no"])

# Show plot
plt.show()

#Changing the size of scatter plot points
#Use relplot() and the mpg DataFrame to create a scatter plot with "horsepower" on the x-axis and "mpg" on the y-axis. Vary the size of the points by the number of cylinders in the car ("cylinders").
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create scatter plot of horsepower vs. mpg

sns.relplot(x="horsepower",y="mpg",data=mpg,size="cylinders",kind="scatter")


# Show plot
plt.show()

#To make this plot easier to read, use hue to vary the color of the points by the number of cylinders in the car ("cylinders").
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create scatter plot of horsepower vs. mpg
sns.relplot(x="horsepower", y="mpg", 
            data=mpg, kind="scatter", 
            size="cylinders",hue="cylinders")

# Show plot
plt.show()

#Changing the style of scatter plot points
''''
Use relplot() and the mpg DataFrame to create a scatter plot with "acceleration" on the x-axis and "mpg" on the y-axis. Vary the style and color of the plot points by country of origin ("origin").
'''
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a scatter plot of acceleration vs. mpg
sns.relplot(x="acceleration", y="mpg", 
            data=mpg, kind="scatter", 
            style="origin",hue="origin")



# Show plot
plt.show()

#Interpreting line plots
#Use relplot() and the mpg DataFrame to create a line plot with "model_year" on the x-axis and "mpg" on the y-axis.
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create line plot
sns.relplot(x="model_year",y="mpg",data=mpg,kind="line")

# Show plot
plt.show()

#Visualizing standard deviation with line plots
''''
Change the plot so the shaded area shows the standard deviation instead of the confidence interval for the mean.
'''
# Make the shaded area show the standard deviation
sns.relplot(x="model_year", y="mpg",
            data=mpg, kind="line",ci="sd")

# Show plot
plt.show()

#Plotting subgroups in line plots
''''
Use relplot() and the mpg DataFrame to create a line plot with "model_year" on the x-axis and "horsepower" on the y-axis. Turn off the confidence intervals on the plot.
'''
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create line plot of model year vs. horsepower
sns.relplot(x="model_year", y="horsepower",
            data=mpg, kind="line",ci=None)

# Show plot
plt.show()

''''
Create different lines for each country of origin ("origin") that vary in both line style and color.
'''
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Change to create subgroups for country of origin
sns.relplot(x="model_year", y="horsepower", 
            data=mpg, kind="line", 
            ci=None,hue="origin")

# Show plot
plt.show()

''''
Add markers for each data point to the lines.
Use the dashes parameter to use solid lines for all countries, while still allowing for different marker styles for each line.
'''
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Add markers and make each line have the same style
sns.relplot(x="model_year", y="horsepower", 
            data=mpg, kind="line", 
            ci=None, style="origin", 
            hue="origin",markers=True,dashes=False)

# Show plot
plt.show()
# Introduction to Data Visualization with Seaborn

# Chapter 1
# Introduction to Seaborn

#Making a scatter plot with lists
#Import Matplotlib and Seaborn using the standard naming convention.
# Import Matplotlib and Seaborn
import seaborn as sns
import matplotlib.pyplot as plt

#Create a scatter plot of GDP (gdp) vs. number of phones per 1000 people (phones).
# Create scatter plot with GDP on the x-axis and number of phones on the y-axis
sns.scatterplot(x=gdp, y=phones)

#Display the plot.
# Show plot
plt.show()

#Change the scatter plot so it displays the percent of the population that can read and write (percent_literate) on the y-axis.
# Change this scatter plot to have percent literate on the y-axis
sns.scatterplot(x=gdp, y=percent_literate)

# Show plot
plt.show()

#Making a count plot with a list
''''
Import Matplotlib and Seaborn using the standard naming conventions.
Use Seaborn to create a count plot with region on the y-axis.
Display the plot.
'''
# Import Matplotlib and Seaborn
import seaborn as sns
import matplotlib.pyplot as plt

# Create count plot with region on the y-axis
sns.countplot(y=region)

# Show plot
plt.show()

#"Tidy" vs. "untidy" data
''''
Read the csv file located at csv_filepath into a DataFrame named df.
Print the head of df to show the first five rows.
'''
# Import Pandas
import pandas as pd

# Create a DataFrame from csv file
df = pd.read_csv(csv_filepath)

# Print the head of df
print(df.head())

#Making a count plot with a DataFrame
''''
Import Matplotlib, Pandas, and Seaborn using the standard names.
Create a DataFrame named df from the csv file located at csv_filepath.
Use the countplot() function with the x= and data= arguments to create a count plot with the "Spiders" column values on the x-axis.
Display the plot.
'''
# Import Matplotlib, Pandas, and Seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create a DataFrame from csv file
df = pd.read_csv(csv_filepath)

# Create a count plot with "Spiders" on the x-axis
sns.countplot(x="Spiders",data=df)

# Display the plot
plt.show()

#Hue and scatter plots
#Create a scatter plot with "absences" on the x-axis and final grade ("G3") on the y-axis using the DataFrame student_data. Color the plot points based on "location" (urban vs. rural).

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a scatter plot of absences vs. final grade
sns.scatterplot(x="absences",y="G3",data=student_data,hue="location")

# Show plot
plt.show()

#Make "Rural" appear before "Urban" in the plot legend.
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Change the legend order in the scatter plot
sns.scatterplot(x="absences", y="G3", 
                data=student_data, 
                hue="location",
                hue_order=["Rural","Urban"])

# Show plot
plt.show()

#Hue and count plots
''''
Fill in the palette_colors dictionary to map the "Rural" location value to the color "green" and the "Urban" location value to the color "blue".
Create a count plot with "school" on the x-axis using the student_data DataFrame.
Add subgroups to the plot using "location" variable and use the palette_colors dictionary to make the location subgroups green and blue.
'''
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a dictionary mapping subgroup values to colors
palette_colors = {"Rural": "green", "Urban": "blue"}

# Create a count plot of school with location subgroups
sns.countplot(x="school", data=student_data,hue="location",palette=palette_colors)

# Display plot
plt.show()
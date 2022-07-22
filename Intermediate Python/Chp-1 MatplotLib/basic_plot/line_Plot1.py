import matplotlib.pyplot as plt

year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]

# Print the last item from year and pop

print(year[-1])
print(pop[-1])

# Import matplotlib.pyplot as plt

# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year, pop)
# plt.scatter(year, pop)
#
# # Put the x-axis on a logarithmic scale
# plt.xscale('log')

# Display the plot with plt.show()
plt.show()

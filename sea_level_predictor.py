import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Use Pandas to import the data from epa-sea-level.csv.
df = pd.read_csv('epa-sea-level.csv')

# Use matplotlib to create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')

# Use the linregress function to get the slope and y-intercept of the line of best fit
slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

# Plot the line of best fit
plt.plot(df['Year'], slope * df['Year'] + intercept, color='red', label='Line of Best Fit (1880-2013)')

# Plot a new line of best fit using data from year 2000 onwards
recent_data = df[df['Year'] >= 2000]
slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
plt.plot(recent_data['Year'], slope_recent * recent_data['Year'] + intercept_recent, color='green', label='Line of Best Fit (2000-2013)')

# Extend the line to predict sea level rise in 2050
plt.plot([1880, 2050], [intercept + slope * 1880, intercept + slope * 2050], linestyle='--', color='red')
plt.plot([2000, 2050], [intercept_recent + slope_recent * 2000, intercept_recent + slope_recent * 2050], linestyle='--', color='green')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()

# Save and return the image
plt.savefig('sea_level_rise.png')
plt.show()

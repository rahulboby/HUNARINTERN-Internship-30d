import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

# --- Creating the database
data = {
        "Year": [1810, 1820, 1830, 1840, 1850, 1860, 1870, 1880, 1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980],
        "Average_Height": [169.7, 169.1, 166.7, 166.5, 165.6, 166.6, 167.2, 168, 169.4, 170.9, 171, 173.9, 174.9, 176, 176.9, 177.1, 176.8]
        }
df = pd.DataFrame(data)

# --- Getting the mean of the height throughout the years
mean_height = df["Average_Height"].mean()

# --- Creating a bar plot between the Year and Average Height
sn.barplot(data = df, y = "Average_Height", x = "Year", palette="viridis")
plt.xticks(rotation=90)
plt.ylabel(f"The Mean height: {mean_height:.2f}")

# --- Adding the mean height as a horizontal line
plt.axhline(mean_height, color='red', linestyle='--', linewidth=1.5, label=f'Mean Height: {mean_height:.2f} cm')

# --- Getting Histogram of height range
plt.hist(df["Average_Height"], bins = 5, color="red", edgecolor = "black")

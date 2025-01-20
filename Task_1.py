import pandas as pd

orig_data = pd.read_csv(r"C:\Users\Rahul\Desktop\HunarIntern\food_coded.csv")
data = pd.read_csv(r"C:\Users\Rahul\Desktop\HunarIntern\food_coded.csv")

# Idea: Fill the missing values of the columns with more than 10 nan using
# Either mean, median or mode
# for the rest, we delete all the rows with missing values
# this ensures not too much data is lost

#-------FILLING MISSING VALUES------------
#to find the columns with more than 10 missing values
columns_with_nans = data.columns[data.isnull().sum() > 10]

for col in columns_with_nans:
    if data[col].dtype in ["int64", "float64"]:
        #Replacing with median for numeric values
        data[col] = data[col].fillna(data[col].median())
    else:
        #replacing with mode for non numeric values
        data[col] = data[col].fillna(data[col].mode()[0])

data.dropna (inplace = True)


print("Original Data Shape:", orig_data.shape)
print("Remaining Missing Values:\n", orig_data.isnull().sum())

print("Cleaned Data Shape:", data.shape)
print("Remaining Missing Values:\n", data.isnull().sum())
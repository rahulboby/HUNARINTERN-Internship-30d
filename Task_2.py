import pandas as pd

#importing training model for linear regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data = pd.read_csv(r"C:\Users\Rahul\Desktop\HunarIntern\task 2\house_price_data.csv")

#---------------- Pre Processing -----------------------

#dropping NaN and duplicate values
data = data.dropna(axis=0)
data = data.drop_duplicates()

# Drop irrelevant columns (These columns won't affect the price)
data = data.drop(columns=['date', 'street', 'country'])

# Convert catagorial columns into dummies
data = pd.get_dummies(data, columns=['city', 'statezip'], drop_first=True)

#remove impossible houses (inaccurate data)
data = data[(data['price'] > 0) & (data['bedrooms'] > 0) & (data['bathrooms'] > 0)]

#----------------- Creating Testing and Training Data -----------------

#setting the features
x = data.drop(columns=['price'])

#setting the target (the price of the house)
y = data['price']

#split training and testing model
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.1, random_state=42)

#--------------------- Implementing the model ---------------------
model = LinearRegression()
model.fit(x_train, y_train)

test_predicted_y = model.predict(x_test)
mse = mean_squared_error(y_test, test_predicted_y)
r_squared_score = r2_score(y_test, test_predicted_y)

print(f"MSE: {mse}")
print(f"R2 Score: {r_squared_score}")

#Thus this model has an accuracy score of around 0.77
#The model is ready to predict new values from datasets using this model
#
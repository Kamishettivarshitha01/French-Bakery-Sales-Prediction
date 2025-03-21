# -*- coding: utf-8 -*-
"""bakery.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uwFophKV-qUlsqloQbmFbe-v87aNNYxu
"""

import pandas as pd

df=pd.read_csv('/content/Bakery sales.csv')

df

df.shape

df.head()

df.tail()

df.describe()

df.shape

df.columns

df.isna().sum()

df['ticket_number'].value_counts()

df.info()

import matplotlib.pyplot as plt
import plotly.express as px
fig = px.histogram(df,x='Quantity')
fig.show()

df.duplicated().sum()

df = df.drop_duplicates()
df.shape

df.dtypes

df = df.rename(columns = {'date' : 'Date',
                         'time' : 'Time',
                          'ticket_number' : 'Transaction_id',
                          'article' : 'Menu',
                          'unit_price' : 'Price'})

df['Menu'] = df['Menu'].str.title()

df = df.replace(to_replace = {'Quantity' : {'.' : ' '}, # np.NaN
                              'Price' : {'€' : ' ' , ',' : '.' }}, regex=True)

df = df.astype({'Quantity' : 'int',
                'Price' : 'float',
                'Transaction_id' : 'int',
                'Menu' : 'str'})

df = df[(df['Price'] > 0) & (df['Quantity'] > 0)]

df['Revenue'] = df['Quantity'] * df['Price']

df.head()

df['Quantity'].value_counts()

df['Date'] = pd.to_datetime(df['Date'])

df['Day_time'] = pd.to_datetime(df['Time']).dt.hour
df['Day_time'].unique()

# Extract day and year from the 'Date' column
df['Day'] = df['Date'].dt.day
df['Year'] = df['Date'].dt.year

# Now you can select these columns
df = df[['Quantity', 'Price', 'Revenue', 'Day', 'Year', 'Day_time']]

df

from sklearn.model_selection import train_test_split

# Assuming 'df' is your DataFrame and 'Revenue' is the target variable
# Replace 'Revenue' with your actual target variable column name if different
X = df[['Quantity', 'Price', 'Day', 'Year', 'Day_time']]  # Features
y = df['Revenue']  # Target variable

# Split the data into training and testing sets (e.g., 80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Now you can proceed with your model training
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

model_lr = LinearRegression()
model_lr.fit(X_train, y_train)

# Assuming 'df' is your DataFrame containing the correct features
# ['Quantity', 'Price', 'Revenue', 'Day', 'Year', 'Day_time']

# Split the data into training and testing sets
X = df[['Quantity', 'Price', 'Day', 'Year', 'Day_time']]
y = df['Revenue']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model_lr = LinearRegression()
model_lr.fit(X_train, y_train)

# Make predictions using the correct DataFrames (X_train, X_test)
y_pred_train_lr = model_lr.predict(X_train)
y_pred_test_lr = model_lr.predict(X_test)

# ... (rest of your code for calculating metrics)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.model_selection import train_test_split # Import train_test_split


# Assuming X_train and y_train are your training data
# Re-assign X_train to train_x and y_train to train_y
# It's best to perform train_test_split here if not done before
# to make sure test_x is defined
x = df.drop('Revenue',axis=1) # Assuming df is your original DataFrame
y = df['Revenue']
train_x, test_x, train_y, test_y = train_test_split(x, y, test_size = 0.3, random_state = 42)

model_lr = LinearRegression()
model_lr.fit(train_x, train_y)

y_pred_train_lr=model_lr.predict(train_x)
y_pred_test_lr=model_lr.predict(test_x) # Now test_x is defined

y_pred_train_lr=model_lr.predict(train_x)
y_pred_test_lr=model_lr.predict(test_x)
train_mse_lr=mean_squared_error(train_y,y_pred_train_lr)
test_mse_lr=mean_squared_error(test_y,y_pred_test_lr)
train_r2_lr=r2_score(train_y,y_pred_train_lr)
test_r2_lr=r2_score(test_y,y_pred_test_lr)

print(train_mse_lr)
print(test_mse_lr)
print(train_r2_lr)
print(test_r2_lr)

!pip install scikit-learn
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

# Assuming train_x, train_y, test_x, test_y are defined from previous cells

# Initialize and train the KNN model
model_knn = KNeighborsRegressor(n_neighbors=5)
model_knn.fit(train_x, train_y)

# Make predictions
y_pred_train_knn = model_knn.predict(train_x)
y_pred_test_knn = model_knn.predict(test_x)  # Define y_pred_test_knn before using it

# Calculate and print metrics
mae = mean_absolute_error(test_y, y_pred_test_knn)
print("MAE of the knn model on your test dataset:", mae)

mse = mean_squared_error(test_y, y_pred_test_knn)
print("MSE of the knn model on your test dataset:", mse)

rmse = np.sqrt(mse)
print("RMSE of the knn model on your test dataset:", rmse)

r2 = r2_score(test_y, y_pred_test_knn)
print("R-squared of the knn model on your test dataset:", r2)

print("Accuracy of the KNN model on your train dataset,accuracy_train")
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score # Import regression metrics

# Calculate MAE
mae = mean_absolute_error(train_y, y_pred_train_knn)
print("MAE of the knn on your train dataset", mae)

# Calculate MSE
mse = mean_squared_error(train_y, y_pred_train_knn)
print("MSE of the knn on your train dataset", mse)

# Calculate RMSE
rmse = np.sqrt(mse)  # Assuming you have imported numpy as np
print("RMSE of the knn on your train dataset", rmse)

# Calculate R-squared
r2 = r2_score(train_y, y_pred_train_knn)
print("R2 of the knn on your train dataset", r2)

print(y_pred_train_knn)

print(y_pred_test_knn)

from sklearn.cluster import KMeans
k=3
model_kmeans=KMeans(n_clusters=k,random_state=42)
columns_for_cllustering=["Quantity","Year"] # Change 'year' to 'Year'
df_for_clustering=df[columns_for_cllustering]
model_kmeans.fit(df_for_clustering)
cluster_labels=model_kmeans.labels_
cluster_centers=model_kmeans.cluster_centers_
plt.figure(figsize=(8,6))
plt.scatter(df_for_clustering['Quantity'],df_for_clustering['Year'],c=cluster_labels,cmap='viridis',alpha=0.5) # Change 'year' to 'Year'
plt.scatter(cluster_centers[:,0],cluster_centers[:,1],marker='x',s=100,color='red')
plt.xlabel("Quantity")
plt.ylabel("Year") # Change 'year' to 'Year'
plt.title("K-means Clustering")
#plt.legend() # legend might not be necessary if not specifying specific labels for the scatter plots
plt.show()

df = pd.read_csv('/content/Bakery sales.csv') # Reload your data
   # ... (your data cleaning and transformation steps) ...

import pandas as pd

# Reload your data
df = pd.read_csv('/content/Bakery sales.csv')

# Rename the columns
df = df.rename(
    columns={
        'date': 'Date',
        'time': 'Time',
        'ticket_number': 'Transaction_id',
        'article': 'Menu',
        'unit_price': 'Price'
    }
)

# Data Cleaning and Transformation Steps (re-apply from previous cells)
df['Menu'] = df['Menu'].str.title()
df = df.replace(
    to_replace={
        'Quantity': {
            '.': ' '
        },  # np.NaN
        'Price': {
            '€': ' ',
            ',': '.'
        }
    },
    regex=True
)
df = df.astype({
    'Quantity': 'int',
    'Price': 'float',
    'Transaction_id': 'int',
    'Menu': 'str'
})
df = df[(df['Price'] > 0) & (df['Quantity'] > 0)]
df['Revenue'] = df['Quantity'] * df['Price']
df['Date'] = pd.to_datetime(df['Date'])
df['Day_time'] = pd.to_datetime(df['Time']).dt.hour
df['Day'] = df['Date'].dt.day
df['Year'] = df['Date'].dt.year
df = df[['Quantity', 'Price', 'Revenue', 'Day', 'Year', 'Day_time']]


# Now you can access the columns
x = df[['Quantity', 'Price']]
y = df['Revenue']

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

from sklearn.tree import DecisionTreeRegressor # Use DecisionTreeRegressor for regression

dt = DecisionTreeRegressor(criterion='squared_error') # Corrected class name
dt.fit(train_x, train_y)
y_pred_test_dt = dt.predict(test_x)
y_pred_train_dt = dt.predict(train_x)

from sklearn.metrics import mean_squared_error, r2_score

train_mse_dt = mean_squared_error(train_y, y_pred_train_dt)
test_mse_dt = mean_squared_error(test_y, y_pred_test_dt)
train_r2_dt = r2_score(train_y, y_pred_train_dt)
test_r2_dt = r2_score(test_y, y_pred_test_dt)

print(f"Train MSE: {train_mse_dt}, Train R2: {train_r2_dt}")
print(f"Test MSE: {test_mse_dt}, Test R2: {test_r2_dt}")

from sklearn.ensemble import RandomForestRegressor # Import the RandomForestRegressor class

random_forest = RandomForestRegressor(n_estimators=100, random_state=10)

# fit the regressor with training dataset
rf=random_forest.fit(X_train, y_train)

# predict the values on test dataset using predict()
y_pred = rf.predict(X_test)

# Import the necessary function for RMSE calculation
from sklearn.metrics import mean_squared_error
import numpy as np

# ... (your existing code) ...

# Calculate rmse using mean_squared_error
randomforest_rmse = np.sqrt(mean_squared_error(y_test, y_pred))

from sklearn.metrics import r2_score


# calculate R-squared using rsquared
rf_rsquared = r2_score(y_test,y_pred)
# calculate Adjusted R-Squared using rsquared_adj
rf_rsquared_adj = 1 - ((1 - rf_rsquared) * (len(df) - 1) / (len(df) - 13 - 1))

print(mae)
print(mse)
print(randomforest_rmse)
print(rf_rsquared)
print(rf_rsquared_adj)

random_forest = pd.DataFrame({'Model': ["Random Forest Regressor"],
                     "MAE":[mae],
                     "MSE":[mse],
                     'RMSE':[randomforest_rmse],

                     'Adj. R-Squared': [rf_rsquared_adj]
                   })

# Initialize result_tabulation if it doesn't exist
if 'result_tabulation' not in locals():
    result_tabulation = pd.DataFrame(columns=['Model', 'MAE', 'MSE', 'RMSE', 'Adj. R-Squared'])

result_tabulation = pd.concat([result_tabulation, random_forest], ignore_index = True)

# print the result table
result_tabulation
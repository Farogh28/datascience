import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    'age': [25, 30, 35, 40, 45],
    'salary': [50000, 60000, 70000, 80000, 90000]
}
df = pd.DataFrame(data)

X = df[['age']]
y = df['salary'] 

lr = LinearRegression()

lr.fit(X, y)
print(lr.coef_)
print(lr.intercept_)
new_age = 65
new_data = pd.DataFrame({'age': [new_age]}) 
predicted_target = lr.predict(new_data)

print("Predicted target:", predicted_target[0])
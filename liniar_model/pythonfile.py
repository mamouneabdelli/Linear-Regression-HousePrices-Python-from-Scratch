import numpy as np
import pandas as pd
def linear_model(x, w, b):
    return w * x + b

def linear_cost(x, y, w, b):
    m = len(x)
    y_pred = linear_model(x, w, b)
    return (1/(2*m)) * np.sum((y_pred - y)**2)

def linear_gradient_descent(x, y, w, b, alpha, iterations):
    m = len(x)
    for i in range(iterations):
        y_pred = linear_model(x, w, b)
        dw = (1/m) * np.sum((y_pred - y) * x)
        db = (1/m) * np.sum(y_pred - y)
        w = w - alpha * dw
        b = b - alpha * db
        print(f"Iteration {i+1}: Cost = {linear_cost(x, y, w, b):.6f}")
    return w, b



data = pd.read_csv("train.csv")

# Pick one feature (1D)
x = data["LotArea"].fillna(data["LotArea"].mean()).values  # 1D array

# min max scaling application 
x_scaled = (x - x.min()) / (x.max() - x.min())

# Target
y = data["SalePrice"].values
y_scaled = (y - y.min()) / (y.max() - y.min())


w = 0
b = 0
alpha = 0.1
iterations = 50


w, b = linear_gradient_descent(x_scaled, y_scaled, w, b, alpha, iterations)#1D feaature


y_pred_scaled = linear_model(x_scaled, w, b)
y_pred_real = y_pred_scaled * (y.max() - y.min()) + y.min()



#logistic model 



#import numpy as np

#def sigmoid(z):
  #  return 1 / (1 + np.exp(-z))

#def logistic_model(x, w, b):
    #return sigmoid(w * x + b)

#def logistic_cost(x, y, w, b):
  #  m = len(x)
   # y_pred = logistic_model(x, w, b)
   # cost = -(1/m) * np.sum(y*np.log(y_pred) + (1-y)*np.log(1-y_pred))
   # return cost

#def logistic_gradient_descent(x, y, w, b, alpha, iterations):
  #  m = len(x)

   # for _ in range(iterations):
       # y_pred = logistic_model(x, w, b)

      #  dw = (1/m) * np.sum((y_pred - y) * x)
      #  db = (1/m) * np.sum((y_pred - y))

     #  w = w - alpha * dw
      #  b = b - alpha * db

   # return w, b


#data charging from the datset using pandas 
## Load dataset
#data = pd.read_csv("train.csv")

# Select target column
#y = data["SalePrice"]

# Select features
#X = data[
   # [
     #   "Id",
     #   "MSSubClass",
     #   "LotFrontage",
       #  "LotArea",
        # "OverallQual",
       #  "OverallCond",
      #   "YearBuilt",
        # "YearRemodAdd",
        # "MasVnrArea"
   # ]
#]


#X = X.dropna()
#y = y[X.index]   

#link of data set used 

#https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data?select=train.csv

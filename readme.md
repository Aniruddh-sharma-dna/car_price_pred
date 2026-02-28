Hello everyone , this is my car price prediction project , I am using the data from kaggle and I am trying to predict the price of the cars , I have tried to use the different models and I have got the best results.

you can try this project on your local machine or you can download the project and run it on your local machine.

in this project I have used the following libraries:
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import joblib

after installing you are able to run this. 
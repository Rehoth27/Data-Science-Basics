import pandas as pd
from scipy.stats import skew, kurtosis
df = pd.read_csv("/home/rohit/Downloads/diabetes.csv")
print("Skewness:", skew(df['Glucose']))
print("Kurtosis:", kurtosis(df['Glucose']))

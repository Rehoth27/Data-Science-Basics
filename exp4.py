import pandas as pd
iris = pd.read_csv("/home/rohit/Downloads/Iris.csv")
print("Mean:", iris.mean(numeric_only=True))
print("Mode:", iris.mode())

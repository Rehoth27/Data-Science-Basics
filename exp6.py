import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv('/home/rohit/Downloads/diabetes.csv')
form2 = {'family': 'serif', 'color': 'darkred', 'size': 15}
plt.title("Age distribustion",fontdict=form2)

sns.histplot(data=df,x='Age',color="aqua")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("worldometer_data.csv")
print(df)

x =df['TotalCases']
y = df['Population']
plt.plot(x,y, color='red')
plt.title("Covid-19 cases study", loc="center", color= 'purple', weight = 'bold', size = 15)
plt.xlabel("No. of Total Cases", color= 'orange', font = 'arial', weight= 'bold')
plt.ylabel("Total Population", color= 'blue', font='arial', weight= 'bold')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame({'a':[1,2,3,4,5], 'b':[6,7,8,9,10], 'c':[11,12,13,14,15]})

print("Means:", np.mean(df['b']), np.mean(df['c']), "Max:", max(df['b']), max(df['c']))

plt.plot(df['a'], df['b'], color='blue', label='b')
plt.plot(df['a'], df['c'], color='pink', label='c')
plt.title('b vs c')
plt.xlabel('a')
plt.ylabel('values')
plt.legend()
plt.show()

# Create sample data
data = np.random.randn(100)

# Create a seaborn histogram
sns.histplot(data, kde=True)
plt.title("Sample Distribution")
plt.show()

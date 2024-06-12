import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data.csv')

#first few rows of set
print("First few rows of the ds:")
print(df.head())

#summary statistics
print("\nsummary statistics:")
print(df.describe())

#display info abt set
print("\ndisplay info abt set:")
print(df.info())

#column of set
print("\ncolumn of set:")
print(df.columns)

#check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

#drop rows with missing values
df = df.dropna()

#remove duplicate rows
df = df.drop_duplicates()

#convert data types if necessary
#Example: df['Column_name'] = df['column_name'].astype(int)

#Group by a column and calc the mean of each group
# print("\nMean values grouped by 'column_name':")
# grouped_df = df.groupby('Age').mean()
# print(grouped_df)

#calc mean of specify column
mean_value = df['Age'].mean()
print(f"\nMean value of 'Age': {mean_value}")

#calc sum of specific column
sum_value = df['Age'].sum()
print(f"\nSum of 'Age': {sum_value}")

#filter data based on condition
value = 10
filtered_df = df[df['Age'] > value]
print(f"\nFiltered data where 'Age' > {value}:")
print(filtered_df)

#create simple line plot
plt.figure()
df['Age'].plot(kind='line')
plt.title('Line plot of Age')
plt.xlabel('Index')
plt.ylabel('value')
plt.show

#Create histogram
plt.figure()
df['Age'].plot(kind='hist')
plt.title('Histogram of Age')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

#Create box plot
plt.figure()
sns.boxplot(x='Age', data=df)
plt.title('Box Plot of Age')
plt.show()
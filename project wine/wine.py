import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('winequality-red.csv')
print(df.head())

print(df.isnull().sum())
df.fillna(df.mean(), inplace=True)

print(df.dtypes)

plt.figure(figsize=(12, 6))
sns.boxplot(data=df[['fixed_acidity', 'volatile_acidity', 'citric_acid', 'chlorides', 'density', 'pH', 'sulphates']])
plt.title('Выбросы в числовых переменных')
plt.show()

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

df_filtered = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]

corr_matrix = df.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Корреляционная матрица переменных')
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(x='fixed_acidity', y='pH', data=df)
plt.title('Взаимосвязь фиксированной кислотности и pH')
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(x='density', y='pH', data=df)
plt.title('Взаимосвязь плотности и pH')
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(x='sulphates', y='pH', data=df)
plt.title('Влияние сульфатов на pH')
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(x='sulphates', y='density', data=df)
plt.title('Влияние сульфатов на плотность')
plt.show()

df[['fixed_acidity', 'volatile_acidity', 'pH', 'sulphates', 'density']].hist(bins=20, figsize=(12, 8))
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(x='free_sulfur_dioxide', y='fixed_acidity', data=df)
plt.title('Влияние свободного диоксида серы на фиксированную кислотность')
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(x='total_sulfur_dioxide', y='fixed_acidity', data=df)
plt.title('Влияние общего диоксида серы на фиксированную кислотность')
plt.show()

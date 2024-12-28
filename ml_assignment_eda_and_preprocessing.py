# -*- coding: utf-8 -*-
"""ML_Assignment_EDA_and_Preprocessing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_uO4a_D9kZMl9CBrMi63taxbMfCdvsqZ

Data Exploration
"""

import numpy as np
import pandas as pd

#load the dataset
df = pd.read_csv('/content/Employee.csv')

#display first 5 rows
df.head()

#shape of the dataframe
df.shape

#column names
df.columns

#count of unique values
df.nunique()

#unique values in 'Company' column
df['Company'].unique()

#unique values in 'Age' column
df['Age'].unique()

#unique values in 'Salary' column
df['Salary'].unique()

#unique values in 'Place' column
df['Place'].unique()

#unique values in 'Country' column
df['Country'].unique()

#unique values in 'Gender' column
df['Gender'].unique()

df.describe().T

df.describe(include='all')

df.info()

#checking null values
df.isnull().sum()

#renaming the columns
df.rename(columns={'Company': 'company', 'Age': 'age', 'Salary': 'salary', 'Place': 'place', 'Country': 'country', 'Gender': 'gender'}, inplace=True)

df.columns

"""Data Cleaning"""

#missing values
df.isna().sum()

#unique values in 'company' column
df['company'].unique()

"""Before replacing null values in 'company' column, in 'company' column it seems that 'TCS' in different names like  'Tata Consultancy Services' and 'CTS' which is also mispelled, so renaming this 'Tata Consultancy Services' and 'CTS' to 'TCS'. Then there is 'Infosys' and 'Infosys Pvt Lmt', so renaming this 'Infosys Pvt Lmt' to 'Infosys'"""

#replacing values in 'company' column
df['company'] = df['company'].replace({
    'Tata Consultancy Services' : 'TCS',
    'CTS' : 'TCS',
    'Infosys Pvt Lmt' : 'Infosys'
})

#count of null values in 'company' column
df['company'].isna().sum()

#replacing null values using mode in 'company' column
mode_value = df['company'].mode()[0]
df['company'] = df['company'].fillna(mode_value)

#checking null values after replacing it with mode
df['company'].isna().sum()

#unique values in 'age' column
df['age'].unique()

#replacing value '0' in age as Nan
df['age'] = df['age'].replace(0, np.nan)

#checking null vallues in 'place' column
df['place'].isna().sum()

#replacing null values using mode in 'place' column
mode_value_place = df['place'].mode()[0]
df['place'] = df['place'].fillna(mode_value_place)

#checking null values after replacing it with mode
df['place'].isna().sum()

#checking for other missing values
df.isnull().sum()

#checking the outliers of 'age' and 'salary' before replacing null values
import matplotlib.pyplot as plt
import seaborn as sns

#visualizing outliers in 'age' column using boxplots
plt.figure(figsize=(10, 5))
sns.boxplot(x=df['age'])
plt.title('Outliers in Age')
plt.show()

"""It seems that there is no any outliers in 'age' column"""

#visualizing outliers in 'Salary' column using boxplots
plt.figure(figsize=(10, 5))
sns.boxplot(x=df['salary'])
plt.title('Outliers in Salary')
plt.show()

"""It seems that there is no any outliers in 'salary' column"""

#replacing null values in 'age' and 'salary' using median
df.fillna({
    'age' : df['age'].median(),
    'salary' : df['salary'].median()
}, inplace=True)

#checking null values
df.isnull().sum()

#checking duplicate rows
df.duplicated().sum()

#removing duplicate rows
df.drop_duplicates(inplace=True)

#checking duplicates after removal
df.duplicated().sum()

"""Data Analysis"""

#filtering data with 'age' > 40 and salary < 5000
filtered_df = df[(df['age'] > 40) & (df['salary'] < 5000)]

filtered_df

#plotting the chart with 'age' and 'salary'
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df['age'], y=df['salary'])
plt.title('Age v/s Salary')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.show()

#count of number of people by place
df['place'].value_counts()

#visualization of number of people by place
place_counts = df['place'].value_counts()

plt.figure(figsize=(8,5))
sns.barplot(x=place_counts.index, y=place_counts.values, palette='viridis', hue=place_counts.index)
plt.title('Number of People by Place')
plt.xlabel('Place')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

"""Data Encoding"""

#endocing using One-Hot/Get-dummies
df_one_hot = df.copy()
df_one_hot = pd.get_dummies(df, columns=['company', 'place', 'country'], prefix=['company', 'place', 'country'], drop_first=True)

df_one_hot

#encoding using label encoder
from sklearn.preprocessing import LabelEncoder
df_le = df.copy()
le = LabelEncoder()
df_le['company'] = le.fit_transform(df_le['company'])
df_le['place'] = le.fit_transform(df_le['place'])
df_le['country'] = le.fit_transform(df_le['country'])

df_le

"""Feature Scaling"""

#before scaling splitting into features (X) and target (y)
#using df_one_hot here

X = df_one_hot.drop(columns=['gender'])
y = df_one_hot['gender']

X.head()

y.head()

#splitting data into train and test

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

#feature scaling using standardization(StandardScaler)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#feature scaling using normaliztion(MinMaScaler)
#using df_le here
#splitting into features and target

X = df_le.drop(columns=['gender'])
y = df_le['gender']

X.head()

y.head()

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


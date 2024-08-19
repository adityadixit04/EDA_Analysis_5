import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("D:\\Study\\Intership\\Task 5\\US_Accidents_March23.csv")

# Preview the data
print(df.head())
print(df.info())

# Data Preprocessing
# Handle missing values
df = df.dropna()  # or df.fillna() depending on the data

# Convert columns to appropriate data types
df['date'] = pd.to_datetime(df['date'])  # Example for a date column
df['hour'] = df['time'].apply(lambda x: int(x.split(':')[0]))  # Extract hour from time

# Feature Engineering (if needed)
df['month'] = df['date'].dt.month
df['day_of_week'] = df['date'].dt.dayofweek

# Exploratory Data Analysis (EDA)
# Distribution of accidents over time
plt.figure(figsize=(10, 6))
sns.histplot(df['hour'], bins=24, kde=False)
plt.title('Distribution of Accidents by Hour')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Accidents')
plt.show()

# Accident count by weather conditions
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='weather_condition')
plt.title('Accidents by Weather Condition')
plt.xlabel('Weather Condition')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()

# Accidents by road condition
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='road_condition')
plt.title('Accidents by Road Condition')
plt.xlabel('Road Condition')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()

# Accident hotspots visualization (assuming you have latitude and longitude)
plt.figure(figsize=(10, 10))
sns.scatterplot(x='longitude', y='latitude', data=df, hue='severity', palette='Reds', alpha=0.5)
plt.title('Accident Hotspots')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

# Identifying contributing factors
correlation = df.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of Factors Contributing to Accidents')
plt.show()

# Advanced Analysis (optional)
# Grouping by time of day, weather, and road condition
grouped_df = df.groupby(['hour', 'weather_condition', 'road_condition']).size().unstack().fillna(0)
plt.figure(figsize=(12, 8))
sns.heatmap(grouped_df, cmap='viridis')
plt.title('Accidents by Time, Weather, and Road Condition')
plt.xlabel('Road Condition')
plt.ylabel('Hour of the Day')
plt.show()

# Save processed data or results if needed
df.to_csv('processed_data.csv', index=False)

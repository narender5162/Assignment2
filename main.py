import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def world_bank_data(filename):
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(filename)
    converted_df = df.set_index(['Country Name', 'Indicator Name']).stack().unstack(0).reset_index()
    converted_df.columns.name = None
    return df, converted_df


file_path = 'Countryindicators.csv'
df, converted_df = world_bank_data(file_path)

'''converted_df.to_csv('converteddata.csv')'''

# Cleaning Transposed data
data = pd.read_csv('converteddata.csv')
'''data=data.dropna()'''

# Summary Statistics
stats1=df.describe()
print(stats1)

#histogram Distribution
selected_data = df[['2010', '2011']].select_dtypes(include='number')
# Create histograms for each numeric column
selected_data.hist(figsize=(12, 6), bins=20)
plt.suptitle('Histograms for Numeric Columns in 2019 and 2020', y=1.02)
plt.show()

# Line Chart Code
selected_data = data[(data['Indicator Name'] == 'CO2 emissions (kt)') &
                   (data['Year'].notna())]  # Ensure there's a valid year

# Select only the relevant columns
selected_data = selected_data[['Year', 'Bangladesh', 'Denmark', 'Cyprus']]
grouped_data = selected_data.groupby('Year').sum()


# Plot the line chart
plt.figure(figsize=(8, 6))
plt.plot(grouped_data.index, grouped_data['Bangladesh'], label='Bangladesh')
plt.plot(grouped_data.index, grouped_data['Cyprus'], label='Cyprus')
plt.plot(grouped_data.index, grouped_data['Denmark'], label='Denmark')
plt.title('Comparison of Co2 Emission for Between Bang , Denmark Cyprus')
plt.xlabel('Year')
plt.ylabel('Access to electricity (% of population)')
plt.legend()
plt.grid(True)
plt.show()

# Bar Char Comparison
dataforbar = data[data['Indicator Name'] == 'Ease of doing business rank (1=most business-friendly regulations)'][
    ['Bahrain', 'Spain']]
aggregated_data = dataforbar.sum()
aggregated_data.plot(kind='bar', color=['blue', 'orange', 'green', 'red'], figsize=(10, 6))
plt.title('Ease of doing business Comparison Bahrain vs Spain')
plt.xlabel('Country')
plt.ylabel('Business rank')
plt.show()


#pie chart
urban = df[df['Indicator Name'] == 'Forest area (sq. km)']
years_columns = df.columns[2:]
urban['Total'] = urban[years_columns].sum(axis=1)
top5_countries = urban.nlargest(10, 'Total')
plt.figure(figsize=(8, 8))
plt.pie(top5_countries['Total'], labels=top5_countries['Country Name'], autopct='%1.1f%%', startangle=90)
plt.legend(bbox_to_anchor=(1, 0.5), loc="center left", title="Country Name", bbox_transform=plt.gcf().transFigure)
plt.title('top 10 Countries with vast Forest Area')
plt.show()

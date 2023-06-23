import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def load_data(file_path):
    """
  Retrieve and preprocess data from a CSV file.
  
  Args:
      file_path (str): The file path of the CSV file.
      
  Returns:
      pandas.DataFrame: The processed DataFrame.
  """
    data = pd.read_csv(file_path)
    data = data.drop(columns=['Series Name', 'Series Code', 'Country Code'])
    data = data.dropna()
    data = data.rename(columns={'Country Name': 'Country',
                                'Age dependency ratio, old' : 'Age dependency ratio (% of working-age population)'})

    # Select only South Asian countries
    south_asian_countries = ['Bangladesh', 'Bhutan', 'India', 'Maldives', 'Nepal', 'Pakistan', 'Sri Lanka']
    data = data[data['Country'].isin(south_asian_countries)]

    return data


def bar():
    """ Defining the function """
    M = data['Country']
    N = pd.to_numeric(data['2010 [YR2010]'], errors='coerce')
    colors = ['#8DD3C7', '#cc90fc', '#BEBADA', '#FB8072', '#80B1D3', '#FDB462', '#B3DE69']
    plt.figure(figsize=(10, 5))

    # Sort the data by 'N' in descending order
    sorted_indices = np.argsort(N.dropna())[::-1]
    M = M.iloc[sorted_indices]
    N = N.iloc[sorted_indices]

    bars = plt.bar(M, N, label='Age dependency ratio (% of working-age population)', color=colors)
    plt.xlabel('Country', fontsize=14)
    plt.ylabel('% of working-age population', fontsize=14)
    plt.title('Age dependency ratio (% of working-age population) for 2010')
    plt.legend()

    # Adjust the y-axis limits to provide space for labels
    plt.ylim(top=max(N.dropna()) * 1.1)

    # Rotate x-axis labels and adjust spacing
    plt.xticks(rotation=90, ha='center')

    # Add value labels on top of each bar
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.1f}', ha='center', va='bottom')

    plt.tight_layout()
    plt.show()



def multiline():
    """ Defining the function """
    
    colors = ['#8DD3C7', '#cc90fc', '#BEBADA', '#FB8072', '#80B1D3', '#FDB462', '#B3DE69']

    plt.figure(figsize=(10, 5))

    for i, country in enumerate(data['Country']):
        x = list(range(2001, 2011))  # X-axis values (years)
        # Y-axis values (age dependency ratio)
        y = data.loc[data['Country'] == country,
                     '2001 [YR2001]':'2010 [YR2010]'].values[0]

        # Convert non-numeric values ('..') to NaN
        y = pd.to_numeric(y, errors='coerce')

        # Exclude NaN values from the plot
        mask = ~np.isnan(y)
        plt.plot(np.array(x)[mask], y[mask], label=country, color=colors[i % len(colors)])

    plt.xlabel('Year', fontsize=14)
    plt.ylabel('% of working-age population', fontsize=14)
    plt.title('Age dependency ratio (% of working-age population)')
    plt.legend()
    plt.show()



def pie_chart():
    """ Defining the function """
    plt.figure(figsize=(8, 8))

    # Filter the data for the year 2002
    year = '2001 [YR2001]'
    data_2001 = data[['Country', year]].copy()

    # Convert non-numeric values ('..') to NaN
    data_2001[year] = pd.to_numeric(data_2001[year], errors='coerce')

    # Drop countries with NaN values
    data_2001.dropna(inplace=True)

    # Custom colors for the pie chart
    colors = ['#8DD3C7', '#cc90fc', '#BEBADA', '#FB8072', '#80B1D3', '#FDB462', '#B3DE69']
    plt.pie(data_2001[year], labels=data_2001['Country'],
            autopct='%1.1f%%', colors=colors)
    plt.title(f'Age dependency ratio (% of working-age population) - {year}')
    plt.axis('equal')
    plt.show()


# File path of the CSV file
file_path = r"C:\Users\yeshwanth\Downloads\P_Data_Extract_From_Population_estimates_and_projections\ce1603e2-e5be-4ef0-886b-c0865194d945_Data.csv"
data = load_data(file_path)
print(data)

multiline()
pie_chart()
bar()


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset to inspect its contents
file_path = "C:/Users/87975/Desktop/Master Curricular/data virsualization/project/the age structure of China/regression.csv"
df = pd.read_csv(file_path)


# Setting up the ggplot style for the plots
plt.style.use('ggplot')

# Plotting Population Change vs other variables with fitted regression lines
variables = ['Fertility Rate (Children per Woman)',
             'Marriage Registrations (10,000 couples)',
             'Price-To-Income Ratio']

for var in variables:
    plt.figure(figsize=(10, 6))
    sns.regplot(x=var, y='Population Change', data=df, scatter_kws={"s": 50}, line_kws={"color": "blue"})
    plt.title(f'Population Change vs {var}')
    plt.xlabel(var)
    plt.ylabel('Population Change')
    plt.show()

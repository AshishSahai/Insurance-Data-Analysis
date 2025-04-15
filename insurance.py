import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Read data
def read_data(data):
  df = pd.read_csv(data)
  return df


#EDA- Exploratory Data Analysis
def explore_data(data):
    #Print first 10 rows
    print(data.head(10))

    #Print info such as Range index, columns, Data types, memory usage
    print("\n Data info",data.info())

    #Print mean, min, max etc
    print("\n Data description: \n",data.describe())

    #Find the missing values if any
    print("\n Missing values: \n",data.isnull().sum())

    print("\n age by region: \n", data.groupby("region",observed=True)["charges"].mean().round(2))
    print("\nGender Statistics: \n",data["sex"].describe())

#Prints the mean of children in age gaps
    print("\nAge summary by children:\n ", data.groupby(pd.cut(data["age"],bins=5),observed=True)["children"].sum().round(2))
    dependents_by_age = data.groupby(pd.cut(data["age"],bins=5),observed=True)["children"].sum().round(2)
    return dependents_by_age

def visualize(data):
    plt.figure(figsize=(10,5))
    data.plot(kind="bar", color="blue")
    plt.title("Dependents of Insurer by age")
    plt.xlabel("age")
    plt.ylabel("children")
    plt.tight_layout()
    plt.show()



insurance_data = read_data("insurance.csv")
dependents_by_age = explore_data(insurance_data)
visualize(dependents_by_age)
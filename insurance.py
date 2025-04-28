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

#Smoker count
    print("\n Smoker count: \n", data["smoker"].value_counts())

    data["smoker_binary"] = data["smoker"].map({"yes":1,"no":0})
    bins = [17, 30, 40, 50, 60, 65]
    labels = ['18-30', '31-40', '41-50', '51-60', '61-65']
    data["age_group"] = pd.cut(data["age"], bins=bins, labels=labels, right=True)
    print("\n Smokers by age: \n",data.groupby("age_group",observed=True)["smoker"].value_counts())

#Prints the mean of children in age gaps
    print("\nAge summary by children:\n ", data.groupby("age_group",observed=True)["children"].sum().round(2))
    dependents_by_age = data.groupby("age_group",observed=True)["children"].mean().round(2)


    data["rate_of_smoker_by_bmi"] = data["smoker_binary"]/data["bmi"]
    print("\n Rate of smoker per bmi(sample): \n",data["rate_of_smoker_by_bmi"].head())
    charges_vs_smoker_by_bmi = data.groupby("charges", observed=True)["rate_of_smoker_by_bmi"]
    print("\n Average rate of smoker/bmi by charges: \n", data.groupby("charges", observed=True)["rate_of_smoker_by_bmi"].mean().round(4))

    return dependents_by_age, charges_vs_smoker_by_bmi

def plot_dependents_of_insurer(data):
    plt.figure(figsize=(10,6))
    data.plot(kind="bar", color="blue")
    plt.title("Dependents of Insurer by age")
    plt.xlabel("age")
    plt.ylabel("children")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig("images/Dependents_by_age.png")
    plt.show()


def plot_smoker_bmi_charges(data):
    plt.figure(figsize=(10,6))

    plt.title("Insurance charges vs Smoker/BMI rate")
    plt.xlabel("Smoker(1)/BMI rate(Inverse BMI for smokers only)")
    plt.ylabel("Charges")
    sns.scatterplot(x="rate_of_smoker_by_bmi", y= "charges", hue="smoker", style="sex", data=data, alpha= 0.7)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("images/charges_vs_smoker_bmi.png")
    plt.show()


def main():

    insurance_data = read_data("insurance.csv")
    dependents_by_age, charges_vs_smoker_by_bmi = explore_data(insurance_data)
    plot_dependents_of_insurer(dependents_by_age)
    plot_smoker_bmi_charges(insurance_data)




if __name__ == "__main__":
    main()
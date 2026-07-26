import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("train.csv")
print(df.shape)
print(df.isnull().sum())

print(df.groupby("Sex")["Survived"].mean())
print(df.groupby("Pclass")["Survived"].mean())

df["AgeGroup"] = pd.cut(df["Age"], [0,12,18,60,120],
                        labels=["child","teen","adult","senior"])
print(df.groupby("AgeGroup", observed=True)["Survived"].mean())

for col in ["Sex", "Pclass"]:
    df.groupby(col)["Survived"].mean().plot(kind="bar")
    plt.title(f"Survival rate by {col}"); plt.tight_layout()
    plt.savefig(f"by_{col}.png"); plt.clf()

sns.histplot(data=df, x="Age", hue="Survived", stat="density",
             common_norm=False, bins=20, element="step")
plt.savefig("age_hist.png")

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/salesdaily.csv")
df = df.drop_duplicates().dropna(subset=["datum"])
df["datum"] = pd.to_datetime(df["datum"])
df["drug"] = df["drug"].replace({"Amox": "Amoxicillin"})

amox = df[df["drug"] == "Amoxicillin"].copy()
amox["month"] = amox["datum"].dt.to_period("M")
monthly = amox.groupby("month")["units"].sum()
by_store = amox.pivot_table(index="month", columns="store",
                             values="units", aggfunc="sum")

supplier = pd.read_csv("data/supplier_log.csv")
merged = amox.merge(supplier, on=["store", "datum"], how="left")

monthly.plot(kind="line", marker="o")
plt.axvline("2015-03", color="red", linestyle="--")
plt.title("Amoxicillin sales by month")
plt.savefig("march_dip.png")

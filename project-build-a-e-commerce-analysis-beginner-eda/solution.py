df = df.drop_duplicates()
df = df.dropna(subset=["price"])
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df = df.dropna(subset=["date"])
df["revenue"] = df["price"] * df["qty"]
print(df.shape)

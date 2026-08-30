df = pd.read_csv('sales.csv')
df.dtypes
# date    object

df[df['date'] > '2024-03-01'].head(3)
#          date  value
# 1   2024-03-10    88
# 4   2024-11-02    41   <- year ignored, string beats '2024-03-01'
# 7   2024-03-02    93

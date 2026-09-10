drops = []
for i in range(1, len(sales)):
    if sales[i] < sales[i-1]:
        drops.append(sales[i])

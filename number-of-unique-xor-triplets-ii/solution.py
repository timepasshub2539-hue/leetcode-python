for i in range(n):
  for j in range(i, n):
    for k in range(j, n):
      xors.add(nums[i]^nums[j]^nums[k])

arr = [2, 3, 4, 5]
n = len(arr) + 1

expected_sum = (n * (n + 1)) // 2

actual_sum = sum(arr)
print(expected_sum - actual_sum)
 
def sum_list(my_list):
  total = 0
  for item in my_list:
    if isinstance(item, (int, float)):  
        return total


my_list = [1, 2.5, "hello", True, [10, 20]]


total_sum = sum_list(my_list)
print("Sum of numeric elements:", total_sum)
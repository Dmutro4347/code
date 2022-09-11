def binary_search(list, item):
  high = len(list) - 1
  low = 0
  while low <= high:
    mid = (low + high) // 2
    guess = list[mid]
    if guess == item:
      return mid
    elif guess > item:
      high = mid - 1
    elif mid < item:
      low = mid + 1

a = [i for i in range(1, 11)]

print(binary_search(a, 5))
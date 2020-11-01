arr = [1,4,5,6,7,6,4,3,1,3,2]

def findPeak(arr):
  middle = int(len(arr) / 2 - 1)
  if arr[middle] < arr[middle - 1]:
    findPeak(arr[:middle - 1])
  elif arr[middle] < arr[middle + 1]:
    findPeak(arr[middle+1:])
  else:
    return arr[middle]


print(findPeak(arr)) # 7

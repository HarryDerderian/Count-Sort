def count_sort(arr, valueEnd):
  # TODO : Write your code here
 
  # To account for negative numbers, I'll shift all values by the max value.
  # For example, assuming the max is 1000 and the min is -1000, the value of 0 would be 1000,
  # -1000 would be 0, and 1000 would be 2000.

  # Step 1: Create an empty array that stores twice the amount of valueEnd; this accounts for negative numbers.
  freq_array = [0] * (2 * (valueEnd+1))
  
  # Count the occurrences of a value within the array.
  # index + shift amount represents that number.
  for num in arr :
    freq_array[num+valueEnd] += 1

  # Increment every index value by its previous index value.
  shadow = 0  
  for index in range(1, 2 * (valueEnd+1)) :
    freq_array[index] += freq_array[shadow]
    shadow += 1
  
  # Create a new array with the same length as the unsorted array.
  sorted_arr = [0] * len(arr) 
  
  # Iterate through the unsorted array, check the offset index within the freq array.
  # The value found will now be the index where that number is inserted into the sorted array.
  for number in arr :
    index = freq_array[number + valueEnd]
    freq_array[number+valueEnd] -= 1
    sorted_arr[index-1] = number
  
  return sorted_arr


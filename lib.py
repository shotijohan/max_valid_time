def max_valid_time(A, B, C, D):
    number_list = [A, B, C, D]
    number_list.sort(reverse=True)

    placing_array = ["", "", "", ""]
    limit = 0

    placing_array[0] = poper(number_list, 2)

    limit = 3 if placing_array[0] == 2 else 9
    
    placing_array[1] = poper(number_list, limit)
    placing_array[2] = poper(number_list, 5)
    placing_array[3] = poper(number_list, 9)

    if number_list: 
        return "NOT POSSIBLE"

    return "{}{}:{}{}".format(
        str(placing_array[0]), str(placing_array[1]), 
        str(placing_array[2]), str(placing_array[3]))

def poper(array, compare_with):
  for index in range(0, len(array)):
      if array[index] <= compare_with:
          return array.pop(index)

def findMaxMin(list):
  my_arr = []
  if (max(list))==(min(list)):
    my_arr.append(len(list))
    return my_arr

  else:
    my_arr.append(min(list))
    my_arr.append(max(list))
    return my_arr

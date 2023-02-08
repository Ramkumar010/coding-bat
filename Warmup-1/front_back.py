def front_back(string):
  if len(string) <= 1:
    return string
  middle = string[1:len(string)-1]
  return string[len(string)-1] + middle + string[0]
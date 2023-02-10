def caught_speeding(speed, is_birthday):
  if speed<=60 and not is_birthday:
    return 0
  if speed>61 and speed<=80 and not is_birthday:
    return 1
  if speed>80 and not is_birthday:
    return 2
    
  if speed<=65 and is_birthday:
    return 0
  if speed>65 and speed<=85 and is_birthday:
    return 1  
  if speed>85 and is_birthday:
    return 2  
    
    

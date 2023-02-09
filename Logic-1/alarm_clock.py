def alarm_clock(day, vacation):
  if (day>=1 and day<=5) and vacation:
    return "10:00"
  if (day==0 or day==6) and vacation:
    return "off"
  if (day>=1 and day<=5) and not vacation:
    return "7:00"
  if (day==0 or day==6) and not vacation:
    return "10:00"

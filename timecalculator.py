

def add_time(start, duration, day=False):

  week_index = {"monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}

  week_arr = ["Monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

  duration_tuple = duration.partition(":")
  duration_hours = int(duration_tuple[0])
  duration_minutes = int(duration_tuple[2])

  start_tuple = start.partition(":")
  start_minutes_tuple = start_tuple[2].partition(" ")
  start_hours = int(start_tuple[0])
  start_minutes = int(start_minutes_tuple[0])
  am_or_pm = start_minutes_tuple[2]
  am_or_pm_flip = {"AM": "PM", "PM": "AM"}

  amount_of_days = int(duration_hours / 24)

  minutes_results = start_minutes + duration_minutes
  if minutes_results >= 60:
    start_hours += 1
    minutes_results = minutes_results % 60
  amount_of_am_pm_flip = int((start_hours + duration_hours) / 12)
  end_hours = (start_hours + duration_hours) % 12

  minutes_results = minutes_results if minutes_results > 9 else "0" + str(end_hours)
  end_hours = end_hours = 12 if end_hours == 0 else end_hours
  if(am_or_pm == "PM" and start_hours + (duration_hours % 12) >= 12):
    amount_of_days += 1

  am_or_pm = am_or_pm_flip[am_or_pm] if amount_of_am_pm_flip % 2 ==  1 else am_or_pm

  return_time = str(end_hours) + ":" + str(minutes_results) + " " + am_or_pm
  if(day):
    day = day.lower()
    index = int((week_index[day]) + amount_of_days) % 7
    new_day = week_arr[index]
    return_time += ", " + new_day

  if(amount_of_days == 1):
    return return_time + " " + "(next day)"
  elif(amount_of_days > 1):
    return return_time + "(" + str(amount_of_days) + "days later)"

  return return_time
  


print(add_time("3:00 PM", "3:10"))
# Returns: 6:10 PM

print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday

print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM

print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)
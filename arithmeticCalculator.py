import re

def arithmetic_arranger(exercises, solve = False):

  if len(exercises) > 5:
    return "Error: Too many problems."

  first = ""
  second = ""
  lines = ""
  sumx = ""
  string = ""

  for exercise in exercises:
    if(re.search("[^\s0-9.+-=]", exercise)):
      if (re.search("[/]", exercise or re.search("[*]", exercise))):
        return "Error: Operator must be '+' or '-'."
      return "Error: Numbers must only contain digits."

    # Check for first and last number and also operand
    first_num = exercise.split(" ")[0]
    operator = exercise.split(" ")[1]
    last_num = exercise.split(" ")[2]

    # Check the lenght of the number given
    if (len(first_num) >= 5 or len(last_num) >= 5):
      return "Error: Numbers cannot be more than four digits."

    # Check if operation is positive or negative and also tackles the solve attribute
    combination = ""
    if(operator == "+"):
      combination = str(int(first_num) + int(last_num))
    elif(operator == "-"):
      combination = str(int(first_num) - int(last_num))

    # operation on the amount of lines to add
    lenght = max(len(first_num), len(last_num)) + 2
    top = str(first_num).rjust(lenght)
    bottom = operator + str(last_num).rjust(lenght - 1)

    line = ""

    res = str(combination).rjust(lenght)

    for leng in range(lenght):
      line += "-"

    # check is see if the exercise has ended
    if(exercise != exercises[-1]):
      first += top + '   '
      second += bottom + '   '
      lines += line + '   '
      sumx += res + '   '
    else:
      first += top
      second += bottom
      lines += line
      sumx += res

  # check to see if we perform calculatio or not
  if solve:
    string = first + "\n" + second + "\n" + lines + sumx
  else:
    string = first + "\n" + second + "\n"
  return string

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
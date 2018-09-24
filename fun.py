# Implement modulo without using the (%) operator.
def modulo(a, b):
    return a - b * (a/b)

# Take an input string and determine if exactly 3 question marks
# exist between every pair of numbers that add up to 10.
# If so, return true, otherwise return false.
def question_mark(s):
  curr_digit = 0
  equal_10 = False
  num_q_marks = 0
  for character in s:
    if character.isdigit():
      if int(character) + curr_digit == 10:
        if num_q_marks != 3:
          return False
        equal_10 = True
      curr_digit = int(character)
      num_q_marks = 0
    elif character == '?':
      num_q_marks += 1
  if(equal_10):
      return True
  else:
      return False

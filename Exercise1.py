#Exercise1.py
#This program is to calculate sum of two arbitrary numbers

print('Please enter the first number: ')
While True:
  try:
      x = float(input(''))
  except ValueError:
      print('Your data is not a number. Please enter again: ')
  continue
  else:
      break
      
print('Please enter the second number: ')
While True:
  try:
      y = float(input(''))
  except ValueError:
      print('Your data is not a number. Please enter again: ')
  continue
  else:
      break
      
print('Sum of the two numbers is: ', x + y)

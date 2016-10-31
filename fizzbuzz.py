#Create a function fizz_buzz to return 'Fizz', 'Buzz', 'FizzBuzz', or 
#the argument it receives, all depending on the argument of the function, 
#a number that is divisible by, 3, 5, or both 3 and 5, respectively.

def fizz_buzz(num):
  if num%3 == 0 and num%5 == 0:
    return "FizzBuzz"
  elif num%5 == 0:
    return "Buzz"
  elif num%3 == 0:
    return "Fizz"
  else:
    return num
    
fizz_buzz(105)   


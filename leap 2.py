#year = int(input("year: "))
#divisor = 4

def leap(year):
    if year % 4 != 0:
       return "not leap year"
    elif year % 400  == 0:
       return " leap year"
    elif year % 100 == 0:
       return "not leap year"
    else:
      return "leap year"


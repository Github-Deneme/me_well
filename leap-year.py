# To get year (integer input) from the user
# This is my first explanation
year = int(input("Enter a year: "))

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
    else:
        print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))
    # "Is it a prime number?" joseph hoca çözümü 
    n = int(input("Enter a positive number to check if it is a Prime Number: "))
    counter = 0 
    for i in range(1, n + 1) :
          if n % i == 0 :
                  counter += 1 

                  if (n == 0) or (n == 1) or (counter >= 3) :
                        print(n, " is not a Prime Number")
                    else :
                          print(n, " is a Prime Number")

# İF Condition true durumunda çalışır.

if 1 == 1:
    print("something")

def number_check(number):
    if number > 10:
        print("Number is bigger than ten")
    elif number < 10:
        print("Number is smaller than ten")
    else:
        print("Number equals ten.")

number_check(11)
number_check(10)
number_check(9)
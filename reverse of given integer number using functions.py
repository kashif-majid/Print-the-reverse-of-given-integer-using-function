def rev(number):
    reverse = 0
    while (number > 0):
        reminder = number % 10
        reverse = (reverse * 10) + reminder
        number = number // 10

    return reverse

i=1
while i==1:
    n = int(input("\nENTER INTEGER YOU WANT TO REVERSE: "))
    print("THE REVERSE OF {} IS: {}".format(n,rev(n)))

    i = int(input("\nIF U WANT TO CONTINUE PRESS 1 ELSE PRESS ANY KEY: "))

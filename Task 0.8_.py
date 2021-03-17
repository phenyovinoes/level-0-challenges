def converter_to_time(number):
    if number % 60 == 0 and number < 120:
        print(str(number // 60) + " hour " + str(number % 60) + " minutes")
    elif number % 60 == 0 and number >= 120:
        print(str(number // 60) + " hours " + str(number % 60) + " minute")
    elif number % 60 == 1 and number >= 120:
        print(str(number // 60) + " hours " + str(number % 60) + " minute")
    elif number % 60 == 1 and number < 120:
        print(str(number // 60) + " hour " + str(number % 60) + " minute")
    elif number % 60 >= 2 and number >= 120:
        print(str(number // 60) + " hours " + str(number % 60) + " minutes")
    elif number % 60 >= 2 and number < 120:
        print(str(number // 60) + " hour " + str(number % 60) + " minutes")


converter_to_time()

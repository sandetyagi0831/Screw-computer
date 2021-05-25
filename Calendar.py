
def monthcal(startday, totaldays):
    print("\nSun Mon Tues Wed Thus Fri Sat")
    print("-----------------------------")
    for i in range(1, startday):
        print("  ", end=" ")
    for i in range(1, totaldays + 1):
        if i < 10:
            print("  " + str(i), end=" ")
        else:
            print(" " + str(i), end=" ")
        startday = startday + 1
        if startday == 8:
            startday = 1
            print()
a = int(input("input Start day of the month (1-7): "))
b = int(input("Total no.of days in the month (28/29/30/31): "))
monthcal(a, b)

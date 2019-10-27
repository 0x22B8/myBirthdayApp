import datetime
import sys
import delta

birthday_day = int(sys.argv[1])
birthday_month = int(sys.argv[2])
birthday_year = int(sys.argv[3])

try:
    if delta.deltaCounting(birthday_day, birthday_month) == 0:
        print("♥♥♥♥♥♥♥♥♥♥♥♥♥♥")
        print("♥Today is your Birthday! ♥")
        print("♥♥♥♥♥♥♥♥♥♥♥♥♥♥")
    else:
        print("Until your birthday: ", delta.deltaCounting(birthday_day, birthday_month), " day(s)!")
except ValueError:
    print("Input 3 numbers as args (e.g. UntilMyBirthday.py 2 9 1995)")

sys.exit(0)

import datetime

today = datetime.date.today()
birthday = datetime.date(1995, 1, 2)
if today.month == birthday.month and today.day == birthday.day:
    print('Today is your birthday!')
else:
    birthdayInThisYear = datetime.date(today.year, birthday.month, birthday.day)
    if today.day <= birthday.day:
        if today.month <= birthday.month:
            delta = birthdayInThisYear - today
            print("Until your birthday", delta.days, "day(s).")
        else:
            delta = today - birthdayInThisYear
            print("Until your birthday", 365 - delta.days, "day(s).")
    else:
        if today.month < birthday.month:
            delta = birthdayInThisYear - today
            print("Until your birthday", delta.days, "day(s).")
        else:
            delta = today - birthdayInThisYear
            print("Until your birthday", 365 - delta.days, "day(s).")
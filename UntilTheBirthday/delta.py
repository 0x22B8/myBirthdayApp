import datetime

def deltaCounting(arg1, arg2):
    today = datetime.date.today()
    birthdayInThisYear = datetime.date(today.year, arg2, arg1)
    if today.day <= arg1:
        if today.month <= arg2:
            delta = birthdayInThisYear - today
            return delta.days
        else:
            delta = today - birthdayInThisYear
            return 365 - delta.days
    else:
        if today.month < arg2:
            delta = birthdayInThisYear - today
            return delta.days
        else:
            delta = today - birthdayInThisYear
            return 365 - delta.days

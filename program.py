import datetime


def print_title():
    print("-------------------------")
    print("      BIRTHDAY APP")
    print("-------------------------")
    print("")


def get_dob():
    year = input("What year were you born [YYYY]?")
    month = input("What month were you born [MM]?")
    day = input("What day were you born [DD]?")
    dob = datetime.date(int(year), int(month), int(day))
    return dob


def calculate_birthday(dob, today):
    bday = datetime.date(today.year, dob.month, dob.day)

    time_until_bday = today - bday

    return time_until_bday.days


def print_birthday(time_until_bday, dob):
    print("It looks like you were born on {}".format(str(dob)))
    if time_until_bday < 0:
        print("Looks like your birthday is in {} days!".format(time_until_bday))
    elif time_until_bday > 0:
        print("Looks like your birthday was {} days ago!".format(time_until_bday))
    else:
        print("Happy Birthday!!!")


def main():
    print_title()
    dob = get_dob()
    today = datetime.date.today()
    time_until_bday = calculate_birthday(dob, today)
    print_birthday(time_until_bday, dob)


if __name__ == "__main__":
    main()

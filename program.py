import journal


def print_title():
    print("--------------------------")
    print("   PERSONAL JOURNAL APP")
    print("--------------------------")
    print("")


def main_loop():
    username = input("What's your name?")
    jnal = journal.load(username)
    user_input = 'q'

    while user_input != 'x' and user_input:
        user_input = input("What do you want to do? [L]ist, [A]dd or E[x]it?")
        user_input = user_input.lower()
        if user_input == 'l':
            list_entries(jnal)
        elif user_input == 'a':
            add_entry(jnal)
        elif user_input != 'x' and user_input:
            print("Invalid entry")

    journal.save(username, jnal)
    return


def add_entry(jnal):
    entry = input("Enter your journal entry:\n")
    journal.add_entry(entry, jnal)
    return


def list_entries(jnal):
    for entry in jnal:
        print(entry)
    return


def main():
    print_title()
    main_loop()


if __name__ == "__main__":
    main()

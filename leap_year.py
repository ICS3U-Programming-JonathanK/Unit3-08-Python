#!/usr/bin/env python3
# Created by: Jonathan Kene
# Created on: May. 18, 2021
# This program checks to see if year typed from the user is a leap year or not


def main():

    years_string = input("Enter a year: ")
    print("")

    # make sure if the user types anything but an integer, it's not valid
    try:
        years_int = int(years_string)
        years_int = int(years_string)
        print("")
    except ValueError:
        print("Please enter a valid number")

    else:
        if (years_int > 0):
            if (years_int % 4) == 0:
                if (years_int % 100) == 0:
                    if (years_int % 400) == 0:
                        print("{0} is a leap year".format(years_int))
                    else:
                        print("{0} is not a leap year".format(years_int))
                else:
                    print("{0} is a leap year".format(years_int))
            else:
                print("{0} is not a leap year".format(years_int))
        else:
            print("{0} is not a valid year".format(years_int))
    finally:
        print("")
        print("Thank you for your input")


if __name__ == "__main__":
    main()

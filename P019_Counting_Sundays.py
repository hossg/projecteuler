# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

import os
import logging

expectedAnswer = 171

logger = logging.getLogger(os.path.basename(__file__))
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')


class day:
    day = 1
    month = 1
    year = 1900
    DayOfWeek = 1


def tickDay(d: day):
    d.day += 1
    if (d.month in [4, 6, 9, 11] and d.day == 31):
        d.month += 1
        d.day = 1
    elif (d.month == 2):
        leapYear = False
        if d.year % 4 == 0:
            leapYear = True
        if d.year % 100 == 0:
            leapYear = False
        if d.year % 400 == 0:
            leapYear = True
        if leapYear and d.day == 30:
            d.month += 1
            d.day = 1
        elif d.day == 29:
            d.month += 1
            d.day = 1
    elif d.day == 32:
        d.month += 1
        d.day = 1

    if d.month > 12:
        d.year += 1
        d.month = 1

    d.DayOfWeek += 1
    if d.DayOfWeek == 8:
        d.DayOfWeek = 1

# print("{} - {}/{}/{}".format(d.DayOfWeek, d.day,d.month,d.year))


def solution():
    count = 0
    d = day()

    while d.year < 1901:
        if (d.day == 1 and d.DayOfWeek == 7):
            count += 1
        tickDay(d)
    count1900 = count

    while d.year < 2001:
        if (d.day == 1 and d.DayOfWeek == 7):
            count += 1
        tickDay(d)
    count2000 = count

    #we need to calculate the number of 1st Sundays in an intermediate range, i.e. subtract off those
    # that occured in 1900 itself in order to answer the question
    sol = count2000 - count1900

    return sol


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logging=logging.getLogger(os.path.basename(__file__))
    solution = solution()
    logging.info('Solution = {}'.format(solution))
    assert (solution == expectedAnswer)

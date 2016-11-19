# https://www.hackerrank.com/challenges/time-conversion

import sys

def convert_time(time):
    period = time[-2:]
    hours = time[0:2]
    converted_hours = ''

    if period == 'AM':
        converted_hours = int(hours) % 12
    if period == 'PM':
        if hours != '12':
            converted_hours = int(hours) + 12
        else:
            converted_hours = hours
    converted_hours = str(converted_hours) if converted_hours > 9 else ('0' + str(converted_hours))
    return (converted_hours + time[2:-2])


def main():
    time = input().strip()
    print(convert_time(time))

if __name__ == '__main__':
    main()
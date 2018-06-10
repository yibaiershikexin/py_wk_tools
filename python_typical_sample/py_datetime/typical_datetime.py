import datetime
from pprint import pprint

# python3

# '2018-06-10 19:01:02.905515'
NOW = str(datetime.datetime.now())
DATETIME_NOW = datetime.datetime.now()
NOW_PARSE = "%Y-%m-%d %H:%M:%S.%f"


def str_to_datetime(datetime_str):
    # string corresponding time
    # '2018-06-10 19:09:31.975972'
    # datetime.datetime(2018, 6, 10, 19, 9, 31, 975972)
    _datetime = datetime.datetime.strptime(datetime_str, NOW_PARSE)
    pprint(datetime_str)
    pprint(_datetime)


def datetime_to_str(date_time):
    datetime_str = DATETIME_NOW.strftime("%d/%m/%y")
    pprint(date_time)
    pprint(datetime_str)


def main():
    # str_to_datetime(NOW)
    datetime_to_str(DATETIME_NOW)


main()

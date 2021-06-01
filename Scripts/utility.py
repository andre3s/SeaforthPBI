from datetime import datetime


def create_time():
    cur_timestamp = datetime.now()
    cur_month = cur_timestamp.strftime('%m')
    cur_year = cur_timestamp.strftime('%Y')

    return cur_month, cur_year

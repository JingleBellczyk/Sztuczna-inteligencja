from constants import *

# change time to datetime
def fix_time(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    hours = hours % 24
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'

# convert time to seconds
def time_to_seconds(time):
    return time.second + time.minute*60 + time.hour*3600

def seconds_to_hour_and_minute(seconds):
	return "godziny: ", seconds // HOUR_SECONDS,"minuty: ", (seconds % HOUR_SECONDS) // MIN_SECONDS
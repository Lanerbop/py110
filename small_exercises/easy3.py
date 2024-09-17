# AFTER MIDNIGHT (PART 1) -> purty good. could use constants for calculation

# Input: An integer representing minutes b/a midnight if -/+
# Ouptut: The time of day in a 24-hour format

# Data Structure:
# - Integers

# Algorithm
# - use an if statement to determine whether to add or sub time
# - if adding, add number % 1440 to minutes. 
# - initialize hours as minutes // 60
# - initialize final minutes as minutes % 60
# - if subtracting, initialize minutes to 1440 - (int % 1440)
# - initialize hours as minutes // 60
# - initialize final minutes as minutes % 60

# create conversion function
# - set minutes as parameter
# - initialize hours as minutes // 60
# - initialize final minutes as minutes % 60
# - return f string {2digthour}:{2digitminute}

# def minutes_to_time(minutes):
#     hours = minutes // 60
#     final_minutes = minutes % 60
#     return f"{hours:02}:{final_minutes:02}"

# def time_of_day(given_minutes):
#     MINUTES_PER_DAY = 1440
#     if given_minutes >= 0:
#         minutes = given_minutes % MINUTES_PER_DAY
#     else:
#         minutes = 1440 - (-given_minutes % MINUTES_PER_DAY)

#     return minutes_to_time(minutes)

# print(time_of_day(0) == "00:00")        # True
# print(time_of_day(-3) == "23:57")       # True
# print(time_of_day(35) == "00:35")       # True
# print(time_of_day(-1437) == "00:03")    # True
# print(time_of_day(3000) == "02:00")     # True
# print(time_of_day(800) == "13:20")      # True
# print(time_of_day(-4231) == "01:29")    # True

# AFTER MIDNIGHT (PART 2)

# def after_midnight(time_string):
#     hours = int(time_string[:2])
#     minutes = int(time_string[3:])
#     return (hours * 60 + minutes) % 1440

# def before_midnight(time_string):
#     return (1440 - after_midnight(time_string)) % 1440

# print(after_midnight("00:00") == 0)     # True
# print(before_midnight("00:00") == 0)    # True
# print(after_midnight("12:34") == 754)   # True
# print(before_midnight("12:34") == 686)  # True
# print(after_midnight("24:00") == 0)     # True
# print(before_midnight("24:00") == 0)    # True

# DOUBLE CHAR (PART 1)



def hello_func():
    print('Hello Functions!')

hello_func()

def hello(greetings, name = 'you'):
    return f'{greetings}, {name}'

print(hello('hi', 'Saroj'))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'Statics', 'Database', 'Java']
info = { 'name' : 'Saroj', 'age': 24, 'gender': 'Male', 'phoneno': 9843322391}

student_info(*courses, **info)


#Number of days per month. First value placeholder for indexing purposes
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """
    Return True for leap years, and False for non-leap years.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """
    Return number of days in that month in that year
    """
    if not 1 <= month <= 12:
        return "Invalid Value"

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(is_leap(2020))
print(days_in_month(2021,3))


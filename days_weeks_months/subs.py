import datetime
import math

goal_subs = 100000
current_sub = 3400
subs_to_goal = goal_subs - current_sub
avg_subs_day = 200

days_to_go = math.ceil(subs_to_goal / avg_subs_day)

today = datetime.date.today()

print(today + datetime.timedelta(days=days_to_go))
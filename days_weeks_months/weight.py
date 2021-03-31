import datetime

current_weight = 70
goal_weight = 60
avg_kgs_week = 1

start_date = datetime.date.today()
end_date = start_date

while current_weight > goal_weight:
    end_date += datetime.timedelta(days=7)
    current_weight -= avg_kgs_week

print(end_date)
print(f'Reached Goal in {(end_date - start_date).days // 7} weeks')
from file_import import import_csv
from datetime import datetime
from decimal import Decimal
from helper import create_leaderboard, sum_distance

date_format = '%Y-%m-%dT%H:%M:%S.000%z'
# 2023-05-23T16:02:00.000+02:00

# variables
total_distance    = Decimal()
bike_distance     = Decimal()
other_distance    = Decimal()
bike_leaderboard  = {}
other_leaderboard = {}

# importing and polishing data + Time Restrictions
current_month = datetime(2023, 5, 1)
data = import_csv('data/may.csv')
for row in data:
    row['Date'] = datetime.strptime(row['Date'], date_format).replace(tzinfo=None)
data = [row for row in data if row['Date'] > current_month]

# Bikers:
bike_activities = [row for row in data if row['Type'] == 'Ride']
bike_distance   = sum_distance(bike_activities)
bike_leaderboard = create_leaderboard(bike_activities)
print(f"Total bike distance:\t{bike_distance}")
for i, athlete in enumerate(bike_leaderboard): print(f"{i+1}.\t{athlete[0]}\t{athlete[1]}")

print()
# Others
other_activities = [row for row in data if row['Type'] != 'Ride']
other_distance   = sum_distance(other_activities)
other_leaderboard = create_leaderboard(other_activities)
print(f"Total other distance:\t{other_distance}")
for i, athlete in enumerate(other_leaderboard): print(f"{i+1}.\t{athlete[0]}\t{athlete[1]}")



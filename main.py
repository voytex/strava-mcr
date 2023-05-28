from file_import import import_csv
from datetime import datetime
from decimal import Decimal

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
bike_distance   = sum([Decimal(row['Distance']) for row in bike_activities])
for row in bike_activities:
    if row['Name'] not in bike_leaderboard.keys():
        bike_leaderboard[row['Name']] = Decimal(row['Distance'])
    else:
        bike_leaderboard[row['Name']] += Decimal(row['Distance'])
bike_leaderboard = sorted(bike_leaderboard.items(), key=lambda item: item[1], reverse=True)
print(bike_leaderboard)


# Others
other_activities = [row for row in data if row['Type'] != 'Ride']
other_distance   = sum([Decimal(row['Distance']) for row in other_activities])
for row in other_activities:
    if row['Name'] not in other_leaderboard.keys():
        other_leaderboard[row['Name']] = Decimal(row['Distance'])
    else:
        other_leaderboard[row['Name']] += Decimal(row['Distance'])
other_leaderboard = sorted(other_leaderboard.items(), key=lambda item: item[1], reverse=True)
print(other_leaderboard)




# # Total Club Distance:
# total_distance = sum([Decimal(row['Distance']) for row in data])
# print(f"Total Club Distance (Ride-only)\t{total_distance}")

# # Leaderboard
# athletes = {}
# for row in data:
#     if row['Name'] in athletes.keys():
#         athletes[row['Name']] += Decimal(row['Distance'])
#     else:
#         athletes[row['Name']] =  Decimal(row['Distance'])

# print(athletes)
# # for row in data: print(f"{row['Name']}\t{row['Type']}\t{row['Distance']}\t{row['Date']}")

# athletes = sorted(athletes.items(), key=lambda item: item[1], reverse=True)
# print(athletes)
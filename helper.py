from decimal import Decimal

def create_leaderboard(activities: list) -> dict:
    """Creates ordered leaderboard dictionary"""
    leaderboard = {}
    for row in activities:
        if row['Name'] not in leaderboard.keys():
            leaderboard[row['Name']] = Decimal(row['Distance'])
        else:
            leaderboard[row['Name']] += Decimal(row['Distance'])
    return sorted(leaderboard.items(), key=lambda item: item[1], reverse=True)

def sum_distance(activities: list) -> Decimal:
    """Sums 'Distance' of all activites"""
    return sum([Decimal(row['Distance']) for row in activities])
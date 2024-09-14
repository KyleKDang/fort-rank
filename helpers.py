from datetime import datetime

date_format = "%Y-%m-%d"

def calculate_age(birth_date_str):

    birth_date = datetime.strptime(birth_date_str, date_format)
    
    today = datetime.today()

    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    
    return age


def calculate_all_time(placements):
    region_multipliers = {
        'NAW': 0.75,
        'NAE': 1.0,
        'NA': 1.0,
        'EU': 1.25,
        'Global': 1.6,
        'Global (Third-Party Event)': 0.8
    }

    total = 0

    for placement in placements:
        rank = placement[3]
        region = placement[5]

        multiplier = region_multipliers.get(region, 1.0)

        total += (100 - (rank - 1) * 10) * multiplier

    return total

def calculate_2024(placements):
    region_multipliers = {
        'NAW': 0.75,
        'NAE': 1.0,
        'NA': 1.0,
        'EU': 1.2,
        'Global': 1.6,
        'Global (Third-Party Event)': 0.8
    }

    total = 0

    for placement in placements:
        date_str = placement[2]
        date = datetime.strptime(date_str, date_format)

        year = str(date.year)

        if year == "2024":

            rank = placement[3]
            region = placement[5]

            multiplier = region_multipliers.get(region, 1.0)

            total += (100 - (rank - 1) * 10) * multiplier

    return total

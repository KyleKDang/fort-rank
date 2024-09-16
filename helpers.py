from datetime import datetime

date_format = "%Y-%m-%d"

def calculate_age(birth_date_str):

    birth_date = datetime.strptime(birth_date_str, date_format)
    
    today = datetime.today()

    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    
    return age


def get_ordinal(number):
    if 10 <= number % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(number % 10, 'th')
    return f"{number}{suffix}"


def calculate_all_time(placements):
    region_multipliers = {
        'NAW': 0.5,
        'NAE': 1.0,
        'NA': 1.0,
        'EU': 1.2,
        'Global': 2,
        'Global (Third-Party Event)': 0.25
    }

    total = 0

    for placement in placements:
        rank = placement[3]
        region = placement[5]

        multiplier = region_multipliers.get(region, 1.0)

        if rank == 1:
            total += 200 * multiplier
        else:
            total += (100 - (rank - 1) * 10) * multiplier

    return total


def calculate_by_year(placements, selected_year):
    region_multipliers = {
        'NAW': 0.5,
        'NAE': 1.0,
        'NA': 1.0,
        'EU': 1.2,
        'Global': 3.0,
        'Global (Third-Party Event)': 0
    }

    total = 0

    for placement in placements:
        date_str = placement[2]
        date = datetime.strptime(date_str, date_format)

        year = str(date.year)

        if year == selected_year:

            rank = placement[3]
            region = placement[5]

            multiplier = region_multipliers.get(region, 1.0)

            if rank == 1:
                total += 200 * multiplier
            else:
                total += (100 - (rank - 1) * 10) * multiplier

    return total

from datetime import datetime

def calculate_age(birth_date_str):
    date_format = "%Y-%m-%d"
    
    birth_date = datetime.strptime(birth_date_str, date_format)
    
    today = datetime.today()

    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    
    return age

def calculate_all_time(placements):
    region_multipliers = {
        'NAE': 0.75,
        'NA': 1.0,
        'EU': 1.25,
        'Global': 2.0
    }

    total = 0

    for placement in placements:
        rank = placement[3]
        region = placement[5]

        multiplier = region_multipliers.get(region, 1.0)

        total += (100 - (rank - 1) * 10) * multiplier

    return total

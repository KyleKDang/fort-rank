from datetime import datetime

def calculate_age(birth_date_str):
    date_format = "%Y-%m-%d"
    
    birth_date = datetime.strptime(birth_date_str, date_format)
    
    today = datetime.today()

    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    
    return age

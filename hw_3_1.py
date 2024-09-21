from datetime import datetime

def get_days_from_today(date_string):

    # перетворюємо рядок в дату
    date = datetime.strptime(date_string, '%Y-%m-%d').date()

    # відображаємо поточну дату 
    current_date = datetime.today().date()

    # різниця в днях
    days_difference = (current_date - date).days
    
    # повертаємо результат 
    return days_difference



print(get_days_from_today("2024-09-20"))
print(get_days_from_today("2024-10-20"))

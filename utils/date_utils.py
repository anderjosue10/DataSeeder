from datetime import datetime, timedelta

def add_days(date, days):
    return date + timedelta(days=days)

def is_after(date1, date2):
    return date1 > date2
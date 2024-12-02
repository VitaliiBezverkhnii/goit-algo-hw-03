from datetime import datetime


def get_days_from_today(date: str) -> int:
    """
    Calculates the number of days between the given date and today.

    :param date: A string representing the date in the format "YYYY-MM-DD".
    :return: An integer indicating the number of days between the given date and today.
    """
    try:
        date_converted = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        difference = (today - date_converted).days
        return difference
    except ValueError as e:
        msg = f"Invalid date format or value: {date}. Expected format is 'YYYY-MM-DD'."
        print(msg)

print(get_days_from_today("1987-05-12"))
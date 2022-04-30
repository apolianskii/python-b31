import locale


class DateHelper:

    def __init__(self, date):
        locale.setlocale(locale.LC_ALL, 'en_US')  # ensures month names in English
        self.day_value = str(date.day)  # 1, 2, 3...
        self.month_value = date.strftime("%B")  # January, February, March...
        self.year_value = str(date.year)  # 1999, 2000, 2001...
        locale.setlocale(locale.LC_ALL, '')

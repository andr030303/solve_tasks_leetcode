# Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

# Example 1:

# Input: date = "2019-01-09"
# Output: 9
# Explanation: Given date is the 9th day of the year in 2019.
# Example 2:

# Input: date = "2019-02-10"
# Output: 41



class Solution(object):
    date = object
    def dayOfYear(self, date):

        # Делаем список из количетва дней в каждом месяце високосного года и обычного
        days_in_months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
        days_in_months_2 = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]

        # Из ввода берем год, месяц и день
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:])
        result = 0

        # Пробегаемся по всем месяцам и прибавляем количество дней в их месяцах, после него добавляем день
        if year % 4 == 0:
            for i in range(month):
                result += days_in_months_2[i]
            result += day
        else:
            for i in range(month):
                result += days_in_months[i]
            result += day
        return result




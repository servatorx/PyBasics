class MyData:
    def __init__(self, param1):
        self.param1 = param1

    @staticmethod
    def CheckData(day, month, year):
        if day >= 1 and day <= 31:
            if month >= 1 and month <= 12:
                if year > 1900 and year < 2021:
                    return True
        return False

    @classmethod
    def Data(cls, date_to_check):
        my_date = date_to_check.split('-')
        if (cls.CheckData(int(my_date[0]), int(my_date[1]), int(my_date[2]))):
            print(f"Дата {date_to_check} корректна")
        else:
            print(f"Дата {date_to_check} НЕ корректна")


MyData.Data("10-12-2020")
MyData.Data("10-13-2020")
MyData.Data("33-12-2020")



class Mathematician:
    def square_nums(self, nums: list) -> list:
        return [num ** 2 for num in nums]

    def remove_positives(self, nums: list) -> list:
        return [num for num in nums if num <= 0]

    def filter_leaps(self, years: list) -> list:
        """Залишає лише високосні роки."""
        return [year for year in years if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)]

m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]

assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]

# Перевірка років (2001 - ні, 1884 - так, 1995 - ні, 2003 - ні, 2020 - так)
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

print("Усі перевірки пройдено успішно!")
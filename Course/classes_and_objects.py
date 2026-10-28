# Day 21/30
# L.1

class Statistics:
    def __init__(self, list):
        self.list = list

    def print_list(self):
        a = [i for i in self.list]
        print(a)

    def count(self):
        cnt = 0
        for i in self.list:
            cnt += 1
        return cnt

    def sum(self):
        sum = 0
        for i in self.list:
            sum += i
        return sum

    def min(self):
        min = self.list[0]
        for i in self.list:
            if i < min:
                min = i
        return min

    def max(self):
        max = self.list[0]
        for i in self.list:
            if i > max:
                max = i
        return max

    def range(self):
        max = self.max()
        min = self.min()
        range = max - min
        return range

    def mean(self):
        avg = self.sum() / self.count()
        return avg

    def median(self):
        self.list.sort()
        if len(self.list) % 2 == 0:
            return (self.list[len(self.list) - 1 // 2] + self.list[len(self.list) // 2]) / 2
        else:
            return self.list[len(self.list) // 2]

    def mode(self):
        new_set = set(self.list)
        new_dict = {}
        max = -1
        new_list = []
        for number in new_set:
            count = self.list.count(number)
            new_dict[number] = count
            if count > max:
                max = count

        for key, value in new_dict.items():
            if value == max:
                new_list.append(key)
                new_list.append(f'{max}')

        return (new_list)

    def var(self):
        new_list = []
        sum = 0
        cnt = 0
        for number in self.list:
            new_list.append((number - self.mean()) ** 2)
        for number in new_list:
            sum += number
            cnt += 1

        return sum / cnt

    def std(self):
        return self.var() ** 0.5

    def describe(self):
        print(self.count())
        print(self.sum())
        print(self.min())
        print(self.max())
        print(self.range())
        print(self.mean())
        print(self.median())
        print(self.mode())
        print(self.var())
        print(self.std())

list = [31, 32, 32, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(list)

# L.2

class PersonAccount:
    def __init__(self, first_name, last_name, incomes, expenses):
        self.first_name = first_name
        self.last_name = last_name
        self.incomes = incomes
        self.expenses = expenses

    def add_income(self, dict):
        for key, value in dict.items():
            self.incomes[key] = value

    def add_expense(self, dict):
        for key, value in dict.items():
            self.expenses[key] = value

    def total_income(self):
        total_sum = 0
        for key, value in self.incomes.items():
            total_sum += int(key)
        return total_sum

    def total_expense(self):
        total_sum = 0
        for key, value in self.expenses.items():
            total_sum += int(key)
        return total_sum

    def account_balance(self):
        balance = self.total_income() - self.total_expense()
        return balance

    def account_info(self):
        print(self.display_info())
        print(f"Общий доход: {self.total_income()}")
        print(f"Общие расходы: {self.total_expense()}")
        print(f"Баланс счёта: {self.account_balance()}")

    def display_info(self):
        return self.first_name, self.last_name, self.incomes, self.expenses

person = PersonAccount('Matthew', 'Carbonara', {120000: 'Зарплата', 1000: 'Подарок от друга'}, {40000: 'Плата за жильё'})
person.add_income({'1000': 'Подарок'})
person.add_expense({'8403': 'ЖКХ'})
person.account_info()o
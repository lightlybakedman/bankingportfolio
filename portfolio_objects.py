from interest_rates import get_central_bank_rate
import random
from copy import deepcopy

percentage_to_decimal = lambda x: x / 100
random_interest_rate = lambda: random.randrange(-100, 100, 1) / 1000


class Portfolio:
    def __init__(self, accounts: list):
        self.accounts = accounts

    def calculate_balances(self):
        for account in self.accounts:
            account.calculate_balance()

    def calculate_total_balance(self):
        return sum([account.balance for account in self.accounts])

    def rebalance(self):
        total_balance = self.calculate_total_balance()
        for account in self.accounts:
            account.balance = total_balance / len(self.accounts)


class RandomInterestAccount:
    def __init__(self, currency: str, balance: int, country: str):
        self.currency = currency
        self.balance = balance
        self.country = country

    def calculate_balance(self):
        self.balance = self.balance * (1 + random_interest_rate())


# test values
initial_amount = 10000

germany = RandomInterestAccount("AUD", initial_amount, "Germany")
united_states = RandomInterestAccount("AUD", initial_amount, "United States")
australia = RandomInterestAccount("AUD", initial_amount, "Australia")
china = RandomInterestAccount("AUD", initial_amount, "China")

accounts = [germany, united_states, australia, china]

initial_portfolio = Portfolio(accounts)


def generate_portfolio_over_time(portfolio: Portfolio, years: int):
    values = {0: portfolio}
    for year in range(1, years):
        portfolio.calculate_balances()
        portfolio.rebalance()
        print(f"Year {year + 1}: {portfolio.calculate_total_balance()}")
        values[year] = deepcopy(portfolio)


generate_portfolio_over_time(initial_portfolio, 20)

# # plotting

# import matplotlib.pyplot as plt

# balances = [list(account.calculate_balance(20).values()) for account in accounts]
# years_list = list(range(starting_year, starting_year + years + 1))

# # print(balances)
# plt.plot(years_list, balances[0], label="Germany")
# plt.plot(years_list, balances[1], label="United States")
# plt.plot(years_list, balances[2], label="Australia")
# plt.plot(years_list, balances[3], label="China")
# leg = plt.legend(loc="upper center")  # add labels to lines
# # plt.axis([starting_year, starting_year + years, 0, 20000])
# plt.show()

from interest_rates import get_central_bank_rate
import random

percentage_to_decimal = lambda x: x / 100


class ConstantInterestAccount:
    def __init__(
        self, currency: str, initial_amount: int, country: str, starting_year: int
    ):
        self.currency = currency
        self.initial_amount = initial_amount
        self.country = country
        self.starting_year = starting_year

        self.rate = get_central_bank_rate(country)

    def calculate_balance(self, years: int):
        balances = {self.starting_year: self.initial_amount}
        for year in range(1, years + 1):
            balances[self.starting_year + year] = (
                self.initial_amount * (1 + percentage_to_decimal(self.rate)) ** year
            )  # calculate the balance for each year
        return balances


class RandomAccount:
    def __init__(
        self, currency: str, initial_amount: int, country: str, starting_year: int
    ):
        self.currency = currency
        self.initial_amount = initial_amount
        self.country = country
        self.starting_year = starting_year

    def calculate_balance(self, years: int):
        get_rate = (
            lambda: random.randrange(-100, 100, 1) / 1000
        )  # random interest rate from -10.0% to 10.0%
        balances = {self.starting_year: self.initial_amount}
        for year in range(1, years + 1):
            balances[self.starting_year + year] = balances[
                self.starting_year + year - 1
            ] * (1 + get_rate())
        return balances


# test values
initial_amount = 10000
starting_year = 2023
years = 20

germany = ConstantInterestAccount("AUD", initial_amount, "Germany", starting_year)
united_states = ConstantInterestAccount(
    "AUD", initial_amount, "United States", starting_year
)
australia = ConstantInterestAccount("AUD", initial_amount, "Australia", starting_year)
china = RandomAccount("AUD", initial_amount, "China", starting_year)

accounts = [germany, united_states, australia, china]

print("a")  # debugging breakpoint

# plotting

import matplotlib.pyplot as plt

balances = [list(account.calculate_balance(20).values()) for account in accounts]
years_list = list(range(starting_year, starting_year + years + 1))

print(balances)
plt.plot(years_list, balances[0], label="Germany")
plt.plot(years_list, balances[1], label="United States")
plt.plot(years_list, balances[2], label="Australia")
plt.plot(years_list, balances[3], label="China")
# plt.axis([starting_year, starting_year + years, 0, 20000])
plt.show()

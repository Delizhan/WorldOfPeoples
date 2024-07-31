from random import randint

class BankAccount:
    def __init__(self, name, currency, accounts, balance = 0.0):
        self.__name = name
        self.__card_number = self.generate_card_number(accounts)
        self.__balance = balance

        self.__currency = currency
        self.__credit_limit = 10000.0
        self.__credit_funds = self.__credit_limit # кредитні кошти
        self.__credit_funds_give = 0.0
        self.__credit_funds_take = self.__credit_limit
        self.__interest_rate = 0.02 # місячна відсоткова ставка
        self.__credit_has_not_been_repaid_for = 0 # лічильник часу, який відслідковує, скільки місяців не повертались кредитні кошти
        self.__is_blocked = False
        self.__count_credit = 1

    @property
    def name(self):
        return self.__name

    @property
    def card_number(self):
        return self.__card_number

    @property
    def balance(self):
        return self.__balance

    @property
    def currency(self):
        return self.__currency

    @property
    def credit_limit(self):
        return self.__credit_limit

    @property
    def credit_funds(self):
        return self.__credit_funds

    @property
    def credit_funds_give(self):
        return self.__credit_funds_give

    @property
    def credit_funds_take(self):
        return self.__credit_funds_take

    @property
    def interest_rate(self):
        return self.__interest_rate

    @property
    def credit_has_not_been_repaid_for(self):
        return self.__credit_has_not_been_repaid_for

    @property
    def count_credit(self):
        return self.__count_credit

    @property
    def is_blocked(self):
        return self.__is_blocked

    @is_blocked.setter
    def is_blocked(self, is_blocked):
        self.__is_blocked = is_blocked

    def generate_card_number(self, accounts):
        while True:
            number = ""
            for i in range(4):
                block = ''.join([str(randint(0,9)) for _ in range(4)])
                number += block + " "
            number.strip() #видалення останнього пробілу

            if len(accounts) != 0:
                count = 0
                for ac in accounts:
                    if ac.card_number != number:
                        count += 1
                if count == len(accounts):
                    return number
            else:
                return number

    def deposit (self, funds): # покласти на рахунок
        if self.__count_credit != 0:
            if self.__credit_funds < self.__credit_limit:
                if funds <= (self.__credit_limit - self.__credit_funds):
                    self.__credit_funds += funds
                    funds -= self.__credit_funds
                else:
                    funds -= (self.__credit_limit - self.__credit_funds)
                    self.__credit_funds = self.__credit_limit
        self.__balance += funds

    def withdraw(self, funds):
        if self.__balance >= funds:
            self.__balance -= funds
            return f"З Вашого рахунку знято {funds} {self.__currency}."
        elif self.__balance + self.__credit_funds >= funds:
            withdrawn_from_credit = funds - self.__balance
            self.__credit_funds -= withdrawn_from_credit
            self.__balance = 0
            return f"З основного рахунку та кредитного рахунку знято {funds} {self.__currency}."
        else:
            return "Для зняття недостатньо коштів."

    def change_limit(self, new_limit):
        if self.__credit_has_not_been_repaid_for == 0:
            self.__credit_limit = new_limit
            return f"Кредитний ліміт змінено: {self.__credit_limit} {self.__currency}."
        else:
            return "Кредитний ліміт не можна змінити через кредитну заборгованість."

    def __str__(self):
        return (f"Рахунок: {self.__name}\n"
                f"Номер картки: {self.__card_number}\n"
                f"Баланс: {self.__balance} {self.__currency}\n"
                f"Кредитний ліміт: {self.__credit_limit} {self.__currency}\n"
                f"Кредитні кошти: {self.__credit_funds} {self.__currency}\n"
                f"Сума коштів, що взята в кредит: {self.__credit_funds_take} {self.__currency}\n"
                f"Виплачена сума коштів: {self.__credit_funds_give} {self.__currency}\n"
                f"Кількість кредитів: {self.__count_credit}\n"
                f"Заборгованість: {self.__credit_has_not_been_repaid_for} місяців\n"
                f"Блокування карти: {self.__is_blocked}")

    def interest_accrual(self):
        if self.__credit_has_not_been_repaid_for == 0:
            self.__balance *= (1 + self.__interest_rate)

    def credit_observe(self):
        if self.__credit_funds_take == self.__credit_funds_give:
            self.__credit_has_not_been_repaid_for = 0
            self.__credit_funds_give = 0.0
            self.__credit_funds_take = 0.0
            self.__credit_funds = 0.0
        else:
            self.__credit_has_not_been_repaid_for += 1

    def repay_loan(self, funds): # погасити кредит - власне вигаданий метод
        remains_return = self.__credit_funds_take - self.__credit_funds_give
        if remains_return <= 0:
            return "Кредит уже погашено."
        elif funds < remains_return:
            self.__credit_funds_give += funds
            return "Кошти прийнято."
        elif funds == remains_return:
            self.__credit_funds_give = 0.0
            self.__credit_funds_take = 0.0
            self.__count_credit -= 1
            return "Кредит погашено."
        elif funds > remains_return:
            remainder = funds - remains_return
            self.__credit_funds_give = 0.0
            self.__credit_funds_take = 0.0
            self.__balance += remainder
            self.__count_credit -= 1
            return f"Кредит погашено. Залишок ({remainder} {self.__currency}) зараховано на баланс."

    def take_loan(self, funds):
        if self.__count_credit == 0:
            if funds <= self.__credit_limit:
                self.__credit_funds = funds
                self.__credit_funds_take = funds
                self.__count_credit += 1
                return f"Ви успішно взяли кредит у розмірі {funds} {self.__currency}."
            else:
                return (f"Банк не можете дати кредит у розмірі {funds} {self.__currency}.\n"
                        f"Кредитний ліміт становить {self.__credit_limit} {self.__currency}.")
        else:
            return "Ви уже маєте кредит."

from random import randint, uniform

class Person:
    def __init__(self, name, bank, name_ac, currency_ac, accounts, balance_ac=0.0):
        self.__name = name
        self.__cash = randint(1000, 50000)
        self.__account = bank.create_account(name_ac, currency_ac, accounts, balance_ac)

    @property
    def name(self):
        return self.__name

    @property
    def cash(self):
        return self.__cash

    @property
    def account(self):
        return self.__account
    def deposit(self, funds):
        if self.__cash >= funds:
            self.__account.deposit(funds)
            self.__cash -= funds
            return "Поповнення банківського рахунку здійснено."
        else:
            return "Для поповнення банківського рахунку недостатньо коштів."

    def withdraw(self, funds):
        if self.__account.balance >= funds or self.__account.balance + self.__account.credit_funds >= funds:
            print(self.__account.withdraw(funds))
            self.__cash += funds

    def interact_with_casino(self, casino):
        if self.__cash >= 10:
            bet = uniform(10, self.__cash)
            winning = casino.play(bet)
            self.__cash += winning - bet
            return f"Кеш після гри в казино: {self.__cash}."
        else:
            return (f"У Вас недостатньо коштів для гри в казино.\nМінімальна ставка = 10 {self.__account.currency}.\n"
                    f"Кеш: {self.__cash} {self.__account.currency}.")

    def interact_with_bank_user(self):
        while True:
            print()
            print(f"1 - поповнити банківський рахунок;\n"
                  f"2 - зняти кошти з банківського рахунку;\n"
                  f"3 - взяти кредит;\n"
                  f"4 - погасити кредит;\n"
                  f"5 - показати інформацію про банківський рахунок;\n"
                  f"6 - вийти з меню.\n")
            print()
            while True:
                try:
                    number = int(input("Введіть номер дії, яку хочете здійснити --> "))
                    if not number or number < 1 or number > 6:
                        raise Exception
                    else:
                        break
                except Exception:
                    print("Некоректно введений номер.")

            if number == 1:
                print(f"Ви маєте {self.__cash} {self.__account.currency}.")
                if self.__cash != 0.0:
                    while True:
                        try:
                            money = float(input("Введіть суму коштів, що хочете зарахувати на банківський рахунок --> "))
                            if not money:
                                raise Exception
                            elif money <= 0 or money > self.__cash:
                                raise Exception
                            else:
                                break
                        except Exception:
                            print("Некоректно введена сума коштів.")

                    print(self.deposit(money))
                else:
                    print("Недостатньо коштів.")

            elif number == 2:
                print(f"На банківському рахунку Ви всього маєте {self.__account.balance + self.__account.credit_funds} {self.__account.currency}.")
                if self.__account.balance + self.__account.credit_funds != 0:
                    while True:
                        try:
                            money = float(input("Введіть суму коштів, що хочете зняти з банківського рахунку --> "))
                            if not money or money <= 0 or money > self.__account.balance + self.__account.credit_funds:
                                raise Exception
                            else:
                                break
                        except Exception:
                            print("Некоректно введена сума коштів.")

                    self.withdraw(money)

            elif number == 3:
                while True:
                    try:
                        money = float(input("Введіть суму коштів, що хочете взяти в кредит --> "))
                        if not money or money <= 0:
                            raise Exception
                        else:
                            break
                    except Exception:
                        print("Некоректно введена сума коштів.")

                print(self.__account.take_loan(money))

            elif number == 4:
                print(f"Ви маєте {self.__cash} {self.__account.currency} в кеші.")
                if self.__cash != 0.0:
                    while True:
                        try:
                            money = float(input("Введіть суму коштів, щоб погасити кредит --> "))
                            if not money or money <= 0 or money > self.__cash:
                                raise Exception
                            else:
                                break
                        except Exception:
                            print("Некоректно введена сума коштів.")

                    print(self.__account.repay_loan(money))
                    if self.__account.credit_funds != self.__account.credit_funds_give:
                        self.__cash -= money
                else:
                    print("Недостатньо коштів.")

            elif number == 5:
                print(self.__account)
            elif number == 6:
                break

    def interact_with_bank_auto(self):
        if self.__account.count_credit != 0: # 4 - погасити кредит
            if self.__cash != 0.0:
                print(self.__account.repay_loan(self.__cash))
        if self.__account.count_credit != 0:
            if self.__account.balance != 0:
                print(self.__account.repay_loan(self.__account.balance))

        if self.__cash < 500: # 2 - зняти кошти
            if self.__account.balance != 0.0:
                self.withdraw(self.__account.balance)

        if self.__cash > 3000: # 1 - поповнити банківський рахунок
            print(self.deposit(2000))

        if self.__cash == 0.0 and self.__account.balance == 0.0: # 3 - взяти кредит
            print(self.__account.take_loan(self.__account.credit_limit))

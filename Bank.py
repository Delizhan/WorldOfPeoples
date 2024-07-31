from BankAccount import BankAccount

class Bank:
    def __init__(self):
        self.__account_list = []

    @property
    def account_list(self):
        return self.__account_list

    def create_account(self, name_ac, currency_ac, accounts, balance_ac = 0.0):
        new_account = BankAccount(name_ac, currency_ac, accounts, balance_ac)
        self.__account_list.append(new_account)
        return new_account  # Запис посилання на акаунт до об'єкту Person

    def process_accounts(self):
        for account in self.__account_list:
            account.credit_observe()
            # Якщо заборгованість довше 6 місяців, то блокуємо акаунт
            if account.credit_has_not_been_repaid_for >= 6:
                account.is_blocked = True
            elif account.credit_has_not_been_repaid_for == 0:
                account.change_limit(account.credit_limit * 2)
                account.interest_accrual()
            print(account, "\n")
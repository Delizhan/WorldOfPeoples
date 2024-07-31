from Person import Person
from Bank import Bank
from Casino import Casino

class World:
    def __init__(self, population):
        self.people = []
        self.bank = Bank()
        self.casino = Casino()
        self.__population = population

    def live(self):
        print(f"1 - операції з банківським рахунком, що проводяться користувачем за одного з мешканців;\n"
              f"2 - операції з банківським рахунком, що проводяться автоматично над усіма мешканцями;\n"
              f"3 - гра в казино за одного з мешканців;\n"
              f"4 - гра в казино усіх мешканців автоматично;\n"
              f"5 - пройшов місяць;\n")
        while True:
            try:
                number = int(input("Введіть номер дії, яку хочете здійснити --> "))
                if not number or number < 1 or number > 5:
                    raise Exception
                else:
                    break
            except Exception:
                print("Некоректно введений номер.")

        if number == 1:
            while True:
                print(f"У світі всього проживає {len(self.people)} людей.")
                try:
                    n = int(input("Введіть номер людини, під ім'ям якої хочете проводити відповідні операції --> "))
                    if not number or number < 1 or number > len(self.people):
                        raise Exception
                    else:
                        n -= 1
                        break
                except Exception:
                    print("Некоректно введений номер.")
            if self.people[n].account.is_blocked == False:
                self.people[n].interact_with_bank_user()
            else:
                print("Ваш банківський рахунок заблоковано.")

        elif number == 2:
            for person in self.people:
                print(f"{person.name}:")
                person.interact_with_bank_auto()
                print()

        elif number == 3:
            while True:
                print(f"У світі всього проживає {len(self.people)} людей.")
                try:
                    n = int(input("Введіть номер людини, під ім'ям якої хочете проводити відповідні операції --> "))
                    if not number or number < 1 or number > len(self.people):
                        raise Exception
                    else:
                        n -= 1
                        break
                except Exception:
                    print("Некоректно введений номер.")

            print(self.people[n].interact_with_casino(self.casino))

        elif number == 4:
            for person in self.people:
                print(f"{person.name}:")
                print(person.interact_with_casino(self.casino))
                print()

        elif number == 5:
            print("Зміни, які відбулися після обробки акаунтів:")
            self.bank.process_accounts()
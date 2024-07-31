from Person import Person
from World import World

world = World(10)
person1 = Person("Деліжан І.С.", world.bank, "UA123052990000012345678912345", "USD", world.bank.account_list, 10000.0)
world.people.append(person1)
person2 = Person("Вестніков В.М.", world.bank, "UA123052990000012345678912347", "EUR", world.bank.account_list, 5000.0)
world.people.append(person2)
person3 = Person("Гальцов І.М.", world.bank, "UA123052990000012345678912348", "USD", world.bank.account_list, 1000.0)
world.people.append(person3)
person4 = Person("Демиденко К.В.", world.bank, "UA123052990000012345678912349", "UAH", world.bank.account_list, 2000.0)
world.people.append(person4)
person5 = Person("Єфременко Б.В.", world.bank, "UA123052990000012345678912344", "USD", world.bank.account_list, 1500.0)
world.people.append(person5)
person6 = Person("Замоздра В.О.", world.bank, "UA123052990000012345678912312", "EUR", world.bank.account_list, 1000.0)
world.people.append(person6)
person7 = Person("Коляндра Ю.М.", world.bank, "UA123052990000012345678912315", "USD", world.bank.account_list, 1000.0)
world.people.append(person7)
person8 = Person("Кузьмичов І.І.", world.bank, "UA1230529900000123456789123435", "UAH", world.bank.account_list, 3000.0)
world.people.append(person8)
person9 = Person("Лагута В.Д.", world.bank, "UA123052990000012345678912365", "EUR", world.bank.account_list, 1300.0)
world.people.append(person9)
person10 = Person("Макарук А.В.", world.bank, "UA123052990000012345678912345", "UAH", world.bank.account_list, 1000.0)
world.people.append(person10)

while True:
      print()
      print(f"1 - додати мешканця до світу;\n"
            f"2 - показати інформацію про всіх мешканців світу;\n"
            f"3 - світ прокинувся;\n"
            f"4 - вийти з програми.\n")
      number = -1
      while True:
            try:
                  number = int(input("Введіть номер дії, яку хочете здійснити --> "))
                  if not number or number < 1 or number > 4:
                        raise Exception
                  else:
                        print()
                        break
            except Exception:
                  print("Некоректно введений номер.")

      if number == 1:
            while True:
                  try:
                        name = input("Введіть ПІБ мешканця --> ")
                        if not name or len(name.split()) == 0:
                              raise Exception
                        else:
                              break
                  except Exception:
                        print("Некоректно введенe ім'я.")

            while True:
                  try:
                        rec = input("Введіть номер рахунку (14 цифр) --> ")
                        if not rec or len(rec.split()) == 0 or\
                              len(rec) != 14 or not rec.isdigit():
                              raise Exception
                        else:
                              break
                  except Exception:
                        print("Некоректно введений номер рахунку.")

            while True:
                  try:
                        cur = input("Введіть валюту (USD/EUR/UAH) --> ")
                        if cur != "USD" and cur != "EUR" and cur != "UAH":
                              raise Exception
                        else:
                              break
                  except Exception:
                        print("Некоректно введена валюта.")

            while True:
                  try:
                        bal = float(input("Введіть баланс --> "))
                        if not bal:
                              raise Exception
                        else:
                              break
                  except Exception:
                        print("Некоректно введений баланс.")

            person = Person(name, world.bank, "UA1230529900000" + rec, cur, world.bank.account_list, bal)
            world.people.append(person)
            print()

      elif number == 2:
            for person in world.people:
                  print(f"ПІБ: {person.name};")
                  print(f"Кеш: {person.cash};")
                  print(person.account)
                  print()

      elif number == 3:
            world.live()
      elif number == 4:
            break
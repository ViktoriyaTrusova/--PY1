money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

grow = 1.05
month = 0  # количество месяцев, которое можно прожить
delta = salary - spend

while money_capital + delta >= spend:
    money_capital += spend
    spend = spend * grow

    month += 1

      break
print(month)



def select_money():
    moneys = [100, 50, 20, 10, 5, 1]
    new_list = []
    money = int(input('找零：'))
    for i in range(0, len(moneys)):
        if money == 0:
            break
        new_money = money // moneys[i]
        if new_money > 0:
            money = money - new_money * moneys[i]
            for j in range(new_money):
                new_list.append(moneys[i])
            print(f'{moneys[i]}\t元\t{new_money}张\t')

    print(new_list)


select_money()

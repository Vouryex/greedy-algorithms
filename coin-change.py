def init_change(denominations):
    change = {}
    for denomination in denominations:
        change[denomination] = 0
    return change


def max_denomination(denominations, money):
    max = denominations[0]
    for i in range(1, len(denominations)):
        denomination = denominations[i]
        if denomination > max and denomination <= money:
            max = denomination
    return max


def display_change(change_dict):
    print("Denomination       Quantity")
    for change in change_dict:
        print("{0:^12}       {1:^8}".format(change, change_dict[change]))


def coin_change(denominations, money):
    change = init_change(denominations)
    while money != 0:
        max = max_denomination(denominations, money)
        change[max] += 1
        money -= max
    display_change(change)


denominations = [1, 5, 8, 10]
money = 16
coin_change(denominations, money)

# time complexity: O(n) where n denotes money

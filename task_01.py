""" Задача: дано суму грошей та масив монет. Знайти мінімальну кількість монет, які можна використати для видачі суми грошей. 
    ДЛЯ ПОРІВНЯННЯ ШВИДКОСТІ РОБОТИ ВИКОРИСТАНО ЗМІННУ КІЛЬКИІТЬ МОНЕТ, ЯКІ ПОТРІБНІ ДЛЯ ВИДАЧІ СТАЛОЇ СУМИ ГРОШЕЙ.
"""
import time

# Жадібний алгоритм
def find_coins_greedy(amount, coins):
    coins = sorted(coins, reverse=True) # Сортування монет за спаданням
    start_time = time.time()
    coin_count = {}
    for coin in coins:
        if amount == 0:
            break
        count = amount // coin
        if count > 0:
            coin_count[coin] = count
            amount -= count * coin
    end_time = time.time()
    elapsed_time = end_time - start_time
    return coin_count, elapsed_time

# Динамічне програмування
def find_min_coins(amount, coins):
    coins = sorted(coins, reverse=True) # Сортування монет за спаданням
    start_time = time.time()
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    coin_count = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in coin_count:
            coin_count[coin] += 1
        else:
            coin_count[coin] = 1
        amount -= coin

    end_time = time.time()
    elapsed_time = end_time - start_time
    return coin_count, elapsed_time

# Масиви малої та великої розмірностей
amount = 1013
coins_small = [50, 25, 10, 5, 2, 1]
coins_large = [50, 25, 10, 5, 2, 1, 3, 15, 20, 40, 60, 100, 200, 500, 1000, 2000, 5000, 10000]

greedy_small, t = find_coins_greedy(amount, coins_small)
print(f"Жадібний алгоритм (мало монет): {greedy_small} - час виконання: {t:.6f} секунд")

greedy_large, t = find_coins_greedy(amount, coins_large)
print(f"Жадібний алгоритм (багато монет): {greedy_large} - час виконання: {t:.6f} секунд")

dp_small, t = find_min_coins(amount, coins_small)
print(f"Динамічне програмування (мало монет): {dp_small} - час виконання: {t:.6f} секунд")

dp_large, t = find_min_coins(amount, coins_large)
print(f"Динамічне програмування (багато монет):{dp_large} - час виконання: {t:.6f} секунд")

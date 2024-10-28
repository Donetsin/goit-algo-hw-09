""" Задача: дано суму грошей та масив монет. Знайти мінімальну кількість монет, які можна використати для видачі суми грошей. 
    ДЛЯ ПОРІВНЯННЯ ШВИДКОСТІ РОБОТИ ВИКОРИСТАНО ЗМІННУ СУМИ ГРОШЕЙ ПРИ СТАЛІЙ КІЛЬКОСТІ МОНЕТ.
"""
import time

# Жадібний алгоритм
def find_coins_greedy(amount, coins):
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
small_amount = 113
large_amount = 1000113
coins = [50, 25, 10, 5, 2, 1]

greedy_small_time, t = find_coins_greedy(small_amount, coins)
print(f"Жадібний алгоритм (мала сума): {greedy_small_time} - час виконання: {t:.6f} секунд")

greedy_large_time, t = find_coins_greedy(large_amount, coins)
print(f"Жадібний алгоритм (велика сума): {greedy_large_time} - час виконання: {t:.6f} секунд")

dp_small_time, t = find_min_coins(small_amount, coins)
print(f"Динамічне програмування (мала сума): {dp_small_time} - час виконання: {t:.6f} секунд")

dp_large_time, t = find_min_coins(large_amount, coins)
print(f"Динамічне програмування (велика сума):{dp_large_time} - час виконання: {t:.6f} секунд")

from itertools import count

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Primes = []
NotPrimes = []

item_num = 0
for i in range(1, len(numbers)):
    item_num = numbers[i]
    is_prime = True
    for j in range(2, item_num):
        if item_num % j == 0:
            if item_num != j:
                NotPrimes.append(item_num)
                is_prime = False
                break
    if is_prime:
        Primes.append(item_num)

SetNotPrimes = set(NotPrimes)
NotPrimes = list(SetNotPrimes)

print(f'Primes: {Primes}')
print(f'NotPrimes: {NotPrimes}')

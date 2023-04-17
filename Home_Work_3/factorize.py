import time
from multiprocessing import Pool, cpu_count

def factorize(numbers):
    result = []
    for number in numbers:
        factors = []
        for i in range(1, number + 1):
            if number % i == 0:
                factors.append(i)
        result.append(factors)
    return result

def factorize_single(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def factorize_parallel(numbers):
    with Pool(cpu_count()) as pool:
        return pool.map(factorize_single, numbers)

numbers = [1, 2, 4, 8, 16, 32, 64, 128]

start_time = time.time()
result = factorize(numbers)
end_time = time.time()

print("Synchronous execution time:", end_time - start_time)

start_time = time.time()
result = factorize_parallel(numbers)
end_time = time.time()

print("Parallel execution time:", end_time - start_time)

import time
from concurrent.futures import ThreadPoolExecutor
def formula_1(iterations):
    result = []
    for x in range(iterations):
        result.append(x ** 2 - x ** 2 + x ** 4 - x ** 5 + x + x)
    return sum(result)

def formula_2(iterations):
    result = []
    for x in range(iterations):
        result.append(x + x)
    return sum(result)

def compute(iterations):
    with ThreadPoolExecutor() as executor:
        start_time_1 = time.time()
        future_1 = executor.submit(formula_1, iterations)
        duration_1 = time.time() - start_time_1

        start_time_2 = time.time()
        future_2 = executor.submit(formula_2, iterations)
        duration_2 = time.time() - start_time_2

        result_1 = future_1.result()
        result_2 = future_2.result()
        start_time_3 = time.time()

        final_result = result_1 + result_2
        duration_3 = time.time() - start_time_3
    return duration_1, duration_2, duration_3, final_result

iterations_list = [10000, 100000]
for iterations in iterations_list:
    print(f"\nВыполнение для {iterations} итераций:")
    duration_1, duration_2, duration_3, final_result = compute(iterations)

    print(f"Длительность выполнения формулы 1: {duration_1:.6f} секунд")
    print(f"Длительность выполнения формулы 2: {duration_2:.6f} секунд")
    print(f"Длительность выполнения формулы 3: {duration_3:.6f} секунд")
    print(f"Итоговый результат: {final_result}")
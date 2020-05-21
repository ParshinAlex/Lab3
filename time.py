import task_numpy
import task_pandas
import timeit
import numpy as np
import matplotlib.pyplot as plt

main_path = "collected_data/household_power_consumption.txt"

victim_arr = task_numpy.get_array(main_path)
victim_df = task_pandas.get_df(main_path)
times_numpy = []
times_pandas = []
x = []

func = 4  # Input number of function here

for i in range(1, 7):
    i = 10 ** i
    x.append(i)
    rnd_row_index = np.random.choice(np.arange(0, len(victim_arr)), i, replace=True)
    arr_numpy = victim_arr[rnd_row_index]
    arr_pandas = victim_df.sample(i, replace=True)
    times_numpy.append(timeit.timeit(stmt='task_numpy.task_{}(arr_numpy)'.format(func), globals=globals(), number=1))
    times_pandas.append(timeit.timeit(stmt='task_pandas.task_{}(arr_pandas)'.format(func), globals=globals(), number=1))

print("Times (numpy): ", times_numpy)
print("Times (pandas): ", times_pandas)

fig, ax = plt.subplots()
ax.plot(x, times_numpy, label='Numpy')
ax.plot(x, times_pandas, label='Pandas')
ax.set_xscale('log')
ax.set_title("Затраты времени: NumPy и Pandas")
ax.set_xlabel("Количество элементов")
ax.set_ylabel("Время, с")
ax.grid(True)
ax.legend()
plt.show()

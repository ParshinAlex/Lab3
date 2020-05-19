import numpy as np
from datetime import datetime
import timeit

main_path = "collected_data/household_power_consumption.txt"


def get_array(path):
    types = {
        'names': ('Date', 'Time', 'Active', 'Reactive', 'Voltage', 'Intensity', 'Meter1', 'Meter2', 'Meter3'),
        'formats': ('U8', 'U8', 'float', 'float', 'float', 'float', 'int', 'int', 'int')
    }
    data = np.genfromtxt(path, delimiter=";", skip_header=True, dtype=types, missing_values=['?'])
    nan_mask = np.zeros((len(data)), dtype=bool)
    for column in data.dtype.names[2:]:
        nan_mask = nan_mask | np.isnan(data[column])
    data = data[~nan_mask]
    return data


def task_1(arr):
    return arr[arr['Active'] > 5.0]


def task_2(arr):
    return arr[arr['Voltage'] > 235.0]


def task_3(arr):
    return arr[(arr['Intensity'] >= 19.0) & (arr['Intensity'] <= 20.0) & (arr['Meter2'] > arr['Meter3'])]


def print_met(arr, meter):
    mean_met = np.mean(arr[meter])
    print('{}: {}'.format(meter, mean_met))


def task_4(arr):
    rnd_row_index = np.random.choice(np.arange(0, len(arr)), 500000, replace=True)
    print_met(arr[rnd_row_index], 'Meter1')
    print_met(arr[rnd_row_index], 'Meter2')
    print_met(arr[rnd_row_index], 'Meter3')
    return arr[rnd_row_index]


def task_5(arr):
    arr_night = arr[arr['Time'] >= '18:00:00']
    met2_max_condition = (arr_night['Meter2'] > arr_night['Meter1']) & (arr_night['Meter2'] > arr_night['Meter3'])
    arr_night_met2_max = arr_night[met2_max_condition]
    parts = np.array_split(arr_night_met2_max, 2)
    first_half = parts[0]
    second_half = parts[1]
    #  print("First half: \n", first_half[::3])
    #  print("Second half: \n", second_half[::4])


def get_mask(arr):
    mask = np.zeros(len(arr), dtype=bool)
    for i in range(0, len(arr)):
        # Write here your mask to get data from large array
        mask[i] = (datetime.strptime(arr['Date'][i].decode('UTF-8'), '%d/%m/%Y') >= datetime.strptime('1/1/2007',
                                                                                                      '%d/%m/%Y'))
    return mask


def start():
    print("Execution time: ", timeit.timeit(stmt='task_5(victim)', globals=globals(), number=1))

# start()
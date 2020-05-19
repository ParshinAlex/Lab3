import pandas as pd
import datetime
import timeit

main_path = "collected_data/household_power_consumption.txt"
pd.set_option('display.max_columns', 8)


def get_df(path):
    types = {'Date': 'object', 'Time': 'object', 'Active': 'float', 'Reactive': 'float', 'Voltage': 'float',
             'Intensity': 'float', 'Meter1': 'float', 'Meter2': 'float', 'Meter3': 'float'}
    data = pd.read_csv(path, delimiter=';', na_values='?', dtype=types)
    data.columns = ['Date', 'Time', 'Active', 'Reactive', 'Voltage', 'Intensity', 'Meter1', 'Meter2', 'Meter3']
    data = data.dropna()
    data['DateTime'] = pd.to_datetime(data['Date'] + data['Time'], format="%d/%m/%Y%H:%M:%S")
    data.drop(columns=['Date', 'Time'], inplace=True)
    data.set_index('DateTime', inplace=True)
    return data


def task_1(df):
    merged_df = df[df['Active'] > 5]
    return merged_df


def task_2(df):
    merged_df = df[df['Voltage'] > 235]
    return merged_df


def task_3(df):
    condition = (df['Intensity'] >= 19) & (df['Intensity'] <= 20) & (df['Meter2'] > df['Meter3'])
    return df[condition]


def print_mean(df, met):
    result = df[met].mean()
    print("Mean of {}: {}".format(met, result))


def task_4(df):
    merged_df = df.sample(500000, replace=True)
    print_mean(merged_df, 'Meter1')
    print_mean(merged_df, 'Meter2')
    print_mean(merged_df, 'Meter3')
    return merged_df


def task_5(df):
    night_condition = ((df.index.time >= datetime.time(18, 0, 0)) & (df['Active'] > 6) &
                       (df['Meter2'] > df['Meter3']) & (df['Meter2'] > df['Meter1']))
    merged_df = df[night_condition]
    half = len(merged_df) // 2 + 1
    first_half = merged_df[:half:3]
    second_half = merged_df[half::3]
    #  print(first_half)
    #  print(second_half)


def start():
    victim = get_df(main_path)
    begin = timeit.default_timer()
    task_5(victim)
    stop = timeit.default_timer()
    execution_time = stop - begin
    print("Time: ", execution_time)


#start()

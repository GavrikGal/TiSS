import datetime

import pandas as pd

test_filename_set = [
    r'Е 1903103 FHD DVI (0) 3m ВП.txt',
    r'Е 1903103 FHD DVI (45) 4m ВП.txt',
    r'Е 1903103 FHD DVI (90) 3m ВП.txt',
    r'Е 1903103 FHD DVI (135) 5m ВП.txt',
    r'Е 1903103 FHD DVI (180) 6m ВП.txt',
    r'Е 1903103 FHD DVI (225) 5m ВП.txt',
    r'Е 1903103 FHD DVI (270) 3m ВП.txt',
    r'Е 1903103 FHD DVI (315) 3m ВП.txt',
    r'Е 2301002 1280х1024 VGA 30.txt',
    r'Е 2200101 VGA R2=6 Ft=54.txt',
    r'Е 2301303 1280х1024 VGA 8м.txt',
    r'Е 2304406 1280х1024 VGA 30м.txt',
]

test_index_number_answer_set = [
    '1903103',
    '1903103',
    '1903103',
    '1903103',
    '1903103',
    '1903103',
    '1903103',
    '1903103',
    '2301002',
    '2200101',
    '2301303',
    '2304406',
]

test_index_angle_answer_set = [
    0,
    45,
    90,
    135,
    180,
    225,
    270,
    315,
    None,
    None,
    None,
    None,
]

test_data_r2_answer_set = [
    3,
    4,
    3,
    5,
    6,
    5,
    3,
    3,
    30,
    6,
    8,
    30,
]


test_file_name = r'Е 2200101 VGA R2=6 Ft=54.txt'
test_dir = r'tests\data\ВМЦ-45ЖК\2022'

test_index_frequencies_answer = [
    54.0,
    162.0,
    270.0,
    378.0,
    486.0,
    594.0,
]

test_index_date_answer = datetime.datetime.strptime("25.02.2022 09:36", "%d.%m.%Y %H:%M")

test_data_signals_answer = [
    32.77,
    28.15,
    33.20,
    22.44,
    25.01,
    27.59
]

test_data_noise_answer = [
    12.00,
    11.00,
    10.00,
    9.00,
    8.00,
    20.00
]

test_data_dirs = [r'tests\data\ВМЦ-45ЖК\2022',
                  r'tests\data\ВМЦ-45ЖК\2023-1',
                  r'tests\data\ВМЦ-45ЖК\2023-2',
                  ]

test_df_name_answer_set = [
    '2022',
    '2023-1',
    '2023-2',
]

test_data_read_answer_sets = [
    pd.DataFrame([6.0, 4.0, 8.0, 4.0, 4.0, 4.0, 4.0, 4.0, 3.0, 4.0, 3.0, 3.0, 5.0, 4.0]),
    pd.DataFrame([8.0, 9.0, 15.0, 20.0, 15.0, 9.0, 10.0, 9.0, 15.0, 15.0, 15.0, 10.0,
                  7.0, 7.0, 9.0, 8.0, 15.0]),
    pd.DataFrame([25.0, 30.0, 6.0, 15.0, 6.0, 6.0, 10.0, 6.0, 20.0, 9.0, 15.0, 7.0, 9.0,
                  10.0, 15.0, 9.0, 10.0, 30.0, 9.0, 40.0, 7.0, 15.0, 15.0, 30.0, 20.0,
                  6.0, 25.0, 20.0, 25.0, 15.0, 15.0])]

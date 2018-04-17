import pandas as pd
import numpy as np

timestamp_seconds_int = pd.Series(np.random.randint(1521685107 - 604800, 1521685107, 1000000, dtype='int64'))
timestamp_seconds_float = timestamp_seconds_int.astype('float64')

print((pd.to_datetime(timestamp_seconds_int, unit='s') == pd.to_datetime(timestamp_seconds_float, unit='s')).all())


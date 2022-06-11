#%%
from pathlib import Path

import pandas as pd

pd.read_csv(Path().joinpath('donnees', 'pokemon.csv'))
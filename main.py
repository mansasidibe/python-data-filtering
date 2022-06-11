#%%
from pathlib import Path

import pandas as pd

## lecture de fichier csv
pokemon = pd.read_csv(Path().joinpath('donnees', 'pokemon.csv'))

print(pokemon)


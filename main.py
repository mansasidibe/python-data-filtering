#%%
from pathlib import Path
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

## lecture de fichier csv
pokemon = pd.read_csv(Path().joinpath('donnees', 'pokemon.csv'))

## choix un nombre d'élément dans la liste
pokemon_show = pokemon.sample(5)

## somme des colonne null
somme = pokemon.isnull().sum()




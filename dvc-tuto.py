import pandas as pd
import dvc.api

# Get url from DVC
import pandas as pd
import dvc.api

path='data/wine_original.csv'
repo='https://github.com/CarlosTussi/dvc-tuto'
rev= 'v1'

data_url = dvc.api.get_url(
  path=path,
  repo=repo,
  rev=rev
  )

data = pd.read_csv(data_url, sep=";")
print(data)
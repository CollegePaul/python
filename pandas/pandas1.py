import pandas as pd

column = ["Mario", "Luigi", "Bowser", "Daisy"]

data_params= {"Name": column,
             "Height": [1.5, 1.5, 1.9, 1.6],
             "Weight": [34,32, 100, 26]}

data = pd.DataFrame(data_params)

selectWeight = data["Weight"]
select_row = data.iloc[1]

print(select_row)

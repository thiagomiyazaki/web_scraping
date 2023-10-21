import pandas as pd

states = ["São Paulo", "Minas Gerais", "Rio de Janeiro", "Bahia"]
population = [44420459, 20538718, 16054524, 14136417]

dict_states = {
    'Estados': states,
    "População": population
}

df_states = pd.DataFrame.from_dict(dict_states)

# print(df_states)

df_states.to_csv('estados.csvv', index=False)
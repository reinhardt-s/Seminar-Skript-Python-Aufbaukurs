# https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html
import pandas as pd

data_frame = pd.read_excel('./Material-Liste.xlsx', sheet_name="Materialliste-Weihnachtsbaum", header=None)

material_dict = dict(zip(data_frame[0], data_frame[1]))

cost = 0
for key in material_dict.keys():
    cost += material_dict[key]
cost = "{:.2f}".format(cost)
print(f"Der Weihnachtsbaum kostet {cost} EUR")

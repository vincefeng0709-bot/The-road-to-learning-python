import pandas as pd

# 第二课学习的是pandas的DataFrame（二维表格型的数据）
# 主要讲解的是如何创建一个dataframe，如何index需要的数据，如何添加一行或者一列数据

# eg1
data = {
    "Name": ["小米粒", "小小薇", "王大妈"],
    "Age": [8, 12, 53]
}

# 常用df作为dataframe的简称使用
df = pd.DataFrame(data)
print(df)

# 当然默认的会给一个index，也可以自行的定义index

df_index = pd.DataFrame(data, index=["A", "B", "C"])
print(df_index)

# 同样的与series（一维数据）那样可以通过.loc/.iloc索引需要的数据
index_1 = df_index.loc["B"]
index_2 = df_index.iloc[1]

print(index_1)
print(index_2)

# 添加一列新的数据
df["Phone_number"] = ["1911", "2033", "2766",]
df_index["Phone_number"] = ["1911", "2033", "2766",]
print(df)

# 添加一行新的数据时，必须用字典的形式，需要添加几行数据，对应的就需要多少个字典
# 定义好需要添加的新数据（new_row）之后就需要配合使用.concat()方法，将数据添加到原先的表格当中了
new_row = pd.DataFrame([{"Name": "周扒皮", "Age": "35", "Phone_number": "1522"}, {
                       "Name": "猫小猫", "Age": "20", "Phone_number": "9110"}])
# ignore_index用来将合并的两个df的索引也合并
df = pd.concat([df, new_row], ignore_index=True)

print(df)

# 或者也可直接给所加数据行定义一个index
new_row_index = pd.DataFrame([{"Name": "周扒皮", "Age": "35", "Phone_number": "1522"}, {
    "Name": "猫小猫", "Age": "20", "Phone_number": "9110"}], index=["D", "E"])
# ignore_index用来将合并的两个df的索引也合并
df_index = pd.concat([df_index, new_row_index])

print(df_index)

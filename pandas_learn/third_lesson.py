import pandas as pd

# 第三课主要学习的是如何用pandas对csv文件进行的操作，对csv内的数据进行筛选

df = pd.read_csv("clear_data.csv")

# 默认会打印出前五行和后五行的数据
print(df)

# 要想打印出整个文件的数据用到df.to_string()
# print(df.to_string())


# 同样的如果数据是josn文件形式方法类似，其他文件类似即可
# df = pd.read_json("文件名")


# 对dataframe的一系列操作

# eg1
# 根据列名打印出相对应的数据,多行以此类推
df_column = df["Age"]
df_column_max = df[["Age", "G", "CP"]]
print(df_column)  # 默认的也是打印出首尾各五行数据，需要全部打印出来的话用.to_string()方法
# print(df_column.to_string())
print(df_column_max)


# 同样的可以用.loc[]和.iloc[]去访问index锁定的数据,也可进行切片操作,在所需要切片的范围之后添加对应的列明也可以得到所需要展现的数据
df_loc = df.loc[0:11, ["Age", "BW"]]
df_iloc = df.iloc[0:11, [0, 5]]
print(df_loc)
print(df_iloc)


'''
对原有的数据定义一个index，
比如对df = pd.read_csv("clear_data.csv")这个数据定义一个以Age为新的index，只需要在读取csv时添加说明
index_col="Age"即可：
如：df_Age = pd.read_csv("clear_data.csv",index_col="Age")
'''

# 小练习，以一个查询系统为例子，可自行根据需要定义查询的index，另外用try和except方法，结合input方法实现
df_oscar = pd.read_csv("oscar_best_movies.csv")
'''
df_oscar = pd.read_csv("oscar_best_movies.csv", index_col="Country")
oscar_movie = input("请选择你需要查询的奥斯卡最佳影片的国家")

try:
    print(df_oscar.loc[oscar_movie])
except KeyError:
    print(f"{oscar_movie}not found this contury")
'''


movie_country = df_oscar["Country"].unique()
movie_language = df_oscar["Language"].unique()

print(f"电影的国家类别：{list(movie_country)}")
print(f"电影的语言：{list(movie_language)}")


# eg2
# 对数据进行数学描述，求均值，求和，求最值等
df_mean = df.mean(numeric_only=True)  # numeric_only方法只对数据类型的数据进行操作
df_sum = df.sum(numeric_only=True)
df_max = df.max(numeric_only=True)
df_min = df.min(numeric_only=True)
df_count = df.count()

print(f"均值：\n{df_mean}\n求和：\n{df_sum}\n最大值：\n{df_max}\n最小值：\n{df_min}\n计数：\n{df_count}")


# eg3
# 数据清洗
# 1.drop的使用，可以将对应的列进行删除
df_drop_Age = df.drop(columns=["Age", "CP"])
print(df_drop_Age)

# 删除对用列里面的空行用dropna（subset=["列名"]）
df_drop_Age = df.dropna(subset=["Height"])
print(df_drop_Age)

# 删除整个数据表格中的空数据，就不需指定某列了直接dropna（）即可
df_drop_Age = df.dropna()
print(df_drop_Age)

# 当然对于缺失的数据我们可以通过fillna填写对应的缺失部分,要以字典的形式填充，先确定要补充的列名在定义需要填充的内容是什么
df = df.fillna({"Height": "None"})

print(df.to_string())

# 替换指定列中的某些数值用replace（）
df["CP"] = df["CP"].replace({1.0: "one",
                             2.0: "two",
                             3.0: "three"})
print(df.to_string())

# 修改某类数据的数据类型
df["GDM"] = df["GDM"].astype(bool)
print(df.to_string())

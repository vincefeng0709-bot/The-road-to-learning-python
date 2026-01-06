import pandas as pd

# 第一课先从pandas的Series（将数据想象成电子表格中的一列）开始，
# 1.介绍了series的index修改功能（在末尾的index中自行定义所需要的索引）
# 2.通过series.loc可指定index并修改对应的数据项
# 3..iloc可直接索引数据表格中的逻辑index，从而直接返回所需的数据
# 4.原始数据如果有自带的index（像字典这一类的数据），可直接用所带的index，不用另外再设定index


# eg1

# 以简单的列表为例子
data = [100, 102, 104, 213, 4532, 6774, 98234]

series = pd.Series(data)

print(series)
# 改变data中的数据形式，对应的也会发生改变

# 默认的创建的data中的数据索引是从0开始的这种数值索引形式

# 再后面的index当中可直接修改data的索引方式
series = pd.Series(data, index=["a", "b", "c", "d", "e", "f", "g"])

print(series)

# 如果想根据索引打印出所需要的数据时可进行对series的进一步说明
print(series.loc["b"])

# 能通过.loc指定索引访问，当然也能通过其锁定对应的数据进行修改
series.loc["a"] = 1550

print(series)

# 当然获取索引的数据的方式还有.iloc(默认的是从0开始的索引)
print(series.iloc[0])


# 打印出列表数据中大于或者小于某个范围的所有数据
print(series[series > 300])


# eg2

# 下面以字典为例子，以每天上班所需的交通方式为例子
Transportation = {"day1": "train", "day2": "subway", "day3": "bus", }

series_transport = pd.Series(Transportation)

print(series_transport)  # 直接使用字典所带的index了

x = series_transport.loc["day1"]
y = series_transport.iloc[0]

print(f"x = {x}")
print(f"y = {y}")

# 尝试修改字典中的index
Transportation = {"day1": "train", "day2": "subway", "day3": "bus", }

series_transport = pd.Series(Transportation)
series_transport.index = ["A", "B", "C"]
print(series_transport)

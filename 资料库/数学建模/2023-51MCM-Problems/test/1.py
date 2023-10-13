import pandas
data=pandas.read_excel(r"C:\Users\Administrator\Desktop\2023-51MCM-Problems\2023-51MCM-Problem B\附件1(Attachment 1)2023-51MCM-Problem B.xlsx")
# print(data['发货城市 (Delivering city)'])
import numpy as np
print(data["收货城市 (Receiving city)"])

# 计算两个城市之间的相关系数
def calc_corr(city1, city2):
    # 提取出货量数据
    data_city1 = data[(data["发货城市 (Delivering city)"] == city1) & (data["收货城市 (Receiving city)"] == city2)]["快递运输数量(件) (Express delivery quantity (PCS))"].values
    data_city2 = data[(data["发货城市 (Delivering city)"] == city2) & (data["收货城市 (Receiving city)"] == city1)]["快递运输数量(件) (Express delivery quantity (PCS))"].values

    # 计算相关系数
    corr = np.corrcoef(data_city1, data_city2)[0, 1]

    return corr


# 计算两个城市之间的相关系数
city1 = "A"
city2 = "O"
corr = calc_corr(city1, city2)
print(f"{city1}和{city2}之间的相关系数为{corr}")
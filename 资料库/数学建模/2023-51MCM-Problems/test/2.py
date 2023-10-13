import pandas as pd
import numpy as np
from scipy.stats import pearsonr

# 读取数据
# data1 = pd.read_excel('附件1.xlsx',index_col=0)
# data2 = pd.read_excel('附件2.xlsx', index_col=0)
# data3 = pd.read_excel('附件3.xlsx', index_col=0)
data=pd.read_excel(r"C:\Users\Administrator\Desktop\2023-51MCM-Problems\2023-51MCM-Problem B\附件1(Attachment 1)2023-51MCM-Problem B.xlsx")
# print(data['发货城市 (Delivering city)'])
import numpy as np

# 获取城市列表
city_set=list(data["发货城市 (Delivering city)"])
receive_city=list(data["收货城市 (Receiving city)"])
city_set.extend(receive_city)
city_set=set(city_set)

# 城市名转换成数字
city_dict = {city: i for i, city in enumerate(city_set)}
print(city_dict)

# # 构建收货量矩阵和发货量矩阵
receive_matrix = np.zeros((len(city_set), len(city_set)))
send_matrix = np.zeros((len(city_set), len(city_set)))

for index, row in data.iterrows():
    # send_city = city_dict[index]
    send_city=row[1]
    receive_city=row[2]
    value=row[3]
    send_matrix[city_dict[send_city]][city_dict[receive_city]]+=value
    receive_matrix[city_dict[receive_city]][city_dict[send_city]]+=value

    # for col, value in row.iteritems():
    #     receive_city = city_dict[col]
    #     send_matrix[send_city][receive_city] += value
    #     receive_matrix[receive_city][send_city] += value

# 计算各城市发货量和收货量排名

send_rank = sorted([(list(city_dict.keys())[list(city_dict.values()).index(i)], sum(send_matrix[i])) for i in range(len(city_set))], key=lambda x: x[1], reverse=True)
receive_rank = sorted([(list(city_dict.keys())[list(city_dict.values()).index(i)], sum(receive_matrix[i])) for i in range(len(city_set))], key=lambda x: x[1], reverse=True)

print(send_rank)
print(receive_rank)
# 计算各城市快递数量增长/减少趋势排名
# city_set=list(data["发货城市 (Delivering city)"])
# receive_city=list(data["收货城市 (Receiving city)"])
growth_rate_dict = {}
rate_dict={}
# df_grouped=data.groupby(['发货城市 (Delivering city)','收货城市 (Receiving city)']).sum().reset_index()
# #df_grouped["增长率"]= (df_grouped['快递运输数量(件) (Express delivery quantity (PCS))'] - df_grouped['快递运输数量(件) (Express delivery quantity (PCS))'].shift(1)) / df_grouped['快递运输数量(件) (Express delivery quantity (PCS))'].shift(1)
# print(df_grouped["发货城市 (Delivering city)"])
# for index, row in data.iterrows():
#     send_city=row[1]
#     receive_city=row[2]
#     value=row[3]
#     if send_city not in rate_dict:
#         rate_dict[send_city]=[value]
#     else:
#         rate_dict[send_city].append(value)
    # if receive_city not in rate_dict:
    #     rate_dict[receive_city]=[value]
    # else:
    #     rate_dict[receive_city].append(value)
# print(rate_dict)
# for city in city_dict:
#     city=city_dict[city]
#     print(city)
#     row = receive_matrix[city]
#     print(row)
#     growth_rate = (row[-1] - row[0]) / row[0]
#     growth_rate_dict[list(city_dict.keys())[list(city_dict.values()).index(city)]] = growth_rate
#
# growth_rank = sorted(growth_rate_dict.items(), key=lambda x: x[1], reverse=True)

# 计算各城市之间的相关系数
corr_dict = {}
for i in range(len(city_set)):
    for j in range(i+1, len(city_set)):
        corr, _ = pearsonr(receive_matrix[i], receive_matrix[j])
        corr_dict[(list(city_dict.keys())[list(city_dict.values()).index(i)], list(city_dict.keys())[list(city_dict.values()).index(j)])] = corr
print(corr_dict)
# 综合分析
score_dict = {}
for city in city_dict:
    # print(city)
    send_ranking = [i + 1 for i in range(len(send_rank)) if send_rank[i][0] == city][0]
    receive_ranking = [i + 1 for i in range(len(receive_rank)) if receive_rank[i][0] == city][0]
    # growth_ranking = [i + 1 for i in range(len(growth_rank)) if growth_rank[i][0] == city][0]
    corr_score=0
    for c in corr_dict:
        if city in c and corr_dict[c]>=-1 and corr_dict[c]<=1:
            corr_score+=corr_dict[c]

    print(corr_score)

    score_dict[city] = {"send_ranking": send_ranking,
                        "receive_ranking": receive_ranking,
                        # "growth_ranking": growth_ranking,
                        # "corr_score": sum([corr_dict[(city, c)] for c in corr_dict if city in c])
                        "corr_score": corr_score
                        }
# + x[1]["growth_ranking"]
#
score_rank = sorted(score_dict.items(), key=lambda x: x[1]["send_ranking"] + x[1]["receive_ranking"]-x[1]["corr_score"])
print(score_rank)
for key in score_rank[:5]:
    print(key[0])

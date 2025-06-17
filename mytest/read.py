import numpy as np

# 以内存映射模式读取大型.npy文件
data = np.load('../data/haiyou/LIC2003PV.npy', mmap_mode='r')
datas = np.load('../data/haiyou/LIC2003MV.npy', mmap_mode='r')
# 此时数据并未完全加载到内存中，只有在访问时才会加载相应部分
print(len(data))  # 只加载前10个元素
print(len(datas))  # 只加载前10个元素


# import numpy as np
# import json

# # 读取.npy文件
# data = np.load('../data/haiyou/LIC2003PV.npy')

# # 将NumPy数组转为Python列表
# data_list = data.tolist()

# # 转为JSON字符串
# json_data = json.dumps(data_list)

# # 保存为JSON文件
# with open('output.json', 'w') as f:
#     json.dump(data_list, f)
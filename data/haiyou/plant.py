import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # 切换到 TkAgg 后端
import matplotlib.pyplot as plt
# 读取 .npy 文件
data = np.load('PIC2022PV.npy')

# 提取第一列数据
column_1 = data[:, 0]

# 绘制第一列数据
plt.figure(figsize=(12, 6))
plt.plot(column_1, label='Column 1 Data')
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Plot of Column 1')
plt.legend()
plt.grid(True)
plt.show()
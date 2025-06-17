#读取一个csv文件
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import csv
#读取一个csv文件
def read_csv(file_name):
    csv_reader = pd.read_csv(file_name, header=None)
    return csv_reader
data = read_csv('../data/oscillator2/test_id.csv.csv')

#读取第一列元素
data1 = data[0]
#使用plt画出所有点

import numpy as np


# 数组
def l_array():
    a = np.array([1, 2, 3, 4, 5])  # 直接输入数字生成数组
    print(a)
    print(a.ndim)  # 维度
    print(a.shape)  # 形状
    a = np.arange(1, 100, 3, dtype=float)  # 生成均等分布数组 dtype -> 数据类型
    print(a)
    a = np.linspace(0, 1, 7)  # 生成均等采样数组
    print(a)
    a = np.ones(2)  # 生成全1数组
    print(a)
    a = np.zeros(2)  # 生成全0数组
    print(a)
    a = np.random.rand(3)  # 生成3个成员的随机数组
    print(a)
    a = np.random.randn(3)  # 生成3个成员的高斯数组
    print(a)


# 多项式操作
def l_poly():
    p = np.poly1d([3, 2, -1])  # 解一元二次方程
    print(p(0))


# 导入数据
def l_data():
    data = np.loadtxt('../data/populations.txt')
    print(data)
    # np.savetxt('data/test.txt', data)


l_data()

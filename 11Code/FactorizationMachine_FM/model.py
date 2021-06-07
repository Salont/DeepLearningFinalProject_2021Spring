import sys
sys.path.append("..")

import torch
import pandas as pd
import numpy as np

class FactorizationMachine(torch.nn.Module):
    def __init__(self, n, k):
        super(FactorizationMachine, self).__init__()
        # n是特征维度，k是每个特征的embedding维度
        self.n, self.k = n, k
        self.lr = torch.nn.Linear(self.n, 1, bias = True)
        self.v = torch.nn.Parameter(torch.randn(self.n, self.k)) # 随机初始化一个 n * k 阶矩阵
        self.sm = torch.nn.Sigmoid()
        torch.nn.init.uniform_(self.v, -0.1, 0.1)
        
    def fm_layer(self, x):
        linear_part = self.lr(x)
        interaction_part_1 = torch.mm(x, self.v)
        interaction_part_1 = torch.pow(interaction_part_1, 2)
        interaction_part_2 = torch.mm(torch.pow(x, 2), torch.pow(self.v, 2))
        # 和的平方 减 平方的和 : https://zhuanlan.zhihu.com/p/37963267
        output = linear_part + 0.5 * torch.sum(interaction_part_2 - interaction_part_1)
        return output

    def forward(self, x):
        output = self.fm_layer(x)
        y = self.sm(output)
        return y

if __name__ == "__main__":
    model = FactorizationMachine()
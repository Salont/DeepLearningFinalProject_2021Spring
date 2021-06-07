import torch
import pandas as pd
import numpy as np

class LogisticRegression(nn.Module):
    def __init__(self):
        super(LogisticRegression, self).__init__()
        self.lr = torch.nn.Linear(5, 1)  # 输入3维，输出1维
        self.sm = torch.nn.Sigmoid()     # LR的激活函数为Sigmoid
        
    def forward(self, x):
        temp = self.lr(x)
        y = self.sm(temp)
        return y

if __name__ == "__main__":
    model = LogisticRegression()
import models
import torch.nn as nn
import torch
import sys
from sklearn import metrics
from torch.autograd import Variable
import random

# 适用于LR,FM
class Train():
    def __init__(self):
        self.max_epoch = 500
        #self.model = models.LogisticRegression()
        self.model = models.FactorizationMachine(5, 3)
        self.criterion = nn.BCELoss()
        self.optimizer = torch.optim.Adam(self.model.parameters())
        return

    def train(self, model, x_train, y_train, x_test, y_test):
        for epoch in range(self.max_epoch):
            train_output = self.model(x_train) # 计算输出
            train_loss = self.criterion(train_output.squeeze(), y_train.squeeze()) # 计算损失
            test_output = self.model(x_test) # 计算输出
            test_loss = self.criterion(test_output.squeeze(), y_test.squeeze()) # 计算损失
            
            self.optimizer.zero_grad()
            train_loss.backward()
            self.optimizer.step() # 更新参数
            
            # 每100轮打印损失
            if (epoch + 1) % 10 == 0:
                trainLoss = float(train_loss.detach().numpy())
                testLoss = float(test_loss.detach().numpy())
                # 计算auc
                y_label = y_train.detach().squeeze().numpy()
                y_pred = train_output.detach().squeeze().numpy()
                auc = metrics.roc_auc_score(y_label, y_pred)
                print("epoch:%4s/%s, train loss:%.3f, test loss:%.3f, auc:%.3f" % (epoch + 1, self.max_epoch, trainLoss, testLoss, auc))
        return

if __name__ == "__main__":
    sys.stdout  = open("../Res/train.log", mode = 'w', encoding='utf-8')
    random.seed(666)
    x_train = torch.randn(300, 5)
    y_train = [[random.randint(0, 1) for _ in range(1)] for _ in range(300)]
    x_train = torch.FloatTensor(x_train)
    y_train = torch.FloatTensor(y_train)
    x_test = torch.randn(300, 5)
    y_test = [[random.randint(0, 1) for _ in range(1)] for _ in range(300)]
    x_test = torch.FloatTensor(x_test)
    y_test = torch.FloatTensor(y_test)
    runner = Train()
    runner.train(runner.model, x_train, y_train, x_test, y_test)
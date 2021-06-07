import sys
sys.path.append("..")

import torch
import pandas as pd
import torch.nn as nn
import numpy as np
import lightgbm
import random
from settings import lgb_params, LGBM_modelPath
import metric
import tensorflow

class LGBM():
    def __init__(self):
        self.load_model()
        return
    
    # search hyper parameters
    def hyper_search(self):
        
        
        return
    
    # get the interactive features
    def leaf_encoder(self):
        
        return
    
    # fit data and print epoch:loss
    def fit(self, x_train, y_train, x_test, y_test):
        lgb_train = lightgbm.Dataset(x_train, y_train)
        lgb_eval = lightgbm.Dataset(x_test, y_test, reference = lgb_train)
        gbm = lightgbm.train(lgb_params,
                            lgb_train,
                            num_boost_round = 100,
                            valid_sets = lgb_eval)
        y_pred = gbm.predict(x_train, pred_leaf = True)
        print(y_pred)
        num_leaf = lgb_params["num_leaves"]
        transformed_training_matrix = np.zeros([len(y_pred), len(y_pred[0]) * num_leaf],
									   dtype=np.int64)  # N * num_tress * num_leafs
        for i in range(0, len(y_pred)):
            temp = np.arange(len(y_pred[0])) * num_leaf + np.array(y_pred[i])
            transformed_training_matrix[i][temp] += 1
        print(transformed_training_matrix.shape)
        print(transformed_training_matrix)
        # 这里接一个metric打印loss，明天来开发（今5.24）
        return
    
    # load model
    def load_model(self):
        self.model = lightgbm.LGBMClassifier(lgb_params)
        # self.model = lightgbm.Booster(model_file = LGBM_modelPath)

    # save model: must save after fit
    def save_model(self):
        self.model.booster_.savemodel(LGBM_modelPath)

if __name__ == "__main__":
    sys.stdout  = open("../../Res/train.log", mode = 'w', encoding='utf-8')
    random.seed(666)
    x_train = np.random.rand(300, 5)
    # y_train = [[random.randint(0, 1) for _ in range(1)] for _ in range(300)]
    y_train = [random.randint(0, 1) for _ in range(300)]
    x_test = np.random.rand(300, 5)
    # y_test = [[random.randint(0, 1) for _ in range(1)] for _ in range(300)]
    y_test = [random.randint(0, 1) for _ in range(300)]
    lgb = LGBM()
    lgb.fit(x_train, y_train, x_test, y_test)
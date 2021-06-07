#import prettyTable
from sklearn import metrics
import math

def cal_single_loss(arg):
    y_label, y_pred = arg[0], arg[1]
    loss = - (y_label * math.log10(y_pred) + (1 - y_label) * math.log10(1 - y_pred))
    return loss
    
def metric(y_label, y_pred):
    '''
    input: 2 list
    output: Accuracy, Auc, Loss
    '''
    n = len(y_label)
    right_prediction, wrong_prediction = 0, 0
    for pred, label in zip(y_pred, y_label):
        if abs(pred - label) < 0.5:
            right_prediction += 1
        else:
            wrong_prediction += 1
    
    Accuracy = right_prediction / n
    Auc = metrics.roc_auc_score(y_label, y_pred)
    
    temp = [y_label, y_pred]
    temp = list(zip(*temp))
    temp = list(map(cal_single_loss, temp))
    Loss = sum(temp) / n
    print("Accuracy: %.3f, Auc: %.3f, Loss: %.3f" % (Accuracy, Auc, Loss))
    
if __name__ == "__main__":
    y_label = [1, 1, 0]
    y_pred = [0.9, 0.88, 0.21]
    metric(y_label, y_pred)
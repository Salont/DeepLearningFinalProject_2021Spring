import pandas as pd
import numpy as np 
import json
import sys
from settings import stdoutPath, DataPath
pd.set_option("display.max_rows", 1000)
pd.set_option("display.max_columns", 1000)

class DataCenter():
    def __init__(self):
        self.data = pd.read_csv(DataPath)
        
    def preprocess(self):
        
        return
    
    def delete_useless_columns(self):
        
        return
    
if __name__ == "__main__":
    sys.stdout  = open(stdoutPath, mode = 'w', encoding='utf-8')
    data = pd.read_csv(DataPath)
    print(data.head())
import sys
sys.path.append("../")

import torch
import pandas as pd
import numpy as np

class FeaturesLinear(torch.nn.Module):
    
    def __init__(self, field_dims, output_dim = 1):
        super(FeaturesLinear).__init__()
        self.fc = torch.nn.Embedding(sum(field_dims), output_dim)
        self.bias = torch.nn.Parameter(torch.zeros((output_dim,)))
        torch.nn.init.uniform_(self.bias, 0, 0)
        self.offsets = np.array((0, *np.cumsum(field_dims)[:-1]), dtype=np.long) 

    def forward(self, x):  
        """
        :param x: Long tensor of size ``(batch_size, num_fields)``
        """
        print("FeaturesLinear x=", x)
        x = x + x.new_tensor(self.offsets, dtype = np.long).unsqueeze(0)  
        print("FeaturesLinear return = ", torch.sum(self.fc(x), dim = 1) + self.bias)
        return torch.sum(self.fc(x), dim = 1) + self.bias

class FieldAwareFactorizationMachine(torch.nn.Module):
    
    def __init__(self, field_dims, embed_dim):
        super(FieldAwareFactorizationMachine).__init__()
        self.num_fields = len(field_dims)   
        self.embeddings = torch.nn.ModuleList([
            torch.nn.Embedding(sum(field_dims), embed_dim) for _ in range(self.num_fields)
        ]) 
        self.offsets = np.array((0, *np.cumsum(field_dims)[:-1]), dtype=np.long)
        for embedding in self.embeddings:
            torch.nn.init.xavier_uniform_(embedding.weight.data)

    def forward(self, x):
        """
        :param x: Long tensor of size ``(batch_size, num_fields)``
        """
        x = x + x.new_tensor(self.offsets, dtype = np.long).unsqueeze(0)
        xs = [self.embeddings[i](x) for i in range(self.num_fields)]  
        ix = list()
        for i in range(self.num_fields - 1):
            for j in range(i + 1, self.num_fields):
                ix.append(xs[j][:, i] * xs[i][:, j])
        ix = torch.stack(ix, dim=1)

class FieldAwareFactorizationMachineModel(torch.nn.Module):
    
    def __init__(self, field_dims, embed_dim):
        super(FieldAwareFactorizationMachineModel).__init__()
        self.linear = FeaturesLinear(field_dims)
        self.ffm = FieldAwareFactorizationMachine(field_dims, embed_dim)

    def forward(self, x):
        """
        :param x: Long tensor of size ``(batch_size, num_fields)``
        """
        ffm_term = torch.sum(torch.sum(self.ffm(x), dim=1), dim=1, keepdim=True)
        x = self.linear(x) + ffm_term
        return torch.sigmoid(x.squeeze(1))

if __name__ == "__main__":
    sys.stdout  = open("../../Res/train.log", mode = 'w', encoding='utf-8')
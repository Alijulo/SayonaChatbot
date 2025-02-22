import torch
import torch.nn as nn
import torch.nn.init as init

class NeuralNet(nn.Module):
    def __init__(self,input_size,hidden_size,num_classes):
        super(NeuralNet,self).__init__()
        # passing the dataset to pipeline layers
        self.l1=nn.Linear(input_size,hidden_size)
        # batch normalization increases training speed
        self.bn1=nn.BatchNorm1d(hidden_size)
        self.l2=nn.Linear(hidden_size,hidden_size)
        self.bn2=nn.BatchNorm1d(hidden_size)
        self.l3=nn.Linear(hidden_size,num_classes)
        self.relu=nn.ReLU()

        # regularization-To prevent overfitting, incorporate regularization techniques such as dropout:
        self.dropout=nn.Dropout(0.5)
        # initializing weights using Xavier initialization,helps in better convergence during training
        init.xavier_uniform_(self.l1.weight)
        init.xavier_uniform_(self.l2.weight)
        init.xavier_uniform_(self.l3.weight)


    def forward(self,x):
        out=self.l1(x)
        out=self.bn1(out)
        out=self.relu(out)

        out=self.l2(out)
        out=self.bn2(out)
        out=self.relu(out)

        out=self.dropout(out)
        out=self.l3(out)
        return out

import json
from nltk_utils import tokenize,lemmantize,bag_of_words #,stem
import numpy as np

import torch
import torch.nn as nn
from torch.utils.data import Dataset,DataLoader
from torch.optim.lr_scheduler import ReduceLROnPlateau

from neural_network_model import NeuralNet

with open('intents.json','r' ) as f:
    intents=json.load(f)

all_words=[]
tags=[] 
xy=[]
# for intent in intents['intents']:
#     tag=intent['tag']
#     tags.append(tag
#     for pattern in intents['patterns']:
#         w=tokenize(pattern)
#         all_words.extend(w)
#         xy.append((w,tag))
for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        w = tokenize(pattern)
        all_words.extend(w)
        xy.append((w, tag))

ignore_words=['?','!','.',","]

all_words=[lemmantize(w) for w in all_words if w not in ignore_words]

all_words=sorted(set(all_words))
tags=sorted(set(tags))
print(all_words)
print(tags)

X_train=[]
y_train=[]
for(pattern_senetnce,tag) in xy:
    bag=bag_of_words(pattern_senetnce,all_words)
    X_train.append(bag)

    label=tags.index(tag)
    y_train.append(label)


X_train=np.array(X_train)
y_train=np.array(y_train)

class Chatdataset(Dataset):
    def __init__(self):
        self.n_samples=len(X_train)
        self.x_data=X_train
        self.y_data=y_train

    def __getitem__(self, index):
        return self.x_data[index],self.y_data[index]
    

    def __len__(self):
        return self.n_samples
    
batch_size=8
input_size=len(X_train[0])
hidden_size=8
output_size=len(tags)
learning_rate=0.001
num_epochs=1000


dataset=Chatdataset()
train_loader=DataLoader(dataset=dataset,batch_size=batch_size, shuffle=True, num_workers=0)
# print(input_size,len(all_words))
# print(output_size,tags)

device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model=NeuralNet(input_size,hidden_size,output_size).to(device)

critarion=nn.CrossEntropyLoss()
optimizer=torch.optim.Adam(model.parameters(),lr=learning_rate)
scheduler=ReduceLROnPlateau(optimizer,mode='min',factor=0.1,patience=5)

best_loss=float('inf')
for epoch in range(num_epochs):
    for(words, labels) in train_loader:
        words=words.to(device)
        labels=labels.to(torch.long)

        output=model(words)
        loss=critarion(output,labels)

        #backword and optimizer
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
     # Validation step (assuming validation_loader is defined)
    model.eval()  # Set model to evaluation mode
    val_loss=0.0
    with torch.no_grad():
        for val_words,val_lebals in train_loader:
            val_words=val_words.to(device)
            val_lebals=val_lebals.to(torch.long).to(device)

            val_output=model(val_words)
            val_loss+=critarion(val_output,val_lebals).item()

        val_loss/=len(train_loader)
        # Step scheduler based on validation loss
        scheduler.step(val_loss)


    if(epoch+1)%100==0:
        print(f"epoch {epoch+1}/{num_epochs}, loss={loss.item():.4f}")

print(f"final loss={loss.item():.4f}")

    # Save the model if validation loss has decreased
if val_loss<best_loss:
    best_loss=val_loss
    data={
        "model_state":model.state_dict(),
        "input_size":input_size,
        "output_size":output_size,
        "hidden_size":hidden_size,
        "all_words":all_words,
        "tags":tags
    }

    FILE ="data.pth"
    torch.save(data,FILE)

print(f"Training complete. Best validation loss: {best_loss:.4f}. Model saved as 'best_model.pth'.")
print(f"training complite.. and file saved to {FILE}")

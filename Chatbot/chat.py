import random
import torch
import json
from nltk_utils import tokenize,bag_of_words
from neural_network_model import NeuralNet


device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json','r') as f:
    intents=json.load(f)

FILE='data.pth'
data=torch.load(FILE)
input_size=data["input_size"]
output_size=data["output_size"]
hidden_size=data["hidden_size"]
all_words=data["all_words"]
tags=data["tags"]
model_state=data["model_state"]
model=NeuralNet(input_size,hidden_size,output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name="AI"
print("lets chat! type quit to exit")
while True:
    sentence=input('You: ')
    if sentence=='quit':
        break
    sentence = tokenize(sentence)
    X=bag_of_words(sentence,all_words)
    X=X.reshape(1,X.shape[0])
    X=torch.from_numpy(X).to(device)
    
    output=model(X)
    _, pridected=torch.max(output,dim=1)
    tag=tags[pridected.item()]
    probability=torch.softmax(output,dim=1)
    prob_tag=probability[0][pridected.item()]
    
    if prob_tag.item() > 0.75:
        for intent in intents["intents"]:
            if tag==intent["tag"]:
                print(f"{bot_name}: {random.choice(intent['responses'])}")
    else:
        print( f"{bot_name}: I dont understand you!!!")

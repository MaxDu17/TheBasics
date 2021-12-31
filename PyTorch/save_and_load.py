import torch
import torchvision.models as models

model = models.vgg16(pretrained=True) #loads a model for instructional purposes
torch.save(model.state_dict(), 'model_weights.pth') #saves everything from the state dictionary

#now, we can reload using a very simple approach
model = models.vgg16() # we do not specify pretrained=True, i.e. do not load default weights
model.load_state_dict(torch.load('model_weights.pth'))
model.eval()


# to save the model and the weights:
torch.save(model, 'model.pth')
model = torch.load("model.pth")
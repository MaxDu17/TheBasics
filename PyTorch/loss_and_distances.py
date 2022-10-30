import torch
from torch import nn
BATCH = 10
P = 3
R = 4
EMBED = 7

embeddings_1 = torch.rand((BATCH, P, EMBED))
embeddings_2 = torch.rand((BATCH, R, EMBED))

# PAIRWISE NORM
pairwise_l2 = torch.cdist(embeddings_1, embeddings_2, p = 2.0)
print(pairwise_l2.shape) #should be B X P X R

# DOT PRODUCT
dot_product_sim =  torch.bmm(embeddings_1, torch.transpose(embeddings_2, 1, 2))
print(dot_product_sim.shape)

# COSINE
dot_product_sim =  torch.bmm(embeddings_1, torch.transpose(embeddings_2, 1, 2))
magnitude_1 = torch.linalg.norm(embeddings_1, dim = 2, keepdim = True)
magnitude_2 = torch.linalg.norm(embeddings_2, dim = 2, keepdim = True)
magnitude_matrix = torch.bmm(magnitude_1, torch.transpose(magnitude_2, 1, 2))
cosine_distance = dot_product_sim / magnitude_matrix
print(cosine_distance.shape)



# loss functions

nn.CrossEntropyLoss() #takes in an B X D unnormalized logits, and a (B) set of labels or a B X D distribution over labels
nn.BCEWithLogitsLoss() #takes in a B X D unnormalized logits, and B X D set of labels
nn.BCELoss() # takes in a B x D normalized distribution and a B X D set of labels
print(nn.functional.one_hot(torch.tensor([2, 3, 1]))) #helpful one-hot label maker


import torch
BATCH = 10
P = 3
R = 4
EMBED = 7

embeddings_1 = torch.rand((BATCH, P, EMBED))
embeddings_2 = torch.rand((BATCH, R, EMBED))

#pairwise norm
pairwise_l2 = torch.cdist(embeddings_1, embeddings_2, p = 2.0)
print(pairwise_l2.shape) #should be B X P X R

#NOT DONE
#show cosine, dot product, etc
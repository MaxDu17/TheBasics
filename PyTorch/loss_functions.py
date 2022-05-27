from torch import nn

nn.CrossEntropyLoss() #takes in two N X D matrices and computes cross entropy
nn.MSELoss() # takes in two matrices of the same shape
nn.L1Loss()
nn.SmoothL1Loss() # for derivative problems
nn.BCELoss() # takes in two N X 1 matrices and computes element-wise binary cross entorpy
nn.BCEWithLogitsLoss() # same as above but you use logits
nn.CosineSimilarity()
nn.NLLLoss() # negative log likelihood
nn.KLDivLoss() # KL divergence


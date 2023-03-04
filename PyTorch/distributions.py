import torch.distributions as pyd
import torch

probs = torch.tensor([1,2,1,3])
m = pyd.Categorical(probs)
sampled = m.sample()
log_prob = m.log_prob(sampled) #also works for a batch
print(sampled)
print(log_prob)


m = pyd.MultivariateNormal(torch.tensor([1.0, 2.0, 1.0]), torch.eye(3)) #also takes in a batch B x D, B X D X D
rsampled = m.rsample() #this is differentiable because of the reparameterizatoin trick

print(rsampled)

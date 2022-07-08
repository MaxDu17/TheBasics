from torch.utils.data import DataLoader
import torch
from torch.utils.data import IterableDataset
from torch.utils.data import Dataset
from torch.utils.data import random_split
import numpy as np

#an iterable-style dataset
class CustomIterable(IterableDataset):  # object,
    def __init__(self):
        super(CustomIterable).__init__()

    def __len__(self):
        return 100

    def sampling_function(self):
        return np.random.randint(100)

    def __iter__(self):
        while True:
            yield self.sampling_function()

# a map style dataset (both work)
#the advantagbe is that you can easily split into training and testing sets, and you can also iterate better
class CustomMapDataset(Dataset):
    def __init__(self):
        super(CustomMapDataset).__init__()
        self.elems = np.arange(100)

    def __len__(self):
        return 100

    def __getitem__(self, idx): #disadvangate: you need to restart when you reach the end
        return self.elems[idx]



iterable_dataset = CustomIterable()
map_dataset = CustomMapDataset()

#if batch-size is None, then batching is disabled and we return a member of the dataset object directly
# if collate_fn is none, a default concatenating function is used. If batching is disabled, this function is called on one sample
# if num_workers is 0, then there is no threading involved. Otherwise, there are multiple workers taht help fetcht the data
#if we pin memory, things can be faster when we later turn them into cuda tensors
#sampler is how we sample. If none, we do a simple random. It's an iterable
#batch-sampler will return a batch of incies. Can't exist with batch_size, shuffle, sampler, or drop_last (it essentially takes over everything)
#drop_last will remove the last batch if it doesn't have the right number of elements
#worker_init_fn is an initialization routine for hte workers

iterable_sampler = DataLoader(iterable_dataset, batch_size=1, shuffle=False, sampler=None,
           batch_sampler=None, num_workers=0, collate_fn=None,
           pin_memory=False, drop_last=False, timeout=0,
           worker_init_fn=None, prefetch_factor=2,
           persistent_workers=False)

map_sampler = DataLoader(map_dataset, batch_size=10, shuffle=False, sampler=None,
           batch_sampler=None, num_workers=0, collate_fn=None,
           pin_memory=False, drop_last=False, timeout=0,
           worker_init_fn=None, prefetch_factor=2,
           persistent_workers=False)

#do NOT return cuda tensors in multiprocessing loading. It's slow and unstable
# torch.utils.get_worker_info() # useful to get worker stats

#### iterating through a dataloader object #####

# infinite loop
# for batch in iterable_sampler:
#     print("here")
#     print(batch)

# using the iter() constructor
sampler_iter = iter(map_sampler)
for i in range(10):
    batch = sampler_iter.next()
    # print(batch)

#### splitting training and testing ####
train, valid = random_split(map_dataset, [30, 70]) #30 + 70 = 100, which was the size specified in the dataset object
train_map_sampler = DataLoader(train, batch_size=1, shuffle=False, sampler=None,
           batch_sampler=None, num_workers=0, collate_fn=None,
           pin_memory=False, drop_last=False, timeout=0,
           worker_init_fn=None, prefetch_factor=2,
           persistent_workers=False)


#### Other data calls to take note of
# combine stuff and split stuff
# d = torch.utils.data.ConcatDataset([a, b, c]) #combine datasets together
# d = torch.utils.data.ChainDataset([a, b, c]) #chaining datasets together for IterableDatasets
# d = torch.utils.data.Subset(a, [1, 2, 3, 4, 8]) #selects a subset of the dataset

# samplers
# d = torch.utils.data.SequentialSampler(a) #samples from a map-style dataset sequentially
# d = torch.utils.data.RandomSampler(a, replacement = False, num_samples =None) #samples from a dataset randomly
# d = torch.utils.data.BatchSampler(d, batch_size = 10, drop_last = True) #takes in a sampler and makes it into a batch


# EXAMPLE OF A WEIGHTED SAMPLER
# weights takes in any non-negative value. Zeros are never selected. num_samples is the number of samples you draw. It must be larger than the number of batches you plan to have, or else you raise a StopIteration error

weights = np.zeros(100)
weights[[1, 2, 3, 45, 78]] = 1 # there are 100 values in the dataset, but here we demonstrate an extreme weighing algorithm, which selects only 1, 2, 3, 45, 78
d = torch.utils.data.WeightedRandomSampler(weights, num_samples = 100, replacement = True) #and the "d" goes into the "sampler" field of the DataLoader
map_sampler = DataLoader(map_dataset, batch_size=10, shuffle=False, sampler=d)

s = iter(map_sampler)
for i in range(10):
    print(s.next())


from torch.utils.data import DataLoader
import torch
from torch.utils.data import IterableDataset
from torch.utils.data import Dataset
from torch.utils.data import random_split

#an iterable-style dataset
class CustomIterable(IterableDataset):  # object,
    def __init__(self):
        pass

    def __len__(self):
        pass

    def sampling_function(self):
        return 1

    def __iter__(self):
        while True:
            yield self.sampling_function()

# a map style dataset (both work)
#the advantagbe is that you can easily split into training and testing sets, and you can also iterate better
class CustomDataset(Dataset):
    def __init__(self):
        pass

    def __len__(self):
        return 100

    def __getitem__(self, idx):
        return 1



dataset = CustomIterable()
dataset2 = CustomDataset()

#if batch-size is None, then batching is disabled and we return a member of the dataset object directly
# if collate_fn is none, a default concatenating function is used. If batching is disabled, this function is called on one sample
# if num_workers is 0, then there is no threading involved. Otherwise, there are multiple workers taht help fetcht the data
#if we pin memory, things can be faster when we later turn them into cuda tensors
#sampler is how we sample. If none, we do a simple random. It's an iterable
#batch-sampler will return a batch of incies. Can't exist with batch_size, shuffle, sampler, or drop_last (it essentially takes over everything)
#drop_last will remove the last batch if it doesn't have the right number of elements
#worker_init_fn is an initialization routine for hte workers

sampler = DataLoader(dataset, batch_size=1, shuffle=False, sampler=None,
           batch_sampler=None, num_workers=0, collate_fn=None,
           pin_memory=False, drop_last=False, timeout=0,
           worker_init_fn=None, prefetch_factor=2,
           persistent_workers=False)

sampler2 = DataLoader(dataset2, batch_size=1, shuffle=False, sampler=None,
           batch_sampler=None, num_workers=0, collate_fn=None,
           pin_memory=False, drop_last=False, timeout=0,
           worker_init_fn=None, prefetch_factor=2,
           persistent_workers=False)

#do NOT return cuda tensors in multiprocessing loading. It's slow and unstable
# torch.utils.get_worker_info() # useful to get worker stats

#### iterating through a dataloader object #####

# infinite loop
# for batch in sampler:
#     print("here")
#     print(batch)

# using the iter() constructor
sampler_iter = iter(sampler2)
for i in range(10):
    batch = sampler_iter.next()
    print(batch)

#### splitting training and testing ####
a, b = random_split(dataset2, [30, 70]) #30 + 70 = 100, which was the size specified in the dataset object
sampler3 = DataLoader(a, batch_size=1, shuffle=False, sampler=None,
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
# d = torch.utils.data.WeightedRandomSampler(weights, num_samples = 3, replacement = True)
# d = torch.utils.data.BatchSampler(d, batch_size = 10, drop_last = True) #takes in a sampler and makes it into a batch 
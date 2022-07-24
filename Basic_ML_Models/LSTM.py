import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
# num_layers – Number of recurrent layers. E.g., setting num_layers=2 would mean stacking two LSTMs together to form a stacked LSTM, with the second LSTM taking in outputs of the first LSTM and computing the final results. Default: 1
# bias – If False, then the layer does not use bias weights b_ih and b_hh. Default: True
# batch_first – If True, then the input and output tensors are provided as (batch, seq, feature) instead of (seq, batch, feature). Note that this does not apply to hidden or cell states. See the Inputs/Outputs sections below for details. Default: False
# dropout – If non-zero, introduces a Dropout layer on the outputs of each LSTM layer except the last layer, with dropout probability equal to dropout. Default: 0
# bidirectional – If True, becomes a bidirectional LSTM. Default: False
# proj_size – If > 0, will use LSTM with projections of corresponding size. Default: 0

lstm = nn.LSTM(input_size = 3, hidden_size = 3, num_layers = 1, batch_first = True, bidirectional = False)  # Input dim is 3, output dim is 3

# direct sequential exectuion
# this is not a special case--we are just using a little "hack" of the network
inputs = [torch.randn(1, 3) for _ in range(5)]  # make a sequence of length 5, batch 1
hidden = (torch.zeros(1, 1, 3),
          torch.zeros(1, 1, 3)) #h_0, c_0
for i in inputs:
    x = i.view(1, 1, -1) # [batch, length, dim]
    out, hidden = lstm(x, hidden)
    # hidden is (h_k, c_k), which is ready to be passed into the next one
#out is [batch, 1, out_dim] (because you are executing sequentially!)

######################

inputs = torch.randn(5, 10, 3) # batch 5, length 10, dim 3
out, hidden = lstm(inputs) # this is how you run it without any hidden initialization
# see below for how to interpret the out and the hidden variables

# here's how to initialize an LSTM using some hidden representation
# we must provide an initialization to every input we are feeding in, hence the 5 here
hidden = (torch.zeros(1, 5, 3), torch.zeros(1, 5, 3))  # initialize to whatever you want
out, hidden = lstm(inputs, hidden)

# the "out" contains all the hidden states (useful for seq-to-seq, for example)
print(out.shape) #[batch, length, out_dim]
# the "hidden" contains (h_n, c_n) tuple, which is useful for forward / back propagation
print(hidden[0].shape) # [1, batch, out_dim]

# these two are equal. In general, if you want a temporal representation, this is all you need
print(out[:, -1, :])
print(hidden[0])

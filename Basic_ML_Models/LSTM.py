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

batch_size = 5
sequence_length = 10
input_dim = 3
output_dim = 7

# the main model
lstm = nn.LSTM(input_size = input_dim, hidden_size = output_dim, num_layers = 1, batch_first = True, bidirectional = False)

############# DIRECT SEQUENTIAL EXECUTION ##########
inputs = [torch.randn(batch_size, input_dim) for _ in range(sequence_length)]  # make a sequence of length 10, batch 5
hidden = (torch.zeros(1, batch_size, output_dim),
          torch.zeros(1, batch_size, output_dim)) #h_0, c_0

for i in inputs:
    x = i.view(batch_size, 1, -1) # [batch, length, dim]
    out, hidden = lstm(x, hidden)
    # hidden is (h_k, c_k), which is ready to be passed into the next one
#out is [batch, 1, out_dim] (because you are executing sequentially!)

######### BATCHED WHOLE-SEQUENCE EXECUTION #########
inputs = torch.randn(batch_size, sequence_length, input_dim) # batch 5, length 10, dim 3
out, hidden = lstm(inputs) # this is how you run it without any hidden initialization
# see below for how to interpret the out and the hidden variables

# here's how to initialize an LSTM using some hidden representation
hidden = (torch.zeros(1, batch_size, output_dim), torch.zeros(1, batch_size, output_dim))  # initialize to whatever you want
out, hidden = lstm(inputs, hidden)

# the "out" contains all the hidden states (useful for seq-to-seq, for example)
print(out.shape) #[batch, length, out_dim]
# the "hidden" contains (h_n, c_n) tuple, which is useful for forward / back propagation
print(hidden[0].shape) # [1, batch, out_dim]

# these two are equal. In general, if you want a temporal representation, this is all you need
print(out[:, -1, :])
print(hidden[0])

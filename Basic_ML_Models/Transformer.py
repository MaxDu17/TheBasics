import math
import torch
from torch import nn, Tensor
import torch.nn.functional as F
from torch.nn import TransformerEncoder, TransformerEncoderLayer

# this is adapted to a general transformer setup. We don't consider the specific use of natural language
class TransformerEncoderModel(nn.Module):
    def __init__(self, d_model: int, nhead: int, d_hid: int,
                 nlayers: int, d_embed: int, dropout: float = 0.5):
        # d_model: input dimensions
        # nhead: number of attention heads
        # d_hid: hidden representation size (i.e. what the transformer works with)
        # nlayers: how many transformer layers do we use (remember that each transformer layer consists of many components)

        super().__init__()
        self.pos_encoder = PositionalEncoding(d_model, dropout)
        encoder_layers = TransformerEncoderLayer(d_model, nhead, d_hid, dropout)
        self.transformer_encoder = TransformerEncoder(encoder_layers, nlayers)
        self.decoder = nn.Linear(d_model, d_embed) #this step is not necessary; remove if you want

    def forward(self, src: Tensor, src_mask: Tensor) -> Tensor:
        """
        Args:
            src: Tensor, shape [seq_len, batch_size]
            src_mask: Tensor, shape [seq_len, seq_len]

        Returns:
            output Tensor of shape [seq_len, batch_size, d_embed]
        """
        src = self.pos_encoder(src)
        output = self.transformer_encoder(src, src_mask)
        output = self.decoder(output)
        return output

# makes a mask needed for decoding
def generate_square_subsequent_mask(sz: int) -> Tensor:
    """Generates an upper-triangular matrix of -inf, with zeros on diag."""
    return torch.triu(torch.ones(sz, sz) * float('-inf'), diagonal=1)

class PositionalEncoding(nn.Module):
    def __init__(self, d_model: int, dropout: float = 0.1, max_len: int = 5000):
        super().__init__()
        self.dropout = nn.Dropout(p=dropout)
        position = torch.arange(max_len).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2) * (-math.log(10000.0) / d_model))
        pe = torch.zeros(max_len, 1, d_model)
        pe[:, 0, 0::2] = torch.sin(position * div_term)
        pe[:, 0, 1::2] = torch.cos(position * div_term)
        # saves a fixed sine-cosine positional encoding vector
        self.register_buffer('pe', pe)

    def forward(self, x: Tensor) -> Tensor:
        """
        Args:
            x: Tensor, shape [seq_len, batch_size, embedding_dim]
        """
        x = x + self.pe[:x.size(0)] # adding the positional encoding
        return self.dropout(x)

# arbitrary numbers; replace them as fit
sequence_length = 15
batch_size = 5
input_dims = 20
embedding_size = 40
model = TransformerEncoderModel(d_model = input_dims, nhead = 2, d_hid = 200, nlayers = 2, d_embed = embedding_size)
posenc = PositionalEncoding(d_model = input_dims)

input = torch.randn((sequence_length, batch_size, input_dims)) #this is the shape for the input

mask = generate_square_subsequent_mask(sequence_length) #this mask prevents using a future term to generate the current representation.

# when you create an embedding, this mask may not be necessary. Here, we replace it with a dummy one
mask = torch.ones((sequence_length, sequence_length))
x = model(input, mask) # [sequence_length, batch_size, embedding_size]
print(x.shape)

# general note: to run the transformer live, just keep on adding to the input (you need to run feed-forward the whole sequence
# every time, unlike the LSTM which carries over a hidden state between runs.)


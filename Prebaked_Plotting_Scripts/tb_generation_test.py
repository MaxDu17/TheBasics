from torch.utils.tensorboard import SummaryWriter
import numpy as np

log_dir = "test.tb"
RND_STATE = 1234
N_EVENTS = 10
N_PARTICLES = 1000
MU = 0
SIGMA = 2
writer = SummaryWriter(log_dir)
rng = np.random.RandomState(RND_STATE)
for i in range(N_EVENTS):
  x = rng.normal(MU, SIGMA, size=N_PARTICLES)
  writer.add_histogram('dist', x + i, i)
writer.close()
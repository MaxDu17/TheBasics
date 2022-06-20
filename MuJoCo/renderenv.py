import mujoco_py
import os
import time
import numpy as np
mj_path, _ = mujoco_py.utils.discover_mujoco()
xml_path = os.path.join(mj_path, 'model', 'humanoid.xml')
model = mujoco_py.load_model_from_path(xml_path)
sim = mujoco_py.MjSim(model)
times = []
for _ in range(100):
  t0 = time.time()
  sim.render(64, 64)
  times.append(time.time() - t0)
  print(time.time() - t0)
print(np.mean(times), times[-1])

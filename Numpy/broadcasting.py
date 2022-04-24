import numpy as np

#rule 1: broadcasting dimensions are compared from right to left.
#rule 2: two dimension values are compatible if they are equal, or one of them is 1
#rule 3: missing dimensions (to the left) are automatically marked as 1. For example, (244, 244) can be marked as (1, 244, 244)

#upshot: scalars are always broadcastable
#upshot: you must add a trailing extra dimension if you are trying to combine something like 233 x 233 x 3 with 233 x 233

scalar = 3
v1 = np.zeros((200, 200, 3))
v2 = np.zeros((200, 1, 1))
v3 = np.zeros((200, 200))
v5 = np.zeros((1, 200, 1))
v6 = np.zeros((200, 1, 200))

v1 * scalar #easily legal
v1 * v2 #this is legal
x = v2 * v3 #also legal. We broadcast the last two dims of v2 and then add a leading dim to v3
v5 * v6 #mutual broadcasting (interesting!)

try:
    v1 * v3 #illegal because the rightmost dimensions don't match
except:
    v4 = np.expand_dims(v3, axis = 2)
    v1 * v4

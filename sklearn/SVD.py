from sklearn.decomposition import TruncatedSVD

import numpy as np
X = np.random.random((10, 10))
svd = TruncatedSVD(n_components=3) # more paramters but shouldn't need to adjust
svd.fit(X)
print(sum(svd.explained_variance_ratio_)) #essentially how much variance is expained
print(svd.singular_values_) #essentially how much variance is expained

reduced = svd.fit_transform(X) #essentially if you want to just reduce dimensionality, all you need is this line
print(reduced.shape)

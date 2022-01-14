import numpy as np

x = [1, 2, 3]
np.array(x, dtype='uint8')      # Create arrays
# arr.astype(np.float64)

np.arange(0, 10)                # excludes maximum value
np.arange(0, 10, 2)             # start, stop, step
np.linspace(0, 10)              # includes min/max
np.linspace(0, 10, 2)           # start, stop, #values

np.zeros(5)
np.zeros((5, 5))
np.ones(5)
np.ones((5, 5))
np.eye(5)
np.triu(np.ones(5), k=0)        # upper triangle, k specifies triangle
np.tril(np.ones(5), k=0)        # lower triangle, k specifies triangle
np.ones_like((5, 5))            # matrix like a given matrix

# Random numbers
# [0, 1[
np.random.rand(5)
np.random.rand(5, 5)

# normal dist-
np.random.randn(5)
np.random.randn(5, 5)

# [i, j[
np.random.randint(0, 1)
np.random.randint(0, 1, 10)     # returns array


# Methods on arrays
arr = np.arange(25).reshape(5, 5)
arr.max()
arr.argmax()                    # returns index of max value
arr.min()
arr.argmin()                    # returns index of min value
arr.std()
arr.shape

np.sqrt(arr)
np.exp(arr)
np.max(arr)
np.sin(arr)
np.sin(arr)
np.mean(arr)
np.std(arr)
np.corrcoef(arr)
np.mean(arr)
np.median(arr)


# Indexing
arr[0:5]                        # [i, j[
arr[0:5] = 0                    # broadcast to 0
arr[0:5] > 0                    # boolean logic
arr[0:5] + 0                    # arithmetic [+, -, *, /, **]
arr.copy()                      # deep copy
arr[0, 1] == arr[0][1]          # same
arr[[1, 2]]                     # index with a list
np.where(arr == 1)  # find index


# Merge / Join/ Split
arr.ravel()                     # flatten to 1D array
np.concatenate([arr, arr], axis=0)
a, b, c = np.split(arr, [1, 3])
np.repeat([1, 2], 3)           # repeat each elemet 3 times
np.tile([1, 2], 3)             # repeat array 3 times


# Sort
arr.sort(axis=0)

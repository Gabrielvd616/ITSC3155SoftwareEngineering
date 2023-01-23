import numpy as np

rnums = np.random.rand(10)
print('Random numbers:')
print(rnums)
print('Mean: ' + str(np.mean(rnums)) + ', Median: ' + str(np.median(rnums)) + ', Standard Deviation: ' + str(np.std(rnums)))

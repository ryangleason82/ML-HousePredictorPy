import numpy as np
a = np.array([1, 2, 3, 4, 5, 6])
print(a.shape)
print(a.dtype.name)
print(np.subtract(a, 2))


def knn(features, labels, predictionPoint, k):
    mean, variance = np.moments(features, 0)
    scaledPrediction = predictionPoint.subtract(mean).divide(variance.pow(0.5))

    return features.subtract(mean)
    .divide(variance.power(0.5))
    .subtract(scaledPrediction)
    .power(2)
    .sum(1)
    .power(0.5)
    .expandDims(1)
    .concat(labels, 1)
    .unstack()
    .sort((a, b)= > (a.get(0) > b.get(0) if 1 else -1))
    .slice(0, k)
    .reduce((acc, pair)= > acc + pair.get(1), 0) / k

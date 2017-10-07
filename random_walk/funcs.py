def std_dev(X):
    mean = float(sum(X)) / len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean) ** 2
    return (tot / len(X)) ** 0.5  # Square root of mean difference


def cv(x):
    mean = sum(x) / float(len(x))
    try:
        return std_dev(x) / mean
    except ZeroDivisionError:
        return float('nan')

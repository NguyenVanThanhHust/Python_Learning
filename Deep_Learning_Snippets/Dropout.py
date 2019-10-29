def Dropout(x, dropout_percent):
    mask = np.random.binominal([np.ones_like(x)], (1-dropout-percent))[0] / (1-dropout_percent)
    return x*mask
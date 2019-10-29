def CreateWeights():
    #Initialization of the Weights and the biases with the random gaussian function with mean zero and variance between 1/sqtr(num_inputs_layer)
    ninputs = 784
    #Number of neurons in the first layer
    wl1 = 500
    #Second layers
    wl2 = 300
    nclass = 10
    
    #layer1 
    #mean = 0, variance = ninputs**-0.5
    w1 = np.random.normal(0, ninputs**-0.5, [ninputs, wl1])
    b1 = np.random.normal(0, ninputs**-0.5, [1, wl1])
    
    #layer2
    w2 = np.random.normal(0, wl1**-0.5, [wl1, wl2])
    b2 = np.random.normal(0, wl1**-0.5, [1, wl2])
    
    #layer3
    w3 = np.random.normal(0, wl2**-0.5, [wl2,nclass])
    b3 = np.random.normal(0, wl2**-0.5, [1,nclass])
    
    return [w1,w2,w3, b1,b2,b3]
#Relu function is = x if(x>0) else = 0

def ReLU(x, derivative = False):
    if(derivative == False):
        return x*(x>0) #mean x*1
    else :
        return 1*(x>0) #mean 1*1
    
x = np.arange(20) - 10
relu = ReLU(x)

plt.plot(x, relu)
plt.show()
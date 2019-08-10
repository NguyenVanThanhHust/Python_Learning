if os.path.isfile('../data_folder/MNIST_csv/train.csv'): #on kaggle
    data_df = pd.read_csv('../data_folder/MNIST_csv/train.csv')
    print('train.csv loaded: data_df({0[0]},{0[1]})'.format(data_df.shape))
elif os.path.isfile('data_folder/MNIST_csv/train.csv'):
    data_df = pd.read_csv('data_folder/MNIST_csv/train.csv') # on local environment
    print('train.csv loaded: data_df({0[0]},{0[1]})'.format(data_df.shape))
else:
    print('Error: train.csv not found')
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
import pprint
#print(help(np.load))
#data = np.load(r'test-images-idx3-ubyte.gz',allow_pickle=True)
data = input_data.read_data_sets("tmp/MNIST/", one_hot=True)
print("Size of:")
print("- Training-set:\t\t{}".format(len(data.train.labels)))
print("- Test-set:\t\t{}".format(len(data.test.labels)))
print("- Validation-set:\t{}".format(len(data.validation.labels)))

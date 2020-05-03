#Numpy and argparse HW

#imports:
import sys, os
import numpy as np
import pickle
import argparse
import my_module as mymod


#Creating 1D array:
a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])

#Create 2D array:
aa = np.array(np.arange(9)).reshape((3,3))
bb = np.array(np.arange(12)).reshape((4,3))

#indexing arrays:
print('\nIndexing for last row of of aa')
row3 = (aa[2,:])
print(row3)

#concatenating arrays:
print('\nConcatenating aa and bb')
cc = np.concatenate((aa,bb),axis=0) #can't concatentate with axis 1 because size of arrays is differnet
print(cc)

#adding arrays:
print('\nAdding aa and part of bb')
dd = aa + bb[1:,:]
print(dd)

#Boolean mask of array:
print('\n Make a Boolean mask of dd >= 13')
mask = dd >= 13
print(mask)
print('\n Elemnts in maks')
print(dd[mask])

#create float array
print('\nMake float array of aa')
aaf = aa.astype(float)
print(aaf)

#Finding mean, max in array
print('\nMaximum of aa')
max = np.max(aa)
print(max)

print('\nMean of aa')
mean = np.mean(aa)
print(mean)

#Saving array dd as a pickle file:
this_dir = os.path.abspath('.').split('/')[-1]
this_parent = os.path.abspath('.').split('/')[-2]

out_dir = '../' + this_parent + '_output/'
print('Creating ' + out_dir + ', if needed')
mymod.make_dir(out_dir)

out_fn = out_dir + 'numpy_argparse_HW_out.p'
pickle.dump(dd, open(out_fn, 'wb'))

#reading the array back in:
array = pickle.load(open(out_fn, 'rb'))
print('\nImported array')
print(array)

#argparse
def boolean_string(s):
    # this function helps with getting Boolean input
    if s not in ['False', 'True']:
        raise ValueError('Not a valid boolean string')
    return s == 'True' # note use of ==

parser = argparse.ArgumentParser()

parser.add_argument('-a', '--vector_aa', default=aa, type=int)
parser.add_argument('-b', '--vector_dd', default=dd, type=int)
parser.add_argument('-v', '--verbose', default=False, type=boolean_string)

args = parser.parse_args()

if args.verbose:
    print('\nMatrix multiplication of aa and dd is:')
    print(args.vector_aa @ args.vector_dd)

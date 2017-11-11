# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in

import os
import bson                       # this is installed with the pymongo package
import pickle
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

# Simple data processing
file_name = 'output.bson'

data = bson.decode_file_iter(open('./data/train_example.bson', 'rb'))
count = 0
output_file = open('output.bson', 'ab')

while count < 10:
    for c, d in enumerate(data):
        print(c,d)
        # data_encoded = bson.BSON.encode(d)
        # output_file.write(data_encoded)
    count += 1
output_file.close()

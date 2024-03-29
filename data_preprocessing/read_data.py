# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import io
import bson                       # this is installed with the pymongo package
import matplotlib.pyplot as plt
from skimage.data import imread   # or, whatever image library you prefer
import multiprocessing as mp      # will come in handy due to the size of the data
import pickle

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

from subprocess import check_output
# Simple data processing

data = bson.decode_file_iter(open('./data/train_example.bson', 'rb'))

prod_to_category = dict()

for c, d in enumerate(data):
    product_id = d['_id']
    category_id = d['category_id'] # This won't be in Test data
    prod_to_category[product_id] = category_id
    for e, pic in enumerate(d['imgs']):
        picture = imread(io.BytesIO(pic['picture']))
        # do something with the picture, etc

# prod_to_category = pd.DataFrame.from_dict(prod_to_category, orient='index')
# prod_to_category.index.name = '_id'
# prod_to_category.rename(columns={0: 'category_id'}, inplace=True)
# prod_to_category.head()
print(prod_to_category)
with open("training_example.txt","w") as training_file:
    for key in prod_to_category:
        training_file.write(str(key) + "\t" + str(prod_to_category[key]) + "\n")

print(prod_to_category)

plt.imshow(picture);

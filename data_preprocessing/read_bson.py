import os
import bson                       # this is installed with the pymongo package
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

# Simple data processing
import sys

for line in sys.stdin:

    data = bson.BSON.decode(line)
    print(data)

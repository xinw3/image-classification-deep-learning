import os
import bson

def mapper():
    file_name = 'output.bson'

    data = bson.decode_file_iter(open('./data/train_example.bson', 'rb'))
    category_dict = dict()
    for c, d in enumerate(data):
        category_id = d['category_id']
        category_dict[category_id] = category_dict.get(category_id,0) + 1

    print (category_dict)

    min_val = min(category_dict.values())
    max_val = max(category_dict.values())
    sum_count = sum(category_dict.values())

    print ("min count: " + str(min_val))
    print ("max count: " + str(max_val))
    print ("total count: " + str(sum_count))


if __name__ == "__main__":
    mapper()

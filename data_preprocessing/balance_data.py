import os
import bson

def find_min():

    input_filepath = './data/train_example.bson'
    data = bson.decode_file_iter(open(input_filepath, 'rb'))
    category_dict = dict()
    for c, d in enumerate(data):
        category_id = d['category_id']
        category_dict[category_id] = category_dict.get(category_id,0) + 1

    print (category_dict)

    min_val = min(category_dict.values())
    max_val = max(category_dict.values())
    sum_count = sum(category_dict.values())

    print ("total category: " + str(len(category_dict)))
    print ("min count: " + str(min_val))
    print ("max count: " + str(max_val))
    print ("total count: " + str(sum_count))

    return min_val

def split_data(threshold):
    output_filename = 'output.bson'
    data = bson.decode_file_iter(open('./data/train_example.bson', 'rb'))
    category_dict = dict()
    output_file = open(output_filename, 'wb')

    for c, d in enumerate(data):
        category_id = d['category_id']
        category_dict[category_id] = category_dict.get(category_id,0) + 1
        if category_dict[category_id] > threshold:
            continue
        data_encoded = bson.BSON.encode(d)
        output_file.write(data_encoded)


if __name__ == "__main__":
    # Default value for threshold
    threshold = 1000
    # comment if have known the min_val 12
    threshold = find_min()
    split_data(threshold)

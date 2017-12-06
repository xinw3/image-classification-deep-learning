import os
import bson
import argparse
import json


def find_min():

    input_filepath = './data/all_classes_train.bson'
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
    with open("category_dict.json","w+") as dict_file:
    	json.dump(category_dict, dict_file)

    return min_val, category_dict

def split_data(threshold):
    output_filename = 'output.bson'
    data = bson.decode_file_iter(open('../data/train_example.bson', 'rb'))
    example_count = dict()
    output_file = open(output_filename, 'wb')

    for c, d in enumerate(data):
        category_id = d['category_id']
        example_count[category_id] = example_count.get(category_id,0) + 1
        if example_count[category_id] > threshold:
            continue
        data_encoded = bson.BSON.encode(d)
        output_file.write(data_encoded)

    print ("write file to: " + output_filename)

if __name__ == "__main__":
    # Default value for threshold
    parser = argparse.ArgumentParser()
    parser.add_argument('--threshold', type=int, default=12, help='examples of each category')
    parser.add_argument('--display_category', type=bool, default=False, help='show the distribution of categories')
    args = parser.parse_args()

    if args.display_category == True:
        min_val, category_dict = find_min()

    # comment if have known the min_val 12
    # threshold = find_min()
    if hasattr(args, threshold):
    	split_data(args.threshold)

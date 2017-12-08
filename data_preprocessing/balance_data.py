import os
import bson
import argparse
import json

def find_min():
    print("finding min..")
    input_filepath = '../data/train.bson'
    data = bson.decode_file_iter(open(input_filepath, 'rb'))
    category_dict = dict()
    for c, d in enumerate(data):
        category_id = d['category_id']
        category_dict[category_id] = category_dict.get(category_id,0) + 1
    #print (category_dict)
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

def split_data(threshold, percentage):
    output_filename = 'output_1000_10%.bson'
    data = bson.decode_file_iter(open('../data/train.bson', 'rb'))
    example_count = dict()
    output_file = open(output_filename, 'wb')
    category_dict = json.load(open("category_dict.json",'r'))
    
    for c, d in enumerate(data):
        category_id = d['category_id']
        category_id = str(category_id)
        example_count[category_id] = example_count.get(category_id,0) + 1
        if category_dict[category_id] < threshold or example_count[category_id] > percentage * category_dict[category_id]:
            continue
        data_encoded = bson.BSON.encode(d)
        output_file.write(data_encoded)

    print ("write file to: " + output_filename)

if __name__ == "__main__":
    # Default value for threshold
    parser = argparse.ArgumentParser()
    parser.add_argument('--threshold', type=int, default=1, help='filtering threslod (lower bound) of each category')
    parser.add_argument('--percentage', type=float, default=1, help='percentage of each category')
    parser.add_argument('--display_category', type=bool, default=False, help='show the distribution of categories')
    args = parser.parse_args()

    if args.display_category == True:
        min_val, category_dict = find_min()
    else:
    # comment if have known the min_val 12
    # threshold = find_min()
        split_data(args.threshold, args.percentage)
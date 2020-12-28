# 2nd Oct, 2020 Sumantra Sharma
# inputs - %train, %val, %test, path to json file containing dict of filenames randomly selected from the dataset folders
# output - text files in ~/dataset/<VOC2012><VOC2007><I2R_Data_2><I2R_Data>/ImageSets/Main
import argparse
import sys
import random
import json
import os
parser = argparse.ArgumentParser(
    description="Program to set proportions of training, validation and testing data in the final imagesets ")
parser.add_argument("-d",
                    "--dataset_dir",
                    help="Path to dataset folder containing json file ",
                    default = '~/dataset',
                    type=str)
parser.add_argument("-tr",
                    "--train_p",
                    help="Percentage of total dataset to use for training",
                    default = 70,
                    type=int)
parser.add_argument("-v",
                    "--val_p",
                    help="Percentage of total dataset to use for validation",
                    default = 20,
                    type=int)
parser.add_argument("-ts",
                    "--test_p",
                    help="Percentage of total dataset to use for testing",
                    default = 10,
                    type=int)

args = parser.parse_args()
print(args)
all_files =[]
fnames_train = []
fnames_val = []
fnames_test = []
data_dict = { 
				"train" : [args.train_p,  fnames_train],
				"val" :	[args.val_p,  fnames_val],
				"test": [args.test_p, fnames_test]
			}

def main():	
# 	check percentages
	sum = 0
	for k,v in data_dict.items():
		sum +=v[0]
	if sum >100:
		print("Invalid percentages entered, exiting program")
		print(sum)
		sys.exit(0)	

	d = args.dataset_dir
#	open directory and read folder names
	folders =	[o for o in os.listdir(d) 
                	if os.path.isdir(os.path.join(d,o))]

#  open json file
	with open(args.dataset_dir+'/dataset.txt', 'r') as fp:
	    data = json.load(fp)

# 	make a tuple, combine all files in a single list and shuffle
	for key,value in data.items() :
		for fnames in value[1]:
			all_files.append((fnames,key))
	random.shuffle(all_files)

# 	check if ImageSets/Main folder exsists, if not create it
	for fol in folders:
		if not os.path.exists(os.path.join(args.dataset_dir, fol,'ImageSets/Main')):
    			print("Creating folder", os.path.join(args.dataset_dir, fol,'ImageSets/Main'))
    			os.makedirs(os.path.join(args.dataset_dir, fol,'ImageSets/Main'))


# 	pick specific no. of files from the list depending upon percentages and save text files
	for key,value in data_dict.items():
		print('Adding ', key, 'examples to the list')
		count = 0
		value[1] = all_files[count: count + int((value[0]/100)*len(all_files))]

	for key,value in data_dict.items():
		print("Adding", len(value[1]) , "filenames to" , key, "dataset")
		for tup in value[1]:
			filename = os.path.join(args.dataset_dir, tup[1], 'ImageSets/Main',key+'_generated.txt'); 
			with open(filename, "a") as f:
				print('Adding entry :', tup[0] , 'to file : ', filename)
				f.write(tup[0]+'\n')
	
	
			
if __name__ == '__main__':
	main()






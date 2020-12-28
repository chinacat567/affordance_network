# Sept 29th, Sumantra Sharma
# Glob through /Annotations, randomly select train%, val% and test% filenames and dump 
# the filenames in ImageSets/Main/train,txt, val.txt, test.txt
import os
import glob
import argparse
import sys
import random

# Initiate argument parser
parser = argparse.ArgumentParser(
    description="Program to randomly select training, validation and test datasets from a large dataset")
parser.add_argument("-x",
                    "--xml_dir",
                    help="Path to the folder where the input xml files are stored.",
                    type=str)
parser.add_argument("-train",
                    "--train_p",
                    help="Percentage of total dataset to select for training", type=int)
parser.add_argument("-val",
                    "--val_p",
                    help="Percentage of total dataset to select for validation", type=int)
parser.add_argument("-test",
                    "--test_p",
                    help="Percentage of total dataset to select for testing", type=int)
parser.add_argument("-o_train",
                    "--output_path_train",
                    help="Path of output text (.txt) file containing filenames of training images", type=str)
parser.add_argument("-o_val",
                    "--output_path_val",
                    help="Path of output text (.txt) file containing filenames of validation images", type=str)
parser.add_argument("-o_test",
                    "--output_path_test",
                    help="Path of output text (.txt) file containing filenames of test images", type=str)

args = parser.parse_args()
fnames = []
fnames_train = []
fnames_val = []
fnames_test = []
data_dict = { 
				"train" : [args.train_p, args.output_path_train, fnames_train],
				"val" :	[args.val_p, args.output_path_val, fnames_val],
				"test": [args.test_p, args.output_path_test, fnames_test]
			}

def save_to_txt_file(path, fnames):
	f = open(path, 'w');
	for a in fnames:
		print('Adding entry :', a , 'to file : ', path)
		f.write(a+'\n')

def main():
	
	#	check if all arguments have been entered
	for k in args.__dict__:
		if args.__dict__[k] is None:
			print('Argument', k , 'not entered, exiting program')
			sys.exit(0)
	sum = 0
	for k,v in data_dict.items():
		sum +=v[0]
	if sum >100:
		print("Invalid percentages entered, exiting program")
		print(sum)
		sys.exit(0)

	#	glob through jpeg directory and save filenames in dict
	print('Globbing through directory : ' , args.xml_dir)
	for name in glob.glob(args.xml_dir+'/*xml'):
		fnames.append(os.path.split(name)[1][:-4])
	# 	shuffle the filenames to get random files
	random.shuffle(fnames)
	# 	select random training examples and save names to text file
	for key,value in data_dict.items():
		print('Adding ', key, 'examples to the list')
		count = 0
		value[2] = fnames[count: count + int((value[0]/100)*len(fnames))]
		save_to_txt_file(value[1], value[2])

	for key, value in data_dict.items():
		print('Succesfully added ', len(value[2]), 'filenames to' , value[1])


if __name__ == '__main__':
	main()

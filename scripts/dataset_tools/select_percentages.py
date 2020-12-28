# 2nd Oct, 2020 Sumantra Sharma
# inputs - %VOC2012,%VOC2007,%I2R_Data, %I2R_Data_2 of the total images to select from ~/dataset/<VOC2012><VOC2007><I2R_Data_2><I2R_Data>/Annotations/*xml
# 		 - datasat_dir (path to the dataset directory)
# output - a json file containing the filenames of all the images selected 

#  3rd Nov, 2020 : Adding option to read the folders in dataset directory through a text files
import os
import glob
import argparse
import sys
import random
import json

parser = argparse.ArgumentParser(add_help=False)
parser_full = argparse.ArgumentParser(
         description="Program to randomly select specified percentages of files from the dataset folder")

parser.add_argument("-d",
                    "--dataset_dir",
                    help="Path to the dataset folder, default = ~/dataset",
                    default = '~/dataset/',
                    type=str)
#  Open dataset directory and store folder namaes in a list
d = parser.parse_known_args()[0].dataset_dir
if not os.path.isdir(d):
     print("Usage python3 select_percentages.py -d ")
folders =      [o for o in os.listdir(d) 
                    if os.path.isdir(os.path.join(d,o))]
parser_full.add_argument("-d",
                    "--dataset_dir",
                    help="Path to the dataset folder, default = ~/dataset",
                    default = '~/dataset/',
                    type=str)
for f in folders:
     parser_full.add_argument("-"+f,
                         "--"+f+"_p",
                         help="Percentage of dataset to select, default = 100",
                         default = 100,
                         type=int)     
args = parser_full.parse_args()

for arg in vars(args):
    print (arg,'=', getattr(args, arg))
data_dict = {}
for f in folders:
	data_dict[f] = [getattr(args,f+"_p")	, []]

def main():			
#  glob through files and randomly select
	for key,value in data_dict.items():
		file_names = []
		count = 0
		for name in glob.glob(os.path.join(args.dataset_dir,key,'Annotations/') + '*xml'):
			file_names.append(os.path.split(name)[1][:-4])
			count+=1
		value[1] =random.sample(file_names, int((value[0]/100)*len(file_names)))
		print('Randomly selected', len(value[1]), 'filenames from', key, 'from a total of', count, 'files')
# 	save fnames dict to json filwe
	filename = os.path.join(args.dataset_dir,'dataset.txt')
	os.makedirs(os.path.dirname(filename), exist_ok=True)
	with open(filename, "w") as f:
		f.write(json.dumps(data_dict))
			
if __name__ == '__main__':
	main()

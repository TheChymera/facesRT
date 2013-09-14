#!/usr/bin/env python
__author__ = 'Horea Christian'
from os import listdir, path
import pandas as pd

local_dir = path.dirname(path.dirname(path.realpath(__file__))) + '/' # navigates to the folder containing the "analysis" folder
results_subdir = 'results/px0/'
ignore_file_name = 'chr'

results_dir = local_dir + results_subdir

def get_and_filter_results():
	files = [lefile for lefile in listdir(results_dir) if lefile.endswith('.csv') and not lefile.endswith(ignore_file_name+'.csv')]
	data_all = pd.DataFrame([]) # empty container frame for concatenating input from multiple files
	for lefile in files:
		data_lefile = pd.DataFrame.from_csv(results_dir+lefile)
		data_lefile['ID'] = path.splitext(lefile)[0]
		data_lefile = data_lefile[data_lefile['RT'] >=0] # remove entries with instant RTs here
		data_lefile = data_lefile[data_lefile['correct answer'] == data_lefile['keypress']] # remove entries with incorrect answers here
		data_all = pd.concat([data_all, data_lefile], ignore_index=True)
	return data_all
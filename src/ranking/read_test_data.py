# -*- coding: utf-8 -*-
# @Author: vamshi
# @Date:   2018-04-16 00:29:25
# @Last Modified by:   vamshi
# @Last Modified time: 2018-04-17 00:52:55

import os,sys
import pandas as pd
import numpy as np
from ranking import *
import pickle


evidence = "mean"
test_data_dir = "../../data/test_data.tsv"
test_data = pd.read_csv(test_data_dir,sep='\t',names=['questions','ranking','category','site_index','site','remarks'],encoding='utf-8')

questions = test_data['questions'].as_matrix()
#print questions

gt = test_data['ranking']
gt = gt.as_matrix()
#print(gt)
ground_truth = []
for s in gt[1:]:
	s = s.encode('ascii','ignore')
	#print s
	l = list(s.split(','))
	#print l
	ground_truth.append([int(x) for x in l])
	#print list(int(s.split(',')))
#print ground_truth

pred = []
for question in questions:
	index = similarity(question.encode('ascii','ignore'))
	pred.append(index)

with open("pred_"+evidence+".pickle","wb") as f:
	pickle.dump(pred, f)


def eval(pred,gt,n):
	s=0
	for pr,g in (pred,gt):
		s += len(list(set(pred) & set(gt)))/n
	return s/len(gt) 

print("top n accuracy is %d"%eval(pred,ground_truth))


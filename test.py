import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import scipy.sparse as scs # sparse matrix construction 
import scipy.linalg as scl # linear algebra algorithms
import scipy.optimize as sco # for minimization use
import matplotlib.pylab as plt # for visualization

import time
import sys
from sudoku_solver import solver

# We test the following algoritm on small data set.

if __name__ == "__main__":
	if len(sys.argv) < 2:
		data = pd.read_csv("./small2.csv") 
	else:
		data = pd.read_csv(sys.argv[1])

	corr_cnt = 0
	start = time.time()

	random_seed = 42
	sample_max  = 1000

	np.random.seed(random_seed)

	if len(data) > sample_max:
	    samples = np.random.choice(len(data), sample_max)
	else:
	    samples = range(len(data))


	for i in range(len(samples)):
	    quiz = data["quizzes"][samples[i]]
	    solu = data["solutions"][samples[i]]

	    ans = solver(quiz)

	    if (ans == solu):
	        corr_cnt += 1

	    if (i+1) % 20 == 0:
	        end = time.time()
	        print("Aver Time: {t:6.2f} secs. Success rate: {corr} / {all} ".format(t=(end-start)/(i+1), corr=corr_cnt, all=i+1) )

	end = time.time()
	# report:
	print("Aver Time: {t:6.2f} secs. Success rate: {corr} / {all} ".format(t=(end-start)/(sample_max), corr=corr_cnt, all=sample_max) )


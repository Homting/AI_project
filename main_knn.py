#!/usr/local/bin/python3
# File Name: main_knn.py
# Author: Jin LI
# mail: jin.li@vub.ac.be; homtingli@gmail.com
# Created Time: 2017-05-20 15:14:30

import toolkit as tk
from AI_knn import knn
import numpy as np
from validation import cross, nice_print_model_info,draw_map
'''
attributes, instences = tk.readDataSet("./dataset/iris.csv")
# print(instences)
attributes = list(attributes)

instences = tk.Z_ScoreNormalization(instences, len(attributes))
print(instences)
# print(instences)
'''

iris_attr, iris = tk.readDataSet("./dataset/iris.csv")
acc, mcca, ka, map, t1, t2 = cross(knn, iris_attr, iris)

nice_print_model_info(acc, mcca, ka)
draw_map(map)

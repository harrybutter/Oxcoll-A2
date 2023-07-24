"""OIC nickname generator"""

import pandas as pd
import numpy as np
import random as rd

place = input("Your place : ")
name = input("Name : ")

places = pd.read_csv('place.txt')
jobs = pd.read_csv('job.txt')


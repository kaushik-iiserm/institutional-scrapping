import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import pickle
### 
with open('analysis.pkl','rb') as file:
    loaded_file = pickle.load(file)
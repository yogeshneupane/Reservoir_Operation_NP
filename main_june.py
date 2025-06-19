import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utils_june import *
from fitness_june import fitness_calculate
from psocheck import *
from process_june import processing

#calculates best release
best_release = PSO()


#back calculate and graphs
processing(best_release)
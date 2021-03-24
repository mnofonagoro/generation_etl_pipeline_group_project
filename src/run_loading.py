from os import read
from loading import run_loading
#for running locally
path = '/workspace/2021-02-23-isle-of-wight.csv'
file = open('{}'.format(path))
run_loading(file)
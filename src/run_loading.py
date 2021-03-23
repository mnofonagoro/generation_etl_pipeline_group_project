from os import read
from loading import run_loading
#for running locally
file = open('/workspace/2021-02-23-isle-of-wight.csv')
run_loading(file)
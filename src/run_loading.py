from os import read
from loading import run_loading
# for running locally 
file = open('/workspace/chesterfield_23-03-2021_09-00-00.csv')
# /workspace/chesterfield_23-03-2021_09-00-00.csv
# file = open('{}'.format(path))
run_loading(file)
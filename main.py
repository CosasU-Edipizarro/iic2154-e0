# Python modules
import json

# PIP modules

# Local modules
import features

filename = 'dataset.json'
with open(filename) as file_object:
    dataset = [json.loads(line) for line in file_object]

if __name__ == '__main__':
    # Use features

    ## Use top tweets feature
    ## Use top users feature
    ## Use top days feature
    ## Use top hashtags feature

    print("\n ### END OF CODE ### \n")

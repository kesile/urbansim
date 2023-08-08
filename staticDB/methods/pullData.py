import pickle

def pullData(path):
    with open(path, 'rb') as file:
        loaded_people = pickle.load(file)
    return loaded_people
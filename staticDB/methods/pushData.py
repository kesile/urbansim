import pickle

def pushData(push, path):
    try:
        with open(path, 'wb') as file:
            pickle.dump(push, file)
    except FileNotFoundError:
        return "Incorrect Path"
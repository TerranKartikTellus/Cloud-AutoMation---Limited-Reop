import pickle

def save_object_to_file(obj, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(obj, file)
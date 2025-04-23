import os

def blob_to_image(blob, path):
    with open(path, 'wb') as file:
        file.write(blob)
    return path

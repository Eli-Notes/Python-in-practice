import os

# make dir
(not os.path.exists(path_str)) and os.makedirs(path_str)

# read files in a dir
file_names = os.listdir(path_input_data)
file_names.sort()
for fn in file_names:
    pass

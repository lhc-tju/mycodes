def get_names(path,filetype):
    '''获取目录下所有指定文件类型的文件名'''
    import os
    name = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if filetype in file:
                name.append(file)
    return name
	
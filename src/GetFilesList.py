import os
    
def get_file_list(path):
    fileList = {
        "filesInput": [],
        "filesOutput": []
    }
    
    for file in os.listdir(path):
        fullPath = os.path.join(path, file)
        
        if os.path.isfile(fullPath):
            if file.endswith('.in'):
                fileList["filesInput"].append(fullPath)
            elif file.endswith('.sol'):
                fileList["filesOutput"].append(fullPath)
        else:
            sublist = get_file_list(fullPath)
            fileList = {**fileList, **sublist}

    return fileList

import subprocess, os
from src.GetFilesList import get_file_list
from src.ReadFile import read_file

def formatPath(path):
    return path.replace('\\', '/')

def join_paths(path1, path2):
    path = os.path.join(path1, path2)
    return formatPath(path)

def showSimpleFilename(filename):
    filename = filename.replace('/', '\\')
    index = filename[::-1].index('\\')
    index = filename[::-1].index('\\', index + 1)
    index = filename[::-1].index('\\', index + 1)
    return filename[len(filename)-index:]

def get_my_results(directory, filesInput):
    myResults = []

    for fileName in filesInput:
        # read the file
        fullPath = join_paths(directory, fileName)

        # get the file contents
        fileContents = read_file(fullPath)

        # assign the input to the file "Contas_a_Pagar.py" and run the test
        command = f"python .\\code\\main.py < {fullPath}"

        # run in operating system shell
        output = subprocess.check_output(command, shell=True)

        # decode the result
        reult = output.decode().strip()

        # save my results
        myResults.append(reult)
    
    return myResults

def get_solutions(directory, filesOutput):
    solutions = []
    # for each file in the list
    for fileName in filesOutput:
        # read the file
        fullPath = join_paths(directory, fileName)

        # get the file contents
        solutions.append(read_file(fullPath))
    
    return solutions

def runCode(directory):
    # get all the files
    fileList = get_file_list(directory)
    
    # get the files input
    filesInput = fileList["filesInput"]
    
    # get the files output
    filesOutput = fileList["filesOutput"]
    
    # get the results
    myResults = get_my_results(directory, filesInput)
    

    # get the solution
    solutions = get_solutions(directory, filesOutput)
    
    # compare the results
    n_corrects = 0
    for i in range(len(myResults)): 
        print(f"Test {showSimpleFilename(filesInput[i])}")
        solutionSTR = solutions[i]
        myResultSTR = myResults[i].replace('\r', '')

        if myResultSTR != solutionSTR:
            print("Wrong answer for this file!")
            print(f"Your answer:\n{myResultSTR}\n")
            print(f"Correct answer:\n{solutionSTR}")
        else:
            print(f"Correct answer!")
            print(f"{solutionSTR}")
            n_corrects += 1
        
        if len(myResults) - 1 > i:
            print('---------------------------------------------')
        else:
            print()
    
    print(f"You scored {n_corrects*100/len(myResults)}% on the test!")

def main():
    pathIn = r"C:\Users\paler\Downloads\2023f1p2_leilao\2023f1p2_leilao" or input()
    directory = formatPath(pathIn)
    runCode(directory)

if __name__ == '__main__':
    main()
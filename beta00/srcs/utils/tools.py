import sys
from colorama import Style, Fore

def printLog(str, bright=False):
    if bright == True:
        str = Style.BRIGHT + str
    print(Fore.GREEN + str + Style.RESET_ALL)

def printError(str, bright=False):
    if bright == True:
        str = Style.BRIGHT + str
    print(Fore.RED + str + Style.RESET_ALL)

def printInfo(str, bright=False):
    if bright == True:
        str = Style.BRIGHT + str
    print(Fore.BLUE + str + Style.RESET_ALL)

def printModel(model):
    print(Style.BRIGHT + Fore.BLUE + f'\n################  {model["role"]}  ################' + Style.RESET_ALL)

    model_data = list(model.keys())
    model_data.remove('role')
    for data in model_data:
        printInfo(f'===> {data}:', bright=True)
        printInfo(f'{model[data]}')

def getPrompt(file_name):
    with open(file_name, 'r') as file:
        prompt = file.read()
    return prompt.replace('\n', ' ')

def Get_Project():
    if len(sys.argv) <= 1:
        project = input(Fore.GREEN + 'Decrit ton projet dans tous les details: \n' + Style.RESET_ALL)
    else:
        with open(sys.argv[1]) as project_file:
            project = project_file.read()
    return project.replace('\n', ' ')
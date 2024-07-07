from colorama import Style, Fore

def printLog(str):
    print(f'{Fore.GREEN}{str}{Style.RESET_ALL}')

def printError(str):
    print(f'{Fore.RED}{str}{Style.RESET_ALL}')

def getPrompt(file_name):
    with open(file_name, 'r') as file:
        prompt = file.read()
    return prompt.replace('\n', ' ')
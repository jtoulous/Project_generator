import subprocess
from utils.tools import printInfo
#from transformers import AutoTokenizer

def Execute_Cmd(cmd):
    printInfo(f'\n==> exec:', bright=True)
    printInfo(cmd)
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    stdout, stderr = process.communicate()
    exit_code = process.returncode

    stdout_str = stdout.decode('utf-8')
    stderr_str = stderr.decode('utf-8')
    return_query = 'exit_code: ' + str(exit_code) + ' stdout: ' + stdout_str + ' stderr: ' + stderr_str

    return return_query


def Process_Query(model, query, tokenizer):
    behavior_reminder = "Rappel: " + model['behavior']
    processed_query = ""

    for old_cmd in model['history']:
        processed_query = processed_query + old_cmd
    processed_query = processed_query + '\n' + behavior_reminder + '\n' + query
    model['history'].append(processed_query)
    processed_query = tokenizer.bos_token + processed_query + tokenizer.eos_token
    return model, processed_query


def getHisto(model):
    full_histo = "conversation History: "
    for his in model['history']:
        full_histo = full_histo + his + " "
    full_histo = full_histo + 'History finished'
    return full_histo
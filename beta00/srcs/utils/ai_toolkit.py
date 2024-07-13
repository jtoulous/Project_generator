import subprocess
from transformers import AutoTokenizer

def Execute_Cmd(cmd):
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    stdout, stderr = process.communicate()
    exit_code = process.returncode

    stdout_str = stdout.decode('utf-8')
    stderr_str = stderr.decode('utf-8')

    return exit_code, stdout_str, stderr_str

def Process_Query(model, query, tokenizer):
    behavior_reminder = "Rappel: " + model['behavior']
    processed_query = ""

    for old_cmd in model['history']:
        processed_query = processed_query + old_cmd
    processed_query = processed_query + '\n' + behavior_reminder + '\n' + query
    model['history'].append(processed_query)
    processed_query = tokenizer.bos_token + processed_query + tokenizer.eos_token
    return model, processed_query

def Clean_History(history, max_tokens, tokenizer):
    joined_histo = " ".join(history)
    tokens = tokenizer.encode(joined_histo)

    if len(tokens) < max_tokens:
        return history
    else:
        return   
    return 
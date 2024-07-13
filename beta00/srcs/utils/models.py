from transformers import GPTJForCausalLM, GPTNeoXForCausalLM, GPT2LMHeadModel, AutoTokenizer
from .tools import getPrompt, printLog, printError
from .ai_toolkit import Process_Query, Clean_History

class Models():
    def __init__(self):
#        supervisor_model = "EleutherAI/gpt-j-6B" 
#        projectLead_model = "EleutherAI/gpt-j-6B"
#        codeGen_model = "EleutherAI/gpt-neox-20b"

        supervisor_model = "gpt2" 
        projectLead_model = "gpt2"
        codeGen_model = "gpt2"

        self.supervisor = {
            'model_name': supervisor_model,
            'role': 'supervisor',
#            'model': GPTJForCausalLM.from_pretrained(supervisor_model),
            'model': GPT2LMHeadModel.from_pretrained(projectLead_model),
            'tokenizer': AutoTokenizer.from_pretrained(supervisor_model),
            'behavior': getPrompt('utils/prompts/Supervisor_behavior.txt'),
            'project': "",
            'history': [],
            'max_tokens': 1024
        }

        self.project_lead = {
            'model_name': projectLead_model,
            'role': 'project lead',
#            'model': GPTJForCausalLM.from_pretrained(projectLead_model),
            'model': GPT2LMHeadModel.from_pretrained(projectLead_model),
            'tokenizer': AutoTokenizer.from_pretrained(projectLead_model),
            'behavior': getPrompt('utils/prompts/ProjectLead_behavior.txt'),
            'history': [],
            'max_tokens': 1024
        }

        self.code_gen = {
            'model_name': codeGen_model,
            'role': 'code generator',
#            'model': GPTNeoXForCausalLM.from_pretrained(codeGen_model),
            'model': GPT2LMHeadModel.from_pretrained(codeGen_model),
            'tokenizer': AutoTokenizer.from_pretrained(codeGen_model),
            'behavior': getPrompt('utils/prompts/CodeGen_behavior.txt'),
            'history': [],
            'max_tokens': 1024
        }

    def init_project(self):
        next_query = self.Supervisor_query(self.supervisor['project'] + '\n Commence maintenant.')
        return next_query

    def Supervisor_query(self, query):
        tokenizer = self.supervisor['tokenizer']
        self.supervisor['history'] = Clean_History(
                self.supervisor['history'], 
                self.supervisor['max_tokens'],
                tokenizer
            )
        self.supervisor, processed_query = Process_Query(
                self.supervisor, 
                query,
                tokenizer                   
            )

        printLog(f'\nTo superviser ===> {query}\n')
        inputs = tokenizer(processed_query, return_tensors="pt")
        outputs = self.supervisor['model'].generate(
                inputs['input_ids'],
                attention_mask=inputs['attention_mask'],
                pad_token_id=tokenizer.eos_token_id,
                max_length=50,
                num_return_sequences=1
        )
        response = self.supervisor['tokenizer'].decode(outputs[0], skip_special_tokens=True)
        return response


#def ProjectLead_query(self, msg):

#def CodeGen_query(self, msg):

    def System_query(query, project_status):
        if query == 'DONE':
            return '', 'DONE'
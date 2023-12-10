#
# llm.py - Class for calling the LLM API
#
# v1.1 - stubs
# v1.2 - initial llm calls
#
from llama_cpp import Llama
from utils import *

MODEL_TINY = "../models/orca_mini_v3_7b.Q6_K.gguf"

class LLM:
    def summarize(self, columns_output):
        #
        # summarize() is meant to evaluate the output of all
        # cortical column routines, forming the next thought
        #
        llm = Llama(model_path="../models/orca_mini_v3_7b.Q6_K.gguf", verbose=False, n_threads=6, n_gpu_layers=-1, main_gpu=0, n_ctx=2048)
        #llm = Llama(model_path="../models/llama-2-7b-chat.Q5_K_S.gguf", verbose=False)
        prompt = "Summarize the following opinions into one thought in one sentence."
        colout_str = " | ".join(columns_output)
        new_prompt = "### System: You are an AI assistant that follows instruction extremely well. Help as much as you can. ### User: " + prompt + " ### Input: " + colout_str + " ### Response: "

        output = llm(new_prompt, max_tokens=64, stop=["### System:", "\n"], echo=False)
        return output['choices'][0]['text']

    def query(self, prompt, model):
        #
        # query() is for sending a prompt to a model
        #
        llm = Llama(model_path=model, verbose=False, n_threads=6, n_gpu_layers=-1, main_gpu=0, n_ctx=2048)
        new_prompt = "### System: You are an AI assistant that follows instruction extremely well. Help as much as you can. ### User: " + prompt + "### Input: ### Response: "
        output = llm(new_prompt, max_tokens=64, stop=["### System:", "\n"], echo=False)
        response_text = output['choices'][0]['text']
        return(response_text)

    def bool(self, prompt, model):
        #
        # bool() is for asking T/F type questions
        #
        llm = Llama(model_path=model, verbose=False, n_threads=6, n_gpu_layers=-1, main_gpu=0, n_ctx=2048)
        new_prompt = "### System: You are an AI assistant that follows instruction extremely well. Help as much as you can. Assume the question is a YES or NO type question, and those are the only two answers you can give.### User: " + prompt + "### Input: ### Response: "
        output = llm(new_prompt, max_tokens=64, stop=["### System:", "\n"], echo=False)
        response_text = output['choices'][0]['text']
        print("      result:" + response_text)
        if is_yes(response_text):
            print("        returning True")
            return(True)
        else:
            print("        returning False(" + response_text + ")")
            return(False)

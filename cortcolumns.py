#
# cortcolumns.py - set of classes representing the cortical
#     column-like personalities that make up a consciousness.
#
# v1.1 - stubs
# v1.2 - initial llm calls
#
from llama_cpp import Llama

MODEL_TINY = "../models/orca_mini_v3_7b.Q6_K.gguf"

class Analytical_Arthur:
    def analyze_input(self, prompt):
        llm = LLM()
        personality = "You are Analytical Arthur, an expert at analyzing the details of a prompt."
        question1 = "Given the following prompt, generate a question you might ask yourself to generate more detail, or say 'no comment': " + prompt
        output1 = llm.query(personality + question1, MODEL_TINY)
        print("    AA:" + output1)
        if output1.strip().lower() == "no comment":
            output2 = output1
        else:
            question2 = output1
            output2 = llm.query(personality + question2, MODEL_TINY)
            print("    AA:" + output2)
        return "Analytical output based on: " + prompt + " : " + output2

class Curious_Caroline:
    def explore_input(self, prompt):
        llm = LLM()
        personality = "You are Curious Caroline, an expert at understanding how things work and how they might be used."
        question1 = "Given the following prompt, generate a question you might ask yourself to satisfy curiosity, or say 'no comment': " + prompt
        output1 = llm.query(personality + question1, MODEL_TINY)
        print("    CC:" + output1)
        if output1.strip().lower() == "no comment":
            output2 = output1
        else:
            question2 = output1
            output2 = llm.query(personality + question2, MODEL_TINY)
            print("    CC:" + output2)
        return "Exploratory output based on: " + prompt + " : " + output2

class Empathetic_Emma:
    def consider_input(self, prompt):
        # TODO: Implement logic
        return "Considered output based on: " + prompt

class Creative_Cameron:
    def mod_input(self, prompt):
        # TODO: Implement logic
        return "Creative output based on: " + prompt

class Historical_Henry:
    def past_events(self, prompt):
        # TODO: Implement logic
        return "Historical output based on: " + prompt

class Skeptical_Sara:
    def disprove_input(self, prompt):
        # TODO: Implement logic
        return "Skeptical output based on: " + prompt

class Optimistic_Oliver:
    def imagine_input(self, prompt):
        # TODO: Implement logic
        return "Optimistic output based on: " + prompt

class Pessimistic_Pam:
    def imagine_input(self, prompt):
        # TODO: Implement logic
        return "Pessimistic output based on: " + prompt

class Practical_Paul:
    def pathplan(self, prompt):
        # TODO: Implement logic
        return "Practical output based on: " + prompt

class Theoretical_Tina:
    def why(self, prompt):
        # TODO: Implement logic
        return "Theoretical output based on: " + prompt

class Futuristic_Frank:
    def imagine_input(self, prompt):
        # TODO: Implement logic
        return "Futuristic output based on: " + prompt

class Realistic_Rachael:
    def assess_resources(self, prompt):
        # TODO: Implement logic
        return "Realistic output based on: " + prompt

class LLM:
    def summarize(self, columns_output):
        #
        # summarize() is meant to evaluate the output of all
        # cortical column routines, forming the next thought
        #
        llm = Llama(model_path="../models/orca_mini_v3_7b.Q6_K.gguf", verbose=False, n_threads=6)
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
        llm = Llama(model_path=model, verbose=False, n_threads=6)
        new_prompt = "### System: You are an AI assistant that follows instruction extremely well. Help as much as you can. ### User: " + prompt + "### Input: ### Response: "
        output = llm(new_prompt, max_tokens=64, stop=["### System:", "\n"], echo=False)
        response_text = output['choices'][0]['text']
        return(response_text)

#
# fred.py - "A Model for Consciousness"
#
# v1.1 - stub main loop, cort column classes
#
import argparse
from cortcolumns import *

# Set up argument parsing
parser = argparse.ArgumentParser(description="Run the simulation.")
parser.add_argument("-n", type=int, default=-1, help="Number of iterations to run")
args = parser.parse_args()

def main():
    # if only this easy
    alive = True
    iteration_count = 0

    print("")
    print("╭━━━╮╱╱╱╱╱╱╭╮")
    print("┃╭━━╯╱╱╱╱╱╱┃┃")
    print("┃╰━━┳━┳━━┳━╯┃")
    print("┃╭━━┫╭┫┃━┫╭╮┃")
    print("┃┃╱╱┃┃┃┃━┫╰╯┃")
    print("╰╯╱╱╰╯╰━━┻━━╯")
    print("")
    print("11/2023 J LaCoursiere")
    print("")

    # Instantiate column classes
    analytical_arthur = Analytical_Arthur()
    curious_caroline = Curious_Caroline()
    empathetic_emma = Empathetic_Emma()
    creative_cameron = Creative_Cameron()
    historical_henry = Historical_Henry()
    skeptical_sara = Skeptical_Sara()
    optimistic_oliver = Optimistic_Oliver()
    pessimistic_pam = Pessimistic_Pam()
    practical_paul = Practical_Paul()
    theoretical_tina = Theoretical_Tina()
    futuristic_frank = Futuristic_Frank()
    realistic_rachael = Realistic_Rachael()

    # Instantiate the LLM class
    llm = LLM()

    # Initial prompt
    prompt = "Should we worry about AI?"
    print("I shall begin my journey considering: " + prompt)

    while alive:  # Forever loop?
        # List to collect outputs from each column
        columns_output = []

        # Pass the prompt to each column and collect the outputs
        columns_output.append(analytical_arthur.analyze_input(prompt))
        columns_output.append(curious_caroline.explore_input(prompt))
        columns_output.append(empathetic_emma.consider_input(prompt))
        columns_output.append(creative_cameron.mod_input(prompt))
        columns_output.append(historical_henry.past_events(prompt))
        columns_output.append(skeptical_sara.disprove_input(prompt))
        columns_output.append(optimistic_oliver.imagine_input(prompt))
        columns_output.append(pessimistic_pam.imagine_input(prompt))
        columns_output.append(practical_paul.pathplan(prompt))
        columns_output.append(theoretical_tina.why(prompt))
        columns_output.append(futuristic_frank.imagine_input(prompt))
        columns_output.append(realistic_rachael.assess_resources(prompt))

        # Summarize the columns' outputs to produce the next internal thought
        next_internal_thought = llm.summarize(columns_output)

        # Print the next internal thought (or pass it to a chat interface)
        print("THOUGHT:" + next_internal_thought)

        # Set the next internal thought as the prompt for the next iteration
        prompt = next_internal_thought

        # if an iteration count was supplied (-n), stop when we reach it
        iteration_count += 1
        if 0 <= args.n == iteration_count:
            break

if __name__ == "__main__":
    main()

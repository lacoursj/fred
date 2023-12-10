# ANSI escape codes for formatting
class TextFormat:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    YELLOW = '\033[93m'

# Function to print bold and yellow text
def print_bold_yellow(text):
    formatted_text = f"{TextFormat.BOLD}{TextFormat.YELLOW}{text}{TextFormat.RESET}"
    print(formatted_text)

is_yes = lambda s: s.strip().lower() in {'yes', 'y', 'yeah', 'yep', 'sure', 'ok'}



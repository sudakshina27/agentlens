from llm import ask_llm

# Experiment 1: same question twice -> different answers (sampling)
# ask_llm("Describe the ocean in one sentence.")
# ask_llm("Describe the ocean in one sentence.")

# Experiment 2: two separate calls -> the name is forgotten (stateless API)
# ask_llm("My name is Sudakshina.")
# ask_llm("What's my name?")

# Experiment 3: full history in one request -> the name is remembered
ask_llm([
    {"role": "user", "content": "My name is Sudakshina."},
    {"role": "assistant", "content": "Nice to meet you, Sudakshina!"},
    {"role": "user", "content": "What's my name?"},
])

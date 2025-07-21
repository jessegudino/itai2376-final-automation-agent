def make_decision(memory_items):
    if not memory_items:
        return "I have nothing to work with!"
    else:
        return f"I see you gave me this info: {memory_items[-1]}"

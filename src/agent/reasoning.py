def make_decision(memory_items):
    """
    Example decision-making function.
    Just returns a message based on how many items are in memory.
    """
    if not memory_items:
        return "No input received yet."
    elif "error" in memory_items[-1].lower():
        return "Warning: error detected in the input!"
    else:
        return f"Processed {len(memory_items)} items so far."

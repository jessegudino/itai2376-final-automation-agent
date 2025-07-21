class Agent:
    def process(self, input_text):
        if "error" in input_text.lower():
            return "Alert: Investigate issue"
        elif "start" in input_text.lower():
            return "Action: Initiate system"
        elif "restart" in input_text.lower():
            return "Action: Restart system"
        elif "collect" in input_text.lower():
            return "Action: Begin data collection"
        else:
            return "Action: No match found"

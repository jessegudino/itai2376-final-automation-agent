from agent.core import Agent

if __name__ == "__main__":
    agent = Agent()

    inputs = [
        "Start process",
        "Collect data",
        "error: failed to load file",
        "Restart system"
    ]

    for item in inputs:
        result = agent.process(item)
        print(f"Input: {item}")
        print(f"Decision: {result}")
        print("-----")

from ai import agentResponse

def debate_between_agents(topic, turns):
    """
    Function to facilitate a debate between two agents with opposing beliefs on a given topic.
    
    Args:
        topic (str): The topic to be debated.
        turns (int): The number of turns for the debate.
        
    Returns:
        None
    """
    system_prompt_agent1 = f"You are an AI biased towards the belief that '{topic}' is beneficial or true. Argue in favor of this belief."
    system_prompt_agent2 = f"You are an AI biased towards the belief that '{topic}' is harmful or false. Argue against this belief."

    conversation_history = f"Topic for debate: {topic}"

    for turn in range(1, turns + 1):
        if turn % 2 != 0:  # Odd turns for Agent 1 (pro)
            print(f"\nTurn {turn} - Agent 1 (Pro):")
            response_agent1 = agentResponse(system_prompt_agent1, conversation_history)
            print(response_agent1)
            conversation_history += f"\nAgent 1: {response_agent1}"
        else:  # Even turns for Agent 2 (con)
            print(f"\nTurn {turn} - Agent 2 (Con):")
            response_agent2 = agentResponse(system_prompt_agent2, conversation_history)
            print(response_agent2)
            conversation_history += f"\nAgent 2: {response_agent2}"

if __name__ == "__main__":
    print("Welcome to the AI Debate Program!")
    topic = input("Enter a topic for the debate: ")
    while not topic.strip():
        topic = input("Please enter a valid topic for the debate: ")
    
    try:
        turns = int(input("Enter the number of turns for the debate (e.g., 6): "))
        if turns <= 0:
            raise ValueError("The number of turns must be greater than 0.")
    except ValueError:
        print("Invalid input. Setting default number of turns to 6.")
        turns = 6
    
    debate_between_agents(topic, turns)

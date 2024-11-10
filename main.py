from ai import agentResponse

def debate_between_agents(topic, turns):
    """
    Function to facilitate an in-depth debate between two agents with opposing beliefs on a given topic.
    Each agent presents arguments backed by research, evidence, and citations, and assesses the trustworthiness
    of their information. A judge evaluates the debate based on a rubric and provides scores at the end.
    
    Args:
        topic (str): The topic to be debated.
        turns (int): The number of turns for the debate.
        
    Returns:
        None
    """
    # Initialize system prompts for both agents
    system_prompt_agent_pro = (
        f"You are Agent Pro, an AI assistant advocating that '{topic}' is beneficial or true. "
        "You deeply believe this and will advocate your reasoning in one paragraph."
        "You make sure to disupte points against your belifs while also introducing new points yourself."
        
    )
    
    system_prompt_agent_con = (
        f"You are Agent Con, an AI assistant arguing that '{topic}' is harmful or false. "
        "You deeply believe this and will advocate your reasoning in one paragraph."
        "You make sure to disupte points against your belifs while also introducing new points yourself."
    )
    
    # Initialize conversation history
    conversation_history = []

    # Debate loop
    for turn in range(1, turns + 1):
        if turn % 2 != 0:  # Odd turns for Agent Pro
            print(f"\nTurn {turn} - Agent Pro:")
            system_prompt = system_prompt_agent_pro
            agent_name = "Agent Pro"
        else:  # Even turns for Agent Con
            print(f"\nTurn {turn} - Agent Con:")
            system_prompt = system_prompt_agent_con
            agent_name = "Agent Con"
        
        messages = [{"role": "system", "content": system_prompt}] + conversation_history

        response = agentResponse(messages)
        print(response)
        # Append the assistant's response to the conversation history with the agent's name
        conversation_history.append({"role": "assistant", "name": agent_name, "content": response})

    # Judging the debate
    print("\nDebate concluded. Evaluating the arguments...\n")
    judge_prompt = (
        "You are an impartial judge evaluating the preceding debate. "
        "Assess each agent's arguments based on the following rubric:\n"
        "1. Strength of Arguments\n"
        "2. Use of Evidence and Citations\n"
        "3. Trustworthiness of Sources\n"
        "4. Ability to Refute Opponent's Points\n"
        "Provide scores out of 10 for each category for both agents, "
        "and declare a winner based on the total scores. Provide a summary of your evaluation."
    )
    messages = [{"role": "system", "content": judge_prompt}] + conversation_history
    judge_response = agentResponse(messages)
    print(judge_response)

if __name__ == "__main__":
    print("Welcome to the AI Debate Program 2.0!")
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

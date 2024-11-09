from ai import aiQuery, agentResponse

def internal_debate(topic, turns):
    """
    Function to facilitate an internal debate on a given topic for a specified number of turns.
    
    Args:
        topic (str): The topic to be debated.
        turns (int): The number of turns the AI will internally debate the topic.
        
    Returns:
        None
    """
    system_prompt = "You are an unbiased AI system tasked with debating both sides of a topic internally without making judgments."
    conversation_history = f"Let's start a debate on the topic: {topic}"
    
    for turn in range(1, turns + 1):
        print(f"\nTurn {turn}:")
        response = agentResponse(system_prompt, conversation_history)
        print(response)
        
        # Update conversation history to include the response for context in the next turn
        conversation_history += f"\nAI: {response}"

if __name__ == "__main__":
    print("Welcome to the AI Internal Debate Program!")
    topic = input("Enter a topic for the AI to debate: ")
    while not topic.strip():
        topic = input("Please enter a valid topic for the AI to debate: ")
    
    try:
        turns = int(input("Enter the number of turns for the debate (e.g., 5): "))
        if turns <= 0:
            raise ValueError("The number of turns must be greater than 0.")
    except ValueError:
        print("Invalid input. Setting default number of turns to 5.")
        turns = 5
    
    internal_debate(topic, turns)

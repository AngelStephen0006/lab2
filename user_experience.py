#---------------------------------------
#  User Experience
#    Student C
#---------------------------------------


#---------------------------------------

def choose_difficulty():
    """
    Allows players to choose the difficulty level of the questionsThe user is going to input their choice.

    Parameters: None
    Returns:
    - str: Valid difficulty levels are ('easy', 'medium', 'hard').
    """
    #------------------------
    # Add your code here
    #------------------------
    n = int(input("choose a level:"))
              
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 3
    else:
        print("Invalid input")
        return 1
    
            
    #raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def display_leaderboard(leaderboard):
    """
    Displays the leaderboard, showing top scores in descending order. #comment added 

    Parameters:
    - leaderboard (dict): A dictionary containing player names as keys and their scores as values.

    Returns: None

    The function sorts the leaderboard by scores in descending order and prints the names and scores of the top players. If the leaderboard is empty, it prints a message indicating that there are no scores to display.
    """
    #------------------------
    # Add your code here
    #------------------------
    l=[]
    for value in leaderboard:
        l.append(value)
    l.sort(reverse=True)
    print(l)
    #raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def save_score(player_name, score, file_path='scores.txt'):
    """
    Saves the player's score to a file.

    Parameters:
    - player_name (str): The name of the player.
    - score (int): The score achieved by the player.
    - file_path (str): The file path to save the score.

    Returns: None
    """
    #------------------------
    # Add your code here
    #------------------------
    with open ('scores.txt','a') as file:
        file.write(f"{player_name}:{score}\n")
        
    #------------------------

#---------------------------------------

def load_top_scores(file_path='scores.txt'):
    """
    Loads the top scores from a file into a leaderboard dictionary.

    Parameters:
    - file_path (str): The file path from which to load the scores.

    Returns:
    - dict: The leaderboard dictionary with player names as keys and scores as values.
    """
    #------------------------
    # Add your code here
    #------------------------
    leaderboard={}
    with open(file_path, 'r') as file:
        for line in file:
            player_name, score = line.strip().split(':')
            leaderboard[player_name] = int(score)
    return leaderboard
    #raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def provide_feedback(is_correct):
    """
    Provides feedback to the player after each round.

    Parameters:
    - is_correct (bool): Indicates whether the player's answer was correct.

    Returns: None

    Example:
    - is it correct?   "Well done!"
    - is it incorrect? "Sorry, that's incorrect."
    """
    #------------------------
    # Add your code here
    #------------------------
    if is_correct:
        print("Well done!")
    else:
        print("Sorry, that's incorrect.")
    #raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def fifty_fifty_lifeline(correct_answer, options):
    """
    Provides a 50/50 lifeline by removing two incorrect answers, leaving the correct answer and one other incorrect answer.

    Parameters:
    - correct_answer (str): The correct answer to the current question.
    - options (list): A list containing all possible answers including the correct answer.

    Returns:
    - list: A reduced list of answers containing only the correct answer and one randomly selected incorrect answer.

    This function is designed to be used once per game session by a player who chooses to use the 50/50 lifeline. It randomly selects one incorrect answer to keep along with the correct answer and removes the other options.
    """
    #------------------------
    # Add your code here
    #------------------------
    incorrect_answer=[]
    for word in range (options):
        if word!= correct_answer:
            incorrect_answer.append(word)
    import random
    c=random.shuffle(incorrect_answer)
    print(c,correct_answer)
            
        
        
    #raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def skip_question(allowed_skips):
    """
    Allows the player to skip a question during the game.

    Parameters:
    - allowed_skips (int): The number of skips available to the player.

    Returns:
    - bool: True if the skip was successful (and a skip was available), False otherwise.

    This function checks if the player has any skips available. If so, it decrements the allowed_skips counter and returns True, indicating the question can be skipped. If no skips are available, it returns False. This function should be called before presenting a new question to the player.
    """
    #------------------------
    # Add your code here
    #------------------------
    if allowed_skips >0:
        allowed_skips -= 1
        return True
    else:
        return False
        
        
    #raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------


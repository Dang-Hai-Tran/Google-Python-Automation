import random

def Guess(participants):
    my_participant_dict = {}
    for participant in participants:
        my_participant_dict[participant] = random.randint(1, 9)
    try:
        if my_participant_dict["Larry"] == 9:
            return True
        return False
    except KeyError:
        return None

participants = ['Cathy', 'Fred', 'Jack', 'Tom']
print(Guess(participants))

from Command import Command

from Reinforcement import Reinforcement

def Is_Command(message):

    return message[0] == '!'

# ---------------- Main method ----------------------

message = '!jump'

if Is_Command(message):

    chat = Command(message)

else:

    chat = Reinforcement(message) 

chat.Handle()

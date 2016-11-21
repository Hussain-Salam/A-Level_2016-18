#-------------------------------------------------------
#   _____ _       _                __      _____  __   |
#  / ____(_)     | |               \ \    / / _ \/_ |  |
# | |     _ _ __ | |__   ___ _ __   \ \  / / | | || |  |
# | |    | | '_ \| '_ \ / _ \ '__|   \ \/ /| | | || |  |
# | |____| | |_) | | | |  __/ |       \  / | |_| || |  |
#  \_____|_| .__/|_| |_|\___|_|        \/   \___(_)_|  |
#          | |                                         |
#          |_|                                         |
#-------------------------------------------------------
#      Developer: Hussain Salam | Date: 20/11/2016     |
#-------------------------------------------------------

user_input = input("[SYSTEM]: Enter your Text: ")
user_list = list(user_input)
#print("[DEBUG]: Users Text: ", user_list) - Remove '#' for debugging purposes
text = []
for i in user_list:
    text.append(int(ord(i)))
#print ("[DEBUG]: Text Converted: ", text) - Remove '#' for debugging purposes

index = (0)
for i in text:
    text[0+index] = text[0+index] + 2
    index += 1

#print ("[DEBUG]: Text Converted: ", text) - Remove '#' for debugging purposes

user_list = ""
for i in text:
    user_list += chr(i)
print ("[SYSTEM]: Encrypted Text: ", user_list)

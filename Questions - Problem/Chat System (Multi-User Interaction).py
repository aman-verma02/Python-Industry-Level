
'''
❓ Problem
Design:
send_message(sender, receiver, message)
get_messages(user)

🧠 Thinking
User
dictionary → user → messages
'''


# State + Behavior + Constraints + Edge Cases


class ChatSystem:
    def __init__(self):
        self.chats = {}

    def send_message(self, sender, receiver, message):
        if receiver not in self.chats:
            self.chats[receiver] = []
        
        self.chats[receiver].append((sender, message))

    def get_messages(self, user):
        return self.chats.get(user, [])
    

'''
⚠ Edge Cases
User with no messages
Message ordering
'''
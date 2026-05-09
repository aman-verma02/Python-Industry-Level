'''
❓ Problem
Allow only N requests per user

🧠 Thinking
Use:
dictionary → user → count
'''


class RateLimiter:
    def __init__(self, limit):
        self.limit = limit
        self.users = {}

    def allow_request(self, user):
        if user not in self.users:
            self.users[user] = 1
            return True
        
        if self.users[user] < self.limit:
            self.users[user] += 1
            return True
        
        return False
    

rl = RateLimiter(3)

print(rl.allow_request("Trek"))  # True
print(rl.allow_request("Trek"))  # True
print(rl.allow_request("Trek"))  # True
print(rl.allow_request("Trek"))  # False
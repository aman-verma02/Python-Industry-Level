'''
❓ Problem
Design:

add_task(name, priority)
execute_task() → highest priority first

🧠 Thinking
Use:
list of tuples
sort OR priority queue
'''


class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, priority):
        self.tasks.append((priority, name))

    def execute_task(self):
        if not self.tasks:
            return "No tasks"
        
        # highest priority first
        self.tasks.sort(reverse=True)
        task = self.tasks.pop(0)
        
        return f"Executing {task[1]}"
    

'''
⚠ Edge Cases
Empty queue
Same priority tasks
'''
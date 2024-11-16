from datetime import datetime

from priorityqueue import PriorityQueue

class Task():
    def __init__(self, id, task_name, priority, deadline):
        self.ID = id
        self.Name = task_name
        self.Priority = priority
        self.Deadline = deadline

    def __repr__(self):
        return "{ Name : " +f"{self.Name} , Priority: {self.Priority}, Deadline: {self.Deadline}" + "}"


if __name__ == "__main__":
    priorityQeue = PriorityQueue()
    task = Task(1, "Workout", 1, datetime(2025, 6, 30))
    task2 = Task(2, "Class Work", 2, datetime(2024, 11, 30))

    priorityQeue.insert(task)
    priorityQeue.insert(task2)

    print("Size:", priorityQeue.size())  
    print("Top Priority:", priorityQeue.peek())  
    print("Max:", priorityQeue.extract_max())  
  


    


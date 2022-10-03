class Task:
    def __init__(self, id, cycles_left):
        
        self.id = id
        self.cycles_left = cycles_left
        self._next = None
        self._prev = None
        
    def reduce_cycles(self, reduction):
        #reduces cycles_left by the appropriate amount
        self.cycles_left -= reduction

class TaskQueue:
    def __init__(self, cycles_per_task = 1):
        self.current = None
        self.cycles_per_task = cycles_per_task
        self.len = 0
        self.ids = set()
    
    def __len__(self):
        return self.len
    
    def is_empty(self):
        return self.current == None

    def add_task(self, task):
        if self.current is None:
            self.current = task
            # the element should point to itself if there's one element
            self.current.prev = task 
            self.current.next = task
        else:
            # equates so that the task gets added before the current
            temp = self.current.prev 
            self.current.prev = task 
            task.next = self.current 
            temp.next = task 
            task.prev = temp 
        self.len += 1
        self.ids.add(task.id)

    def remove_task(self,id):
        # raises error to see if the id is in the list
        if(self.len == 0) or (id not in self.ids):
            raise RuntimeError("id does not exist")
        elif self.len == 1 and self.current.id == id: 
            self.current = None
            self.next = None
            self.prev = None
        elif self.current.id == id:
            self.current.next.prev = self.current.prev
            self.current = self.current.next
            self.current.prev.next = self.current
        else:
            task = self.current.next
            for i in range(len(self)):
                if task.id == id:
                    task.next.prev = task.prev
                    task = task.next 
                    task.prev.next = task
                else: 
                    task = task.next
        # decrease length because the task was removed
        self.len -= 1
        
    def execute_tasks(self):
        cycle = 0 
        task = self.current
        while not self.is_empty():
            for i in range(len(self)):
                if self.cycles_per_task <= task.cycles_left:
                    task.reduce_cycles(self.cycles_per_task)
                    cycle += self.cycles_per_task
                    if task.cycles_left == 0:
                        print("Finished task "+str(task.id)+" after "+str(cycle)+" cycles")
                        self.remove_task(task.id)
                    task = task.next
                elif self.cycles_per_task > task.cycles_left: 
                    cycle += task.cycles_left 
                    task.reduce_cycles(task.cycles_left)
                    print("Finished task "+str(task.id)+" after "+str(cycle)+" cycles")
                    self.remove_task(task.id)
                    task = task.next
        return cycle

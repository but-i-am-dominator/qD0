from datetime import datetime

class project:
    """Builder design."""

    def __init__(self, name, details=None, creation_date=None, list_tasks=None):
        self.name = name
        self.creation_date = self.set_creation_date(creation_date)
        # Everything else
        self.due_date = None
        self.completion_date = ''
        self.complete = False
        self.tasks = []

    def set_creation_date(self, date_str):
        try:
            creation_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        except (ValueError, TypeError):
            creation_date = datetime.now()
        return creation_date
    
    def set_completion_date(self, date_str):
        '''Set method for due date. Use "%Y-%m-%d %H:%M:%S"'''
        self.completion_date = date_str
        return self

    def set_due_date(self, date_str):
        '''Set method for due date. Use "%Y-%m-%d %H:%M:%S"'''
        self.due_date = date_str
        return self

    def set_complete(self):
        '''Set method for complete.'''
        self.complete = True
        return self
    
    def set_task(self, task):
        '''Set method for adding a task to the task list.'''
        self.tasks.append(task)
        return self

class task:

    def __init__(self, name, project=None, creation_date=None):
        self.name = name
        self.project = project
        self.creation_date = self.set_creation_date(creation_date)
        self.due_date = ''
        self.completion_date = ''
        self.details = ''
        self.complete = False
        self.priority = ''

    def set_creation_date(self, date_str):
        try:
            creation_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        except (ValueError, TypeError):
            creation_date = datetime.now()
        return creation_date
    
    def set_completion_date(self, date_str):
        '''Set method for due date. Use "%Y-%m-%d %H:%M:%S"'''
        self.completion_date = date_str
        return self

    def set_due_date(self, date_str):
        '''Set method for due date. Use "%Y-%m-%d %H:%M:%S"'''
        self.due_date = date_str
        return self
    
    def set_complete(self):
        '''Set method for complete.'''
        self.complete = True
        return self
    
    def set_priority(self, priority):
        '''Set method for priority. Like-It, Love-It Gotta-Have-It'''
        priority = priority.lower()
        valid_priorities = {"like-it", "love-it", "gotta-have-it"}
        if priority in valid_priorities:
            self.priority = priority
        else:
            self.priority = None 
        return self
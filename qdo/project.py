from datetime import datetime

class project:

    def __init__(self, name):
        self.name = name
        self.creation_date = project.creation_date()

    def creation_date():
        now = datetime.now()
        return (str(now.strftime("%Y-%m-%d")), str(now.strftime("%H:%M:%S")))
    




class task:

    def __init__(self, name, project):
        self.name = name
        self.project = project
        self.creation_date = project.creation_date()
        self.due_date = ''
        self.details = ''

    def creation_date():
        now = datetime.now()
        return (str(now.strftime("%Y-%m-%d")), str(now.strftime("%H:%M:%S")))
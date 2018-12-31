
#TODO check http://zetcode.com/python/prettytable/
#TODO move to a database, possibly sqlite3 and then use pandas for analysis and retrieval.

class task(object):
    def __init__(self, **kwargs):
        self.title = kwargs['title']
        self.tags  = set() if len(kwargs) == 1 else set(kwargs['tags'])
        self.due   = kwargs['due']
        self.done  = False
    
    def __str__(self):
        status = 'done' if self.done is True else 'todo'
        return f'{self.title.ljust(20)} {self.due.ljust(20)} {status}'
        
class tasklist(object):
    def __init__(self, tasks):
        self.tasks = tasks
    def list_for_tags(self, taglist):
        result = []
        for task in self.tasks:
            if len(task.tags.intersection(taglist)) > 0 :
                result.append(task)
        return result


##unit test
def main()
    def printmenu():
        return int(input('1.View 2.Add 3.Search \n\n'))
    task1 = task(title = 'buy milk', tags= {'mall','quick'},due='by next thursday') 
    task2 = task(title = 'clean room', tags= {'house','quick'},due='today') 
    main_task_list = tasklist(tasks = [task1, task2])
    while(True):
        choice = printmenu()
        if choice not in {1,2,3}:
            break
        else:
            if choice == 1:
                for t in main_task_list.tasks:
                    print(t)
                continue
            if choice == 3:
                query = set(input('enter a thing ').split())
                print(*main_task_list.list_for_tags(query), sep='\n\n')
if __name__ == "__main__":
    main()

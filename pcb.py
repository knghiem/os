
# coding: utf-8

# In[6]:


import queue

class Process_Queue():
    def __init__(lst=[]):
        self.q = Queue()
        for i in range(len(lst)):
            item = lst[i]
            q.put(item)
    
    # add one process
    def addProcess(self, p):
        self.q.put(p)
    
    # add multiple processes in order
    def addProcesses(self, lst):
        for i in range(len(lst)):
            item = lst[i]
            self.q.put(item)
    
    # print out processes
    def listProcesses(self):
        qlst = list(self.q.queue)
        for i in range(len(qlst)):
            p = qlst[i]
            println(p)
    
    # default printing method
    def __str__(self):
        size = self.q.qsize
        println("Process Queue of size: ",size, sep="")
        self.listProcesses()

class Process():
    def __init__(name=""):
        self.id = random()
        self.name = name
    
    # default printing method
    def __str__(self):
        println("Process ID ",self.id," | name ", self.name)
    
class Input():
    def __init__(fname=""):
        self.fname = fname
    
    def readInput():
        content = open(self.fname, "r").read()
        return content
    
    def readlnInput():
        lines = open(self.fname, "r").readlines()
        return lines
        
    
    
    
    


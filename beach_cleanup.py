import random
import copy
import math
from heapq import heappush,heappop

class node:
    def __init__(self,pos,g,l,h,parent=None):
        self.pos=pos
        self.g=g
        self.h=h
        self.l=l
        self.f=g+h
        self.parent=parent

    def set_heuristic(self,task_pos,coll_pos):
        dist=0
        if self.l==1:
            dist=abs(self.pos[0]-task_pos[0])+abs(self.pos[1]-task_pos[1])
            dist+=abs(task_pos[0]-coll_pos[0])+abs(task_pos[1]-coll_pos[1])
        if self.l==2:
            dist=abs(self.pos[0]-coll_pos[0])+abs(self.pos[1]-coll_pos[1])
        self.h=dist
        self.f=self.g+self.h

    def __lt__(self,other):
        return self.f<other.f

class Beach :
    
    def __init__(self):
        self.size=10
        self.robot_count=5
        self.collection_point=(0,0)
        self.debri_count=5
        self.debris=random.sample([[(x,y) for y in range(10)] for x in range(10)],self.debri_count)
        self.robot_positions=random.sample([[(x,y) for y in range(10)] for x in range(10)],self.robot_count)
    
    def show(self):
        for i in range(0,self.size):
            print((self.size*9+1)*"-")
            for j in range(0,self.size):
                pos=(i,j)
                a=0
                print("|",end="")

                for k in range(0,len(self.robot_positions)):
                    if pos==self.robot_positions[k]:
                        print(f" R{k} ",end="")
                        a=1
                        break
                if pos==self.collection_point:
                    print(" C0 ",end="")
                    a+=2
                else:       
                    for k in range(0,len(self.debris)):
                        if pos==self.debris[k]:
                            print(f" D{k} ",end="")
                            a+=2
                            break        
                if a==0:
                    print("        ",end="")
                if a==1 or a==2:
                    print("    ",end="")
            print("|")
        print((self.size*9+1)*"-")

    def get_adjacent(self,pos):
        new_pos=[(pos[0]+dx, pos[1]+dy) for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]]
        for i,j in new_pos:
            if i<0 or j<0:
                new_pos.remove((i,j))
            elif i>=self.size or j>=self.size:
                new_pos.remove((i,j))
        return new_pos
    
    def mla_star(self,start,task_pos,t_max):
        collection_pos=self.collection_point
        open=[]
        start_node=node(start,0,0,0,None)
        heappush(open,start_node)
        while len(open)>0:
            current=heappop(open)
            if current.l==1 and current.g>t_max:
                continue
            if current.l==1 and current.pos==task_pos:
                n_1=node(current.pos,current.g,2,current)
                n_1.set_heuristic(task_pos,collection_pos)
                heappush(open,n_1)
            if current.l==2 and current.pos==collection_pos:
                path=[]
                while current:
                    path.append(current.pos)
                    current=current.parent
                path.reverse()
                print(path)
                return path
            
            adjacent_pos=self.get_adjacent(current.pos)
            for neighbour in adjacent_pos:
                if(neighbour==self.collection_point):
                    new_node=node(neighbour,current.g+1,current.l,0,current)
                    new_node.set_heuristic(task_pos,collection_pos)
                    heappush(open,new_node)
                    continue
                for i in self.ongoing_tasks:
                    if neighbour==i['path'][0] or neighbour==i['path'][1]:
                        adjacent_pos.remove(neighbour)
                        break
                else:
                    new_node=node(neighbour,current.g+1,current.l,0,current)
                    new_node.set_heuristic(task_pos,collection_pos)
                    heappush(open,new_node)
        return None
    
    def create_pairs(self,task_list,agent_list):
        pairs=[]
        for t in task_list:
            for a in agent_list:
                heuristic=abs(t["pos"][0][0]-a["pos"][0][0])+abs(t["pos"][0][1]-a["pos"][0][1])#add distance to collection
                pair={"debri":t,"agent":a,"h":heuristic}
                pairs.append(pair)
        pairs.sort(key=lambda x:x["h"])
        return pairs
    
    def move_idle_agent(self,agent_list,a):
        pass

    def task_allocation(self,task_list,agent_list):
        while len(task_list)!=0:
            for i in self.ongoing_tasks:
                position=i["path"].pop(0)
                if(len(i["path"])==0):
                    #print(f"Debri {i["debri"]["index"]} cleaned by agent {i["agent"]["index"]}")
                    self.ongoing_tasks.remove(i)
                    task_list.append(i["agent"])
                if(self.debris[i["debri"]["index"]]==self.robot_positions[i["agent"]["index"]]):
                    self.debris[i["debri"]["index"]]=position
                self.robot_positions[i["agent"]["index"]]=position  
            self.show()
            pairs=self.create_pairs(task_list,agent_list)
            for pair in pairs:
                if(pair["agent"] in agent_list and pair["debri"] in task_list):
                    path_time=self.mla_star(pair["agent"]["pos"][0],pair["debri"]["pos"][0],math.inf)
                    task={"agent":pair["agent"],"debri":pair["debri"],"path":path_time}
                    self.ongoing_tasks.append(task)
                    agent_list.pop(pair["agent"])
                    task_list.remove(pair["debri"])
            for a in agent_list.index:
                if agent_list[a] in task_list :
                    self.move_idle_agent(agent_list,a)
            self.time_step=self.time_step+1
             
    def simulate(self):
        self.time_step=0
        task_list=[{"index":i,"pos":x} for i,x in enumerate(self.debris)]
        agent_list=[{"index":i,"pos":x} for i,x in enumerate(self.robot_positions)]
        self.ongoing_tasks=[]
        self.task_allocation(task_list,agent_list)

if __name__== "__main__":
    arena=Beach()
    arena.simulate()    

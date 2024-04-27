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
        self.size=7
        self.robot_count=4
        self.collection_point=(0,0)
        self.debri_count=4
        population=[]
        for x in range(self.size):
            for y in range(self.size):
                population.append((x,y))
        self.debris=random.sample(population,self.debri_count)
        self.robot_positions=random.sample(population,self.robot_count)
    
    def show(self):
        print("Time : ",self.time_step)
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
        new=list(new_pos)
        for i,j in new:
            if i<0 or j<0:
                new_pos.remove((i,j))
            elif i>=self.size or j>=self.size:
                new_pos.remove((i,j))
        return new_pos
    
    def mla_star(self,start,task_pos,t_max):
        collection_pos=self.collection_point
        open=[]
        start_node=node(start,0,1,0,None)
        heappush(open,start_node)
        while len(open)>0:
            current=heappop(open)
            if current.l==1 and current.g>t_max:
                continue
            if current.l==1 and current.pos==task_pos:
                n_1=node(current.pos,current.g,2,0,current)
                n_1.set_heuristic(task_pos,collection_pos)
                heappush(open,n_1)
            if current.l==2 and current.pos==collection_pos:
                path=[]
                while current:
                    path.append(current.pos)
                    current=current.parent
                path.reverse()
                return path
            
            adjacent_pos=self.get_adjacent(current.pos)
            adjacent=list(adjacent_pos)
            for neighbour in adjacent:
                if(neighbour==self.collection_point):
                    new_node=node(neighbour,current.g+1,current.l,0,current)
                    new_node.set_heuristic(task_pos,collection_pos)
                    heappush(open,new_node)
                    continue
                for i in self.ongoing_tasks:
                    t=current.g
                    if t<len(i['path']) and t<len(i['path'])-1:
                        if neighbour==i['path'][t+0] or neighbour==i['path'][t+1]:
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
                heuristic=abs(t["pos"][0]-a["pos"][0])+abs(t["pos"][1]-a["pos"][1])#add distance to collection
                pair={"debri":t,"agent":a,"h":heuristic}
                pairs.append(pair)
        pairs.sort(key=lambda x:x["h"])
        return pairs
    
    def move_idle_agent(self,agent_list,a):
        pass

    def task_allocation(self,task_list,agent_list):
        while len(task_list)!=0:
            expired=[]
            for i in self.ongoing_tasks:
                position=i["path"].pop(0)
                if(self.debris[i["debri"]["index"]]==self.robot_positions[i["agent"]["index"]]):
                    self.debris[i["debri"]["index"]]=position
                self.robot_positions[i["agent"]["index"]]=position 
                if(len(i["path"])==0):
                    expired.append(i)
            for i in expired:
                self.ongoing_tasks.remove(i)
                i["agent"]["pos"]=self.robot_positions[i["agent"]["index"]]
                agent_list.append(i["agent"])
            self.show()
            pairs=self.create_pairs(task_list,agent_list)
            for pair in pairs:
                if(pair["agent"] in agent_list and pair["debri"] in task_list):
                    path_time=self.mla_star(pair["agent"]["pos"],pair["debri"]["pos"],math.inf)
                    if(path_time==None):
                        continue
                    task={"agent":pair["agent"],"debri":pair["debri"],"path":path_time}
                    self.ongoing_tasks.append(task)
                    agent_list.remove(pair["agent"])
                    task_list.remove(pair["debri"])
            self.time_step=self.time_step+1
        while(len(self.ongoing_tasks)!=0):
            expired=[]
            for i in self.ongoing_tasks:
                position=i["path"].pop(0)
                if(self.debris[i["debri"]["index"]]==self.robot_positions[i["agent"]["index"]]):
                    self.debris[i["debri"]["index"]]=position
                self.robot_positions[i["agent"]["index"]]=position 
                if(len(i["path"])==0):
                    expired.append(i)
            for i in expired:
                self.ongoing_tasks.remove(i)
                i["agent"]["pos"]=self.robot_positions[i["agent"]["index"]]
                agent_list.append(i["agent"])
            self.show()
            self.time_step=self.time_step+1
             
    def simulate(self):
        self.time_step=0
        task_list=[{"index":i,"pos":x} for i,x in enumerate(self.debris)]
        agent_list=[{"index":i,"pos":x} for i,x in enumerate(self.robot_positions)]
        self.ongoing_tasks=[]
        print("Tasks:")
        for i in task_list:
            print(i)
        print("Robots:")
        for i in agent_list:
            print(i)
        self.task_allocation(task_list,agent_list)

if __name__== "__main__":
    arena=Beach()
    arena.simulate()    

import random
import copy
import math

class beach :
    
    def __init__(self):
        self.size=10
        self.robot_count=5
        self.collection_point=(0,0)
        self.debri_count=5
        self.debris=random.sample([[(x,y) for y in range(10)] for x in range(10)],self.debri_count)
        self.robot_positions=random.sample([[(x,y) for y in range(10)] for x in range(10)],self.robot_count)
    
    def show(self):
        pass
    
    def mla_star(self,robot_pos,debri_pos,t_max):
        pass
    
    def create_pairs(self,task_list,agent_list):
        pairs=[]
        for t in task_list:
            for a in agent_list:
                heuristic=abs(t["pos"][0]-a["pos"][0])+abs(t["pos"][1]-agent_list["pos"][1])#add distance to collection
                pair={"debri":t,"agent":a,"h":heuristic}
                pairs.append(pair)
        pairs.sort(key=lambda x:x["h"])
        return pairs
    
    def move_idle_agent(agent_list,a):
        pass

    def task_allocation(self,task_list,agent_list):
        while len(task_list)!=0:
            for i in self.ongoing_tasks:
                position=i["path"].pop(0)
                if(len(i["path"])==0):
                    print(f"Debri {i["debri"]["index"]} cleaned by agent {i["agent"]["index"]}")
                    self.ongoing_task.remove(i)
                    task_list.append(i["agent"])
                if(self.debris[i["debri"]["index"]]==self.robot_positions[i["agent"]["index"]]):
                    self.debris[i["debri"]["index"]]=position
                self.robot_positions[i["agent"]["index"]]=position  
            self.show()
            pairs=self.create_pairs(task_list,agent_list)
            for pair in pairs:
                if(pair["agent"] in agent_list and pair["task"] in task_list):
                    path_time=self.mla_star(pair["agent"]["pos"],pair["task"]["pos"],math.inf)
                    task={"agent":pair["agent"],"debri":pair["debri"],"path":path_time}
                    self.ongoing_tasks.append(task)
                    agent_list.pop(pair["agent"])
                    task_list.remove(pair["task"])
            for a in agent_list.index:
                if agent_list[a] in task_list :
                    self.move_idle_agent(agent_list,a)
            self.time_step=self.time_step+1
             
    def simulate(self):
        self.time_step=0
        task_list=[{"index":i,"pos":x} for i,x in enumerate(self.debris)]
        agent_list=[{"index":i,"pos":x} for i,x in enumerate(self.robot_positions)]
        self.ongoing_task=[]
        self.task_allocation()


#the path collision of robots is checked in the task allocation algorithm where it will 
#reject the pair if it is colloiding with another already assigned path.
#ongoing_task=[list of paths of each robot]
#each path in ongoing_task will have the top position popped out at each iteration such that the new 
#location of the robot is the top position at each iteration
#for idle robots, check if its location is any of the paths ka next location or is in the path of
#any moving robot
#also add the robots who have finished their tasks to the agent_list at the end of the iteration
#


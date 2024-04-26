import random
import copy

class beach :
    def __init__(self):
        self.size=10
        self.robot_count=5
        self.collection_point=(0,0)
        self.debris=[]
        self.robot_positions=random.sample([[(x,y) for y in range(10)] for x in range(10)],self.robot_count)
    def show(self):
        pass
    def mla_star(self,pair):
        pass
    def create_pairs(self,task_list,agent_list):
        pairs=[]
        for t in task_list:
            for a in agent_list.index():
                heuristic=abs(t[0]-agent_list[a][0])+abs(t[1]-agent_list[a][1])#add distance to collection
                pair={"task":t,"agent":a,"h":heuristic}
                pairs.append(pair)
        pairs.sort(key=lambda x:x["h"])
        return pairs

    def task_allocation(self,task_list,agent_list):
        ongoing_tasks=[]
        while len(task_list)!=0:
            pairs=self.create_pairs(task_list,agent_list)
            for pair in pairs:
                if(pair["agent"] in agent_list.index() and pair["task"] in task_list):
                    path_time=self.mla_star(pair)
                    ongoing_tasks.append(path_time)
                    agent_list.pop(pair["agent"])
                    task_list.remove(pair["task"])
            for a in agent_list.index:
                pass

            
        
    def simulate(self):
        self.time_step=0
        task_list=copy.deepcopy(self.debris)
        agent_list={f"agent{i}":x for i,x in enumerate(self.robot_positions)}

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


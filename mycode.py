import random

class arena:
    def __init__(self,size,robot_count,collection_point,debris,obstacles):
        self.size=size
        self.robot_count=robot_count
        self.collection_point=collection_point
        self.debris=debris
        self.obstacles=obstacles
        self.robot_positions=random.sample([[(x,y) for y in range(10)] for x in range(10)],len(robot_count))
    def show():
        pass

def ACO():
    pass


def main():
    arena_size=10
    robot_count=5
    collection_point=(0,0)
    debris=[(7,1),(8,1),(7,2),(8,2),(8,3),(2,3),(3,3),(4,3),(2,4),(3,4),(4,4),(4,5),(0,7),(0,8),(0,9),(1,7),(1,8),(1,9),(8,7),(9,7),(8,8),(9,8),(9,9)]
    obstacles=[(1,1),(0,1),(1,0)]
    myarena=arena(arena_size,robot_count,collection_point,debris,obstacles)

if __name__=="main":
    main()

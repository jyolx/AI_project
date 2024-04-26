# Define world parameters (replace with actual values)
import random
world_size = 100  # Size of the cleaning area
num_robots = 10  # Number of robots in the swarm
debris_locations = [(20, 30), (50, 70)]  # Example debris locations
collection_point = (0, 0)  # Designated collection point
obstacles = [(60, 40)]  # Example obstacle location

# Initialize pheromone grid (all values set to a small starting value)
pheromone_grid = [[0.1 for _ in range(world_size)] for _ in range(world_size)]

# Function to calculate desirability based on debris and obstacles
def desirability(pos):
  # Increase desirability for debris locations
  if pos in debris_locations:
    return 2.0
  # Decrease desirability near obstacles
  for obstacle in obstacles:
    if abs(pos[0] - obstacle[0]) <= 3 or abs(pos[1] - obstacle[1]) <= 3:
      return 0.5
  return 1.0  # Neutral desirability for empty space

# Function for the central system to assign tasks (chooses next move with highest desirability + pheromone)
def assign_task(robot_pos):
  # Get neighboring locations
  neighbors = [(robot_pos[0] + dx, robot_pos[1] + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
  # Filter out-of-bounds and obstacle locations
  neighbors = [n for n in neighbors if 0 <= n[0] < world_size and 0 <= n[1] < world_size and n not in obstacles]
  
  # Calculate desirability and pheromone sum for each neighbor
  desirability_sum = [desirability(n) + pheromone_grid[n[0]][n[1]] for n in neighbors]
  
  # Choose neighbor with highest desirability + pheromone value
  next_move_index = desirability_sum.index(max(desirability_sum))
  return neighbors[next_move_index]

# Main loop (multiple iterations for continuous operation)
for _ in range(100):
  # Central system assigns tasks (determines next move for each robot)
  robot_tasks = [assign_task(robot_pos) for robot_pos in [(random.randint(0, world_size-1), random.randint(0, world_size-1)) for _ in range(num_robots)]]
  
  # Simulate robot movement based on assigned tasks
  for robot_id, task in enumerate(robot_tasks):
    robot_pos = robot_tasks[robot_id]
    # Check if debris is found
    if robot_pos in debris_locations:
      debris_locations.remove(robot_pos)  # Remove collected debris
      # Update pheromone grid (increase desirability of debris area)
      pheromone_grid[robot_pos[0]][robot_pos[1]] += 1.0
    # Check if at collection point
    if robot_pos == collection_point:
      continue
    
    # Update pheromone grid on robot's path (avoid obstacles)
    pheromone_grid[robot_pos[0]][robot_pos[1]] += 0.2  # Deposit pheromone

  # Evaporate pheromone over time (avoid getting stuck on old paths)
  for i in range(world_size):
    for j in range(world_size):
      pheromone_grid[i][j] *= 0.9  # Reduce pheromone by 10%

# Print final pheromone grid (higher values indicate desirable paths)
print(pheromone_grid)

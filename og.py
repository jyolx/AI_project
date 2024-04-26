# Define world parameters (replace with actual values)
import random
world_size = 10  # Size of the cleaning area
num_robots = 10  # Number of robots in the swarm
debris_locations = [(20, 30), (50, 70)]  # Example debris locations
collection_point = (0, 0)  # Designated collection point
obstacles = [(60, 40)]  # Example obstacle location

# Initialize pheromone grid (all values set to a small starting value)
pheromone_grid = [[0.1 for _ in range(world_size)] for _ in range(world_size)]

# Function for a robot to move (random exploration with pheromone influence)
def move_robot(robot_pos):
  # Get neighboring locations
  neighbors = [(robot_pos[0] + dx, robot_pos[1] + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
  # Filter out-of-bounds and obstacle locations
  neighbors = [n for n in neighbors if 0 <= n[0] < world_size and 0 <= n[1] < world_size and n not in obstacles]
  
  # Calculate probability of moving to each neighbor (higher pheromone = higher probability)
  total_pheromone = sum(pheromone_grid[n[0]][n[1]] for n in neighbors)
  probs = [pheromone_grid[n[0]][n[1]] / total_pheromone for n in neighbors]
  
  # Introduce randomness for exploration
  probs = [p * 0.8 + 0.1 for p in probs]  # 80% weight on pheromone, 20% on randomness

  # Choose next move based on probability distribution
  next_move = random.choices(neighbors, weights=probs)[0]
  return next_move

# Main loop (multiple iterations for continuous operation)
for _ in range(100):
  # Simulate robot movement
  for robot_id in range(num_robots):
    robot_pos = (random.randint(0, world_size-1), random.randint(0, world_size-1))  # Random starting position
    while True:
      # Check if debris is found
      if robot_pos in debris_locations:
        debris_locations.remove(robot_pos)  # Remove collected debris
        # Update pheromone grid (increase desirability of debris area)
        pheromone_grid[robot_pos[0]][robot_pos[1]] += 1.0
        break
      # Check if at collection point
      if robot_pos == collection_point:
        break
      
      # Move robot and update pheromone grid (avoid obstacles)
      new_pos = move_robot(robot_pos)
      pheromone_grid[robot_pos[0]][robot_pos[1]] += 0.2  # Deposit pheromone on path
      robot_pos = new_pos
  
  # Evaporate pheromone over time (avoid getting stuck on old paths)
  for i in range(world_size):
    for j in range(world_size):
      pheromone_grid[i][j] *= 0.9  # Reduce pheromone by 10%

# Print final pheromone grid (higher values indicate desirable paths)
print(pheromone_grid)

<h1>Robot Swarm Scheduling - Beach Cleanup Scenario</h1>

<h2>Overview</h2>
<p>This project implements an AI-driven multi-agent system for autonomous debris collection on a simulated beach environment. The robots use an optimized path-planning strategy of <strong>Multi-Level A*</strong> (MLA*), ensuring efficient debris collection and transportation to a central collection point.</p>

<h2>Features</h2>
<ul>
  <li><strong>Multi-Agent Task Allocation:</strong> Assigns debris collection tasks to available robots dynamically.</li>
  <li><strong>Path Planning with MLA*:</strong> Implements an enhanced A* search with multiple levels to optimize robot movement.</li>
  <li><strong>Obstacle Avoidance:</strong> Ensures robots navigate without colliding with ongoing tasks.</li>
  <li><strong>Dynamic Task Handling:</strong> Robots continuously receive and execute new tasks as the simulation progresses.</li>
  <li><strong>Visualization:</strong> Displays a grid-based map of the environment, including robots, debris, and the collection point.</li>
</ul>

<h2>Research Paper Inspiration</h2>
<p>The algorithm is inspired by the research paper: <a href="https://www.andrew.cmu.edu/user/vanhoeve/papers/MAPD_ICAPS_2019.pdf" target="_blank"><strong>A Multi-Label A* Algorithm for Multi-Agent Pathfinding</strong></a>, which explores efficient task allocation and path planning in multi-agent environments. Our implementation adapts these principles to a real-world scenario of autonomous beach cleanup.</p>

<h2>Installation & Usage</h2>

<h3>Prerequisites</h3>
<ul>
  <li>Python 3.x</li>
  <li>Required libraries: <code>heapq</code>, <code>random</code>, <code>math</code>, <code>copy</code></li>
</ul>

<h3>Running the Simulation</h3>
<p>Clone the repository and run the script:</p>

<pre><code>
git clone https://github.com/yourusername/beach-cleanup-ai.git
cd beach-cleanup-ai
python beach_cleanup.py
</code></pre>

<h2>Code Structure</h2>

<pre><code>
📂 beach-cleanup-ai
│-- 📜 beach_cleanup.py   # Main simulation script
│-- 📜 README.md          # Project documentation
</code></pre>

<h2>Algorithm Explanation</h2>

<h3>Multi-Label A* Algorithm</h3>
<ul>
  <li><strong>Initialization:</strong>
    <ul>
      <li>The search starts from the agent’s current location.</li>
      <li>An initial node is added to a queue.</li>
    </ul>
  </li>
  <li><strong>Search Process:</strong>
    <ul>
      <li>Nodes are expanded based on their cost values.</li>
      <li>If a node reaches the maximum allowed time step, it is discarded.</li>
      <li>The algorithm operates in multiple <strong>levels</strong>:
        <ul>
          <li><strong>Level 1:</strong> The agent is searching for a task.</li>
          <li><strong>Level 2:</strong> The agent is executing the assigned task.</li>
        </ul>
      </li>
      <li>Once the agent reaches the goal location in Level 2, the path is returned.</li>
      <li>If no valid path is found, the algorithm terminates with failure.</li>
    </ul>
  </li>
</ul>

<h3>Task Assignment Procedure</h3>
<ul>
  <li><strong>Time-Stepped Execution:</strong>
    <ul>
      <li>The process runs iteratively, updating at each time step.</li>
    </ul>
  </li>
  <li><strong>At each time step:</strong>
    <ul>
      <li>Identify available agents and newly released tasks.</li>
      <li>Form agent-task pairs and prioritize them based on a heuristic value, based on <strong>Manhattan distance</strong> .</li>
      <li>Assign tasks if the <strong>Multi-Label A*</strong> algorithm successfully finds a path.</li>
      <li>Update agent paths accordingly and remove assigned tasks from the pool.</li>
    </ul>
  </li>
  <li><strong>Completion:</strong>
    <ul>
      <li>The loop continues until all tasks are assigned, returning the final solution.</li>
    </ul>
  </li>
</ul>

<h2>Example Output</h2>


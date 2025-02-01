<h1>Robot Swarm Scheduling - Beach Cleanup Scenario</h1>

<h2>Overview</h2>
<p>This project implements an AI-driven multi-agent system for autonomous debris collection on a simulated beach environment. The robots use an optimized path-planning strategy inspired by a research paper on <strong>Multi-Level A*</strong> (MLA*), ensuring efficient debris collection and transportation to a central collection point.</p>

<h2>Features</h2>
<ul>
  <li><strong>Multi-Agent Task Allocation:</strong> Assigns debris collection tasks to available robots dynamically.</li>
  <li><strong>Path Planning with MLA*:</strong> Implements an enhanced A* search with multiple levels to optimize robot movement.</li>
  <li><strong>Obstacle Avoidance:</strong> Ensures robots navigate without colliding with ongoing tasks.</li>
  <li><strong>Dynamic Task Handling:</strong> Robots continuously receive and execute new tasks as the simulation progresses.</li>
  <li><strong>Visualization:</strong> Displays a grid-based map of the environment, including robots, debris, and the collection point.</li>
</ul>

<h2>Research Paper Inspiration</h2>
<p>The algorithm is inspired by <strong>[Title of Research Paper]</strong> by <strong>[Author(s) Name]</strong>, which explores efficient task allocation and path planning in multi-agent environments. Our implementation adapts these principles to a real-world scenario of autonomous beach cleanup.</p>

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
│-- 📜 README.md         # Project documentation
</code></pre>

<h2>Algorithm Explanation</h2>

<h3>Multi-Level A* (MLA*) Path Planning</h3>
<p>The robots use <strong>MLA*</strong> to navigate efficiently:</p>
<ol>
  <li><strong>Task Selection:</strong> The closest robot is assigned a debris pickup task.</li>
  <li><strong>Path Computation:</strong>
    <ul>
      <li>Level 1: Path to the debris.</li>
      <li>Level 2: Path from debris to collection point.</li>
    </ul>
  </li>
  <li><strong>Obstacle Handling:</strong> The algorithm ensures robots don’t interfere with each other's paths.</li>
</ol>

<h3>Task Allocation Strategy</h3>
<ul>
  <li>Robots are paired with debris based on the shortest distance.</li>
  <li>Ongoing tasks are continuously updated, ensuring idle robots get assigned new tasks.</li>
</ul>

<h2>Example Output</h2>


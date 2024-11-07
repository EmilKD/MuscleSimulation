
---

# Rigid-Tendon Musculotendon Model Simulation

This repository contains a simulation of a simplified Rigid-Tendon musculotendon model, demonstrating the dynamics of muscle force application on a two-link system with a rotating joint. The muscle connects to the middle of the second link and influences its motion through generated torque.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Simulation Details](#simulation-details)
  - [Musculotendon Model](#musculotendon-model)
  - [Simulation Dynamics](#simulation-dynamics)
- [Visualization](#visualization)
- [Contributing](#contributing)
- [License](#license)

## Overview
This project simulates a two-link system where a muscle-tendon unit exerts force on a rotating link. The dynamics follow a Rigid-Tendon model, and the simulation visualizes how the muscle force drives motion through a connected joint. The model is inspired by computational biomechanics techniques outlined in **"Flexing Computational Muscle: Modeling and Simulation of Musculotendon Dynamics"** by Millard et al.

## Features
- Simulates muscle force generation using a Rigid-Tendon musculotendon model.
- Visualizes the dynamics of a two-link system influenced by muscle force.
- Plots muscle force, joint angles, angular velocities, and muscle-tendon lengths over time.
- Animation of the two-link system's motion with a muscle attached to the middle of the rotating link.

## Installation
To use this simulation, ensure you have Python installed along with the following dependencies:
- `numpy`
- `matplotlib`

Install the dependencies using pip:
```bash
pip install numpy matplotlib
```

## Usage
1. Clone or download this repository.
2. Run the simulation using the command:
   ```bash
   python RigidTendonModel.py
   ```
3. The script will simulate the dynamics and display plots of the key parameters over time. An animated visualization of the two-link system with the muscle will also be shown.

## Simulation Details

### Musculotendon Model
The muscle force is computed based on a Rigid-Tendon model with considerations for:
- Optimal fiber length
- Maximum isometric force
- Pennation angle at optimal length
- Tendon slack length
- Velocity-dependent force scaling

The model uses functions for force-length and force-velocity relationships to simulate realistic muscle dynamics.

### Simulation Dynamics
The simulation solves for the joint's motion using Newton-Euler dynamics, with the muscle force generating torque that influences the second link's motion. Damping and joint limits are included to model realistic joint constraints.

### Key Parameters
- **`OptimalFiberLength`**: Optimal muscle fiber length.
- **`MaximumForce`**: Maximum isometric force.
- **`link_length`**: Length of the simulated links.
- **`dt`**: Time step for the simulation.

## Visualization
The simulation generates plots of:
- Joint angle over time
- Angular velocity over time
- Muscle force over time
- Muscle-tendon length over time

Additionally, an animated visualization shows the two-link system with a muscle connecting the middle of the rotating link to the fixed base link.

## Contributing
Contributions to improve or extend this simulation are welcome. Feel free to submit issues or pull requests.

## License
This project is open-source and available under the [MIT License](LICENSE).

---

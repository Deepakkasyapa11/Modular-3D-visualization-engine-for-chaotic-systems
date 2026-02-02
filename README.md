# 3D Dynamical Systems Visualizer

A modular Python-based engine designed to simulate and animate complex 3D mathematical systems. This implementation specifically focuses on the **Lorenz Attractor**, demonstrating high-performance coordinate calculation and real-time perspective interpolation.

# Engineering Highlights<img width="318" height="306" alt="Screenshot (138)" src="https://github.com/user-attachments/assets/cac38a76-dbda-49fb-a20b-912eb5e4426b" />


* **Modular Architecture:** Separates the physics engine (`generator.py`) from the rendering layer (`renderer.py`), following clean code principles and decoupling logic from UI.
* **Vectorized Computation:** Utilizes `NumPy` for pre-allocating memory and vectorized coordinate generation, ensuring $O(n)$ complexity for data preparation.
* **Dynamic View Interpolation:** Implements automated camera rotation within the `FuncAnimation` loop to provide a multi-perspective view of 3D spatial data.
* **Zero-Overhead Rendering:** Uses Matplotlib's `Artist` animation method to update only the modified line segments rather than re-rendering the entire canvas.
<img width="593" height="362" alt="Screenshot (139)" src="https://github.com/user-attachments/assets/374f65a9-04d5-472b-b1b7-ad0c5820ad15" />

# Directory Structure

```text
3d-viz-engine/
├── core/
│   ├── __init__.py      # Package initialization
│   ├── generator.py     # Physics & Math Logic
│   └── renderer.py      # Matplotlib Artist Logic
├── assets/              # Performance captures & GIFs
├── main.py              # Application Entry Point
├── .gitignore           # Version control exclusions
└── requirements.txt     # Dependency Manifest

**Technical StackLanguage:** Python 3.9+
Math: NumPy (Vectorized arrays)
Visualization: Matplotlib (3D Toolkit)
Animation: FuncAnimation API 
The Math: Lorenz AttractorThe system evolves according to the following differential equations, which model atmospheric convection:$$\frac{dx}{dt} = \sigma(y - x)$$$$\frac{dy}{dt} = x(\rho - z) - y$$$$\frac{dz}{dt} = xy - \beta z$$This project visualizes the "Butterfly Effect," where infinitesimal changes in initial conditions lead to divergent trajectories, demonstrating the beauty of chaotic systems.🔧 Installation & UsageClone the repository:Bashgit clone [https://github.com/your-username/3d-viz-engine.git](https://github.com/your-username/3d-viz-engine.git)

cd 3d-viz-engine

**Setup Environment**: Bashpip install -r requirements.txt
**Execute Simulation:** Bashpython main.py

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from core.generator import get_lorenz_coords

class Animator3D:
    def __init__(self):
        # Using a context manager style for figure creation
        self.fig = plt.figure(figsize=(12, 8), facecolor='black')
        self.ax = self.fig.add_subplot(111, projection='3d', facecolor='black')
        self.x, self.y, self.z = get_lorenz_coords()
        
        self.line, = self.ax.plot([], [], [], color='#00ffee', lw=1, alpha=0.8)
        self._set_style()

    def _set_style(self) -> None:
        self.ax.set_axis_off()
        self.ax.set_xlim(-25, 25)
        self.ax.set_ylim(-35, 35)
        self.ax.set_zlim(5, 55)

    def update(self, i: int):
        # Slicing for animation frames
        self.line.set_data(self.x[:i], self.y[:i])
        self.line.set_3d_properties(self.z[:i])
        self.ax.view_init(elev=10, azim=i*0.5)
        return self.line,

    def start(self) -> None:
        # blit=True is critical for performance
        _ = FuncAnimation(self.fig, self.update, frames=len(self.x), 
                         interval=10, blit=True)
        plt.show()
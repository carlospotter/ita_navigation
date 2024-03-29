# ita_navigation

[![DOI](https://zenodo.org/badge/265566854.svg)](https://zenodo.org/badge/latestdoi/265566854)

Path planning and drone command for AR.Drone. This work is part of the construction of A UAS Traffic Management simulation platform using the Robot Operating System (ROS).

The package requires the [_tum_simulator_](https://github.com/carlospotter/tum_simulator) and the [_pid_control_ardrone_](https://github.com/carlospotter/pid_control_ardrone) packages.

In order to execute the package, the following steps are required:
1. catkin_make the three packages.
2. Run the simulation.launch file in the _ita_navigation_ package.
3. Run the _nav_2d.py_ or _nav_3d.py_ codes in the _ita_navigation_ package for 2D or 3D A* algorithm, respectively.

A Virtual Machine Testbed for _ita_navigation_ is available in the testbed folder.

---
## 2D navigation demo

[![2D navigation demo](https://img.youtube.com/vi/aGxPD6Bk608/0.jpg)](https://www.youtube.com/watch?v=aGxPD6Bk608)



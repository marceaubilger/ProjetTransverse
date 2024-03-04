import math
import matplotlib.pyplot as plt 
import numpy as np


def compute_time_parameters(strength, angle, precision=0.01):
    # Convert angle from degrees to radians
    angle_rad = np.deg2rad(angle)

    # Gravity constant (m/s^2)
    g = 9.81

    # Initial velocity components
    v_initial_y = strength * np.sin(angle_rad)

    # Compute time of flight
    total_time = (2 * v_initial_y) / g

    # Compute number of steps
    num_steps = int(total_time / precision)

    # Compute time interval
    time_interval = total_time / num_steps

    return total_time, time_interval


def trajectory(angle, initial_speed, total_time, time_interval):
    angle_radians = math.radians(angle)
    speed_x = initial_speed * np.cos(angle_radians)
    speed_y = initial_speed * np.sin(angle_radians)
    g = 9.81 #gravity

    #number of intervals of time
    number_of_points = int(total_time / time_interval)

    #initialization of lists to store the x and y coordinates of the trajectory
    pos_x = [0.0]
    pos_y = [0.0]

    #compute the trajectory
    for i in range(1, number_of_points + 1):
        #computation of the new position
        time = i * time_interval
        position_x = speed_x * time
        position_y = speed_y * time - 0.5 * g * time ** 2

        #adding the position to the list
        pos_x.append(position_x)
        pos_y.append(position_y)

        if pos_y[-1] < 0:  # Check if the last element of pos_y is less than 0
            break

    return pos_x, pos_y
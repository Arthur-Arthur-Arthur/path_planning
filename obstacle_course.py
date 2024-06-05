import math
import numpy as np


def distance(pos1: np.ndarray, pos2: np.ndarray):
    return np.sqrt(np.sum(np.square(pos1 - pos2)))


class PathPlanner:

    
    def __init__(self) -> None:
        self.travel_direction=(1,1)
        self.start = True
        pass

    def plan_path(
        self,
        boat_position: np.ndarray,
        red_b_pos: np.ndarray,
        green_b_pos: np.ndarray,
        yellow_b_pos: np.ndarray,
    ):
        # positions are assumed to be in absolute coordiantes (start is 0,0) and stable, processing or this may need to be added
        # initial code will not handle yellows

        if red_b_pos.size == 0 or green_b_pos.size == 0:
            return "No buoys"
        closest_red = np.argmax(
            distance(boat_position, red_b_pos[i, :]) for i in red_b_pos.shape[0]
        )
        closest_green = np.argmax(
            distance(boat_position, red_b_pos[i, :]) for i in green_b_pos.shape[0]
        )
        mid_point = (closest_green + closest_red) / 2
        if True:
            return mid_point #simplest possible algorithm
        if self.start == True:
            self.travel_direction= mid_point #used to determine if gates are forwards in case of flip
            self.start=False
        else:
            return mid_point
        
            


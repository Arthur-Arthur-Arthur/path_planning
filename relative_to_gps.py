import math
import numpy as np
from typing import Tuple


def relative_3d_to_gps(pos_3d: Tuple[float,float,float], source_coord:Tuple[float,float], compass_angle:float):
    pos_2d=pos_3d[:2]
    pos_2d_rotated=pos_2d[0]*math.cos(compass_angle)+pos_2d[1]*math.sin(compass_angle),pos_2d[1]*math.cos(compass_angle)+pos_2d[0]*math.sin(compass_angle)
    latitude=source_coord[0]
    m_per_deg_lat = 111132.954 - 559.822 * math.cos( 2 * latitude ) + 1.175 * math.cos( 4 * latitude)
    m_per_deg_lon = 111132.954 * math.cos ( latitude )
    pos_2d_scaled=pos_2d_rotated[0]/m_per_deg_lat,pos_2d_rotated[1]/m_per_deg_lon
    pos_2d_added=source_coord[0]+pos_2d_scaled[0],source_coord[1]+pos_2d_scaled[1]
    return pos_2d_added

print(relative_3d_to_gps((100_000,0,100),(56.947507,24.081203),math.radians(0)))
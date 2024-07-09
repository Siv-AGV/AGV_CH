import math

def convert_pgv_values(pgv_msg):
    """
    Convert the PGV scanner values from mm to meters and adjust the x and y values 
    based on the AGV orientation and axis directions.

    Args:
        pgv_msg (PGVScan): The message from the PGV scanner with x_position, y_position, and angle in mm and degrees.

    Returns:
        tuple: Converted and adjusted x_position (m), y_position (m), and angle (radians).
    """
    # Convert values from mm to meters
    x_position_m = pgv_msg.x_position / 1000.0
    y_position_m = pgv_msg.y_position / 1000.0

    # Adjust the angle
    if pgv_msg.angle >= 0:
        converted_angle = (pgv_msg.angle + 180) % 360
    else:
        converted_angle = (pgv_msg.angle + 180)
    
    # Convert the adjusted angle to radians
    # angle_rad = math.radians(converted_angle)
    angle_rad = (converted_angle)

    # Correct the x and y positions based on the AGV orientation
    # When the AGV is offset to the right from the center, x increases negatively
    x_position_adjusted = x_position_m
    # When the AGV is offset to the rear from the center, y increases negatively
    y_position_adjusted = -y_position_m

    # Return the adjusted values
    return x_position_adjusted, y_position_adjusted, angle_rad

# Example usage of the function
class PGVScan:
    def __init__(self, x_position, y_position, angle):
        self.x_position = x_position
        self.y_position = y_position
        self.angle = angle

# Example PGVScan message
pgv_msg_example = PGVScan(52, 31, 3)
converted_values = convert_pgv_values(pgv_msg_example)

print(converted_values)

# Example PGVScan message with negative angle
pgv_msg_example_negative = PGVScan(-100, 200, -175)
converted_values_negative = convert_pgv_values(pgv_msg_example_negative)

print(converted_values_negative)

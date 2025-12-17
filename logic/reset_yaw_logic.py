from pybricks.hubs import EV3Brick
from pybricks.parameters import Port
from pybricks.ev3devices import Motor
from pybricks.robotics import DriveBase

# Initialize the EV3 Brick and Motors
ev3 = EV3Brick()
yaw_motor = Motor(Port.A)  # Adjust the port as necessary

def track_satellite(target_angle, current_angle):
    """
    Adjusts the servo to track a satellite while ensuring no cable tangling.
    - target_angle: The desired angle for tracking.
    - current_angle: The current yaw angle.
    """

    # Check if we're exceeding the 180-degree threshold
    if abs(current_angle) >= 180:
        # Reset by moving back to home (anti-clockwise)
        ev3.screen.print("Resetting yaw...")
        yaw_motor.run_target(speed=100, target_angle=0, then=Motor.STOP.HOLD)

    # Track the satellite clockwise if below the threshold
    elif current_angle < target_angle:
        ev3.screen.print("Tracking...")
        yaw_motor.run_angle(speed=100, rotation_angle=target_angle - current_angle)
    else:
        ev3.screen.print("Already in position.")

# Main loop example
current_ang = 0
while True:
    # Simulate reading the current position of the servo
    current_ang = yaw_motor.angle()

    # Define the satellite's target angle (e.g., 90 degrees)
    satellite_target_angle = 90

    # Use the logic to track/reset the yaw movement
    track_satellite(satellite_target_angle, current_ang)

    # Optionally sleep for some time in between updates
    wait(100)
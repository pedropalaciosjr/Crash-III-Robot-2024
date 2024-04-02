class Constants:
    def __init__(self):
        self.LEFT_FRONT_CAN_ID = 1
        self.LEFT_REAR_CAN_ID = 2
        self.RIGHT_FRONT_CAN_ID = 3
        self.RIGHT_REAR_CAN_ID = 4
        self.FEEDER_WHEEL_CAN_ID = 5
        self.LAUNCH_WHEEL_CAN_ID = 6
        self.CLAW_CAN_ID = 7

        self.DIFFERENTIAL_DRIVE_CURRENT = 50
        self.DIFFERENTIAL_AUTONOMOUS_DRIVE_SPEED = 1
        self.DIFFERENTIAL_AUTONOMOUS_ROTATION_SPEED = 1


        self.FEEDER_WHEEL_CURRENT, self.LAUNCH_WHEEL_CURRENT, self.CLAW_CURRENT = (40, 50, 40)
        self.FEEDER_WHEEL_SPEED, self.LAUNCH_WHEEL_SPEED, self.CLAW_SPEED = (0.5, 0.5, 0.5)

        self.CLIMBER_CURRENT, self.CLIMBER_SPEED = (40, 0)

        self.driver_controller_type, self.operator_controller_type = ("PS5", "PS5")


    
    def autonomous_constants(self):
        pass
        

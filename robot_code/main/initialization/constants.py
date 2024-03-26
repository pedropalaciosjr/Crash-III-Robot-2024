class Constants:
    def __init__(self):
        global LEFT_FRONT_CAN_ID, LEFT_REAR_CAN_ID, RIGHT_FRONT_CAN_ID, RIGHT_REAR_CAN_ID
        global ARM_LEFT_CAN_ID, ARM_RIGHT_CAN_ID, SHOOTER_LEFT_CAN_ID, SHOOTER_RIGHT_CAN_ID, INTAKE_CAN_ID, CLIMBER_CAN_ID
        global DIFFERENTIAL_DRIVE_CURRENT, DIFFERENTIAL_AUTONOMOUS_DRIVE_SPEED, DIFFERENTIAL_AUTONOMOUS_ROTATION_SPEED
        global ARM_LEFT_CURRENT, ARM_RIGHT_CURRENT, SHOOTER_LEFT_CURRENT, SHOOTER_RIGHT_CURRENT, INTAKE_CURRENT
        global ARM_LEFT_SPEED, ARM_RIGHT_SPEED, SHOOTER_LEFT_SPEED, SHOOTER_RIGHT_SPEED, INTAKE_SPEED, INTAKE_REVERSE_SPEED

        global CLIMBER_CURRENT, CLIMBER_SPEED
        global LEFT_FRONT_SPEED, RIGHT_FRONT_SPEED

        global driver_controller_type, operator_controller_type

        self.LEFT_FRONT_CAN_ID = 1
        self.LEFT_REAR_CAN_ID = 2
        self.RIGHT_FRONT_CAN_ID = 3
        self.RIGHT_REAR_CAN_ID = 4
        self.ARM_LEFT_CAN_ID = 5
        self.ARM_RIGHT_CAN_ID = 6
        self.SHOOTER_LEFT_CAN_ID = 7
        self.SHOOTER_RIGHT_CAN_ID = 8
        self.INTAKE_CAN_ID = 9
        self.CLIMBER_CAN_ID = 10

        self.DIFFERENTIAL_DRIVE_CURRENT = 50
        self.DIFFERENTIAL_AUTONOMOUS_DRIVE_SPEED = 1
        self.DIFFERENTIAL_AUTONOMOUS_ROTATION_SPEED = 1


        self.ARM_CURRENT, self.SHOOTER_CURRENT, self.INTAKE_CURRENT = (40, 40, 40)
        self.ARM_SPEED, self.SHOOTER_SPEED, self.INTAKE_SPEED = (0, 1, 0.25)
        self.INTAKE_REVERSE_SPEED = -self.INTAKE_SPEED 

        self.CLIMBER_CURRENT, self.CLIMBER_SPEED = (40, 0)

        self.driver_controller_type, self.operator_controller_type = ("PS4", "Xbox")


    
    def autonomous_constants(self):
        pass
        

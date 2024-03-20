class Constants():
    def robot_base_constants(self):
        global LEFT_FRONT_CAN_ID, LEFT_REAR_CAN_ID, RIGHT_FRONT_CAN_ID, RIGHT_REAR_CAN_ID
        global ARM_LEFT_CAN_ID, ARM_RIGHT_CAN_ID, SHOOTER_LEFT_CAN_ID, SHOOTER_RIGHT_CAN_ID, INTAKE_CAN_ID, CLIMBER_CAN_ID
        global DIFFERENTIAL_DRIVE_CURRENT, DIFFERENTIAL_AUTONOMOUS_DRIVE_SPEED
        global ARM_LEFT_CURRENT, ARM_RIGHT_CURRENT, SHOOTER_LEFT_CURRENT, SHOOTER_RIGHT_CURRENT, INTAKE_CURRENT
        global ARM_LEFT_SPEED, ARM_RIGHT_SPEED, SHOOTER_LEFT_SPEED, SHOOTER_RIGHT_SPEED, INTAKE_SPEED

        global CLIMBER_CURRENT, CLIMBER_SPEED
        global LEFT_FRONT_SPEED, RIGHT_FRONT_SPEED

        global driver_controller_type, operator_controller_type

        LEFT_FRONT_CAN_ID = 1
        LEFT_REAR_CAN_ID = 2
        RIGHT_FRONT_CAN_ID = 3
        RIGHT_REAR_CAN_ID = 4
        ARM_LEFT_CAN_ID = 5
        ARM_RIGHT_CAN_ID = 6
        SHOOTER_LEFT_CAN_ID = 7
        SHOOTER_RIGHT_CAN_ID = 8
        INTAKE_CAN_ID = 9
        CLIMBER_CAN_ID = 10

        DIFFERENTIAL_DRIVE_CURRENT = 100
        DIFFERENTIAL_AUTONOMOUS_DRIVE_SPEED = 1


        ARM_LEFT_CURRENT, ARM_RIGHT_CURRENT, SHOOTER_LEFT_CURRENT, SHOOTER_RIGHT_CURRENT, INTAKE_CURRENT = (100, 100, 100, 100, 100)
        ARM_LEFT_SPEED, ARM_RIGHT_SPEED, SHOOTER_LEFT_SPEED, SHOOTER_RIGHT_SPEED, INTAKE_SPEED = (1, 1, 1, 1, 1)

        CLIMBER_CURRENT, CLIMBER_SPEED = (100, 0)

        driver_controller_type, operator_controller_type = ("PS4", "PS4")


    
    def autonomous_constants(self):
        global AUTONOMOUS_MODE
        AUTONOMOUS_MODE = "null"

        

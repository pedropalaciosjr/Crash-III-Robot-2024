from wpilib import (drive, SmartDashboard, Timer)
from rev import (CANSparkMax, CANSparkBase, MotorType)
import constants

class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        def robot_base():
            const = constants.Constants

            LEFT_FRONT, LEFT_REAR = CANSparkMax(const.LEFT_FRONT_CAN_ID, MotorType.kBrushless), CANSparkMax(const.LEFT_REAR_CAN_ID, MotorType.kBrushless)
            RIGHT_FRONT, RIGHT_REAR = CANSparkMax(const.RIGHT_FRONT_CAN_ID, MotorType.kBrushless), CANSparkMax(const.RIGHT_REAR_CAN_ID, MotorType.kBrushless)

            LAUNCH_WHEEL, FEEDER_WHEEL, ROLLER_CLAW = CANSparkMax(const.LAUNCH_WHEEL_CAN_ID, MotorType.kBrushless), CANSparkMax(const.FEEDER_WHEEL_CAN_ID, MotorType.kBrushless),\
                CANSparkMax(const.ROLLER_CLAW_CAN_ID, MotorType.kBrushless)
            CLIMBER = CANSparkMax(const.CLIMBER_CAN_ID, MotorType.kBrushless)

            LEFT_FRONT.CANSparkBase.setSmartCurrentLimit(const.DIFFERENTIAL_DRIVE_CURRENT)
            LEFT_REAR.CANSparkBase.setSmartCurrentLimit(const.DIFFERENTIAL_DRIVE_CURRENT)
            RIGHT_FRONT.CANSparkBase.setSmartCurrentLimit(const.DIFFERENTIAL_DRIVE_CURRENT)
            RIGHT_REAR.CANSparkBase.setSmartCurrentLimit(const.DIFFERENTIAL_DRIVE_CURRENT)

            LAUNCH_WHEEL.CANSparkBase.setSmartCurrentLimit(const.LAUNCH_WHEEL_CURRENT)
            FEEDER_WHEEL.CANSparkBase.setSmartCurrentLimit(const.FEEDER_WHEEL_CURRENT)
            ROLLER_CLAW.CANSparkBase.setSmartCurrentLimit(const.ROLLER_CLAW_CURRENT)

            CLIMBER.CANSparkBase.setSmartCurrentLimit(const.CLIMBER_CURRENT)

            LEFT_REAR.CANSparkBase.follow(LEFT_FRONT)
            RIGHT_REAR.CANSparkBase.follow(RIGHT_FRONT)

            LEFT_FRONT.CANSparkBase.burnFlash()
            LEFT_REAR.CANSparkBase.burnFlash()
            RIGHT_FRONT.CANSparkBase.burnFlash()
            RIGHT_REAR.CANSparkBase.burnFlash()
            LAUNCH_WHEEL.CANSparkBase.burnFlash()
            FEEDER_WHEEL.CANSparkBase.burnFlash()
            ROLLER_CLAW.CANSparkBase.burnFlash()
            CLIMBER.CANSparkBase.burnFlash()
        
        def joystick_init(driver_controller_type, operator_controller_type):
            self.driver_joystick = wpilib.PS4Controller(0) if (driver_controller_type) == "PS4" else (wpilib.Joystick(0))
            self.operator_joystick = wpilib.PS4Controller(1) if (operator_controller_type) == "PS4" else (wpilib.Joystick(1))



        robot_base()
        joystick_init("PS4", "PS4")

    def robotPeriodic(self):
        current_time = Timer.getFPGATimestamp()
        SmartDashboard.putNumber("Current runtime for robot (s):", current_time)



    def teleopPeriodic(self):
        pass

    def autonomousInit(self):
        global autonomous_start
        autonomous_start = Timer.getFPGATimestamp()
    
    def autonomousPeriodic(self):
        # Autonomous primary commands
        autonomous_periodic = Timer.getFPGATimestamp()
        time_elapsed = lambda final, init : final - init

        time_elapsed = time_elapsed(autonomous_periodic, autonomous_start)


        pass
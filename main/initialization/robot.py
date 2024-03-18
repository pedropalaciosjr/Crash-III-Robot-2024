from wpilib import (
    drive,
    SmartDashboard,
    Timer,
    TimedRobot,
    PS4Controller,
    Joystick,
    MotorControllerGroup)
from rev import (CANSparkMax, CANSparkBase, MotorType)
import constants

class MyRobot(TimedRobot):

    def __robotInit__(self):
        def robot_base():
            const = constants.Constants

            LEFT_FRONT, LEFT_REAR = CANSparkMax(const.LEFT_FRONT_CAN_ID, MotorType.kBrushless), CANSparkMax(const.LEFT_REAR_CAN_ID, MotorType.kBrushless)
            RIGHT_FRONT, RIGHT_REAR = CANSparkMax(const.RIGHT_FRONT_CAN_ID, MotorType.kBrushless), CANSparkMax(const.RIGHT_REAR_CAN_ID, MotorType.kBrushless)

            LAUNCH_WHEEL, FEEDER_WHEEL, ROLLER_CLAW = CANSparkMax(const.LAUNCH_WHEEL_CAN_ID, MotorType.kBrushless), CANSparkMax(const.FEEDER_WHEEL_CAN_ID, MotorType.kBrushless),\
                CANSparkMax(const.ROLLER_CLAW_CAN_ID, MotorType.kBrushless)
            CLIMBER = CANSparkMax(const.CLIMBER_CAN_ID, MotorType.kBrushless)

            LEFT = drive.MotorControllerGroup(LEFT_FRONT, LEFT_REAR)
            RIGHT = drive.MotorControllerGroup(RIGHT_FRONT, RIGHT_REAR)
            
            DIFFERENTIAL_DRIVE = drive.DifferentialDrive(LEFT, RIGHT)

            LEFT_FRONT.setInverted(False)
            RIGHT_FRONT.setInverted(False)
    
            LEFT_FRONT.setSmartCurrentLimit(const.DIFFERENTIAL_DRIVE_CURRENT)
            LEFT_REAR.setSmartCurrentLimit(const.DIFFERENTIAL_DRIVE_CURRENT)
            RIGHT_FRONT.setSmartCurrentLimit(const.DIFFERENTIAL_DRIVE_CURRENT)
            RIGHT_REAR.setSmartCurrentLimit(const.DIFFERENTIAL_DRIVE_CURRENT)

            LAUNCH_WHEEL.setSmartCurrentLimit(const.LAUNCH_WHEEL_CURRENT)
            FEEDER_WHEEL.setSmartCurrentLimit(const.FEEDER_WHEEL_CURRENT)
            ROLLER_CLAW.setSmartCurrentLimit(const.ROLLER_CLAW_CURRENT)

            CLIMBER.setSmartCurrentLimit(const.CLIMBER_CURRENT)

            LEFT_REAR.follow(LEFT_FRONT, bool=False)
            RIGHT_REAR.follow(RIGHT_FRONT, bool=False)

            LEFT_FRONT.burnFlash()
            LEFT_REAR.burnFlash()
            RIGHT_FRONT.burnFlash()
            RIGHT_REAR.burnFlash()
            LAUNCH_WHEEL.burnFlash()
            FEEDER_WHEEL.burnFlash()
            ROLLER_CLAW.burnFlash()
            CLIMBER.burnFlash()
        
        def joystick_init(driver_controller_type, operator_controller_type):
            self.driver_joystick = PS4Controller(0) if (driver_controller_type) == "PS4" else (Joystick(0))
            self.operator_joystick = PS4Controller(1) if (operator_controller_type) == "PS4" else (Joystick(1))



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
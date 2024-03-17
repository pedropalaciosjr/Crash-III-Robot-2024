import wpilib
import wpilib.drive
from rev import CANSparkMax, CANSparkBase, MotorType

class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        def robot_base():
            LEFT_FRONT, LEFT_REAR = CANSparkMax(1, MotorType.kBrushless), CANSparkMax(2, MotorType.kBrushless)
            RIGHT_FRONT, RIGHT_REAR = CANSparkMax(3, MotorType.kBrushless), CANSparkMax(4, MotorType.kBrushless)

            LAUNCH_WHEEL, FEEDER_WHEEL, ROLLER_CLAW = CANSparkMax(5, MotorType.kBrushless), CANSparkMax(6, MotorType.kBrushless), \
            CANSparkMax(7, MotorType.kBrushless)
            CLIMBER = CANSparkMax(8, MotorType.kBrushless)

            DIFFERENTIAL_DRIVE_CURRENT = 100
            LAUNCH_WHEEL_CURRENT, FEEDER_WHEEL_CURRENT, ROLLER_CLAW_CURRENT = 145, 145, 100
            CLIMBER_CURRENT = 100

            LEFT_FRONT.CANSparkBase.setSmartCurrentLimit(DIFFERENTIAL_DRIVE_CURRENT)
            LEFT_REAR.CANSparkBase.setSmartCurrentLimit(DIFFERENTIAL_DRIVE_CURRENT)
            RIGHT_FRONT.CANSparkBase.setSmartCurrentLimit(DIFFERENTIAL_DRIVE_CURRENT)
            RIGHT_REAR.CANSparkBase.setSmartCurrentLimit(DIFFERENTIAL_DRIVE_CURRENT)

            LAUNCH_WHEEL.CANSparkBase.setSmartCurrentLimit(LAUNCH_WHEEL_CURRENT)
            FEEDER_WHEEL.CANSparkBase.setSmartCurrentLimit(FEEDER_WHEEL_CURRENT)
            ROLLER_CLAW.CANSparkBase.setSmartCurrentLimit(ROLLER_CLAW_CURRENT)

            CLIMBER.CANSparkBase.setSmartCurrentLimit(CLIMBER_CURRENT)

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
        
        def joystick_init(type1, type2):
            driver_controller_type, operator_controller_type = type1, type2

            self.driver_joystick = wpilib.PS4Controller(0) if (driver_controller_type) == "PS4" else (wpilib.Joystick(0))
            self.operator_joystick = wpilib.PS4Controller(1) if (operator_controller_type) == "PS4" else (wpilib.Joystick(1))

        robot_base()
        joystick_init("PS4", "PS4")


    def teleopPeriodic(self):
        pass

    def autonomousInit(self):
        pass
    
    def autonomousPeriodic(self):
        pass

    
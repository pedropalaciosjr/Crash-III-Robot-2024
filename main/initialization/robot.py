import wpilib
import wpilib.drive
import rev

class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        LEFT_FRONT, LEFT_REAR = rev.CANSparkMax(1, rev.MotorType.kBrushless), rev.CANSparkMax(2, rev.MotorType.kBrushless)
        RIGHT_FRONT, RIGHT_REAR = rev.CANSparkMax(3, rev.Motortype.kBrushless), rev.CANSparkMax(4, rev.MotorType.kBrushless)

        LAUNCH_WHEEL, FEEDER_WHEEL = rev.CANSparkMax(5, rev.MotorType.kBrushless), rev.CANSparkMax(6, rev.MotorType.kBrushless)

        DIFFERENTIAL_DRIVE_CURRENT = 100
        LAUNCH_WHEEL_CURRENT, FEEDER_WHEEL_CURRENT = 145, 145

        



    def teleop_periodic(self):
        pass

    def autonomous_init(self):
        pass
    
    def autonomous_periodic(self):
        pass

    
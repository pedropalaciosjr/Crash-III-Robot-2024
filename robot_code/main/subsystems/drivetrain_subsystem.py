import rev

from wpilib import event, drive, MotorControllerGroup
from ..initialization import constants as const

class DifferentialDriveSubsystem:
    def __init__(self):
        constants_class = const.Constants()
        self.LEFT_FRONT, self.LEFT_REAR = rev.CANSparkMax(constants_class.LEFT_FRONT_CAN_ID, rev.CANSparkLowLevel.MotorType.kBrushless), rev.CANSparkMax(constants_class.LEFT_REAR_CAN_ID, rev.CANSparkLowLevel.MotorType.kBrushless)
        self.RIGHT_FRONT, self.RIGHT_REAR = rev.CANSparkMax(constants_class.RIGHT_FRONT_CAN_ID, rev.CANSparkLowLevel.MotorType.kBrushless), rev.CANSparkMax(constants_class.RIGHT_REAR_CAN_ID, rev.CANSparkLowLevel.MotorType.kBrushless)

            
        self.LEFT_REAR.follow(self.LEFT_FRONT)
        self.RIGHT_REAR.follow(self.RIGHT_FRONT)

        self.LEFT_FRONT.setInverted(True)
        self.RIGHT_FRONT.setInverted(True)
    
        self.LEFT_FRONT.setSmartCurrentLimit(constants_class.DIFFERENTIAL_DRIVE_CURRENT)
        self.LEFT_REAR.setSmartCurrentLimit(constants_class.DIFFERENTIAL_DRIVE_CURRENT)
        self.RIGHT_FRONT.setSmartCurrentLimit(constants_class.DIFFERENTIAL_DRIVE_CURRENT)
        self.RIGHT_REAR.setSmartCurrentLimit(constants_class.DIFFERENTIAL_DRIVE_CURRENT)


        self.LEFT_FRONT.burnFlash()
        self.LEFT_REAR.burnFlash()
        self.RIGHT_FRONT.burnFlash()
        self.RIGHT_REAR.burnFlash()

        self.LEFT = MotorControllerGroup(self.LEFT_FRONT, self.LEFT_REAR)
        self.RIGHT = MotorControllerGroup(self.RIGHT_FRONT, self.RIGHT_REAR)
        self.DIFFERENTIAL_DRIVE = drive.DifferentialDrive(self.LEFT, self.RIGHT)



    def ps4_drive(self, driver_joystick):
        drive.arcadeDrive(driver_joystick.getLeftY(), driver_joystick.getRightX())

    def xbox_logitech_drive(self, driver_joystick):
        self.DIFFERENTIAL_DRIVE.arcadeDrive(driver_joystick.getLeftY(), driver_joystick.getRightX())

    def auto_drive(self, speed, rotation):
        self.DIFFERENTIAL_DRIVE.arcadeDrive(speed, rotation)
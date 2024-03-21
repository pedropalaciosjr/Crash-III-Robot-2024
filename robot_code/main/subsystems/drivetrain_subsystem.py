import rev

from wpilib import event, drive
from ..initialization import constants as const

class DifferentialDriveSubsystem():
    def __init__(self):
        self.LEFT_FRONT, self.LEFT_REAR = rev.CANSparkMax(const.LEFT_FRONT_CAN_ID, rev.MotorType.kBrushless), rev.CANSparkMax(const.LEFT_REAR_CAN_ID, rev.MotorType.kBrushless)
        self.RIGHT_FRONT, self.RIGHT_REAR = rev.CANSparkMax(const.RIGHT_FRONT_CAN_ID, rev.MotorType.kBrushless), rev.CANSparkMax(const.RIGHT_REAR_CAN_ID, rev.MotorType.kBrushless)



        self.LEFT = drive.MotorControllerGroup(self.LEFT_FRONT, self.LEFT_REAR)
        self.RIGHT = drive.MotorControllerGroup(self.RIGHT_FRONT, self.RIGHT_REAR)
            
        self.DIFFERENTIAL_DRIVE = drive.DifferentialDrive(self.LEFT, self.RIGHT)

        self.LEFT_FRONT.setInverted(False)
        self.RIGHT_FRONT.setInverted(False)
    
        self.LEFT_FRONT.setSmartCurrentLimit(const.DIFFERENTIAL_DRIVE_CURRENT)
        self.LEFT_REAR.setSmartCurrentLimit(const.DIFFERENTIAL_DRIVE_CURRENT)
        self.RIGHT_FRONT.setSmartCurrentLimit(const.DIFFERENTIAL_DRIVE_CURRENT)
        self.RIGHT_REAR.setSmartCurrentLimit(const.DIFFERENTIAL_DRIVE_CURRENT)
    
        self.LEFT_REAR.follow(self.LEFT_FRONT, bool=False)
        self.RIGHT_REAR.follow(self.RIGHT_FRONT, bool=False)

        self.LEFT_FRONT.burnFlash()
        self.LEFT_REAR.burnFlash()
        self.RIGHT_FRONT.burnFlash()
        self.RIGHT_REAR.burnFlash()
    def ps4_drive(self, driver_joystick):
        drive.arcadeDrive(driver_joystick.getLeftY(), driver_joystick.getRightX())

    def xbox_logitech_drive(self, driver_joystick):
        drive.arcadeDrive(driver_joystick.getLeftY(), driver_joystick.getRightX())
from wpilib import event, drive, commands2
from ..initialization import constants as const

class DifferentialDriveSubsystem():
    def __init__(self):
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
        drive.arcadeDrive(self.driver_joystick.getLeftY, self.driver_joystick.getRightX)

    def logitech_drive(self, driver_joystick):
        event.BooleanEvent(drive.arcadeDrive(driver_joystick.getLeftX), bool=True)
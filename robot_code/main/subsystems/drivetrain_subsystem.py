from wpilib import event, drive, commands2
from ..initialization import constants

class DifferentialDriveSubsystem():
    def __init__(self):
        pass
    
    def ps4_drive(self, driver_joystick):
        drive.arcadeDrive(self.driver_joystick.getLeftY, self.driver_joystick.getRightX)

    def logitech_drive(self, driver_joystick):
        event.BooleanEvent(drive.arcadeDrive(driver_joystick.getLeftX), bool=True)
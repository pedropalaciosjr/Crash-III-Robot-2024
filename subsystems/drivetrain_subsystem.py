from wpilib import event, drive
from constants import Constants as const

class DifferentialDriveSubsystem():
    def __init__(self):
        pass
    
    def ps4_drive(self):
        event.BooleanEvent(drive.arcadeDrive(self.driver_joystick), )

    def xbox_drive(self):
        event.BooleanEvent(drive.arcadeDrive(self.driver_joystick))
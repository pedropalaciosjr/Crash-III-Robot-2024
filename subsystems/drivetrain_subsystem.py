from wpilib import event, drive
from constants import Constants as const

class DifferentialDriveSubsystem():
    def __init__(self):
        pass
    
    def ps4_drive(self, driver_controller):
        event.BooleanEvent(drive.arcadeDrive(driver_controller.getLeftX), driver_controller.DIFFERENTIAL_DRIVE_SPEED)

    def xbox_drive(self, driver_controller):
        event.BooleanEvent(drive.arcadeDrive(self.driver_joystick))
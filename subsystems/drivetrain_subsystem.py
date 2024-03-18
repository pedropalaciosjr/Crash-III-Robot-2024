from wpilib import event, drive
from main.initialization.constants import Constants

class DifferentialDriveSubsystem():
    def __init__(self):
        pass
    
    def ps4_drive(self, driver_controller):
        event.BooleanEvent(drive.arcadeDrive(driver_controller.getLeftY, driver_controller.getRightX, bool=True))

    def xbox_drive(self, driver_controller):
        event.BooleanEvent(drive.arcadeDrive(driver_controller.getLeftX), bool=True)
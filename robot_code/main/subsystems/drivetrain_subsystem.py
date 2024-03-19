from wpilib import event, drive, commands2
from ..initialization import constants

class DifferentialDriveSubsystem():
    def __init__(self):
        pass
    
    def ps4_drive(self, driver_controller):
        commands2.button.Trigger(drive.arcadeDrive(driver_controller.getLeftY, driver_controller.getRightX), driver_controller)
        event.BooleanEvent(drive.arcadeDrive(driver_controller.getLeftY, driver_controller.getRightX, bool=True), True)

    def logitech_drive(self, driver_controller):
        event.BooleanEvent(drive.arcadeDrive(driver_controller.getLeftX), bool=True)
class DifferentialDriveSubsystem():
    def __init__(self):
        event.BooleanEvent(drive.arcadeDrive(self.driver_joystick))
        pass
    
    def ps4_drive(self):
        pass

    def xbox_drive(self):
        pass
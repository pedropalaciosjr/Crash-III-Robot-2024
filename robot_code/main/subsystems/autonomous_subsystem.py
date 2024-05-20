import rev
from ..initialization import constants
from commands2 import Subsystem

class AutonomousSubsystem(Subsystem):
    def __init__(self):
      pass  
    
    def autonomous(self, time_elapsed: float, stop_function: function) -> None:
        match self.auto_mode_selected:
            case self.auto_mode_one:
                # Drive forward for 2 seconds at half speed
                if time_elapsed < 2:
                    print(time_elapsed)
                    self.drive.auto_drive(1.0, 0)
    
                else:
                    stop_function([
                        self.drive.LEFT_FRONT, 
                        self.drive.LEFT_REAR, 
                        self.drive.RIGHT_FRONT, 
                        self.drive.RIGHT_REAR, 
                    ])
            case self.auto_mode_two:
                pass
            case self.auto_mode_three:
                pass
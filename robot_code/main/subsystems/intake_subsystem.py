from wpilib import (
    DigitalInput,
    XboxController
)
import rev
from ..initialization import constants as const


class IntakeSubsystem:
    def __init__(self):
        self.constants = const.Constants()
        self.INTAKE = rev.CANSparkMax(self.constants.INTAKE_CAN_ID, rev.CANSparkLowLevel.MotorType.kBrushless)

        self.INTAKE.setSmartCurrentLimit(self.constants.INTAKE_CURRENT)

        self.INTAKE_SENSOR = DigitalInput(5)
    
        self.INTAKE.burnFlash()
    

    def intakePeriodic(self, operator_controller):
        def ps4_intake(self, operator_controller):
            if (operator_controller.getL1Button()) and (self.INTAKE_SENSOR.get() == True):
                self.INTAKE.set(self.constants.INTAKE_SPEED)

        def xbox_intake(self, operator_controller):
            if (operator_controller.getLeftBumper()) and (self.INTAKE_SENSOR.get() == True):
                self.INTAKE.set(self.constants.INTAKE_SPEED) 


        def ps4_intake_reverse(self, operator_controller):
            if (operator_controller.getR1Button()):
                self.INTAKE.set(self.constants.INTAKE_REVERSE_SPEED)
        
        def xbox_intake_reverse(self, operator_controller):
            if (operator_controller.getRightBumper()):
                self.INTAKE.set(self.constants.INTAKE_REVERSE_SPEED)

        if not operator_controller.getL1Button() and not operator_controller.getR1Button():
            self.INTAKE.set(0)
        else:
            if isinstance(operator_controller, XboxController):
                xbox_intake(self, operator_controller)
            else:
                ps4_intake(self, operator_controller)

            if isinstance(operator_controller, XboxController):
                xbox_intake_reverse(self, operator_controller)
            else:
                ps4_intake_reverse(self, operator_controller)




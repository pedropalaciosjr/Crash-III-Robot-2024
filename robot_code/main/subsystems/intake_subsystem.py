from wpilib import (
    DigitalInput
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
    

    def ps4_intake(self, operator_controller):
        print("Testing")
        self.INTAKE.set(self.constants.INTAKE_SPEED) if (operator_controller.getL1Button()) and (self.INTAKE_SENSOR.get() == False) else \
        self.INTAKE.set(0)


    def xbox_intake(self, operator_controller):
        self.INTAKE.set(self.constants.INTAKE_SPEED) if (operator_controller.getLeftBumper()) and (self.INTAKE_SENSOR.get() == True) else \
        self.INTAKE.set(0)

    def ps4_intake_reverse(self, operator_controller):
        self.INTAKE.set(self.constants.INTAKE_REVERSE_SPEED) if (operator_controller.getR2Button()) and (self.INTAKE_SENSOR.get() == False) else \
        self.INTAKE.set(0)

    def xbox_intake_reverse(self, operator_controller):
        self.INTAKE.set(self.constants.INTAKE_REVERSE_SPEED) if (operator_controller.getLeftBumper()) and (self.INTAKE_SENSOR.get() == False) else \
        self.INTAKE.set(0)

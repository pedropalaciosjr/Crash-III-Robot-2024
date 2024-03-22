from wpilib import (
    DigitalInput
)
import rev
from ..initialization import constants as const


class IntakeSubsystem():
    def __init__(self):
        self.INTAKE = rev.CANSparkMax(const.INTAKE_CAN_ID, rev.MotorType.kBrushless)

        self.INTAKE.setSmartCurrentLimit(const.INTAKE_CURRENT)

        self.INTAKE_SENSOR = DigitalInput(5)
    
        self.INTAKE.burnFlash()
    

    def ps4_intake(self, operator_controller):
        self.INTAKE.set(const.INTAKE_SPEED) if (operator_controller.getL1Button()) and (self.INTAKE_SENSOR.get() == False) else \
        self.INTAKE.set(0)

    def xbox_intake(self, operator_controller):
        self.INTAKE.set(const.INTAKE_SPEED) if (operator_controller.getLeftBumper()) and (self.INTAKE_SENSOR.get() == False) else \
        self.INTAKE.set(0)

from wpilib import (
    DigitalInput
)
import rev
from ..initialization import constants as const


class IntakeSubsystem:
    def __init__(self):
        self.INTAKE = rev.CANSparkMax(const.Constants().INTAKE_CAN_ID, rev.CANSparkLowLevel.MotorType(1))

        self.INTAKE.setSmartCurrentLimit(const.Constants().INTAKE_CURRENT)

        self.INTAKE_SENSOR = DigitalInput(5)
    
        self.INTAKE.burnFlash()
    

    def ps4_intake(self, operator_controller):
        self.INTAKE.set(const.Constants().INTAKE_SPEED) if (operator_controller.getL1Button()) and (self.INTAKE_SENSOR.get() == False) else \
        self.INTAKE.set(0)


    def xbox_intake(self, operator_controller):
        self.INTAKE.set(const.Constants().INTAKE_SPEED) if (operator_controller.getLeftBumper()) and (self.INTAKE_SENSOR.get() == False) else \
        self.INTAKE.set(0)

    def ps4_intake_reverse(self, operator_controller):
        self.INTAKE.set(const.Constants().INTAKE_REVERSE_SPEED) if (operator_controller.getL1Button()) and (self.INTAKE_SENSOR.get() == False) else \
        self.INTAKE.set(0)

    def xbox_intake_reverse(self, operator_controller):
        self.INTAKE.set(const.Constants().INTAKE_REVERSE_SPEED) if (operator_controller.getLeftBumper()) and (self.INTAKE_SENSOR.get() == False) else \
        self.INTAKE.set(0)

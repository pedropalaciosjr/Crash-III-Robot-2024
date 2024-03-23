import rev
from ..initialization import constants as const

class ClimberSubsystem:
    def __init__(self):
        self.CLIMBER = rev.CANSparkMax(const.Constants().CLIMBER_CAN_ID, rev.CANSparkLowLevel.MotorType(1))

        self.CLIMBER.setSmartCurrentLimit(const.Constants().CLIMBER_CURRENT)

        self.CLIMBER.burnFlash()
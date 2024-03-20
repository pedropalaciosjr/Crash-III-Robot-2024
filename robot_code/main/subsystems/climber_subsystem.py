import rev
from ..initialization import constants as const

class ClimberSubsystem():
    def __init__(self):
        self.CLIMBER = rev.CANSparkMax(const.CLIMBER_CAN_ID, rev.MotorType.kBrushless)

        self.CLIMBER.setSmartCurrentLimit(const.CLIMBER_CURRENT)

        self.CLIMBER.burnFlash()
import rev
from ..initialization import constants as const

class ClimberSubsystem():
    def __init__(self):
        self.CLIMBER.setSmartCurrentLimit(const.CLIMBER_CURRENT)

        self.CLIMBER.burnFlash()
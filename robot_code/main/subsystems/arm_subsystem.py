import rev
from ..initialization import constants as const

class ArmSubsystem():
    def __init__(self):
        self.ARM_LEFT.setSmartCurrentLimit(const.ARM_LEFT_CURRENT)
        self.ARM_RIGHT.setSmartCurrentLimit(const.ARM_RIGHT_CURRENT)

        self.ARM_LEFT.burnFlash()
        self.ARM_RIGHT.burnFlash()
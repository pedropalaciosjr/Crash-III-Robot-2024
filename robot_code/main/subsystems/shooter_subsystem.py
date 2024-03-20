import rev
from ..initialization import constants as const

class ShooterSubsystem():
    def __init__(self):
        self.SHOOTER_LEFT.setSmartCurrentLimit(const.SHOOTER_LEFT_CURRENT)
        self.SHOOTER_RIGHT.setSmartCurrentLimit(const.SHOOTER_RIGHT_CURRENT)

        self.SHOOTER_LEFT.burnFlash()
        self.SHOOTER_RIGHT.burnFlash()
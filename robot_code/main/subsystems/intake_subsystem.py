import rev
from ..initialization import constants as const


class IntakeSubsystem():
    def __init__(self):
        self.INTAKE.setSmartCurrentLimit(const.INTAKE_CURRENT)

        self.INTAKE.burnFlash()
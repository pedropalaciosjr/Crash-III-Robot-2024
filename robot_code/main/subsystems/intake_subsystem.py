import rev
from ..initialization import constants as const


class IntakeSubsystem():
    def __init__(self):
        self.INTAKE = rev.CANSparkMax(const.INTAKE_CAN_ID, rev.MotorType.kBrushless)

        self.INTAKE.setSmartCurrentLimit(const.INTAKE_CURRENT)

        self.INTAKE.burnFlash()
import rev
from ..initialization import constants as const

class ShooterSubsystem:
    def __init__(self):
        self.SHOOTER_LEFT, self.SHOOTER_RIGHT = rev.CANSparkMax(const.Constants().SHOOTER_LEFT_CAN_ID, rev.CANSparkLowLevel.MotorType(1)), rev.CANSparkMax(const.Constants().SHOOTER_RIGHT_CAN_ID, rev.CANSparkLowLevel.MotorType(1))

        self.SHOOTER_LEFT.setSmartCurrentLimit(const.Constants().SHOOTER_LEFT_CURRENT)
        self.SHOOTER_RIGHT.setSmartCurrentLimit(const.Constants().SHOOTER_RIGHT_CURRENT)

        self.SHOOTER_LEFT.follow(self.SHOOTER_RIGHT)

        self.SHOOTER_LEFT.burnFlash()
        self.SHOOTER_RIGHT.burnFlash()


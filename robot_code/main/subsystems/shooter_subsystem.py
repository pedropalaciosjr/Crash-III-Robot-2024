import rev
from ..initialization import constants as const
from wpilib import MotorControllerGroup, XboxController
from commands2 import Subsystem

class ShooterSubsystem(Subsystem):
    def __init__(self):
        self.SHOOTER_LEFT, self.SHOOTER_RIGHT = rev.CANSparkMax(const.Constants().SHOOTER_LEFT_CAN_ID, rev.CANSparkLowLevel.MotorType.kBrushless), rev.CANSparkMax(const.Constants().SHOOTER_RIGHT_CAN_ID, rev.CANSparkLowLevel.MotorType.kBrushless)

        self.SHOOTER_LEFT.setSmartCurrentLimit(const.Constants().SHOOTER_CURRENT)
        self.SHOOTER_RIGHT.setSmartCurrentLimit(const.Constants().SHOOTER_CURRENT)

        self.SHOOTER_RIGHT.setInverted(False)
        self.SHOOTER_LEFT.setInverted(True)

        self.SHOOTER_LEFT.burnFlash()
        self.SHOOTER_RIGHT.burnFlash()

        self.SHOOTER = MotorControllerGroup(self.SHOOTER_LEFT, self.SHOOTER_RIGHT)

    def shooter(self) -> None:
        self.SHOOTER.set(1)



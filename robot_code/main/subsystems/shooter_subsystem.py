import rev
from ..initialization import constants as const
from wpilib import MotorControllerGroup, XboxController

class ShooterSubsystem:
    def __init__(self):
        self.SHOOTER_LEFT, self.SHOOTER_RIGHT = rev.CANSparkMax(const.Constants().SHOOTER_LEFT_CAN_ID, rev.CANSparkLowLevel.MotorType.kBrushless), rev.CANSparkMax(const.Constants().SHOOTER_RIGHT_CAN_ID, rev.CANSparkLowLevel.MotorType.kBrushless)

        self.SHOOTER_LEFT.setSmartCurrentLimit(const.Constants().SHOOTER_CURRENT)
        self.SHOOTER_RIGHT.setSmartCurrentLimit(const.Constants().SHOOTER_CURRENT)

        self.SHOOTER_RIGHT.setInverted(False)
        self.SHOOTER_LEFT.setInverted(True)

        self.SHOOTER_LEFT.burnFlash()
        self.SHOOTER_RIGHT.burnFlash()

        self.SHOOTER = MotorControllerGroup(self.SHOOTER_LEFT, self.SHOOTER_RIGHT)

    def shooterPeriodic(self, operator_controller) -> None:
        if isinstance(operator_controller, XboxController):
            self.SHOOTER.set(const.Constants().SHOOTER_SPEED) if operator_controller.getYButton() else self.SHOOTER.set(0)
        else:
            self.SHOOTER.set(const.Constants().SHOOTER_SPEED) if operator_controller.getTriangleButton() else self.SHOOTER.set(0)



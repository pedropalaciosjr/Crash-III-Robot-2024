import rev
from ..initialization import constants as const
from wpilib import MotorControllerGroup, XboxController
import commands2

class LaunchFeederSubsystem:
    def __init__(self):
        self.FEEDER_WHEEL, self.LAUNCH_WHEEL = rev.CANSparkMax(const.Constants().FEEDER_WHEEL_CAN_ID, rev.CANSparkLowLevel.MotorType.kBrushless), rev.CANSparkMax(const.Constants().LAUNCH_WHEEL_CAN_ID, rev.CANSparkLowLevel.MotorType.kBrushless)
        self.CLAW = rev.CANSparkMax(const.Constants().CLAW_CAN_ID, rev.CANSparkMaxLowLevel.MotorType.kBrushless)
        
        self.FEEDER_WHEEL.setSmartCurrentLimit(const.Constants().FEEDER_WHEEL_CURRENT)
        self.LAUNCH_WHEEL.setSmartCurrentLimit(const.Constants().LAUNCH_WHEEL_CURRENT)
        self.CLAW.setSmartCurrentLimit(const.Constants().CLAW_CURRENT)

        self.FEEDER_WHEEL.setInverted(False)
        self.LAUNCH_WHEEL.setInverted(True)
        self.CLAW.setInverted(False)

        self.FEEDER_WHEEL.burnFlash()
        self.LAUNCH_WHEEL.burnFlash()
        self.CLAW.burnFlash()

        self.LAUNCH_FEEDER = MotorControllerGroup(self.FEEDER_WHEEL, self.LAUNCH_WEHEL)

    def shooterPeriodic(self, operator_controller):
        if isinstance(operator_controller, XboxController):
            self.SHOOTER.set(const.Constants().SHOOTER_SPEED) if operator_controller.getYButton() else self.SHOOTER.set(0)
        else:
            self.SHOOTER.set(const.Constants().SHOOTER_SPEED) if operator_controller.getTriangleButton() else self.SHOOTER.set(0)

    def feeder(self, speed):
        return commands2.RunCommand(self.FEEDER_WHEEL.set(speed))
    
    def launch(self, speed):
        return commands2.RunCommand(self.LAUNCH_WHEEL.set(speed))



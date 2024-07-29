import rev
from ..initialization import constants as const
from wpilib import MotorControllerGroup, XboxController, PS4Controller, PS5Controller
import commands2

class LaunchFeederSubsystem():
    def __init__(self):
        # super().__init__()

        self.FEEDER_WHEEL, self.LAUNCH_WHEEL = rev.CANSparkMax(const.Constants().FEEDER_WHEEL_CAN_ID, rev.CANSparkLowLevel.MotorType.kBrushless), rev.CANSparkMax(const.Constants().LAUNCH_WHEEL_CAN_ID, rev.CANSparkLowLevel.MotorType.kBrushless)
        self.CLAW = rev.CANSparkMax(const.Constants().CLAW_CAN_ID, rev.CANSparkLowLevel.MotorType.kBrushless)
        
        self.FEEDER_WHEEL.setSmartCurrentLimit(const.Constants().FEEDER_WHEEL_CURRENT)
        self.LAUNCH_WHEEL.setSmartCurrentLimit(const.Constants().LAUNCH_WHEEL_CURRENT)
        self.CLAW.setSmartCurrentLimit(const.Constants().CLAW_CURRENT)

        self.FEEDER_WHEEL.setInverted(False)
        self.LAUNCH_WHEEL.setInverted(False)
        self.CLAW.setInverted(False)

        self.FEEDER_WHEEL.burnFlash()
        self.LAUNCH_WHEEL.burnFlash()
        self.CLAW.burnFlash()

        self.LAUNCH_FEEDER = MotorControllerGroup(self.FEEDER_WHEEL, self.LAUNCH_WHEEL)

    # def shooterPeriodic(self, operator_controller):
    #     if isinstance(operator_controller, XboxController):
    #         self.SHOOTER.set(const.Constants().SHOOTER_SPEED) if operator_controller.getYButton() else self.SHOOTER.set(0)
    #     else:
    #         self.SHOOTER.set(const.Constants().SHOOTER_SPEED) if operator_controller.getTriangleButton() else self.SHOOTER.set(0)

    def feeder(self, speed, subsystem):
        return commands2.cmd.run(self.FEEDER_WHEEL.set(speed), subsystem)
    
    def launch(self, speed, subsystem):
        return commands2.cmd.run(self.LAUNCH_WHEEL.set(speed), subsystem)
    
    def launchfeed_robot(self, operator_controller):
        if isinstance(operator_controller, PS4Controller) or isinstance(operator_controller, PS5Controller):
            if (operator_controller.getSquareButton()):
                self.LAUNCH_FEEDER.set(-1)
            elif (operator_controller.getCrossButton()) and (operator_controller.getCircleButton()):
                self.CLAW.set(-.8)
            elif (operator_controller.getTriangleButton()):
                self.FEEDER_WHEEL.set(.8)
            elif (operator_controller.getCircleButton()):
                self.LAUNCH_WHEEL.set(1)
            elif (operator_controller.getCrossButton()):
                self.CLAW.set(.8)
            else:
                self.LAUNCH_FEEDER.set(0)
                self.CLAW.set(0)
        elif isinstance(operator_controller, XboxController):
            if (operator_controller.getXButton()):
                self.LAUNCH_FEEDER.set(-1)
            elif (operator_controller.getAButton()) and (operator_controller.getBButton()):
                self.CLAW.set(-.8)
            elif (operator_controller.getYButton()):
                self.FEEDER_WHEEL.set(.8)
            elif (operator_controller.getBButton()):
                self.LAUNCH_WHEEL.set(1)
            elif (operator_controller.getAButton()):
                self.CLAW.set(.8)
            else:
                self.LAUNCH_FEEDER.set(0)
                self.CLAW.set(0)
        else:
            print("Operator controller type set as Xbox or other in constants. Only PS4/PS5 controllers are supported.")


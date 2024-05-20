import rev
from wpimath.controller import ArmFeedforward, PIDController
from ..initialization import constants as const
from wpilib import (
    DutyCycleEncoder,
    MotorControllerGroup,
    SmartDashboard,
    Encoder)
from commands2 import Subsystem

class ArmSubsystem(Subsystem):
    def __init__(self):
        global degrees_to_radians, radians_to_degrees
        def degrees_to_radians(self, x):
            return x / 360
        def radians_to_degrees(self, y):
            return y * 360
        
        constants = const.Constants()
        self.ARM_LEFT, self.ARM_RIGHT = rev.CANSparkMax(constants.ARM_LEFT_CAN_ID, rev.CANSparkLowLevel.MotorType.kBrushless), rev.CANSparkMax(constants.ARM_RIGHT_CAN_ID, rev.CANSparkLowLevel.MotorType.kBrushless)
        
        self.ARM_LEFT.setSmartCurrentLimit(constants.ARM_CURRENT)
        self.ARM_RIGHT.setSmartCurrentLimit(constants.ARM_CURRENT)

        self.PID = PIDController(constants.K_P, constants.K_I, constants.K_D)

        self.ARM_GROUP = MotorControllerGroup(self.ARM_LEFT, self.ARM_RIGHT)

        # self.ARM_THROUGHBORE_ENCODER = DutyCycleEncoder(2)
        
        self.ARM_THROUGHBORE = Encoder(
            constants.THROUGH_BORE_A_CHANNEL,
            constants.THROUGH_BORE_CHANNEL_B)
        
        self.feedforward = ArmFeedforward(
            constants.STATIC_GAIN,
            constants.GRAVITY_GAIN,
            constants.VELOCITY_GAIN,
            constants.ACCELERATION_GAIN)

        # self.ARM_ENCODER.setPositionConversionFactor(360 / 21.5)

        self.ARM_LEFT.burnFlash()
        self.ARM_RIGHT.burnFlash()



    def arm_periodic(self) -> None:
        """Implements PID and feedforward control mechanisms."""

        pid_output = self.PID.calculate(self.ARM_THROUGHBORE.getDistance(), degrees_to_radians(self, 40))
        feedforward_output = self.feedforward.calculate(degrees_to_radians(self, 40), 2)

        SmartDashboard.putNumber("Arm Position:", (self.ARM_THROUGHBORE.getDistance() * 360))

        # print(f"Arm Abs Position: {self.ARM_THROUGHBORE.getAbsolutePosition() * 360}")
        print(f"Arm Distance: {self.ARM_THROUGHBORE.getDistance()}")
        print(f"Motor Voltage (L): {self.ARM_LEFT.getBusVoltage()}")

        if (radians_to_degrees(self, self.ARM_THROUGHBORE.getDistance()) <= 20):
            self.ARM_GROUP.setVoltage(0)
        else:
            self.ARM_GROUP.setVoltage(pid_output + feedforward_output)
    
    # def arm_positions(self, driver_controller):
    #     # Amp Position
    #     if driver_controller.getRightBumper():
    #         self.feedforward = self.feedforward_instance.calculate(degrees_to_radians(self, 0), 2, 3)

    #         self.ARM_GROUP.setVoltage(self.PID.calculate(self.ARM_THROUGHBORE_ENCODER, degrees_to_radians(self, 0)) + self.feedforward)
    #     # Ground Intake Position
    #     elif driver_controller.getLeftBumper():
    #         self.feedforward = self.feedforward_instance.calculate(degrees_to_radians(self, 70), 2, 3)

    #         self.ARM_GROUP.setVoltage(self.PID.calculate(self.ARM_THROUGHBORE_ENCODER, degrees_to_radians(self, 70)) + self.feedforward)
    #     # This else block will run if neither the left bumper or right bumper buttons are pressed.
    #     else:
    #         self.ARM_GROUP.setVoltage(0)

        # self.ARM_GROUP.setVoltage()
        # self.ARM_GROUP.setVoltage()
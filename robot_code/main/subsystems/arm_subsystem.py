import rev
from wpimath.controller import ArmFeedforward, PIDController
from ..initialization import constants as const
from wpilib import DutyCycleEncoder, MotorControllerGroup, SmartDashboard, Encoder

class ArmSubsystem:
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

        self.ARM_THROUGHBORE_ENCODER = DutyCycleEncoder(2)
        self.feedforward_instance = ArmFeedforward(constants.STATIC_GAIN, constants.GRAVITY_GAIN, constants.VELOCITY_GAIN ,constants.ACCELERATION_GAIN)

        # self.ARM_ENCODER.setPositionConversionFactor(360 / 21.5)

        self.ARM_LEFT.burnFlash()
        self.ARM_RIGHT.burnFlash()



    def arm_periodic(self):
        # SmartDashboard.putNumber("Arm Position:", (self.ARM_THROUGHBORE_ENCODER.getAbsolutePosition() * 360))
        print(f"Arm Position: {self.ARM_THROUGHBORE_ENCODER.getAbsolutePosition() * 360}")

        self.feedforward = self.feedforward_instance.calculate(degrees_to_radians(self, 40), 2)
        print(f"MOTOR VOLTAGE: {self.ARM_LEFT.getBusVoltage()}")
        print(self.feedforward)
        if (radians_to_degrees(self, self.ARM_THROUGHBORE_ENCODER.getAbsolutePosition()) <= 40):
            self.ARM_GROUP.setVoltage(0)
        else:
            self.ARM_GROUP.setVoltage(self.feedforward)
            #self.PID.calculate(self.ARM_THROUGHBORE_ENCODER.getAbsolutePosition(), degrees_to_radians(self, 40)) + 
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
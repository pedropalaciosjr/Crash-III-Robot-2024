import rev
import wpimath
from ..initialization import constants as const
from wpilib import DutyCycleEncoder, MotorControllerGroup, SmartDashboard

class ArmSubsystem:
    def __init__(self):
        self.ARM_LEFT, self.ARM_RIGHT = rev.CANSparkMax(const.Constants().ARM_LEFT_CAN_ID, rev.CANSparkLowLevel.MotorType.kBrushless), rev.CANSparkMax(const.Constants().ARM_RIGHT_CAN_ID, rev.CANSparkLowLevel.MotorType.kBrushless)
        
        self.ARM_LEFT.setSmartCurrentLimit(const.Constants().ARM_CURRENT)
        self.ARM_RIGHT.setSmartCurrentLimit(const.Constants().ARM_CURRENT)
        
        self.ARM = MotorControllerGroup(self.ARM_LEFT, self.ARM_RIGHT)

        

        # self.ARM_THROUGHBORE_ENCODER = DutyCycleEncoder(2)
        # self.ARM_PID = self.ARM.getPIDController()
        # self.ARM_ENCODER = self.ARM.getEncoder()
        # self.ARM_PID.setFeedbackDevice(self.ARM_ENCODER)

        # self.ARM_PID.setP(0.015)
        # self.ARM_PID.setI(0)
        # self.ARM_PID.setD(0.001)
        # self.ARM_PID.setFF(0)

        # self.ARM_ENCODER.setPositionConversionFactor(360 / 21.5)

        # self.ARM.burnFlash()



    def armPeriodic(self):
        SmartDashboard.putNumber("Arm Position:", (self.ARM_THROUGHBORE_ENCODER.getAbsolutePosition() * 360))
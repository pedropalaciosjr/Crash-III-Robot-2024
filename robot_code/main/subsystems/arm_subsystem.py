import rev
from ..initialization import constants as const

class ArmSubsystem:
    def __init__(self):
        self.ARM_LEFT, self.ARM_RIGHT = rev.CANSparkMax(const.Constants().ARM_LEFT_CAN_ID, rev.CANSparkLowLevel.MotorType(1)), rev.CANSparkMax(const.Constants().ARM_RIGHT_CAN_ID, rev.CANSparkLowLevel.MotorType(1))
        
        self.ARM_LEFT.setSmartCurrentLimit(const.Constants().ARM_LEFT_CURRENT)
        self.ARM_RIGHT.setSmartCurrentLimit(const.Constants().ARM_RIGHT_CURRENT)

        self.ARM_LEFT.burnFlash()
        self.ARM_RIGHT.burnFlash()
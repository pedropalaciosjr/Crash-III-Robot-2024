import rev

from wpilib import event, drive, MotorControllerGroup, Timer, SmartDashboard, PS4Controller, XboxController
from ..initialization import constants as const
import time
import commands2


class DifferentialDriveSubsystem():
    def __init__(self):
        constants_class = const.Constants()

        # super().__init__()

        self.LEFT_FRONT, self.LEFT_REAR = rev.CANSparkMax(constants_class.LEFT_FRONT_CAN_ID, rev.CANSparkLowLevel.MotorType.kBrushless), rev.CANSparkMax(constants_class.LEFT_REAR_CAN_ID, rev.CANSparkLowLevel.MotorType.kBrushless)
        self.RIGHT_FRONT, self.RIGHT_REAR = rev.CANSparkMax(constants_class.RIGHT_FRONT_CAN_ID, rev.CANSparkLowLevel.MotorType.kBrushless), rev.CANSparkMax(constants_class.RIGHT_REAR_CAN_ID, rev.CANSparkLowLevel.MotorType.kBrushless)

        self.LEFT_FRONT.setInverted(False)
        self.RIGHT_FRONT.setInverted(False)
        self.LEFT_REAR.setInverted(False)
        self.RIGHT_REAR.setInverted(False)

        # self.LEFT_FRONT.GetEncoder()
        # self.LEFT_REAR.GetEncoder()
        # self.RIGHT_FRONT.GetEncoder()
        # self.RIGHT_REAR.GetEncoder()
    
        self.LEFT_FRONT.setSmartCurrentLimit(constants_class.DIFFERENTIAL_DRIVE_CURRENT)
        self.LEFT_REAR.setSmartCurrentLimit(constants_class.DIFFERENTIAL_DRIVE_CURRENT)
        self.RIGHT_FRONT.setSmartCurrentLimit(constants_class.DIFFERENTIAL_DRIVE_CURRENT)
        self.RIGHT_REAR.setSmartCurrentLimit(constants_class.DIFFERENTIAL_DRIVE_CURRENT)


        self.LEFT_FRONT.burnFlash()
        self.LEFT_REAR.burnFlash()
        self.RIGHT_FRONT.burnFlash()
        self.RIGHT_REAR.burnFlash()
        
        self.LEFT = MotorControllerGroup(self.LEFT_FRONT, self.LEFT_REAR)
        self.RIGHT = MotorControllerGroup(self.RIGHT_FRONT, self.RIGHT_REAR)
        self.RIGHT.setInverted(False)
        self.LEFT.setInverted(True)
        
        self.DIFFERENTIAL_DRIVE = drive.DifferentialDrive(self.LEFT, self.RIGHT)

        self.turbo_run = False

        self.multiplier = .572
        # Original value: .572

        


    # def drive_robot(self, driver_joystick, drive_class):
    #     return commands2.cmd.run(
    #         lambda : self.DIFFERENTIAL_DRIVE.arcadeDrive(
    #             driver_joystick.getLeftY(), driver_joystick.getRightX()
    #             ), 
    #             drive_class)
    
    def drive_robot(self, driver_joystick, start_time):
        time_elapsed = lambda final, init : final - init
        self.DIFFERENTIAL_DRIVE.arcadeDrive(driver_joystick.getLeftY()*self.multiplier, driver_joystick.getRightX()*self.multiplier)

        if isinstance(driver_joystick, PS4Controller):
            if driver_joystick.getTouchpadPressed():
                self.nitro_start = Timer()
                self.nitro_start.reset()
                self.touchpressed_time = self.nitro_start.getFPGATimestamp()
                print(self.nitro_start.getFPGATimestamp())
                self.turbo_run = True
            

            if self.turbo_run:
                self.nitro_time = self.nitro_start.getFPGATimestamp()
                if time_elapsed(self.nitro_time, self.touchpressed_time) <= 5:
                    SmartDashboard.putBoolean("Turbo Enabled:", self.turbo_run)
                    self.multiplier = 0.7
                else:
                    self.multiplier = 0.572
                    # Original value: 0.572
                    self.turbo_run = False
                    SmartDashboard.putBoolean("Turbo Enabled:", self.turbo_run)
        elif isinstance(driver_joystick, XboxController):
            if driver_joystick.getStartButtonPressed():
                self.nitro_start = Timer()
                self.nitro_start.reset()
                self.touchpressed_time = self.nitro_start.getFPGATimestamp()
                print(self.nitro_start.getFPGATimestamp())
                self.turbo_run = True
            

            if self.turbo_run:
                self.nitro_time = self.nitro_start.getFPGATimestamp()
                if time_elapsed(self.nitro_time, self.touchpressed_time) <= 5:
                    SmartDashboard.putBoolean("Turbo Enabled:", self.turbo_run)
                    self.multiplier = 0.7
                else:
                    self.multiplier = 0.572
                    # Original value: 0.572
                    self.turbo_run = False
                    SmartDashboard.putBoolean("Turbo Enabled:", self.turbo_run)
        else:
            print("Error in controller type variable constant.")
            



    # def xbox_logitech_drive(self, driver_joystick):
    #     self.DIFFERENTIAL_DRIVE.arcadeDrive(driver_joystick.getLeftY(), driver_joystick.getRightX())

    def auto_drive(self, speed, rotation):
        self.DIFFERENTIAL_DRIVE.arcadeDrive(speed, rotation)

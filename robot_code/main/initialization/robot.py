# Project started and written by Pedro Palacios Jr, Team 457.

from wpilib import (
    drive,
    SmartDashboard,
    Timer,
    TimedRobot,
    PS4Controller,
    Joystick,
    CameraServer,
    event)
import rev
from . import constants as const
from ..subsystems import drivetrain_subsystem

class MyRobot(TimedRobot):
    def __robotInit__(self):
        def robot_base():

            self.LEFT_FRONT, self.LEFT_REAR = rev.CANSparkMax(const.LEFT_FRONT_CAN_ID, rev.MotorType.kBrushless), rev.CANSparkMax(const.LEFT_REAR_CAN_ID, rev.MotorType.kBrushless)
            self.RIGHT_FRONT, self.RIGHT_REAR = rev.CANSparkMax(const.RIGHT_FRONT_CAN_ID, rev.MotorType.kBrushless), rev.CANSparkMax(const.RIGHT_REAR_CAN_ID, rev.MotorType.kBrushless)

            self.SPARKMAX_CONTROLLERS = [self.LEFT_FRONT, self.LEFT_REAR, self.RIGHT_FRONT, self.RIGHT_REAR]

            self.LAUNCH_WHEEL, self.FEEDER_WHEEL, self.ROLLER_CLAW = rev.CANSparkMax(const.LAUNCH_WHEEL_CAN_ID, rev.MotorType.kBrushless), rev.CANSparkMax(const.FEEDER_WHEEL_CAN_ID, rev.MotorType.kBrushless),\
                rev.CANSparkMax(const.ROLLER_CLAW_CAN_ID, rev.MotorType.kBrushless)
            self.CLIMBER = rev.CANSparkMax(const.CLIMBER_CAN_ID, rev.MotorType.kBrushless)

            self.LEFT = drive.MotorControllerGroup(self.LEFT_FRONT, self.LEFT_REAR)
            self.RIGHT = drive.MotorControllerGroup(self.RIGHT_FRONT, self.RIGHT_REAR)
            
            self.DIFFERENTIAL_DRIVE = drive.DifferentialDrive(self.LEFT, self.RIGHT)

            self.LEFT_FRONT.setInverted(False)
            self.RIGHT_FRONT.setInverted(False)
    
            self.LEFT_FRONT.setSmartCurrentLimit(const.DIFFERENTIAL_DRIVE_CURRENT)
            self.LEFT_REAR.setSmartCurrentLimit(const.DIFFERENTIAL_DRIVE_CURRENT)
            self.RIGHT_FRONT.setSmartCurrentLimit(const.DIFFERENTIAL_DRIVE_CURRENT)
            self.RIGHT_REAR.setSmartCurrentLimit(const.DIFFERENTIAL_DRIVE_CURRENT)

            self.LAUNCH_WHEEL.setSmartCurrentLimit(const.LAUNCH_WHEEL_CURRENT)
            self.FEEDER_WHEEL.setSmartCurrentLimit(const.FEEDER_WHEEL_CURRENT)
            self.ROLLER_CLAW.setSmartCurrentLimit(const.ROLLER_CLAW_CURRENT)

            self.CLIMBER.setSmartCurrentLimit(const.CLIMBER_CURRENT)

            self.LEFT_REAR.follow(self.LEFT_FRONT, bool=False)
            self.RIGHT_REAR.follow(self.RIGHT_FRONT, bool=False)

            self.LEFT_FRONT.burnFlash()
            self.LEFT_REAR.burnFlash()
            self.RIGHT_FRONT.burnFlash()
            self.RIGHT_REAR.burnFlash()
            self.LAUNCH_WHEEL.burnFlash()
            self.FEEDER_WHEEL.burnFlash()
            self.ROLLER_CLAW.burnFlash()
            self.CLIMBER.burnFlash()

            CameraServer.launch("robot_vision.py:main")
        
        def joystick_init(driver_controller_type = "null", operator_controller_type= "null" ):
            self.driver_joystick = PS4Controller(0) if (driver_controller_type) == "PS4" else (Joystick(0))
            self.operator_joystick = PS4Controller(1) if (operator_controller_type) == "PS4" else (Joystick(1))

        def sparkmax_safety():
            motor_temperatures = []
            brownout_faults = []
            for sparkmax in self.SPARKMAX_CONTROLLERS:
                motor_temperatures.append((1.8 * sparkmax.getMotorTemperature()) + 32)
                brownout_faults.append(sparkmax.getFault(0))
            
            left_front_motor_temperature, left_rear_motor_temperature, right_front_motor_temperature, right_rear_motor_temperature = motor_temperatures
            left_front_brownout = 
            SmartDashboard.putNumber(f"Left Front Motor Temperature (F) {left_front_motor_temperature}")
            SmartDashboard.putNumber(f"Left Rear Motor Temperature (F) {left_rear_motor_temperature}")
            SmartDashboard.putNumber(f"Right Front Motor Temperature (F) {right_front_motor_temperature}")
            SmartDashboard.putNumber(f"Right Rear Motor Temperature (F) {right_rear_motor_temperature}")


            SmartDashboard.putBoolean(f"Left Front Brownout Detected: {brownout_faults}")
            SmartDashboard.putBoolean(f"Left Rear Brownout Detected: {True}")
            SmartDashboard.putBoolean(f"Right Front Brownout Detected: {True}")
            SmartDashboard.putBoolean(f"Right Rear Brownout Detected: {True}")

        robot_base()
        joystick_init(const.driver_controller_type, const.operator_controller_type)

    def robotPeriodic(self):
        current_time = Timer.getFPGATimestamp()
        SmartDashboard.putNumber(f"Robot Runtime (seconds): {current_time}")





    def teleopPeriodic(self):
        drive = drivetrain_subsystem.DifferentialDriveSubsystem()
        drive.ps4_drive(self.driver_joystick) if const.driver_controller_type == "PS4" else drive.xbox_drive(self.driver_joystick)

    def autonomousInit(self):
        global autonomous_start
        autonomous_start = Timer.getFPGATimestamp()
    
    def autonomousPeriodic(self):
        # Autonomous primary commands
        autonomous_periodic = Timer.getFPGATimestamp()
        time_elapsed = lambda final, init : final - init

        time_elapsed = time_elapsed(autonomous_periodic, autonomous_start)


        pass
# Project started and written by Pedro Palacios Jr, Team 457.

from wpilib import (
    drive,
    SmartDashboard,
    Timer,
    TimedRobot,
    PS4Controller,
    XboxController,
    CameraServer,
    event,
    RobotState,
    reportWarning,
    SendableChooser
    )
from rev import FaultID
from robot_code.main.initialization.constants import Constants as const
from robot_code.main.subsystems import drivetrain_subsystem, arm_subsystem, climber_subsystem, intake_subsystem, shooter_subsystem

class MyRobot(TimedRobot):
    def robotInit(self):
        global sparkmax_safety
        def robot_base(self):
            self.drive_class = drivetrain_subsystem.DifferentialDriveSubsystem()
            self.arm_class = arm_subsystem.ArmSubsystem()
            self.shooter_class = shooter_subsystem.ShooterSubsystem()
            self.intake_class = intake_subsystem.IntakeSubsystem()
            self.climber_class = climber_subsystem.ClimberSubsystem()

            self.SPARKMAX_CONTROLLERS = [
                self.drive_class.LEFT_FRONT, 
                self.drive_class.LEFT_REAR, 
                self.drive_class.RIGHT_FRONT, 
                self.drive_class.RIGHT_REAR, 
                self.arm_class.ARM_LEFT, 
                self.arm_class.ARM_RIGHT,
                self.shooter_class.SHOOTER_LEFT,
                self.shooter_class.SHOOTER_RIGHT,
                self.intake_class.INTAKE,
                self.climber_class.CLIMBER
            ]
            self.auto_mode_one = "Auto Mode One"
            self.auto_mode_two = "Auto Mode Two"
            self.auto_mode_three = "Auto Mode Three"

            self.chooser = SendableChooser()

            self.chooser.setDefaultOption("Auto Mode One", self.auto_mode_one)
            self.chooser.addOption("Auto Mode Two", self.auto_mode_two)
            self.chooser.addOption("Auto Mode Three", self.auto_mode_three)

            SmartDashboard.putData("Autonomous Modes", self.chooser)


            CameraServer.launch("robot_vision.py:main")
        
        def joystick_init(self, driver_controller_type = "null", operator_controller_type= "null" ):
            self.driver_joystick = PS4Controller(0) if (driver_controller_type) == "PS4" else (XboxController(0))
            self.operator_joystick = PS4Controller(1) if (operator_controller_type) == "PS4" else (XboxController(1))

        def sparkmax_safety(self):
            motor_temperatures = []
            brownout_faults = []
            for sparkmax in self.SPARKMAX_CONTROLLERS:
                motor_temperatures.append((1.8 * sparkmax.getMotorTemperature()) + 32)
                brownout_faults.append(sparkmax.getFault(FaultID.kBrownout))
            
            left_front_motor_temperature, left_rear_motor_temperature, right_front_motor_temperature, right_rear_motor_temperature,\
                arm_left_temperature, arm_right_temperature, shooter_left_temperature, shooter_right_temperature, intake_temperature, climber_temperature = motor_temperatures
            left_front_brownout, left_rear_brownout, right_front_brownout, right_rear_brownout, arm_left_brownout, \
                 arm_right_brownout, shooter_left_brownout, shooter_right_brownout, intake_brownout, climber_brownout = brownout_faults
            
            SmartDashboard.putNumber("Left Front Motor Temperature (F)", left_front_motor_temperature)
            SmartDashboard.putNumber("Left Rear Motor Temperature (F)", left_rear_motor_temperature)
            SmartDashboard.putNumber("Right Front Motor Temperature (F)", right_front_motor_temperature)
            SmartDashboard.putNumber("Right Rear Motor Temperature (F)", right_rear_motor_temperature)
            SmartDashboard.putNumber("Arm Left Motor Temperature (F)", arm_left_temperature)
            SmartDashboard.putNumber("Arm Right Motor Temperature (F)", arm_right_temperature)
            SmartDashboard.putNumber("Shooter Left Motor Temperature (F)", shooter_left_temperature)
            SmartDashboard.putNumber("Shooter Right Motor Temperature (F)", shooter_right_temperature)
            SmartDashboard.putNumber("Intake Motor Temperature (F)", intake_temperature)
            SmartDashboard.putNumber("Climber Right Motor Temperature (F)", climber_temperature)

            SmartDashboard.putBoolean("Left Front Brownout Detected:", left_front_brownout)
            SmartDashboard.putBoolean("Left Rear Brownout Detected:", left_rear_brownout)
            SmartDashboard.putBoolean("Right Front Brownout Detected:", right_front_brownout)
            SmartDashboard.putBoolean("Right Rear Brownout Detected:", right_rear_brownout)
            SmartDashboard.putBoolean("Arm Left Brownout Detected:", arm_left_brownout)
            SmartDashboard.putBoolean("Arm Right Brownout Detected:", arm_right_brownout)
            SmartDashboard.putBoolean("Shooter Left Brownout Detected:", shooter_left_brownout)
            SmartDashboard.putBoolean("Shooter Right Brownout Detected:", shooter_right_brownout)
            SmartDashboard.putBoolean("Intake Brownout Detected:", intake_brownout)
            SmartDashboard.putBoolean("Climber Brownout Detected:", climber_brownout)

            for state in brownout_faults:
                if state:
                    reportWarning("BROWNOUT DETECTED!")
                    return
                

        robot_base(self)
        sparkmax_safety(self)
        joystick_init(self, const.driver_controller_type, const.operator_controller_type)



    def teleopInit(self):
        self.drive = drivetrain_subsystem.DifferentialDriveSubsystem()
        current_time = Timer.getFPGATimestamp()
        SmartDashboard.putNumber("Robot Runtime (seconds):", current_time)

        sparkmax_safety()

    def teleopPeriodic(self):
        drivetrain_subsystem.DifferentialDriveSubsystem.ps4_drive(self.driver_joystick) if isinstance(self.driver_joystick, PS4Controller) else drivetrain_subsystem.DifferentialDriveSubsystem.xbox_logitech_drive(self.driver_joystick)
        
        intake_subsystem.IntakeSubsystem.ps4_intake(self.operator_joystick) if isinstance(self.operator_joystick, PS4Controller) else intake_subsystem.IntakeSubsystem.xbox_intake(self.operator_joystick)
        intake_subsystem.IntakeSubsystem.ps4_intake_reverse(self.operator_joystick) if isinstance(self.operator_joystick, PS4Controller) else intake_subsystem.IntakeSubsystem.xbox_intake_reverse(self.operator_joystick)
        
        if RobotState.isAutonomous():
            pass

    def autonomousInit(self):
        global autonomous_start
        autonomous_start = Timer.getFPGATimestamp()

        self.auto_mode_selected = self.chooser.getSelected()
        SmartDashboard.putString("Autonomous Mode:", self.auto_mode_selected)
    
    def autonomousPeriodic(self):
        # Autonomous primary commands
        autonomous_periodic = Timer.getFPGATimestamp()
        time_elapsed = lambda final, init : final - init

        time_elapsed = time_elapsed(autonomous_periodic, autonomous_start)

        match self.auto_mode_selected:
            case self.auto_mode_one:
                pass
            case self.auto_mode_two:
                pass
            case self.auto_mode_three:
                pass
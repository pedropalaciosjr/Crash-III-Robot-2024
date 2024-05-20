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
import rev
from cscore import CameraServer
# from commands2 import CommandPS4Controller
from robot_code.main.initialization.constants import Constants
from robot_code.main.subsystems import drivetrain_subsystem, arm_subsystem, climber_subsystem, intake_subsystem, shooter_subsystem, autonomous_subsystem

class MyRobot(TimedRobot):
    def robotInit(self):
        global sparkmax_safety
        global stop
        global drive

        self.drive = drivetrain_subsystem.DifferentialDriveSubsystem()
        self.arm = arm_subsystem.ArmSubsystem()
        self.shooter = shooter_subsystem.ShooterSubsystem()
        self.intake = intake_subsystem.IntakeSubsystem()
        self.climber = climber_subsystem.ClimberSubsystem()
        self.auto = autonomous_subsystem.AutonomousSubsystem()
        self.constants_class = Constants()

        self.SPARKMAX_CONTROLLERS = [
            self.drive.LEFT_FRONT, 
            self.drive.LEFT_REAR, 
            self.drive.RIGHT_FRONT, 
            self.drive.RIGHT_REAR, 
            self.arm.ARM_LEFT, 
            self.arm.ARM_RIGHT,
            self.shooter.SHOOTER_LEFT,
            self.shooter.SHOOTER_RIGHT,
            self.intake.INTAKE,
            # self.climber.CLIMBER
        ]
        self.auto_mode_one = "Auto Mode One"
        self.auto_mode_two = "Auto Mode Two"
        self.auto_mode_three = "Auto Mode Three"

        self.chooser = SendableChooser()

        self.chooser.setDefaultOption("Auto Mode One", self.auto_mode_one)
        self.chooser.addOption("Auto Mode Two", self.auto_mode_two)
        self.chooser.addOption("Auto Mode Three", self.auto_mode_three)

        SmartDashboard.putData("Autonomous Modes", self.chooser)

        sparkmax_safety()
        joystick_init(self, self.constants_class.driver_controller_type, self.constants_class.operator_controller_type)



    def teleopInit(self):
        CameraServer.startAutomaticCapture()
        
    
    def teleopPeriodic(self):
        current_time = Timer.getFPGATimestamp()
        SmartDashboard.putNumber("Robot Runtime (seconds):", current_time)
        sparkmax_safety()
        
        self.drive.ps4_drive(self.driver_joystick) if isinstance(self.driver_joystick, PS4Controller) else self.drive.xbox_logitech_drive(self.driver_joystick)
        self.intake.intakePeriodic(self.driver_joystick)
        self.shooter.shooterPeriodic(self.driver_joystick)
        self.arm.arm_periodic()
        # intake_subsystem.IntakeSubsystem.ps4_intake_reverse(self.operator_joystick) if isinstance(self.operator_joystick, PS4Controller) else intake_subsystem.IntakeSubsystem.xbox_intake_reverse(self.operator_joystick)
        

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

        sparkmax_safety(self)

        # self.arm.ARM_LEFT.set(self.arm.PID.calculate(encoder.getDistance(), setpoint))

        match self.auto_mode_selected:
            case self.auto_mode_one:
                # Drive forward for 2 seconds at half speed
                if time_elapsed < 2:
                    print(time_elapsed)
                    self.drive.auto_drive(1.0, 0)
    
                else:
                    stop([
                        self.drive.LEFT_FRONT, 
                        self.drive.LEFT_REAR, 
                        self.drive.RIGHT_FRONT, 
                        self.drive.RIGHT_REAR, 
                    ])
            case self.auto_mode_two:
                pass
            case self.auto_mode_three:
                pass
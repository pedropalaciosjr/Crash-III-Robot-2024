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
from robotcontainer import RobotContainer
from commands2 import CommandScheduler

class MyRobot(TimedRobot):
    def robotInit(self) -> None:
        self.container = RobotContainer()

        self.auto_mode_one = "Auto Mode One"
        self.auto_mode_two = "Auto Mode Two"
        self.auto_mode_three = "Auto Mode Three"

        self.chooser = SendableChooser()

        self.chooser.setDefaultOption("Auto Mode One", self.auto_mode_one)
        self.chooser.addOption("Auto Mode Two", self.auto_mode_two)
        self.chooser.addOption("Auto Mode Three", self.auto_mode_three)

        SmartDashboard.putData("Autonomous Modes", self.chooser)

        # Camera Initialization & Processing
        camera = CameraServer.startAutomaticCapture()
        camera.setResolution(640, 480)

        cv_sink = CameraServer.getVideo()
        cv_source = CameraServer.putVideo("Rectangle", 640, 480)
    
    def robotPeriodic(self) -> None:
        CommandScheduler.getInstance().run()
   
    def teleopInit(self) -> None:
        pass
        
    
    def teleopPeriodic(self) -> None:
        current_time = Timer.getFPGATimestamp()
        SmartDashboard.putNumber("Robot Runtime (seconds):", current_time)
        self.container.sparkmax_safety()
        
        # self.arm.arm_periodic()
        # intake_subsystem.IntakeSubsystem.ps4_intake_reverse(self.operator_joystick) if isinstance(self.operator_joystick, PS4Controller) else intake_subsystem.IntakeSubsystem.xbox_intake_reverse(self.operator_joystick)
        

    def autonomousInit(self) -> None:
        global autonomous_start
        autonomous_start = Timer.getFPGATimestamp()

        self.auto_mode_selected = self.chooser.getSelected()
        SmartDashboard.putString("Autonomous Mode:", self.auto_mode_selected)
    
    def autonomousPeriodic(self) -> None:
        # Autonomous primary commands
        autonomous_periodic = Timer.getFPGATimestamp()
        time_elapsed = lambda final, init : final - init

        time_elapsed = time_elapsed(autonomous_periodic, autonomous_start)

        self.container.autonomous.autonomous(time_elapsed, self.container.stop)

        self.container.sparkmax_safety(self)
from robot_code.main.subsystems.arm_subsystem import ArmSubsystem
from robot_code.main.subsystems.drivetrain_subsystem import DifferentialDriveSubsystem
from robot_code.main.subsystems.intake_subsystem import IntakeSubsystem
from robot_code.main.subsystems.shooter_subsystem import ShooterSubsystem
from robot_code.main.subsystems.autonomous_subsystem import AutonomousSubsystem
from robot_code.main.initialization.constants import Constants
from wpilib import (SmartDashboard,
                    reportWarning
                    )
from commands2.button import CommandPS4Controller, CommandXboxController
from commands2.cmd import run
import rev

class RobotContainer:
    def __init__(self) -> None:
        # Crash III's Subsystems (Collections of Robot Hardware)
        self.arm = ArmSubsystem()
        self.drive = DifferentialDriveSubsystem()
        self.intake = IntakeSubsystem()
        self.shooter = ShooterSubsystem()
        self.constants = Constants()
        self.autonomous = AutonomousSubsystem()

        self.controllers_init()
        self.button_configurations()

        self.drive.setDefaultCommand(
            run(
                lambda: self.drive.ps4_arcade_drive(self.driver_controller.getLeftY(), self.driver_controller.getRightX()),
                self.drive
            )
        )

        # Motor controller objects storage for stop & controller safety function
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
        ]
    
    def button_configurations(self) -> None:
        """Configures the button bindings for operating controls."""
        self.shooter.setDefaultCommand(
            run(
                lambda: self.shooter.shooter_cmd(0)
            )
        )
        self.intake.setDefaultCommand(
            run(
                lambda: self.intake_cmd_stop(self.stop)
            )
        )
        self.driver_controller.L1().whileTrue(
            run(
                lambda: self.intake.intake(False)
            )
        )
        self.driver_controller.R1().whileTrue(
            run(
                lambda: self.intake.intake(True)
            )
        )
        self.driver_controller.triangle().whileTrue(
            run(
                lambda: self.shooter.shooter_cmd(self.constants.SHOOTER_SPEED)
            )
        )
    
    def sparkmax_safety(self) -> None:
        """Displays motor temperatures and brownout states on motor controllers."""

        motor_temperatures, brownout_faults = [], []
        for sparkmax in self.SPARKMAX_CONTROLLERS:
            motor_temperatures.append((1.8 * sparkmax.getMotorTemperature()) + 32)
            brownout_faults.append(sparkmax.getFault(rev.CANSparkBase.FaultID.kBrownout))
        
        left_front_motor_temperature, left_rear_motor_temperature, right_front_motor_temperature, right_rear_motor_temperature,\
            arm_left_temperature, arm_right_temperature, shooter_left_temperature, shooter_right_temperature, intake_temperature = motor_temperatures
        left_front_brownout, left_rear_brownout, right_front_brownout, right_rear_brownout, arm_left_brownout, \
                arm_right_brownout, shooter_left_brownout, shooter_right_brownout, intake_brownout = brownout_faults
        
        SmartDashboard.putNumber("Left Front Motor Temperature (F)", left_front_motor_temperature)
        SmartDashboard.putNumber("Left Rear Motor Temperature (F)", left_rear_motor_temperature)
        SmartDashboard.putNumber("Right Front Motor Temperature (F)", right_front_motor_temperature)
        SmartDashboard.putNumber("Right Rear Motor Temperature (F)", right_rear_motor_temperature)
        SmartDashboard.putNumber("Arm Left Motor Temperature (F)", arm_left_temperature)
        SmartDashboard.putNumber("Arm Right Motor Temperature (F)", arm_right_temperature)
        SmartDashboard.putNumber("Shooter Left Motor Temperature (F)", shooter_left_temperature)
        SmartDashboard.putNumber("Shooter Right Motor Temperature (F)", shooter_right_temperature)
        SmartDashboard.putNumber("Intake Motor Temperature (F)", intake_temperature)

        SmartDashboard.putBoolean("Left Front Brownout Detected:", left_front_brownout)
        SmartDashboard.putBoolean("Left Rear Brownout Detected:", left_rear_brownout)
        SmartDashboard.putBoolean("Right Front Brownout Detected:", right_front_brownout)
        SmartDashboard.putBoolean("Right Rear Brownout Detected:", right_rear_brownout)
        SmartDashboard.putBoolean("Arm Left Brownout Detected:", arm_left_brownout)
        SmartDashboard.putBoolean("Arm Right Brownout Detected:", arm_right_brownout)
        SmartDashboard.putBoolean("Shooter Left Brownout Detected:", shooter_left_brownout)
        SmartDashboard.putBoolean("Shooter Right Brownout Detected:", shooter_right_brownout)
        SmartDashboard.putBoolean("Intake Brownout Detected:", intake_brownout)

        for state in brownout_faults:
            if state:
                reportWarning("BROWNOUT DETECTED!")
                return
    
    def stop(self, motor_controllers: list) -> None:
        """Invokes the REV stop_motor method on motor controllers passed as an iterable object argument."""

        try:
            for sparkmax in motor_controllers:
                sparkmax.stopMotor()
        except (TypeError):
            print("'stop' function invoked with invalid arguments. This function expects only iterable objects as arguments.")
        
        return
    
    def controllers_init(self, driver_controller_type: str = "null", operator_controller_type: str = "null" ) -> None:
        self.driver_controller = CommandPS4Controller(0) if (driver_controller_type.upper() == "PS4") or (driver_controller_type.upper() == "PS5") \
            else (CommandXboxController(0))
        self.operator_controller = CommandPS4Controller(1) if (operator_controller_type.upper() == "PS4") or (operator_controller_type.upper() == "PS5") \
            else (CommandXboxController(1))
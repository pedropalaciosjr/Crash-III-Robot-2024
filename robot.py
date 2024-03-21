# Project started and written by Pedro Palacios Jr, Team 457.

from wpilib import (
    drive,
    SmartDashboard,
    Timer,
    TimedRobot,
    PS4Controller,
    Joystick,
    CameraServer,
    event,
    RobotState,
    reportWarning,
    SendableChooser
    )
import rev
from robot_code.main.initialization.constants import Constants as const
from robot_code.main.subsystems import drivetrain_subsystem, arm_subsystem, climber_subsystem, intake_subsystem, shooter_subsystem

class MyRobot(TimedRobot):
    def robotInit(self):
        global sparkmax_safety
        def robot_base(self):
            self.SPARKMAX_CONTROLLERS = [
                drivetrain_subsystem.LEFT_FRONT, 
                drivetrain_subsystem.LEFT_REAR, 
                drivetrain_subsystem.RIGHT_FRONT, 
                drivetrain_subsystem.RIGHT_REAR, 
                arm_subsystem.ARM_LEFT, 
                arm_subsystem.ARM_RIGHT,
                shooter_subsystem.SHOOTER_LEFT,
                shooter_subsystem.SHOOTER_RIGHT,
                intake_subsystem.INTAKE,
                climber_subsystem.CLIMBER
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
            self.driver_joystick = PS4Controller(0) if (driver_controller_type) == "PS4" else (Joystick(0))
            self.operator_joystick = PS4Controller(1) if (operator_controller_type) == "PS4" else (Joystick(1))

        def sparkmax_safety(self):
            motor_temperatures = []
            brownout_faults = []
            for sparkmax in self.SPARKMAX_CONTROLLERS:
                motor_temperatures.append((1.8 * sparkmax.getMotorTemperature()) + 32)
                brownout_faults.append(sparkmax.getFault(0))
            
            left_front_motor_temperature, left_rear_motor_temperature, right_front_motor_temperature, right_rear_motor_temperature,\
                launch_wheel_temperature, feeder_wheel_temperature, roller_claw_temperature, climber_temperature = motor_temperatures
            left_front_brownout, left_rear_brownout, right_front_brownout, right_rear_brownout, launch_wheel_brownout,\
                 feeder_wheel_brownout, roller_claw_brownout, climber_brownout = brownout_faults
            
            SmartDashboard.putNumber("Left Front Motor Temperature (F)", left_front_motor_temperature)
            SmartDashboard.putNumber("Left Rear Motor Temperature (F)", left_rear_motor_temperature)
            SmartDashboard.putNumber("Right Front Motor Temperature (F)", right_front_motor_temperature)
            SmartDashboard.putNumber("Right Rear Motor Temperature (F)", right_rear_motor_temperature)
            SmartDashboard.putNumber("Launch Wheel Motor Temperature (F)", launch_wheel_temperature)
            SmartDashboard.putNumber("Feeder Wheel Motor Temperature (F)", feeder_wheel_temperature)
            SmartDashboard.putNumber("Roller Claw Motor Temperature (F)", roller_claw_temperature)
            SmartDashboard.putNumber("Climber Motor Temperature (F)", climber_temperature)

            SmartDashboard.putBoolean("Left Front Brownout Detected:", left_front_brownout)
            SmartDashboard.putBoolean("Left Rear Brownout Detected:", left_rear_brownout)
            SmartDashboard.putBoolean("Right Front Brownout Detected:", right_front_brownout)
            SmartDashboard.putBoolean("Right Rear Brownout Detected:", right_rear_brownout)
            SmartDashboard.putBoolean("Launch Wheel Brownout Detected:", launch_wheel_brownout)
            SmartDashboard.putBoolean("Feeder Wheel Brownout Detected:", feeder_wheel_brownout)
            SmartDashboard.putBoolean("Roller Claw Brownout Detected:", roller_claw_brownout)
            SmartDashboard.putBoolean("Climber Brownout Detected:", climber_brownout)

            for state in brownout_faults:
                if state:
                    reportWarning("BROWNOUT DETECTED!")
                    return
                

        robot_base()
        sparkmax_safety()
        joystick_init(const.driver_controller_type, const.operator_controller_type)



    def teleopInit(self):
        self.drive = drivetrain_subsystem.DifferentialDriveSubsystem()
        current_time = Timer.getFPGATimestamp()
        SmartDashboard.putNumber("Robot Runtime (seconds):", current_time)

        sparkmax_safety()

    def teleopPeriodic(self):
        drivetrain_subsystem.DifferentialDriveSubsystem.ps4_drive(self.driver_joystick) if const.driver_controller_type == "PS4" else drivetrain_subsystem.DifferentialDriveSubsystem.logitech_drive(self.driver_joystick)
    
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
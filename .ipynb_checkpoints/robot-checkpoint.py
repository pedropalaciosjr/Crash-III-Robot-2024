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
    SendableChooser,
    PS5Controller
    )
import rev
from cscore import CameraServer
import commands2
# from commands2 import CommandPS4Controller
from robot_code.main.initialization.constants import Constants as const
from robot_code.main.subsystems import drivetrain_subsystem, climber_subsystem, autonomous_subsystem, launchfeeder_subsystem

class MyRobot(TimedRobot):
    def robotInit(self):
        global sparkmax_safety
        global stop
        global constants_class
        global drive

        self.drive = drivetrain_subsystem.DifferentialDriveSubsystem()
        self.launch_feed = launchfeeder_subsystem.LaunchFeederSubsystem()
        self.climber = climber_subsystem.ClimberSubsystem()
        self.auto = autonomous_subsystem.AutonomousSubsystem()

        self.SPARKMAX_CONTROLLERS = [
            self.drive.LEFT_FRONT, 
            self.drive.LEFT_REAR, 
            self.drive.RIGHT_FRONT, 
            self.drive.RIGHT_REAR, 
            self.launch_feed.FEEDER_WHEEL,
            self.launch_feed.LAUNCH_WHEEL,
            self.launch_feed.CLAW,
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

        
        def joystick_init(self, driver_controller_type = "null", operator_controller_type= "null" ):
            self.driver_joystick = PS4Controller(constants_class.DRIVER_CONTROLLER_PORT) if (driver_controller_type) == "PS4" else (XboxController(constants_class.DRIVER_CONTROLLER_PORT))
            self.operator_joystick = PS4Controller(constants_class.OPERATOR_CONTROLLER_PORT) if (operator_controller_type) == "PS4" else (XboxController(constants_class.OPERATOR_CONTROLLER_PORT))

        def sparkmax_safety(self):
            motor_temperatures = []
            brownout_faults = []
            for sparkmax in self.SPARKMAX_CONTROLLERS:
                motor_temperatures.append((1.8 * sparkmax.getMotorTemperature()) + 32)
                brownout_faults.append(sparkmax.getFault(rev.CANSparkBase.FaultID.kBrownout))
            
            left_front_motor_temperature, left_rear_motor_temperature, right_front_motor_temperature, right_rear_motor_temperature,\
                feeder_motor_temperature, launch_motor_temperature, claw_motor_temperature = motor_temperatures
            left_front_brownout, left_rear_brownout, right_front_brownout, right_rear_brownout, feeder_brownout, \
                 launch_brownout, claw_brownout = brownout_faults
            
            SmartDashboard.putNumber("Left Front Motor Temperature (F)", left_front_motor_temperature)
            SmartDashboard.putNumber("Left Rear Motor Temperature (F)", left_rear_motor_temperature)
            SmartDashboard.putNumber("Right Front Motor Temperature (F)", right_front_motor_temperature)
            SmartDashboard.putNumber("Right Rear Motor Temperature (F)", right_rear_motor_temperature)
            SmartDashboard.putNumber("Arm Left Motor Temperature (F)", feeder_motor_temperature)
            SmartDashboard.putNumber("Arm Right Motor Temperature (F)", launch_motor_temperature)
            SmartDashboard.putNumber("Shooter Left Motor Temperature (F)", claw_motor_temperature)
            # SmartDashboard.putNumber("Climber Right Motor Temperature (F)", climber_temperature)

            SmartDashboard.putBoolean("Left Front Brownout Detected:", left_front_brownout)
            SmartDashboard.putBoolean("Left Rear Brownout Detected:", left_rear_brownout)
            SmartDashboard.putBoolean("Right Front Brownout Detected:", right_front_brownout)
            SmartDashboard.putBoolean("Right Rear Brownout Detected:", right_rear_brownout)
            SmartDashboard.putBoolean("Arm Left Brownout Detected:", feeder_brownout)
            SmartDashboard.putBoolean("Arm Right Brownout Detected:", launch_brownout)
            SmartDashboard.putBoolean("Shooter Left Brownout Detected:", claw_brownout)
            # SmartDashboard.putBoolean("Climber Brownout Detected:", climber_brownout)

            for state in brownout_faults:
                if state:
                    reportWarning("BROWNOUT DETECTED!")
                    return
        
        def stop(self, motor_controllers):
            try:
                for sparkmax in motor_controllers:
                    sparkmax.stopMotor()
            except (TypeError):
                print("'stop' function invoked with invalid arguments. This function expects only iterable objects as arguments.")
            
            return

        constants_class = const()
        sparkmax_safety(self)
        joystick_init(self, constants_class.driver_controller_type, constants_class.operator_controller_type)

        # self.drive.setDefaultCommand(self.drive.drive_robot(self.driver_joystick, self.drive))
        # commands2.button.Trigger(self.driver_joystick.getSquareButton()).whileTrue(commands2.ParallelCommandGroup(self.launch_feed.launch(-constants_class.FEEDER_WHEEL_SPEED, self.launch_feed), \
        #                                                  self.launch_feed.feeder(-constants_class.FEEDER_WHEEL_SPEED, self.launch_feed)))
        # commands2.button.Trigger(self.driver_joystick.getTriangleButton()).whileTrue(self.launch_feed.feeder(constants_class.FEEDER_WHEEL_SPEED, self.launch_feed))
        # commands2.button.Trigger(self.driver_joystick.getCircleButton()).whileTrue(self.launch_feed.launch(constants_class.LAUNCH_WHEEL_SPEED, self.launch_feed))


    def robotPeriodic(self):
        # commands2.CommandScheduler.getInstance().run()

        pass

    def teleopInit(self):
        global start_time
        start_time = Timer()
        start_time.reset()
        start_time = start_time.getFPGATimestamp()
        drive.turbo_run = False
        # CameraServer.startAutomaticCapture()
        
    
    def teleopPeriodic(self):
        current_time = Timer.getFPGATimestamp()
        SmartDashboard.putNumber("Robot Runtime (seconds):", current_time)
        sparkmax_safety(self)

        self.drive.drive_robot(self.driver_joystick, start_time)
        self.launch_feed.launchfeed_robot(self.operator_joystick)
        
        # self.drive.drive_robot(self.driver_joystick)

        # self.shooter.shooterPeriodic(self.operator_joystick)
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

        match self.auto_mode_selected:
            case self.auto_mode_one:
                # Drive forward for 2 seconds at half speed
                if time_elapsed < 2:
                    print(time_elapsed)
                    self.drive.auto_drive(0.572, 0)
    
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
    def testInit(self):
        pass
        # commands2.CommandScheduler.getInstance().cancelAll()
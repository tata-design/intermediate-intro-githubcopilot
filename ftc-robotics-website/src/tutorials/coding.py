import streamlit as st

def show_coding_tutorial():
    """Display the comprehensive coding tutorial for FTC Robotics"""
    
    # Introduction section
    st.markdown(
        """
        <div style='background: linear-gradient(135deg, #e6f2ff 0%, #cce7ff 100%); 
                   padding: 1.5rem; border-radius: 12px; border-left: 4px solid #004080; margin-bottom: 2rem;'>
        <b>Welcome to FTC Robot Programming!</b><br>
        Learn to program your FTC robot using Java and the FTC SDK. This tutorial covers everything from basic 
        robot movement to advanced autonomous programming and sensor integration.
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Video tutorial at the beginning
    st.subheader("🎥 Getting Started with FTC Programming")
    st.markdown("Watch this comprehensive tutorial to begin your FTC programming journey:")
    
    # Embed the YouTube video
    st.video("https://youtu.be/poOy6CaGZkw")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Programming fundamentals section
    st.subheader("🚀 Programming Fundamentals")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(
            """
            <div style='background: white; padding: 1.3rem; border-radius: 12px; border-left: 4px solid #FF8310; 
                       box-shadow: 0 2px 8px rgba(0,0,0,0.1); margin-bottom: 1rem;'>
            <h4 style='color: #FF8310; margin-bottom: 1rem;'>📱 FTC SDK Basics</h4>
            <div style='font-size: 0.9rem; line-height: 1.5;'>
            • <strong>OpMode Structure:</strong> Learn the foundation of FTC programming<br>
            • <strong>Hardware Configuration:</strong> Set up motors, sensors, and servos<br>
            • <strong>TeleOp vs Autonomous:</strong> Understand different operation modes<br>
            • <strong>Android Studio Setup:</strong> Development environment configuration
            </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col2:
        st.markdown(
            """
            <div style='background: white; padding: 1.3rem; border-radius: 12px; border-left: 4px solid #1D63A8; 
                       box-shadow: 0 2px 8px rgba(0,0,0,0.1); margin-bottom: 1rem;'>
            <h4 style='color: #1D63A8; margin-bottom: 1rem;'>🎮 Robot Control</h4>
            <div style='font-size: 0.9rem; line-height: 1.5;'>
            • <strong>Gamepad Input:</strong> Process controller commands<br>
            • <strong>Motor Control:</strong> Drive trains and mechanism control<br>
            • <strong>Sensor Integration:</strong> IMU, encoders, and touch sensors<br>
            • <strong>PID Control:</strong> Precise movement and stabilization
            </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    # Code examples section
    st.subheader("📝 Essential Code Examples")
    
    # Basic TeleOp example
    st.markdown("### 🎮 Basic TeleOp Control")
    st.markdown("This example shows how to create a basic robot control system using gamepad input:")
    
    st.code("""
@TeleOp(name="My TeleOp", group="Linear Opmode")
public class MyTeleOp extends LinearOpMode {
    
    private DcMotor leftDrive = null;
    private DcMotor rightDrive = null;
    
    @Override
    public void runOpMode() {
        // Initialize the hardware variables
        leftDrive = hardwareMap.get(DcMotor.class, "left_drive");
        rightDrive = hardwareMap.get(DcMotor.class, "right_drive");
        
        // Set motor directions
        leftDrive.setDirection(DcMotor.Direction.REVERSE);
        rightDrive.setDirection(DcMotor.Direction.FORWARD);
        
        // Wait for the game to start (driver presses PLAY)
        waitForStart();
        
        // Run until the end of the match (driver presses STOP)
        while (opModeIsActive()) {
            
            // POV Mode uses left stick to go forward, and right stick to turn.
            double drive = -gamepad1.left_stick_y;
            double turn  =  gamepad1.right_stick_x;
            double leftPower    = Range.clip(drive + turn, -1.0, 1.0);
            double rightPower   = Range.clip(drive - turn, -1.0, 1.0);
            
            // Send calculated power to wheels
            leftDrive.setPower(leftPower);
            rightDrive.setPower(rightPower);
            
            // Show the elapsed game time and wheel power.
            telemetry.addData("Status", "Run Time: " + runtime.toString());
            telemetry.addData("Motors", "left (%.2f), right (%.2f)", leftPower, rightPower);
            telemetry.update();
        }
    }
}
""", language="java")
    
    # Hardware configuration example
    st.markdown("### ⚙️ Hardware Configuration")
    st.markdown("Properly configuring your robot's hardware is crucial for reliable operation:")
    
    st.code("""
public class RobotHardware {
    // Motors
    public DcMotor leftFrontDrive = null;
    public DcMotor rightFrontDrive = null;
    public DcMotor leftBackDrive = null;
    public DcMotor rightBackDrive = null;
    public DcMotor armMotor = null;
    
    // Servos
    public Servo clawServo = null;
    public Servo wristServo = null;
    
    // Sensors
    public IMU imu = null;
    public ColorSensor colorSensor = null;
    public DistanceSensor distanceSensor = null;
    
    // Hardware Map
    HardwareMap hwMap = null;
    
    public void init(HardwareMap ahwMap) {
        hwMap = ahwMap;
        
        // Initialize motors
        leftFrontDrive = hwMap.get(DcMotor.class, "left_front_drive");
        rightFrontDrive = hwMap.get(DcMotor.class, "right_front_drive");
        leftBackDrive = hwMap.get(DcMotor.class, "left_back_drive");
        rightBackDrive = hwMap.get(DcMotor.class, "right_back_drive");
        armMotor = hwMap.get(DcMotor.class, "arm_motor");
        
        // Set motor directions
        leftFrontDrive.setDirection(DcMotor.Direction.REVERSE);
        leftBackDrive.setDirection(DcMotor.Direction.REVERSE);
        rightFrontDrive.setDirection(DcMotor.Direction.FORWARD);
        rightBackDrive.setDirection(DcMotor.Direction.FORWARD);
        
        // Set motor run modes
        leftFrontDrive.setMode(DcMotor.RunMode.RUN_USING_ENCODER);
        rightFrontDrive.setMode(DcMotor.RunMode.RUN_USING_ENCODER);
        leftBackDrive.setMode(DcMotor.RunMode.RUN_USING_ENCODER);
        rightBackDrive.setMode(DcMotor.RunMode.RUN_USING_ENCODER);
        
        // Initialize servos
        clawServo = hwMap.get(Servo.class, "claw_servo");
        wristServo = hwMap.get(Servo.class, "wrist_servo");
        
        // Initialize sensors
        imu = hwMap.get(IMU.class, "imu");
        colorSensor = hwMap.get(ColorSensor.class, "color_sensor");
        distanceSensor = hwMap.get(DistanceSensor.class, "distance_sensor");
    }
}
""", language="java")
    
    # Autonomous programming section
    st.markdown("### 🤖 Autonomous Programming")
    st.markdown("Create intelligent autonomous routines that can navigate and complete tasks independently:")
    
    st.code("""
@Autonomous(name="Basic Autonomous", group="Linear Opmode")
public class BasicAutonomous extends LinearOpMode {
    
    private DcMotor leftDrive = null;
    private DcMotor rightDrive = null;
    private IMU imu = null;
    
    static final double COUNTS_PER_MOTOR_REV = 1440;
    static final double DRIVE_GEAR_REDUCTION = 2.0;
    static final double WHEEL_DIAMETER_INCHES = 4.0;
    static final double COUNTS_PER_INCH = (COUNTS_PER_MOTOR_REV * DRIVE_GEAR_REDUCTION) /
                                         (WHEEL_DIAMETER_INCHES * 3.1415);
    
    @Override
    public void runOpMode() {
        
        // Initialize hardware
        leftDrive = hardwareMap.get(DcMotor.class, "left_drive");
        rightDrive = hardwareMap.get(DcMotor.class, "right_drive");
        imu = hardwareMap.get(IMU.class, "imu");
        
        // Set motor directions and modes
        leftDrive.setDirection(DcMotor.Direction.REVERSE);
        rightDrive.setDirection(DcMotor.Direction.FORWARD);
        
        leftDrive.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
        rightDrive.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
        
        leftDrive.setMode(DcMotor.RunMode.RUN_USING_ENCODER);
        rightDrive.setMode(DcMotor.RunMode.RUN_USING_ENCODER);
        
        // Wait for start
        waitForStart();
        
        // Autonomous sequence
        if (opModeIsActive()) {
            // Drive forward 24 inches
            encoderDrive(0.5, 24, 24, 5.0);
            
            // Turn 90 degrees
            gyroTurn(0.3, 90);
            
            // Drive forward 12 inches
            encoderDrive(0.5, 12, 12, 3.0);
            
            telemetry.addData("Path", "Complete");
            telemetry.update();
        }
    }
    
    public void encoderDrive(double speed, double leftInches, double rightInches, double timeoutS) {
        int newLeftTarget;
        int newRightTarget;
        
        if (opModeIsActive()) {
            newLeftTarget = leftDrive.getCurrentPosition() + (int)(leftInches * COUNTS_PER_INCH);
            newRightTarget = rightDrive.getCurrentPosition() + (int)(rightInches * COUNTS_PER_INCH);
            
            leftDrive.setTargetPosition(newLeftTarget);
            rightDrive.setTargetPosition(newRightTarget);
            
            leftDrive.setMode(DcMotor.RunMode.RUN_TO_POSITION);
            rightDrive.setMode(DcMotor.RunMode.RUN_TO_POSITION);
            
            runtime.reset();
            leftDrive.setPower(Math.abs(speed));
            rightDrive.setPower(Math.abs(speed));
            
            while (opModeIsActive() && (runtime.seconds() < timeoutS) &&
                   (leftDrive.isBusy() && rightDrive.isBusy())) {
                
                telemetry.addData("Path1",  "Running to %7d :%7d", newLeftTarget,  newRightTarget);
                telemetry.addData("Path2",  "Running at %7d :%7d",
                                            leftDrive.getCurrentPosition(),
                                            rightDrive.getCurrentPosition());
                telemetry.update();
            }
            
            leftDrive.setPower(0);
            rightDrive.setPower(0);
            
            leftDrive.setMode(DcMotor.RunMode.RUN_USING_ENCODER);
            rightDrive.setMode(DcMotor.RunMode.RUN_USING_ENCODER);
        }
    }
}
""", language="java")
    
    # Sensor integration section
    st.subheader("🔍 Sensor Integration")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### IMU (Inertial Measurement Unit)")
        st.code("""
// Initialize IMU
IMU imu = hardwareMap.get(IMU.class, "imu");
IMU.Parameters parameters = new IMU.Parameters(
    new RevHubOrientationOnRobot(
        RevHubOrientationOnRobot.LogoFacingDirection.UP,
        RevHubOrientationOnRobot.UsbFacingDirection.FORWARD
    )
);
imu.initialize(parameters);

// Get robot heading
YawPitchRollAngles robotOrientation = imu.getRobotYawPitchRollAngles();
double heading = robotOrientation.getYaw(AngleUnit.DEGREES);

telemetry.addData("Heading", "%.2f degrees", heading);
""", language="java")
    
    with col2:
        st.markdown("#### Color Sensor")
        st.code("""
// Initialize color sensor
ColorSensor colorSensor = hardwareMap.get(ColorSensor.class, "color_sensor");

// Read color values
int red = colorSensor.red();
int green = colorSensor.green();
int blue = colorSensor.blue();
int alpha = colorSensor.alpha();

// Determine dominant color
if (red > green && red > blue) {
    telemetry.addData("Color", "Red detected");
} else if (blue > red && blue > green) {
    telemetry.addData("Color", "Blue detected");
} else {
    telemetry.addData("Color", "Unknown");
}
""", language="java")
    
    # Programming tips section
    st.subheader("💡 Advanced Programming Tips")
    
    st.markdown(
        """
        <div style='background: linear-gradient(135deg, #fff8e1 0%, #ffe4b5 100%); 
                   padding: 1.5rem; border-radius: 12px; border-left: 4px solid #FF8310; margin-bottom: 2rem;'>
        <h4 style='color: #FF8310; margin-bottom: 1rem;'>🏆 Pro Tips for Competition Success</h4>
        <div style='font-size: 1rem; line-height: 1.6;'>
        <strong>1. Code Organization:</strong> Use separate classes for hardware, autonomous routines, and utilities<br><br>
        <strong>2. Error Handling:</strong> Always check for null objects and handle exceptions gracefully<br><br>
        <strong>3. Telemetry:</strong> Use comprehensive telemetry for debugging and monitoring<br><br>
        <strong>4. Testing:</strong> Test each component individually before integrating<br><br>
        <strong>5. Documentation:</strong> Comment your code thoroughly for team collaboration
        </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Best practices section
    st.subheader("📋 Best Practices Checklist")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(
            """
            <div style='background: white; padding: 1.3rem; border-radius: 12px; border-left: 4px solid #28a745; 
                       box-shadow: 0 2px 8px rgba(0,0,0,0.1);'>
            <h4 style='color: #28a745;'>✅ Development Practices</h4>
            <div style='font-size: 0.9rem; line-height: 1.5;'>
            ✓ Use meaningful variable names<br>
            ✓ Implement proper error checking<br>
            ✓ Test on actual hardware frequently<br>
            ✓ Version control with Git<br>
            ✓ Regular code reviews with team<br>
            ✓ Document hardware configurations
            </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col2:
        st.markdown(
            """
            <div style='background: white; padding: 1.3rem; border-radius: 12px; border-left: 4px solid #dc3545; 
                       box-shadow: 0 2px 8px rgba(0,0,0,0.1);'>
            <h4 style='color: #dc3545;'>⚠️ Common Pitfalls to Avoid</h4>
            <div style='font-size: 0.9rem; line-height: 1.5;'>
            ✗ Hardcoding values without constants<br>
            ✗ Ignoring encoder overflow<br>
            ✗ Not handling sensor disconnections<br>
            ✗ Blocking the main thread too long<br>
            ✗ Forgetting to update telemetry<br>
            ✗ Not testing edge cases
            </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    # Resources section
    st.subheader("📚 Learning Resources")
    
    st.markdown(
        """
        <div style='background: linear-gradient(135deg, #e6f2ff 0%, #cce7ff 100%); 
                   padding: 1.5rem; border-radius: 12px; border-left: 4px solid #004080; margin-bottom: 2rem;'>
        <h4 style='color: #004080; margin-bottom: 1rem;'>🔗 Essential Links</h4>
        <div style='font-size: 1rem; line-height: 1.8;'>
        • <strong>Official FTC SDK Documentation:</strong> <a href="https://ftctechnh.github.io/ftc_app/doc/javadoc/index.html" target="_blank" style="color: #004080;">FTC Java Docs</a><br>
        • <strong>FTC Programming Resources:</strong> <a href="https://www.firstinspires.org/resource-library/ftc/technology-information-and-resources" target="_blank" style="color: #004080;">FIRST Tech Challenge</a><br>
        • <strong>Game Manual:</strong> <a href="https://www.firstinspires.org/resource-library/ftc/game-and-season-info" target="_blank" style="color: #004080;">Current Season Rules</a><br>
        • <strong>Hardware Guide:</strong> <a href="https://www.revrobotics.com/ftc/" target="_blank" style="color: #004080;">REV Robotics FTC Hub</a><br>
        • <strong>Programming Tutorials:</strong> <a href="https://gm0.org/en/latest/" target="_blank" style="color: #004080;">Game Manual 0 (GM0)</a>
        </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Call to action
    st.markdown(
        """
        <div style='background: linear-gradient(135deg, #1D63A8 0%, #0f4d8c 100%); 
                   padding: 2rem; border-radius: 15px; text-align: center; margin: 2rem 0;
                   box-shadow: 0 4px 15px rgba(29, 99, 168, 0.3);'>
        <h3 style='color: white; margin-bottom: 1rem;'>Ready to Start Your Robotics Journey? 🤖</h3>
        <p style='color: white; font-size: 1.1rem; margin-bottom: 1.5rem;'>
        Join our community and get access to comprehensive tutorials, expert guidance, and start building amazing robots today!
        </p>
        <p style='color: #FF8310; font-weight: bold; font-size: 1.2rem;'>
        Your next breakthrough is just one tutorial away! �
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Add signup button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 Join BotBuilders Hub", use_container_width=True, type="primary", key="coding_signup_btn"):
            st.switch_page("pages/signup.py")

# This allows the module to be run independently for testing
if __name__ == "__main__":
    import streamlit as st
    show_coding_tutorial()
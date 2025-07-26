    public class MyTeleOp extends OpMode {
        @Override
        public void init() {
            // Initialize hardware components
        }

        @Override
        public void loop() {
            // Control robot movement
            double drive = -gamepad1.left_stick_y;
            double turn = gamepad1.right_stick_x;
            double leftPower = drive + turn;
            double rightPower = drive - turn;

            leftMotor.setPower(leftPower);
            rightMotor.setPower(rightPower);
        }
    }
# PicoRosBridge for Skid-Steer Mobile Robot

This firmware is a complete adaptation of the ROS Arduino Bridge for the Raspberry Pi Pico, specially modified for a 4-wheel skid-steer robot using an MDD20A Dual Channel Motor Driver.

## Hardware Configuration
This code handles:
* **4 x L-shape Waveshare 12V gear motors**
* **1 x MDD20A motor driver**
* **2 rear wheel encoders**
* **Communication via Serial over USB** to ROS 2 Humble.

### Pi Pico Pin Mapping

#### Motors (MDD20A)
The Pico controls the motors using PWM and DIR pins.
**Left Motors Channel (M1):**
- `PWM 1`: Pin 2
- `DIR 1`: Pin 3

**Right Motors Channel (M2):**
- `PWM 2`: Pin 8
- `DIR 2`: Pin 9

#### Encoders
Encoders use hardware interrupts for high-speed tracking.
- **Left Rear Encoder**
  - Channel A: Pin 14
  - Channel B: Pin 15
- **Right Rear Encoder**
  - Channel A: Pin 16
  - Channel B: Pin 17
  *(Note: The firmware automatically handles the inverted counting on the right side based on your requirement)*.

#### Status LEDs and Relays (Indicators)
The firmware supports external LED indicators for robot state and movement direction.
- **Heartbeat & Status:**
  - `ONBOARD_LED`: Default Pico LED (Heartbeat every 500ms)
  - `EXTRA_STATUS_LED`: Pin 27 (Mirrors onboard LED)
- **LED Strip Relays (Directional Indicators):**
  - `RELAY1` (Left Strip): Pin 20
  - `RELAY2` (Right Strip): Pin 21
  
  *Relay Behavior based on kinematics:*
  - **Idle:** Off
  - **Forward:** Both solid ON
  - **Backward:** Both flashing (warning mode)
  - **Turning Left:** Left flashing, Right solid ON
  - **Turning Right:** Right flashing, Left solid ON

## ROS 2 Integration Parameters
You provided specific hardware values:
* Left rear count: **~ 562**
* Right rear count: **~ -560** (Inverted; handled automatically by firmware now)
* Wheel diameter: **130 mm (0.13 meters)**
* Track width (Distance between wheels): **24.5 cm (0.245 meters)**

In your ROS 2 bridge Python parameter file (usually `my_robot_params.yaml`), make sure to configure these settings:

```yaml
base_controller:
  ros__parameters:
    # 24.5 cm track width
    base_width: 0.245
    # Ticks per meter = encoder ticks per rev / (pi * wheel diameter)
    # Using 562 ticks per revolution: 562 / (3.14159 * 0.13) = ~1376.1
    ticks_meter: 1376 
    
    # Optional PID Tuning
    Kp: 20
    Kd: 12
    Ki: 0
    Ko: 50
```

## How to Flash in Arduino IDE
1. Open the Arduino IDE.
2. Ensure you have installed the **rp2040 (Raspberry Pi Pico)** board support in the Boards Manager.
3. Open `PicoRosBridge.ino`
4. Select board: `Raspberry Pi Pico`
5. Compile and Upload to the Pico.

The Pico will now act as the `ros_arduino_bridge` brain, receiving velocity commands from ROS 2 and publishing accurate odometry back!

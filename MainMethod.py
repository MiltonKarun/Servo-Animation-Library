import EasingFunctions as easing
from EasedServo import *
from collections import deque
from QueueServo import *


if __name__ == '__main__':

    queue_servo = QueueServo(servo2040.SERVO_1)
    queue_servo.queue_angle(-90, 4000, easing.linear)
    queue_servo.queue_angle(90, 4000, easing.easeInExpo)
    queue_servo.queue_angle(-90, 4000, easing.easeOutExpo)
    queue_servo.process_queue()
    print("Done")

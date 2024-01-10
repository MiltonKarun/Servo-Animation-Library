import EasingFunctions as easing
import time
from EasedServo import *
import time
from collections import deque

class QueueServo(EasedServo):
    def __init__(self, pin, angle=90):  
        super().__init__(pin, angle)
        self.angle_queue = deque((),1000)  # Using deque with max length 1000

    def queue_angle(self, angle, duration, easing_function):
        """Queue up angles to move sequentially."""
        self.angle_queue.append((angle, duration, easing_function)) # Adding Eased Servo Paramenters to angle_queue

    def process_queue(self):
        if self._isMoving == True:
            while self.angle_queue:
                angle, duration, easing_function = self.angle_queue.popleft()  # Using popleft() to remove from the left end
                self.ease_to(angle, duration, easing_function)
                while self._isMoving:
                    self.update()
                    time.sleep(0.01)
                time.sleep_ms(300)
            else:
                if self.angle!=90:
                    self.go_home() #Go to home after all queue servo execution

        # Detach the Servo
        self.detach_servo()



    def flush_queue(self):
        #self.angle_queue.clear()
        print("Queue Emptied")

    def pause_queue(self):
        self._isMoving = False
        print("Queue Paused")

    def resume_queue(self):
        self._isMoving = True
        print("Queue Resumed")

    def go_home(self):
        self.ease_to(90,4000,easing.linear)
        while self._isMoving:
                self.update()
                time.sleep(0.01)
        print("Reached Home")
        pass

    def detach_servo(self):
        self._servo.disable()
        print("Servo Detached")
        pass


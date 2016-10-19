#!/usr/bin/python
import gi
import glob

gi.require_version('Notify', '0.7')
from gi.repository import Notify, GdkPixbuf

def get_capacity_level():
        batteries = glob.glob("/sys/class/power_supply/*/capacity")
        combined_capacity = 0
        for work_file in batteries:
            with open(work_file, 'r') as f:
                read_data = f.read().rstrip()
                combined_capacity += int(read_data)
        return combined_capacity

def charging():
        batteries = glob.glob("/sys/class/power_supply/*/status")
        charging = 0
        for work_file in batteries:
            with open(work_file, 'r') as f:
                read_data = f.read().rstrip()
                if read_data == "Charging":
                    charging = 1
        return charging



def alert(capacity):
    Notify.init("Low battery")
    capacity=Notify.Notification.new("Combined capacity level", str(capacity), "dialog-warn")
    capacity.set_timeout(59)
    capacity.set_urgency(2)
    capacity.show()

def main():
    capacity=get_capacity_level()
    if capacity < 20 and not charging():
        alert(capacity)

if __name__ == "__main__":
    main()

from tkinter import *
import tkinter as tk
import alarm
import timer


def main():
    root = tk.Tk()
    root.title('Clock')

    # Framework
    mainframe = tk.Frame(root)
    mainframe.grid(column=0, row=0)

    # Create frames
    alarm_frame = tk.Frame(mainframe)
    alarm_frame.grid(column=1, row=1)

    # Create instances
    clock = alarm.Clock(12)
    clock_time = clock.time_now()
    # clock_alarm = clock.create_alarm('Alarm 1', 11, 50)
    # print(clock.alarms)

    time_display = tk.Label(alarm_frame, text=clock_time)
    time_display.grid(column=1, row=1)

    time_display.after(1000, clock.time_now)

    root.mainloop()


if __name__ == '__main__':
    main()

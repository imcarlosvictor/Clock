from tkinter import *
import tkinter as tk
import alarm
import timer


def main():
    root = tk.Tk()
    root.title('Clock')

    # Framework
    mainframe = tk.Frame(root)

    # Create frames
    alarm_frame = tk.Frame(mainframe)
    alarm_frame.grid(column=1, row=1)

    # Create instances
    clock = alarm.Clock()
    clock_format = clock.format_time(12)
    clock_time = clock.time_now()

    alarm_frame['text'] = clock_time

    root.mainloop()


if __name__ == '__main__':
    main()

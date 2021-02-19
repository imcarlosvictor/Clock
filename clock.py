import time
from typing import Dict


class Time:
    """Grabs the current time using the time module.

    Methods:
        get_time_12hr():
            Grabs the time and displays it in a 12hr format
            as a string
        get_time_24hr():
            Grabs the time and displays it in a 24hr format
            as a string

    """

    def get_time_12hr(self):
        """Gets the current time.

        Returns:
            Current time in 12hr format.
        """

        cur_time = time.strftime('%I:%M:%S')
        return cur_time

    def get_time_24hr(self):
        """Gets the current time in 24hr format.

        Returns:
            Current time in 24hr format.
        """

        cur_time = time.strftime('%H:%M:%S')
        return cur_time


class Clock:
    """This is a clock.

    Attributes:
        alarms: stores all alarms created by the user.

    Methods:
        format_time():
            Allows user to change the format of the time.
        time_now():
            Grabs the current time using the time library
        create_alarm():
            Create an alarm and store to alarm dictionary
        delete_alarm():
            Delete an alarm from alarms dictionary
        edit_alarm():
            Edit an existing alarm by changing either its
            alarm name or alarm time.
        next_alarm():
            Display the remaining time left before the next
            alarm.
        ring():
            If the current time matches with any alarm time in
            alarms dicitonary, give off an ring.
    """

    def __init__(self):
        self.format = 12
        self.get_time = Time()  # Create Time instance
        self.alarms: Dict[str, str] = {}

    def format_time(self, hr_format: str) -> str:
        """Sets the time format to either the 12hr of 24hr format.

        Args:
            alarm_clock: Pass instance of clock
            hr_format: Either a 12hour of 24hour format.

        Returns:
            Time in the format of the user's choosing.
        """

        if hr_format == 12:
            new_format = self.get_time.get_time_12hr()
            # update label
        else:
            # time_format = time.strftime('%I:%M:%S')
            self.format = 24
            new_format = self.get_time.get_time_24hr()
            # update label

        self.clock_time = new_format
        return self.clock_time

    def time_now(self):
        """Grabs the time."""

        if self.format == 12:
            current_time = self.get_time.get_time_12hr()
        else:
            current_time = self.get_time.get_time_24hr()

        return current_time

    def create_alarm(self):
        """Creates an alarm preset and adds it to the dict of
        existing alarms.

        Returns:
            Creates a new alarm with an alarm name and alarm time.

        Raises:

        """

        # Store values from the entry label
        name_of_alarm: str = ''
        hour: str = ''
        minutes: str = ''
        time_of_day: str = ''

        new_alarm: str = hour + ':' + minutes + time_of_day

        # Check if alarm already exists in a list
        if name_of_alarm in self.alarms:
            err_name = 'Alarm name already exists.'
            print(err_name)
        elif new_alarm in self.alarms:
            err_alarm_time = 'Alarm already exists.'
            print(err_alarm_time)

        self.alarms[name_of_alarm] = new_alarm

    def delete_alarm(self, alarm_name: str):
        """Deletes an existing alarm.

        Args:
            alarm_name: an existing alarm from the alarms Dict

        Raises:
            IndexError: If the key does not exist in alarms.
        """

        try:
            self.alarms.pop(alarm_name)
        except IndexError:
            print('Alarm does not exist.')
        else:
            success_msg = 'Alarm deleted!'
            return success_msg

    def edit_alarm(self, alarm_name: str):
        """Edits an alarm.

        Args:
            alarm: an existing alarm from the alarms list.
        """
        pass

    def next_alarm(self):
        """Displays the time left before the next alarm."""

        # Subtract current time from next alarm
        pass

    def ring(self):
        """Ring once the current time aligns with the alarm."""

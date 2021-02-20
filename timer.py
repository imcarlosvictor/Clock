from datetime import datetime
from typing import Dict, List


class Timer:
    """This is a timer.

    Attributes:
        presets: Holds all presets created by the user.
        counter: Current count for countdown
        running: State variable for the timer
        active_preset: Holds all user presets.
        progress_bar: Displays the remaning time left.

    Methods:
        counter():
            Adjusts and format the time for the counter
        create_preset():
            Creates a preset that consists of a name and time to
            start countdown.
        delete_preset():
            Delete an existing preset.
        edit_preset():
            Edit an existing preset.
        use_preset():
            Pass the time to the counter to start a new session.
        start():
            Start timer
        pause():
            Pauses timer
        resume():
            Resumes timer if paused
        stop():
            Stop and reset timer to the active_preset.
    """

    def __init__(self):
        self.counter = 0  # Sets the counter number
        self.running = False

        self.presets: Dict[str, List[int]] = {}

        # Allow user to add a timer w/o creating a preset
        self.active_preset = ''

    def counter_label(self, label):
        """Starts the countdown.

        Returns:
            String format of the time.
        """
 
        # loop to update a label every second
        def count():
            """Starts count."""

            while self.running:

                # Display time in the proper format
                time = datetime.fromtimestamp(self.counter)
                time_string = time.strftime('%H:%M:%S')
                display_time = time_string

                # Update display and label every second
                label['text'] = display_time
                label.after(1000, count)

                # Updates instance counter
                self.counter -= 1

        # Start count
        count()

    def create_preset(self, preset_name: str, hour: int, minute: int, seconds: int):
        """Allows user to create a preset.

        Args:
            preset_name: Name of preset.
            hour: Hour of preset.
            minute: Minute of preset.
            seconds: Seconds of preset.

        Raises:
            NameError: If preset_name is == ''
            ValueError: If preset time is == 00:00:00
        """

        # NameError if name is empty
        if preset_name == '':
            raise NameError('Enter a title for the preset.')

        # ValueError if time is 00:00:00
        if hour == 0 and minute == 0 and seconds == 0:
            raise ValueError('Preset cannot be 00:00:00.')

        # Convert args to str and pass convert to a list
        # new_preset = map(str, [hour, minute, seconds])
        new_preset = hour, minute, seconds
        preset_time = list(new_preset)  # format [00,00,00] [hr,min,sec]

        # Add to the list of presets
        self.presets[preset_name] = preset_time

    def delete_preset(self, preset_name: str):
        """Delete an existing preset from the preset dictionary.

        Raises:
            KeyError: If key does not exist in the dictionary.
        """

        if preset_name in self.presets:
            self.presets.pop(preset_name)
        else:
            raise KeyError('Preset name does not exist.')

    def edit_preset(self):
        """Edit an existing preset by either changing the name or
        time specified.
        """

        pass

    def use_preset(self, preset_name: str):
        """Pick a preset for the counter."""

        # set active_preset
        active = self.presets[preset_name]
        self.active_preset = active
        # adjust time from label to the timer on the preset

    def start(self, counter, label):
        """Start timer."""

        # Find out how to start a timer
        self.running = True
        self.counter_label(counter, label)
        lbl_start['state'] = 'disabled'
        lbl_pause['state'] = 'enabled'
        lbl_resume['state'] = 'disabled'
        lbl_stop['state'] = 'enable'

    def pause(self):
        """Pause timer."""

        self.running = False
        lbl_start['state'] = 'disabled'
        lbl_pause['state'] = 'enabled'
        lbl_resume['state'] = 'disabled'
        lbl_stop['state'] = 'enable'

    def resume(self, counter, label):
        """Resume timer if paused."""

        self.running = True
        self.counter_label(counter, label)
        lbl_start['state'] = 'disabled'
        lbl_pause['state'] = 'enabled'
        lbl_resume['state'] = 'disabled'
        lbl_stop['state'] = 'enable'

    def stop(self):
        """Stop the timer and reset."""

        self.running = False
        lbl_start['state'] = 'disabled'
        lbl_pause['state'] = 'enabled'
        lbl_resume['state'] = 'disabled'
        lbl_stop['state'] = 'enable'

    def ring(self):
        """Rings once time runs out.

        Args:
            preset_name:
        """
        # from active_preset start countdown, once countdown
        # reaches 0, ring!
        pass

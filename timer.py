from datetime import datetime
from typing import Dict, List


class Timer:
    """This is a timer.

    Attributes:
        presets: Holds all presets created by the user.
        count: Current count for countdown

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
        self.presets: Dict[str, List[int]] = {}

        # Allow user to add a timer w/o creating a preset
        self.active_preset = ''

    def counter_label(self, counter, label) -> str:
        """Starts the countdown.

        Returns:
            String format of the time.
        """
 
        # loop to update a label every second
        def count():
            """Starts count."""

            running = True
            while running:

                # Display time in the proper format
                time = datetime.fromtimestamp(counter)
                time_string = time.strftime('%H:%M:%S')
                display_time = time_string

                # Update display and label every second
                label['text'] = display_time
                label.after(1000, count)

                counter += 1

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

        # NameError
        if preset_name == '':
            raise NameError('Enter a title for the preset.')

        # ValueError
        if hour == '00' and minute == '00' and seconds == '00':
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
        self.active_preset = preset_name
        # adjust time from label to the timer on the preset

    def start(self):
        """Start timer."""

        # Find out how to start a timer
        pass

    def pause(self):
        """Pause timer."""


        pass

    def resume(self):
        """Resume timer if paused."""


        pass

    def stop(self):
        """Stop the timer and reset."""


        pass

    def ring(self):
        """Rings once time runs out.

        Args:
            preset_name:
        """
        # from active_preset start countdown, once countdown
        # reaches 0, ring!
        pass

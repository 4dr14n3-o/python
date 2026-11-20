
class Television:
    #Class variables
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        '''Initialize the television with its default settings.'''
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        '''Turn the television on or off.'''
        self.__status = not self.__status

    def mute(self):
        '''Mute or unmute the television when it is on.'''
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
        '''Increase the channel when the television is on.

	If the max channel is reached, return to the min channel.'''

        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        '''Decrease the channel when the television is on.

	If the min channel is reached, return to the max channel.'''

        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self):
        '''Increase the volume and unmute the television, if necessary.

	Automatically unmute the television when adjusting the volume.

        Volume cannot exceed the max volume.'''

        if self.__status:
            self.__muted = False

            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        '''Decrease the volume and unmute the television, if necessary.

	Automatically unmute the television when adjusting the volume.

        Volume cannot go below the min volume.'''

        if self.__status:
            self.__muted = False

            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        '''Return the current television settings as string.
	Return current power, channel, and volume settings.'''

        return (f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}")

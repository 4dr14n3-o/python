import pytest
from television import Television


#Test the default television settings
def test_init():
    tv = Television()

    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


#Test turning the television on and off
def test_power():
    tv = Television()

    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    tv.power()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


#Test muting/unmuting the television.
def test_mute():
    tv = Television()

    #Mute while television is off.
    tv.mute()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    #Turn television on. Increase volume.
    tv.power()
    tv.volume_up()

    #Mute television.
    tv.mute()

    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    #Unmute television
    tv.mute()

    assert str(tv) == "Power = True, Channel = 0, Volume = 1"


#Test increasing the channel.
def test_channel_up():
    tv = Television()

    #Channel increase changes when television is off.
    tv.channel_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    #Turn television on. Increase channel.
    tv.power()
    tv.channel_up()

    assert str(tv) == "Power = True, Channel = 1, Volume = 0"

    #Increase channel after max channel.
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()

    assert str(tv) == "Power = True, Channel = 0, Volume = 0"


#Test decreasing the channel
def test_channel_down():
    tv = Television()

    #When television is off, no channel decrease occurs.
    tv.channel_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    #Turn television on. Decrease channel.
    tv.power()
    tv.channel_down()

    assert str(tv) == "Power = True, Channel = 3, Volume = 0"

    #Decrease channel.
    tv.channel_down()

    assert str(tv) == "Power = True, Channel = 2, Volume = 0"


#Test increasing the volume
def test_volume_up():
    tv = Television()

    #No volume increase should occur when television is off
    tv.volume_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    #Turn television on. Increase volume.
    tv.power()
    tv.volume_up()

    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    #Increase volume.
    tv.volume_up()

    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

    #Increase past max volume.
    tv.volume_up()

    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

    #Mute television.
    tv.mute()

    #Increase volume while muted.
    tv.volume_up()

    #Television should automatically unmute
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"


#Test decreasing the volume.
def test_volume_down():
    tv = Television()

    #No volume decrease should occur when television is off.
    tv.volume_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    #Turn television on. Increase volume to maximum.
    tv.power()
    tv.volume_up()
    tv.volume_up()

    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

    #Decrease volume.
    tv.volume_down()

    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    #Mute television.
    tv.mute()

    #Decrease volume while tv is muted.
    tv.volume_down()

    #Television should automatically unmute
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    #Decrease volume past minimum.
    tv.volume_down()

    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

#!/usr/bin/env python3
"""
A module with some classes and stuff
"""

class Cat():
    """
    a Cat class
    """

    lives_left = -1
    nr_of_paws = 4


    def __init__(self, eye_color, name, lives_left):
        self.eye_color = eye_color
        self.name = name
        self._lives_left = lives_left

    #Get method for number of lives left
    @property
    def number_lives(self):
        """
        shows number of lives
        """
        return self._lives_left

    #Set method for number of lives left

    @number_lives.setter
    def number_lives(self, new_number):
        """
        number of lives setter
        """
        self._lives_left = new_number


    def description(self):
        """
        description method
        """
        n = self.name
        e = self.eye_color
        l = self._lives_left

        return "My cats name is "+n+", has "+e+" eyes and "+str(l)+" lives left to live."


class Duration():
    """
    A duration class
    """

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds


    def display(self):
        """
        display method
        """
        h = self.hours
        m = self.minutes
        s = self.seconds

        if h < 10:
            h = "0"+str(h)
        elif m < 10:
            m = "0"+str(m)
        elif s < 10:
            s = "0"+str(s)

        string = str(h)+"-"+str(m)+"-"+str(s)
        self.hours = int(h)
        self.minutes = int(m)
        self.seconds = int(s)

        return string


    def duration_to_sec(self):
        """
        converts duration to seconds
        """

        hour_to_seconds = self.hours * 3600
        minutes_to_seconds = self.minutes * 60
        total_seconds = hour_to_seconds + minutes_to_seconds + self.seconds

        return total_seconds

    def __add__(self, other):
        self.hours += other.hours
        self.minutes += other.minutes
        self.seconds += other.seconds

        return self

#!/usr/bin/env -P /usr/bin:/usr/local/bin python3 -B
# coding: utf-8

#
#  Fusee.py
#  Fusee version 1.0
#  Created by Ingenuity i/o on 2023/11/06
#
# Agent fusee
#
import ingescape as igs
import keyboard


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Fusee(metaclass=Singleton):
    def __init__(self):
        # inputs
        self.a = 0
        self.Set_IDI = None

        # outputs
        self._ID_fuseeO = "UNSET"

    # outputs
    def set_keyPressedO(self):
        igs.output_set_impulsion("keyPressed")
    def update (self):
        if self._ID_fuseeO == "UNSET":
            igs.output_set_string("ID_fusee", self._ID_fuseeO)
        else :
            if keyboard.is_pressed("a"):
                if self.a == 0:
                    self.set_keyPressedO()
                self.a = 1
            else:
                if self.a == 1:
                    self.set_keyPressedO()
                self.a = 0


    @property
    def ID_fuseeO(self):
        return self._ID_fuseeO

    @ID_fuseeO.setter
    def ID_fuseeO(self, value):
        self._ID_fuseeO = value
        if self._ID_fuseeO is not None:
            igs.output_set_string("ID_fusee", self._ID_fuseeO)




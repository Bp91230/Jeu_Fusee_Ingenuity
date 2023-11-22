#!/usr/bin/env -P /usr/bin:/usr/local/bin python3 -B
# coding: utf-8

#
#  Moteur.py
#  Moteur version 1.0
#  Created by Ingenuity i/o on 2023/11/06
#
# "no description"
#
import ingescape as igs
import math


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Moteur(metaclass=Singleton):
    def __init__(self):
        self.fuseeStrengh = 10
        self.i = 0
        self.moteurOn = ()
        self.PosFusee = ()
        self.IDFusee = ()

        # inputs_setIDO
        self.IDI = "UNSET"
        self.InfoPlanetI = None

        # outputs
        self._setIDO = None

    def bougerFusees(self):
        x, y, vx, vy, orient = self.PosFusee
        ax = self.moteurOn * math.cos(orient) * self.fuseeStrengh
        ay = self.moteurOn * math.sin(orient) * self.fuseeStrengh

        for planetX, planetY, strengh in self.InfoPlanetI:
            angle = math.atan((planetY - y) / (planetX - x))
            ax = ax + (strengh / ((x - planetX) ** 2 + (y - planetY) ** 2)) * math.cos(angle)
            ay = ay + (strengh / ((x - planetX) ** 2 + (y - planetY) ** 2)) * math.sin(angle)

        vx = vx + ax * (1 / 30)
        vy = vy + ay * (1 / 30)

        self.PosFusee[0] = int(vx / (1 / 30) + x)
        self.PosFusee[1] = int(vy / (1 / 30) + y)
        self.PosFusee[2] = vx
        self.PosFusee[3] = vy
        self.PosFusee[4] = orient + math.atan(ay / ax)

        arguments_list = (self.IDFusee, self.PosFusee[0], self.PosFusee[1])
        igs.service_call("Whiteboard", "moveTo", arguments_list, "")

    def checkCollision(self,points, centre, rayon):
        cx, cy = centre
        for point in points:
            x, y = point
            distance = math.sqrt((x - cx) ** 2 + (y - cy) ** 2)
            if distance <= rayon:
                return False  # Au moins un point est à l'extérieur du cercle
        return True  # Tous les points sont à l'intérieur du cercle

    def update(self):
        #IDI_temp = self.IDI
        #IDI_temp = "UNSET"
        #CoordPlanet_temp = self.CoordPlanetI

        if self.IDI == "UNSET":
            arguments_list = ("https://cdn.futura-sciences.com/sources/images/starship-space-x.PNG", 100, 100)
            new_ID = igs.service_call("Whiteboard", "addImageFromUrl", arguments_list, "")
            #self.setIDO(new_ID)
            print(new_ID)
            self.PosFusee = (100, 100, 0., 0., 0.)
            self.IDFusee = new_ID
            self.MoteurOn = False
            if new_ID == 0:
             self.IDI = "SET"


        #self.bougerFusees()

        #self.checkCollision()

    def keyPressed(self):
        pass #moteurOn = not moteurOn

    # outputs
    @property
    def setIDO(self):
        return self._setIDO

    @setIDO.setter
    def setIDO(self, value):
        self._setIDO = value
        if self._setIDO is not None:
            igs.output_set_string("setID", self._setIDO)
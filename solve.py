import numpy as np
import json

from .score import Car, Score, Ride, check_ride_ids, check_vehicles, eval_ride


    def read_input(self):
        with open(self.input_str, 'r') as f:
            first_line = f.readline()

            self.rows, self.columns, self.vehicles, self.rides, self.bonus, self.steps = tuple(
                map(int, first_line.split(' '))
            )

            self.rides_list = []
            for i in range(self.rides):
                self.rides_list.append(tuple(
                    map(int, f.readline().rstrip().split(' '))
                ))
            self.scheduling = [[] for _ in range(self.vehicles)]

        print("Problem statement:")
        print("Map: {}".format((self.rows, self.columns)),
              "Vehicles: {}".format(self.vehicles),
              "Rides: {}".format(self.rides),
              "Bonus: {}".format(self.bonus),
              "Steps: {}".format(self.steps))
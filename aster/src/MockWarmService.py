import random

class MockWarmService():
    def __init__(self):
        pass

    def openContact(self):
        print("Opening contacts")

    def closeContact(self):
        print("Closing contacts")


    def analog_read(self):
        pres = 4.0
        flow = 1.0
        return pres, flow

    def ser_read(self):
        t_plate = self.rand_temp()
        t_1 = self.rand_temp()
        c_1 = self.rand_co2()
        t_2 = self.rand_temp()
        c_2 = self.rand_co2()
        t_3 = self.rand_temp()
        c_3 = self.rand_co2()
        t_4 = self.rand_temp()
        c_4 = self.rand_co2()
        t_5 = self.rand_temp()
        c_5 = self.rand_co2()
        t_6 = self.rand_temp()
        c_6 = self.rand_co2()
        t_7 = self.rand_temp()
        c_7 = self.rand_co2()
        t_8 = self.rand_temp()
        c_8 = self.rand_co2()
        return t_plate, t_1, c_1, t_2, c_2, t_3, c_3, t_4, c_4, t_5, c_5, t_6, c_6, t_7, c_7, t_8, c_8

    def rand_co2(self):
        return round(random.uniform(1, 6), 1)

    def rand_temp(self):
        return round(random.uniform(35, 40), 1)
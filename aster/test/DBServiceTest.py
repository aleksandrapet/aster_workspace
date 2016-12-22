import unittest
from aster.src.DBService import DBService

class DBServiceTest(unittest.TestCase):
    def test1(self):
        dbService = DBService()
        dbService.read_latest_box_data(1)
        dbService.read_latest_box_data(2)
        dbService.read_latest_box_data(3)
        dbService.read_latest_box_data(4)
        dbService.read_latest_box_data(5)
        dbService.read_latest_box_data(6)
        dbService.read_latest_box_data(7)
        dbService.read_latest_box_data(8)

import logging
import psycopg2

class DBService:
    def __init__(self):
        FORMAT = '%(asctime)-15s %(message)s'
        logging.basicConfig(format=FORMAT,level=logging.DEBUG)
        self.logger = logging.getLogger("DBService")

    def insert_box_data(self, reading_time, position, temp, co2):
        con = None
        try:
            logging.info("Inserting box data: (%s, %s, %s, %s)", reading_time, position, temp, co2)
            con = self.create_connection()
            cur = con.cursor()
            query = "INSERT INTO box_readings(reading_time, position, temp, co2) VALUES(%s, %s, %s, %s)"
            cur.execute(query, (reading_time, position, temp, co2))
            con.commit()
        except psycopg2.DatabaseError, e:
            print 'Error %s' % e

        finally:
            if con:
                con.close()

    def insert_plate_data(self, reading_time, t_plate, pres, flow):
        con = None
        try:
            logging.info("Inserting plate data: (%s, %s, %s, %s)", reading_time, t_plate, pres, flow)
            con = self.create_connection()
            cur = con.cursor()
            query = "INSERT INTO plate_readings(reading_time, t_plate, pres, flow) VALUES(%s, %s, %s, %s)"
            cur.execute(query, (reading_time, t_plate, pres, flow))
            con.commit()
        except psycopg2.DatabaseError, e:
            print 'Error %s' % e

        finally:
            if con:
                con.close()

    def read_latest_box_data(self, position):
        con = None
        try:
            con = self.create_connection()
            cur = con.cursor()
            cur.execute("""SELECT reading_time, temp, co2
                        from box_readings
                        where position = %s
                        order by reading_time desc limit 1""", (position,))
            box_reading = cur.fetchone()
            logging.info("Reading latest box data for box: %s %s", position, box_reading)
            return box_reading
        except psycopg2.DatabaseError, e:
            print 'Error %s' % e
            return None

        finally:
            if con:
                con.close()

    def read_latest_plate_data(self):
        con = None
        try:
            con = self.create_connection()
            cur = con.cursor()
            cur.execute("""SELECT reading_time, pres, flow, t_plate
                                from plate_readings
                                order by reading_time desc limit 1""")
            plate_reading = cur.fetchone()
            logging.info("Reading latest plate data: %s", plate_reading)
            return plate_reading
        except psycopg2.DatabaseError, e:
            print 'Error %s' % e
            return None

        finally:
            if con:
                con.close()

    def create_connection(self):
        return psycopg2.connect(database='pi', host='localhost', port=5432, user='pi', password='pi')


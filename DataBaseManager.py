import ibm_db

from Status import *


class DataBaseManager:
    """A data base manager class.

    Attributes:
    
    """


    def __init__(self):
        """The constructor.

        Args:
            self: The data base manager object to create.

        """

        # Create the connection to the data base server.
        self.conn = ibm_db.connect("DATABASE=BLUDB;HOSTNAME=dashdb-txn-sbox-yp-lon02-01.services.eu-gb.bluemix.net;PORT=50000;PROTOCOL=TCPIP;UID=kpd60209;PWD=w72v2fc2f0-g44q2;", "", "")


        # TO DO: CREATE A TABLE NAMED PATIENTS



    def upload(self, identifier_code: str, status: Status):
        """Upload a new patient to the data base.

        Args:
            self: The data base manager.
            identifier_code: The identifier code of the patient.
            status: The status of the patient.
        """

        # Declare the upload command.
        sql_command =   """
                        INSERT INTO KPD60209.Patients(Chance, Identifier, ID_Number, Hospital, Name)
                        Values(?, ?, ?, ?, ?);
                        """

        stmt = ibm_db.prepare(self.conn, sql_command)

        # Declare a variable stores all the params.
        params = status.chance, identifier_code, status.id_number, status.hospital,status.name

        # Explicitly bind parameters.
        ibm_db.execute(stmt, params)


    def search(self, identifier_code: str) -> Status:
        """Search for a patient in the data base.

        Args:
            self: The data base manager.
            identifier_code: The identifier code of the patient.

        """

        # Declare the upload command.
        sql_command = """
                      SELECT Chance, ID_Number, Hospital, Name
                      FROM KPD60209.Patients
                      WHERE Identifier = ?;
                      """

        stmt = ibm_db.prepare(self.conn, sql_command)

        # Explicitly bind the parameter.
        ibm_db.bind_param(stmt, 1, identifier_code)

        # Excute the sql command.
        ibm_db.execute(stmt)

        # Receive the results.
        results = ibm_db.fetch_both(stmt)

        if results != False:
            # If found.
            return Status(int(results["CHANCE"]), results["HOSPITAL"], results["ID_NUMBER"], results["NAME"])

        return None

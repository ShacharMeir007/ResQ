class Status:
    """An object representing a status of a person.

    Attributes:
        Chance to recognize.
	Identity number.
	Name of the hospital.
	Name of the person.

    """


    def __init__(self, chance: int, hospital: str, id_number: str = None, name: str = None):
        """The constructor.

        Args:
            self: The status object to create.
            chance: The chance to recognize correctly the person.
            hospital: Te hospital that the person is
            id_number: An identity number, optional.
            name: The name of the person, optional.

        """

        # Insert data to attributes.
        self.chance = chance
        self.hospital = hospital
        self.id_number = id_number
        self.name = name

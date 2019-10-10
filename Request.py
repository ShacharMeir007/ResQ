class Request:
    """A request object.

    Attributes:
        index: The index of the request.
        command: A command to execute.
        data: A data to use in order to execute the command.

    """


    def __init__(self, index: int, command: str, data: dict):
        """The constructor.

        Args:
            index: The index of the request.
            command: A command to execute.
            data: A data to use in order to execute the command.

        """

        # Insert data to attributes.
        self.index = index
        self.command = command
        self.data = data

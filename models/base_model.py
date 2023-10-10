"""
This module contains the BaseModel class that all other classses
will inherit common attributes and methods from
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    This is the base class for all other classes in the coming
    tasks. It is going to be the class from which every other
    class inherits from. This is the ADAM class
    """

    def __init__(self):
        """
        This is the constructor for the BaseModel class where
        we initialise some public instance attributes for use
        throughout the program

        Keep everything private to control access rights just
        like we did in Almost A Circle
        """
        self.id = "{}".format(uuid4())
        self.__created_at = datetime.now()
        # updated_at is datetime.now() because that was when
        # it was last updated
        self.__updated_at = datetime.now()

    def save(self):
        """
        This method updates the 'updated_at' attribute to the
        current datetime or the current time and date
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        This method returns a dictionary representation of the
        class for use in serialization to json objects
        """
        return {
                "my_number": self.my_number,
                "name": self.name,
                "__class__": type(self).__name__,
                "updated_at": self.updated_at,
                "id": self.id,
                "created_at": self.created_at
        }

    def validate_data_type(name, value, expected_type):
    """
    Validates that the given value matches the expected data type.
    Args:
        name (str): The name of the variable or field.
        value: The value to be validated.
        expected_type (type): The expected data type of the value.
        
    Returns:
        The validated value if it matches the expected type.
    Raises:
        TypeError: If the value does not match the expected type.
    """
        if not type(value) is Type:
            raise TypeError("{} must be of type {}".format(name, Type))

        return value

    def __str__(self):
        """
        This returns a string representation of the class and its
        attributes. Helpful for debugging and such
        """
        return "[{:s}] ({:s}) {}".format(
            type(self).__name__, self.id, self.__dict__
            )

    # PUBLIC PROPERTIES STORED HERE
    # USEFUL FOR KEEPING ACCESS TO PRIVATE ATTRIUTES CLEAN
    # AND NICE
    @property
    def name(self):
        """
        This property returns the name assigned to the instance

        Return:
            returns the number stored for the instance
        """
        return self.__name

    @name.setter
    def name(self, value):
        """
        This setter property gives access to re-assigning the
        name of the instance

        Args:
            value: the new value to store for the name
        """
        self.__name = self._validate_value("name", value, str)

    @property
    def my_number(self):
        """
        This property returns the number stored for the instance

        Return:
            returns the number stored for the instance
        """
        return self.__my_number

    @my_number.setter
    def my_number(self, value):
        """
        This property gives access to re-assigning the number
        stored for the instance

        Args:
            value: the new value to store
        """
        self.__my_number = self._validate_value("my_number", value, int)

    @property
    def created_at(self):
        """
        This property returns the datetime the instance was created

        Return:
            returns the datetime the instance was first created
        """
        return self.__created_at.isoformat()

    @property
    def updated_at(self):
        """
        This property returns the datetime the instance was created

        Return:
            returns the date the instance was updated at
        """
        return self.__updated_at.isoformat()

    @updated_at.setter
    def updated_at(self, value):
        """
        This property returns the datetime the instance was created

        Args:
            value: the value we are assigning the updated_at to
        """
        self.__updated_at = self._validate_value("updated_at", value, datetime)

#!/usr/bin/python3
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        """Initializes a CustomObject instance.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Indicates if the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Displays the attributes of the CustomObject instance."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serializes the object to a file.

        Args:
            filename (str): The name of the file to save the serialized object.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Error serializing object: {e}")

    @classmethod
    def deserialize(cls, filename):
        """Deserializes an object from a file.

        Args:
            filename (str): The name of the file to load the serialized object from.

        Returns:
            CustomObject: The deserialized object, or None if deserialization failed.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError) as e:
            print(f"Error deserializing object: {e}")
            return None
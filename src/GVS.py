"""
Singleton framework in Python.
"""

"""
Singleton class which will hold itself as an instance and allow us to
modify fields of the class as a singleton.

The way to access the singleton is << GlobalValuesSingleton.get_instance() >>
This can then be saved to a variable and used as the instance with our dictionary of values.
"""

class GVS: # GVS = GlobalValuesSingleton

    # The singleton instance (a self reference)
    __instance = None

    # Any global values that we have are stored in a dictionary for standardized access
    __value_dictionary = {}

    def __init__(self):
        # Do not make multiple instances of the class
        if GVS.__instance is not None:
            raise Exception("Cannot create multiple instances")

        # Set the starting values of the dictionary and the recursive instance
        self.__value_dictionary = {"fp": 500}
        GVS.__instance = self

    @staticmethod
    def get_instance():
        """
        Getter for the instance
        """
        if GVS.__instance is None:
            GVS()

        return GVS.__instance

    def get_value(self, value_key):
        """
        Function of convenience to get a value based on its key

        This could be replaced by value specific functions i.e. "GlobalValuesSingleton.get_free_parking()"
        """
        return GVS.__instance.__value_dictionary[value_key]

    def add_to_value(self, value_key, addition):
        """
        Change the given value by a given amount
        :param value_key: The key of the value to change
        :param addition: The amount to add (can be negative)
        :return: The new value
        """
        dict = GVS.__instance.__value_dictionary
        dict[value_key] = dict[value_key] + addition
        return GVS.__instance.__value_dictionary[value_key]

    def create_value(self, value_key, value):
        """
        Add a new global value
        """
        GVS.__instance.__value_dictionary.set_default(value_key, value)


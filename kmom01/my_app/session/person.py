""""
person class file
"""

class Person():
    """
    A person class
    """

    def __init__(self, firstname, lastname, birthday, img):
        self.firstname = firstname
        self.lastname = lastname
        self.birthday = birthday
        self.img = img

    def calculate_age():
        """
        calculates my age
        """
        return "30"

    @classmethod
    def create_from_json(cls, data):
        """
        Retrives data from json file
        """
        return cls(data["firstname"], data["lastname"], data["birthday"], data["img"])

    def phrase(self):
        """
        Prints out persons name
        """
        return "Jag föddes " +self.birthday +" och jag bor i Heby som är en liten stad utanför Uppsala"

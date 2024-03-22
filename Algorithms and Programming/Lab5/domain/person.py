import utils.helpers as h


class Patient:
    def __init__(self, first_name, last_name, personal_numeric_code, disease):
        """
        Create a patient object with first_name, last_name, personal_numeric_code and disease.
        :param first_name: first_name
        :param last_name: last_name
        :param personal_numeric_code: personal_numeric_code
        :param disease: disease
        """
        if h.checkName(first_name):
            self.__first_name = first_name
        else:
            raise ValueError("The first_name should contain only letters!")
        if h.checkName(last_name):
            self.__last_name = last_name
        else:
            raise ValueError("The last_name should contain only letters!")
        if h.checkPNC(personal_numeric_code):
            self.__personal_numeric_code = personal_numeric_code
        else:
            raise ValueError("Wrong PNC!")
        self.__disease = disease

    def get_first_name(self):
        """
        Get the first_name of the patient.
        :return:The first_name
        """
        return self.__first_name

    def get_last_name(self):
        """
        Get the last_name of the patient.
        :return: The last_name
        """
        return self.__last_name

    def get_personal_numeric_code(self):
        """
        Get the personal_numeric_code of the patient.
        :return: The personal_numeric_code
        """
        return self.__personal_numeric_code

    def get_disease(self):
        """
        Get the disease of the patient.
        :return: The disease
        """
        return self.__disease

    def set_first_name(self, new_first_name):
        """
        Set the first_name of the patient.
        :param new_first_name: new_first_name
        :return: The new_first_name
        """
        if h.checkName(new_first_name):
            self.__first_name = new_first_name
        else:
            raise ValueError("The new_first_name should contain only letters!")

    def set_last_name(self, new_last_name):
        """
        Set the last_name of the patient.
        :param new_last_name: new_last_name
        :return: The new_last_name
        """
        if h.checkName(new_last_name):
            self.__last_name = new_last_name
        else:
            raise ValueError("The new_last_name should contain only letters!")

    def set_personal_numeric_code(self, new_personal_numeric_code):
        """
        Set the personal_numeric_code of the patient.
        :param new_personal_numeric_code: new_personal_numeric_code
        :return: The new_personal_numeric_code
        """
        if h.checkPNC(new_personal_numeric_code):
            self.__personal_numeric_code = new_personal_numeric_code
        else:
            raise ValueError("Wrong PNC!")

    def set_disease(self, new_disease):
        """
        Set the disease of the patient.
        :param new_disease: new_disease
        :return: The new_disease
        """
        self.__disease = new_disease

    def __repr__(self):
        """
        Return the string representation of the patient.
        :return: The string representation of the patient
        """
        return f"Patient({self.__first_name}, {self.__last_name}, {self.__personal_numeric_code}, {self.__disease})"

    def __str__(self):
        """
        Function called when converting object into string.
        :return:
        """
        return self.__repr__()

    def __eq__(self, other):
        """
        Check if two patients objects are equal by comparing their properties.
        :param other: other
        :return:
        """
        return self.__first_name == other.__first_name and self.__last_name == other.__last_name and self.__personal_numeric_code == other.__personal_numeric_code and self.__disease == other.__disease

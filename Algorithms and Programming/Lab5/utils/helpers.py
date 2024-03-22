from datetime import date


def checkName(name):
    """
    Check if the name is correct.
    :param name: name
    :return:
    """
    if name.isalpha():
        return True
    else:
        raise ValueError("The name should contain only letters!")


def checkPNC(PNC):
    """
    Check if the PNC is correct.
    :param PNC: PNC
    :return:
    """
    if len(PNC) != 13:
        raise ValueError("Wrong PNC!")
    elif PNC[0] < "1" or PNC[0] > "6":
        raise ValueError("Wrong PNC!")
    elif PNC[1] + PNC[2] > "22":
        raise ValueError("Wrong PNC!")
    elif PNC[3] + PNC[4] < "01" or PNC[3] + PNC[4] > "12":
        raise ValueError("Wrong PNC!")
    elif PNC[5] + PNC[6] < "01" or PNC[5] + PNC[6] > "31":
        raise ValueError("Wrong PNC!")
    else:
        return True


def checkNumberOfBeds(number):
    """
    Check if the number of beds is an integer greater than 0.
    :param number: number
    :return:
    """
    if type(number) is int:
        return number > 0
    else:
        raise TypeError("Number is not correct!")


def calculateAge(patient):
    """
    Calculate the age of a patient.
    :param patient: patient
    :return:
    """
    PNC = patient.get_personal_numeric_code()
    patient_age = {}
    if int(PNC[0]) < 5:
        patient_age["year"] = int(f"19{PNC[1:3]}")
    else:
        patient_age["year"] = int(f"20{PNC[1:3]}")
    patient_age["month"] = int(PNC[3:5])
    patient_age["day"] = int(PNC[5:7])
    today = date.today()
    return today.year - patient_age["year"] - ((today.month, today.day) < (patient_age["month"], patient_age["day"]))

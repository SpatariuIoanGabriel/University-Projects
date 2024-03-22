from utils.functions import *
import domain.person as p
import utils.helpers as h


class Department:
    def __init__(self, id_, name, number_of_beds, list_of_patients=None):
        """
        Creating a repository containing patients.
        :param id_: id_
        :param name: name
        :param number_of_beds: number_of_beds
        :param list_of_patients: list_of_patients
        """
        self.__id_ = id_
        self.__name = name
        if h.checkNumberOfBeds(number_of_beds):
            self.__number_of_beds = number_of_beds
        else:
            raise TypeError("Number is not correct!")
        self.__list_of_patients = []
        if list_of_patients is not None:
            for patient in list_of_patients:
                if isinstance(patient, p.Patient) and self.__isPersonalNumericCodeUnique(patient.get_personal_numeric_code()):
                    if len(self.__list_of_patients) < self.__number_of_beds:
                        self.__list_of_patients.append(patient)
                    else:
                        raise ValueError("All beds are occupied!")
                else:
                    raise ValueError("PNC already exists!")

    def get_id_(self):
        """
        Get the id_ of the department.
        :return: The id_
        """
        return self.__id_

    def get_name(self):
        """
        Get the name of the department.
        :return: The name
        """
        return self.__name

    def get_number_of_beds(self):
        """
        Get the number_of_beds of the department.
        :return: The number_of_beds
        """
        return self.__number_of_beds

    def get_list_of_patients(self):
        """
        Get the list_of_patients of the department.
        :return: The list_of_patients
        """
        return self.__list_of_patients[:]

    def set_id_(self, new_id_):
        """
        Set the id_ of the department.
        :param new_id_: new_id_
        :return: The new_id_
        """
        self.__id_ = new_id_

    def set_name(self, new_name):
        """
        Set the name of the department.
        :param new_name: new_name
        :return: The new_name
        """
        self.__name = new_name

    def set_number_of_beds(self, new_number_of_beds):
        """
        Set the number_of_beds of the department.
        :param new_number_of_beds: new_number_of_beds
        :return: The new_number_of_beds
        """
        if h.checkNumberOfBeds(new_number_of_beds):
            self.__number_of_beds = new_number_of_beds
        else:
            raise TypeError("Number is not correct!")

    def set_list_of_patients(self, new_list_of_patients=None):
        """
        Set the list of patients of the department.
        :param new_list_of_patients: new_list_of_patients
        :return: The new_list_of_patients
        """
        self.__list_of_patients = []
        if new_list_of_patients is not None:
            for patient in new_list_of_patients:
                if isinstance(patient, p.Patient) and self.__isPersonalNumericCodeUnique(patient.get_personal_numeric_code()):
                    if len(self.__list_of_patients) < self.__number_of_beds:
                        self.__list_of_patients.append(patient)
                    else:
                        raise ValueError("All beds are occupied!")
                else:
                    raise ValueError("PNC already exists!")

    def __isPersonalNumericCodeUnique(self, personal_numeric_code):
        """
        Check if the personal_numeric_code is unique.
        :param personal_numeric_code: personal_numeric_code
        :return:
        """
        for patient in self.__list_of_patients:
            if patient.get_personal_numeric_code() == personal_numeric_code:
                return False
        return True

    def __repr__(self):
        """
        Return the string representation of the Department.
        :return: The string representation of the Department
        """
        return f"Department({self.__id_}, {self.__name}, {self.__number_of_beds}, {self.__list_of_patients})"

    def __str__(self):
        """
        Function called when converting object into string.
        :return:
        """
        return self.__repr__()

    def __eq__(self, other):
        """
        Check if two departments objects are equal by comparing their properties.
        :param other: other
        :return:
        """
        return self.__id_ == other.__id_ and self.__name == other.__name and self.__number_of_beds == other.__number_of_beds and self.__list_of_patients == other.__list_of_patients

    def addPatient(self, first_name, last_name, personal_numeric_code, disease):
        """
        Add a patient to the repository.
        :param first_name: first_name
        :param last_name: last_name
        :param personal_numeric_code: personal_numeric_code
        :param disease: disease
        :return: The list
        """
        if len(self.__list_of_patients) < self.__number_of_beds:
            if self.__isPersonalNumericCodeUnique(personal_numeric_code):
                if h.checkName(first_name) and h.checkName(last_name):
                    self.__list_of_patients.append(p.Patient(first_name, last_name, personal_numeric_code, disease))
                else:
                    raise ValueError("Wrong name!")
            else:
                raise ValueError("PNC already exists!")
        else:
            raise ValueError("All beds are occupied!")
        return self.__list_of_patients[:]

    def getPatientByIndex(self, index):
        """
        Get a patient at a given index.
        :param index: index
        :return: The patient
        """
        if 0 <= index < len(self.__list_of_patients):
            return self.__list_of_patients[index]
        else:
            raise IndexError("Index is not correct!")

    def getPatientByPNC(self, PNC):
        for patient in self.__list_of_patients:
            if patient.get_personal_numeric_code() == PNC:
                return patient
            else:
                raise ValueError("Wrong PNC!")

    def getAllPatients(self):
        """
        Get all patients.
        :return:
        """
        return self.__list_of_patients[:]

    def updatePatientByIndex(self, index, new_first_name, new_last_name, new_disease):
        """
        Update a patient at a given index.
        :param index: index
        :param new_first_name: new_first_name
        :param new_last_name: new_last_name
        :param new_disease: new_disease
        :return: The list with the new patient
        """
        if 0 <= index < len(self.__list_of_patients):
            self.__list_of_patients[index].set_first_name(new_first_name)
            self.__list_of_patients[index].set_last_name(new_last_name)
            self.__list_of_patients[index].set_disease(new_disease)
        else:
            raise IndexError("Index is not correct!")
        return self.__list_of_patients[:]

    def update_patient(self, PNC, new_first_name, new_last_name, new_PNC, new_disease):
        """
        Update a patient by PNC.
        :param PNC: PNC
        :param new_first_name: new_first_name
        :param new_last_name: new_last_name
        :param new_PNC: new_pnc
        :param new_disease = new_disease
        :return:
        """
        if self.__isPersonalNumericCodeUnique(new_PNC):
            for patient in self.__list_of_patients:
                if patient.personal_numeric_code == PNC:
                    patient.first_name = new_first_name
                    patient.last_name = new_last_name
                    patient.personal_numeric_code = new_PNC
                    patient.disease = new_disease
                else:
                    raise ValueError("Wrong PNC!")
        else:
            raise ValueError("PNC already exists!")

    def deletePatientAtIndex(self, index):
        """
        Delete a patient by index.
        :param index: index
        :return: The list
        """
        if 0 <= index < len(self.__list_of_patients):
            del self.__list_of_patients[index]
        else:
            raise IndexError("Index is not correct!")
        return self.__list_of_patients[:]

    def delete_patient(self, PNC):
        """
        Delete a patient from the department.
        :param PNC: PNC
        :return:
        """
        if self.__isPersonalNumericCodeUnique(PNC):
            new_patients = []
            for patient in self.__list_of_patients:
                if patient.get_personal_numeric_code() != PNC:
                    new_patients.append(patient)
        self.__list_of_patients = new_patients
        return new_patients

    def getNrOfPatients(self):
        """
        Get the number of patients.
        :return:
        """
        return len(self.__list_of_patients)

    def sort_by_name(self):
        """
        sort patients by name;
        :return:
        """
        self.__list_of_patients = sorted(self.__list_of_patients,
                                 key=lambda patient: patient.get_first_name() + patient.get_last_name())

    def kPatientsBacktrack(self):
        return getSolutions(self.__list_of_patients)


class Hospital:
    def __init__(self, initial_departments=None):
        """
        Creating a repository containing departments.
        """
        self.__list_of_departments = []
        if initial_departments is not None:
            for department in initial_departments:
                if isinstance(department, Department) and self.__isDepartmentIdUnique(department.get_id_):
                    self.__list_of_departments.append(department)
                else:
                    raise ValueError("The id_ already exists!")

    def get_list_of_departments(self):
        """
        Get the list_of_departments.
        :return: The list_of_departments
        """
        return self.__list_of_departments[:]

    def set_list_of_departments(self, new_list_of_departments=None):
        """
        Set the list of departments.
        :param new_list_of_departments: new_list_of_departments
        :return: The new_list_of_departments
        """
        self.__list_of_departments = []
        if new_list_of_departments is not None:
            for department in new_list_of_departments:
                if isinstance(department, Department) and self.__isDepartmentIdUnique(department.get_id_):
                    self.__list_of_departments.append(department)
                else:
                    raise ValueError("The id_ already exists!")

    def __len__(self):
        """
        Overwriting the len() function.
        :return: integer representing the number of departments
        """
        return len(self.__list_of_departments)

    def __isDepartmentIdUnique(self, id_):
        """
        Check if the id_ is unique.
        :param id_: id_
        :return:
        """
        for department in self.__list_of_departments:
            if department.get_id_() == id_:
                return False
        return True

    def add_patient_to_department(self, id_, first_name, last_name, PNC, disease):
        """
        Add a patient to department.
        :param id_: id_
        :param first_name: first_name
        :param last_name: last_name
        :param PNC: PNC
        :param disease: disease
        :return:
        """
        department = self.getDepartmentByID(id_)
        department.addPatient(first_name, last_name, PNC, disease)
        return department.getAllPatients()

    def addDepartment(self, id_, name, number_of_beds, list_of_patients):
        """
        Add a department to the repository.
        :param id_: id_
        :param name: name
        :param number_of_beds: number_of_beds
        :param list_of_patients: list_of_patients
        :return: The list
        """
        if self.__isDepartmentIdUnique(id_):
            self.__list_of_departments.append(Department(id_, name, number_of_beds, list_of_patients))
        else:
            raise ValueError("The id_ already exists!")
        return self.__list_of_departments[:]

    def getDepartmentByIndex(self, index):
        """
        Get a departments at a given index.
        :param index: index
        :return: The department
        """
        if 0 <= index < len(self.__list_of_departments):
            return self.__list_of_departments[index]
        else:
            raise IndexError("Index is not correct!")

    def getAllDepartments(self):
        """
        Get all patients.
        :return:
        """
        return self.__list_of_departments[:]

    def getDepartmentByID(self, id_):
        """
        Get a department of a given id_.
        :param id_: id_
        :return:
        """
        if self.__isDepartmentIdUnique(id_):
            for department in self.__list_of_departments:
                if department.get_id_ == id_:
                    return department
                else:
                    raise ValueError("Incorrect id_!")
        else:
            raise ValueError("The id_ already exists!")

    def getPatientsFromDepartment(self, id_):
        """
        Get the patients from a department.
        :param id_: id_
        :return:
        """
        department = self.getDepartmentByID(id_)
        return department.getAllPatients()

    def getPatientFromDepartment(self, id_, PNC):
        """
        Get a patient from a department.
        :param id_: id_
        :param PNC: PNC
        :return:
        """
        department = self.getDepartmentByID(id_)
        return department.getPatientByPNC(PNC)

    def updatePatientInDepartment(self, id_, curr_pnc, first_name, last_name, PNC, disease):
        """
        Update a patient from a department in the hospital.
        :param id_: id_
        :param curr_pnc: curr_pnc
        :param first_name: first_name
        :param last_name: last_name
        :param PNC: PNC
        :param disease: disease
        :return:
        """
        department = self.getDepartmentByID(id_)
        department.update_patient(curr_pnc, first_name, last_name, PNC, disease)
        return department.getPatientByPNC(PNC)

    def delete_patient_in_department(self, id_, PNC):
        """
        Delete a patient from a department in the hospital
        :param id_: id_
        :param PNC: PNC
        :return:
        """
        plane = self.getDepartmentByID(id_)
        plane.delete_patient(PNC)
        return plane.getAllPatients()

    def updateDepartmentByIndex(self, index, new_id_, new_name, new_number_of_beds, new_list_of_patients):
        """
        Update a department at a given index.
        :param index: index
        :param new_id_: new_id_
        :param new_name: new_name
        :param new_number_of_beds: new_number_of_beds
        :param new_list_of_patients: new_list_of_patients
        :return: The list with the new department
        """
        if 0 <= index < len(self.__list_of_departments):
            if self.__isDepartmentIdUnique(new_id_):
                self.__list_of_departments[index].set_id_(new_id_)
                self.__list_of_departments[index].set_name(new_name)
                self.__list_of_departments[index].set_number_of_beds(new_number_of_beds)
                self.__list_of_departments[index].set_list_of_patients(new_list_of_patients)
            else:
                raise ValueError("The id_ already exists!")
        else:
            raise IndexError("Index is not correct!")
        return self.__list_of_departments[:]

    def deleteDepartmentAtIndex(self, index):
        """
        Delete a department by index.
        :param index: index
        :return: The list
        """
        if 0 <= index < len(self.__list_of_departments):
            del self.__list_of_departments[index]
        else:
            raise IndexError("Index is not correct!")
        return self.__list_of_departments[:]

    def sort_patients_by_pnc(self, id_):
        """
        3. Sort the patients by pnc.
        :param id_: id_
        :return:
        """
        if len(self) == 0:
            raise ValueError("Empty list!")
        elif not self.__isDepartmentIdUnique(id_):
            raise ValueError("Wrong id!")
        dep = self.getDepartmentByID(id_)
        patients = sort(dep.getAllPatients(), lambda x, y: x.personal_numeric_code() > y.personal_numeric_code)
        self.getDepartmentByID(id_).set_list_of_patients(patients)
        return dep

    def sort_departments_by_number_of_patients(self):
        """
        4. Sort departments according to the number of patients
        :return:
        """
        if len(self) == 0:
            raise ValueError("Empty list!")
        dep = sort(self.__list_of_departments, lambda x, y: x.getNrOfPatients() < y.getNrOfPatients())
        self.__list_of_departments = dep
        return Hospital(self.__list_of_departments)

    def sort_by_age(self, age):
        """
        5. Sort the departments by the number of patients having the age above
        :param age:
        :return:
        """
        def get_patients_above(department):
            counter = 0
            for patient in department.getAllPatients():
                if h.calculateAge(patient) >= age:
                    counter += 1
            return counter

        departments = sort(self.__list_of_departments[:], lambda x1, x2: bool(get_patients_above(x1) <= get_patients_above(x2)))
        self.__list_of_departments = departments
        return Hospital(self.__list_of_departments[:])

    def sort_departments_by_patients_and_name(self):
        """
        6. Sort departments
        :return:
        """
        if len(self) == 0:
            raise ValueError("Empty list!")
        self.sort_departments_by_number_of_patients()
        for departament in self.__list_of_departments:
            departament.sort_by_name()
        return Hospital(self.__list_of_departments[:])

    def department_under_age(self, age):
        """
        7. Get departments with patients under a given age
        :param age: age
        :return:
        """
        def patients_under_age(patients):
            for patient in patients:
                if h.calculateAge(patient) < age:
                    return True
            return False
        department_list = []
        for department in self.__list_of_departments:
            if patients_under_age(department.get_list_of_patients()):
                department_list.append(department)
        if not department_list:
            raise ValueError(f"There are no departments with patients under {age}")
        return Hospital(department_list)

    def get_patients_with_string_name(self, index, string):
        """
        8. Get patients with specific string in name
        :param index: index
        :param string:
        :return:
        """
        if not 0 <= index <= len(self.__list_of_departments):
            raise IndexError("Your index is out of range")
        patients = []
        for patient in self.__list_of_departments[index].getAllPatients():
            if patient.get_first_name().find(string) != -1:
                patients.append(patient)
            elif patient.get_last_name().find(string) != -1:
                patients.append(patient)
        if not patients:
            raise ValueError("The string is not contained in any of the patients names")
        return Hospital(patient)

    def get_patients_with_string_name2(self, index, string):
        """
        Get patients with specific string in name
        :param index: index
        :param string: string
        :return:
        """
        if 0 <= index < len(self.__list_of_departments):
            return Filter(self.__list_of_departments[index].getAllPatients(), lambda x: string in x.get_first_name() or string in x.get_last_name())
        else:
            raise IndexError

    def departments_with_patients_name(self, first_name):
        """
        9.Get departments with patients that have a given first name
        :param first_name:
        :return:
        """
        departments_list = []
        for department in self.__list_of_departments:
            for patient in department.getAllPatients():
                if patient.get_first_name() == first_name:
                    departments_list.append(department)
                    break
        if not departments_list:
            raise ValueError(f"There are no patients with first name {first_name}")
        return Hospital(departments_list)

    def filter_with_patients(self, first_name):
        """
        Get departments with patients that have a given first name
        :param first_name: first_name
        :return:
        """
        return Hospital(Filter(self.__list_of_departments, lambda x: first_name in x.get_first_name()))

    def groups_of_k_with_same_disease(self, k):
        """
        10. Generate all the groups of patients in department with same disease
        :param k:
        :return:
        """
        groups = []
        for department in self.__list_of_departments:
            diseases = []
            for patient in department.getAllPatients():
                if not patient.get_disease() in diseases:
                    diseases.append(patient.get_disease())

            groups.append([department])
            for disease in diseases:
                for combination in getSolutions([], exist=lambda solution: solution[-1] < len(department.getAllPatients()),
                            is_solution=lambda solution: len(solution) == k,
                            consistent=lambda solution: department.getPatientByIndex(
                            solution[-1]).get_disease() == disease and all(i < j for i, j in zip(solution, solution[1:]))):
                    if combination is None:
                        raise ValueError(f"It can not be formed groups of {k} patients")
                    groups[-1].append(list(map(lambda index: department.getAllPatients()[index], combination)))
        return groups[:]

    def groups_of_k_with_p_patients(self, k, p):
        """
        form groups of p patients from at most k departments
        :param k:
        :param p:
        :return:
        """
        groups = []
        for department_combination in getSolutions([],
                                                   exist=lambda solution: solution[-1] < len(self.__list_of_departments),
                                                   is_solution=lambda solution: len(solution) == k,
                                                   consistent=lambda solution: all(
                                                       i < j for i, j in zip(solution, solution[1:]))):
            if department_combination is None:
                raise ValueError(f"It can not be formed groups of {k} departments")
            groups.append([[self.__list_of_departments[index] for index in department_combination]])
            patients = [patient
                        for depart_index in department_combination
                        for patient in self.__list_of_departments[depart_index].getAllPatients()]
            diseases = []
            for patient in patients:
                if not patient.get_disease() in diseases:
                    diseases.append(patient.get_disease())
            for disease in diseases:
                for combination in getSolutions([], exist=lambda solution: solution[-1] < len(patients),
                                is_solution=lambda solution: len(solution) == p,
                                consistent=lambda solution: patients[solution[-1]].get_disease() == disease
                                and all(i < j for i, j in zip(solution, solution[1:]))):
                    if combination is None:
                        raise ValueError(f"It can not be formed groups of {p} patients")
                    groups[-1].append(list(map(lambda index: patients[index], combination)))
        return groups[:]

    def __repr__(self):
        """
        Return the string representation of the class.
        """
        if len(self.__list_of_departments) == 0:
            return "There are no departments!"
        else:
            str_repr = ""
            for department in self.__list_of_departments:
                str_repr += str(department) + "\n"
            return str_repr

    def __eq__(self, other):
        """
        Check if two vectors objects are equal by comparing their properties.
        :param other: other
        :return:
        """
        index = 0
        while index < len(self.__list_of_departments):
            if self.__list_of_departments[index] != other.__list_of_points[index]:
                return False
            index += 1
        return True

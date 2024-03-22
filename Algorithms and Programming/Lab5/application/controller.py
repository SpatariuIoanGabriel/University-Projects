from infrastructure.repositories import Hospital


class Controller:
    def __init__(self, repo):
        """
        Initialise the controller with Hospital.
        """
        self.__repo = repo

    def __str__(self):
        """
        Return the string representation of the airport.
        """
        return self.__repo.s

    def addDepartment(self, id_, name, number_of_beds, list_of_patients):
        """
        Add department
        :param id_: id_
        :param name: name_
        :param number_of_beds: number_of_beds
        :param list_of_patients: list_of_patients
        :return:
        """
        return self.__repo.addDepartment(id_, name, number_of_beds, list_of_patients)

    def getAtIndex(self, index):
        """
        Get department at index.
        :param index: index
        :return:
        """
        return self.__repo.getDepartmentByIndex(index)

    def updateDepartmentAtIndex(self, index, new_id_, new_name, new_number_of_beds, new_list_of_patients):
        """
        Update department
        :param index: index
        :param new_id_: new_id
        :param new_name: new_name
        :param new_number_of_beds: new_number_of_beds
        :param new_list_of_patients: new_list_of_patients
        :return:
        """
        return self.__repo.updateDepartmentByIndex(index, new_id_, new_name, new_number_of_beds, new_list_of_patients)

    def deleteDepartment(self, index):
        """
        Delete department
        :param index:
        :return:
        """
        return self.__repo.deleteDepartmentAtIndex(index)

    def sort_by_number_of_patients(self):
        """
        Sort department by number of patients.
        :return:
        """
        return self.__repo.sort_by_number_of_patients()

    def sort_departments_by_patients_and_name(self):
        """
        Sort by age
        :return:
        """
        return self.__repo.sort_by_number_of_patients_and_name()

    def department_under_age(self, age):
        """
        Get department with patients under a given age
        :param age:
        :return:
        """
        return self.__repo.departments_with_patients_name(age)

    def departments_with_patients_name(self, first_name):
        """
        find departments with patients with given first name
        :param first_name:
        :return:
        """
        new_repo = self.__repo.departments_with_patients_name(first_name)
        print(new_repo)

    def groups_of_k_with_same_disease(self, k):
        """
        print all groups of k patients with same disease
        :param k:
        :return:
        """
        groups = self.__repo.groups_of_k_with_same_disease(k)
        for group in groups:
            if len(group) != 1:
                print(f"Department: {group[0].get_name_id()}:")
                for comb in group[1:]:
                    for patient in comb:
                        print(f"{'':<3}-{patient}")
                    print()

    def groups_of_k_with_p_patients(self, k, p):
        """
        print groups of k departments with groups of p patients with same disease
        :param k:
        :param p:
        :return:
        """
        groups = self.__repo.groups_of_k_with_p_patients(k, p)
        for group in groups:
            if len(group) != 1:
                text = "Departments: "
                for department in group[0]:
                    text += f"{department.get_name_id()}, "
                text = text[:-2] + ":"
                print(text)
                for comb in group[1:]:
                    for patient in comb:
                        print(f"{'':<3}-{patient}")
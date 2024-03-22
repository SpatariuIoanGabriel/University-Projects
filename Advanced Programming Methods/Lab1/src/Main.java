package src;

import src.Domain.Patient;
import src.Service.Service;
import src.Repository.Repository;
import src.UI.UI;

public class Main {
    public static void main(String[] args) {
        Repository repository = new Repository();
        Service patientService = new Service(repository);
        UI ui = new UI(patientService);

        Patient patient1 = new Patient("John", "Doe", "Fever", 1);
        Patient patient2 = new Patient("Alice", "Smith", "Headache", 2);
        Patient patient3 = new Patient("Bob", "Johnson", "Cough", 3);
        Patient patient4 = new Patient("Emily", "Williams", "Sore throat", 4);
        Patient patient5 = new Patient("David", "Brown", "Injury", 5);

        repository.addPatient(patient1);
        repository.addPatient(patient2);
        repository.addPatient(patient3);
        repository.addPatient(patient4);
        repository.addPatient(patient5);

        ui.run();
    }
}

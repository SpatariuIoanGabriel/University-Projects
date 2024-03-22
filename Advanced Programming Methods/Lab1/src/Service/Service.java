package src.Service;

import src.Domain.Patient;
import src.Repository.Repository;
import java.util.ArrayList;

public class Service {
    private Repository repository;

    public Service(Repository r) {
        this.repository = r;
    }

    public void addPatient(String firstname, String surname, String disease, int patientId) {
        Patient patient = new Patient(firstname, surname, disease, patientId);
        this.repository.addPatient(patient);
    }

    public ArrayList<Patient> getAllPatients() {
        return this.repository.getAllPatients();
    }

    public void updatePatient(int id, String firstname, String surname, String disease, int patientId) {
        Patient updatedPatient = new Patient(firstname, surname, disease, patientId);
        this.repository.updatePatient(id, updatedPatient);
    }

    public void removePatient(int id) {
        this.repository.removePatient(id);
    }
}

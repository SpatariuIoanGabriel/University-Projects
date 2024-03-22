package src.Repository;
import src.Domain.Patient;
import java.util.ArrayList;

public class Repository {
    private ArrayList<Patient> patients = new ArrayList<>();

    public void addPatient(Patient p) {
        if (!this.patients.contains(p))
            this.patients.add(p);
    }

    public ArrayList<Patient> getAllPatients() {
        return this.patients;
    }

    public void updatePatient(int id, Patient patient) {
        int pos = 0;
        int indexToUpdate = -1;
        for (Patient p : patients) {
            if (p.getId() == id) {
                indexToUpdate = pos;
            }
            pos++;
        }
        if (!this.patients.contains(patient))
            patients.set(indexToUpdate, patient);
    }

    public void removePatient(int id) {
        int pos = 0;
        int indexToDelete = -1;
        for (Patient b : patients) {
            if (b.getId() == id)
                indexToDelete = pos;
            pos++;
        }
        patients.remove(indexToDelete);
    }
}

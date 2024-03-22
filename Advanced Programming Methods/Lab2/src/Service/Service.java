package Service;

import Domain.Appointment;
import Domain.Patient;
import Exception.*;
import Repository.AppointmentRepo;
import Repository.PatientRepo;

import java.time.LocalDate;

public class Service {
    private PatientRepo patientsRepo;
    private AppointmentRepo appointmentsRepo;

    public Service(PatientRepo patientRepo, AppointmentRepo appointmentRepo) {
        this.patientsRepo = patientRepo;
        this.appointmentsRepo = appointmentRepo;
    }

    // Patient CRUD
    public void addPatient(String FirstName, String Surname, String disease, int PatientId) throws NoIdenticalEntities {
        this.patientsRepo.addEntity(new Patient(FirstName, Surname, disease, PatientId));
    }

    public void removePatientById(int id) throws NoEntityFound {
        this.patientsRepo.removeEntityById(id);
    }

    public Patient getPatientById(int id) throws NoEntityFound {
        return patientsRepo.getEntityById(id);
    }

    public Iterable<Patient> getAllPatients() {return this.patientsRepo.getAllEntities();}

    public void updatePatient(int id, String newFirstName, String newSurname, String newDisease) throws NoEntityFound {
        Patient patient = patientsRepo.getEntityById(id);

        patient.setFirstname(newFirstName);
        patient.setSurname(newSurname);
        patient.setDisease(newDisease);

        this.patientsRepo.updateEntityById(id, patient);
    }

    // Appointment CRUD

    public void addAppointment(Patient patient, int number, LocalDate date) throws NoIdenticalEntities {
        this.appointmentsRepo.addEntity(new Appointment(patient, number, date));
    }

    public void removeAppointmentById(int id) throws NoEntityFound {
        this.appointmentsRepo.removeEntityById(id);
    }

    public Appointment getAppointmentById(int id) throws NoEntityFound {
        return appointmentsRepo.getEntityById(id);
    }

    public Iterable<Appointment> getAllAppointments() {return this.appointmentsRepo.getAllEntities();}

    public void updateAppointment(Integer number, LocalDate newDate) throws NoEntityFound {
        Appointment appointment = getAppointmentById(number);

        appointment.setDate(newDate);

        this.appointmentsRepo.updateEntityById(number, appointment);
    }
}

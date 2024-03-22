package Service;

import Exception.*;
import Repository.IRepository;
import java.time.LocalDate;
import Domain.*;


public class Service {
    private IRepository<Patient, Integer> patientsRepo;
    private IRepository<Appointment, Integer> appointmentsRepo;

    public Service(IRepository<Patient, Integer> patientRepo, IRepository<Appointment, Integer> appointmentRepo) {
        this.patientsRepo = patientRepo;
        this.appointmentsRepo = appointmentRepo;
    }

    // Patient CRUD
    public void addPatient(String Name, String Email, String disease, int PatientId) throws NoIdenticalEntities {
        Patient newPatient = new Patient(Name, Email, disease, PatientId);
        PatientValidator.patientValidator(newPatient);
        this.patientsRepo.addEntity(newPatient);
    }

    public void removePatientById(int id) throws NoEntityFound {
        this.patientsRepo.removeEntityById(id);
    }

    public Patient getPatientById(int id) throws NoEntityFound {
        return patientsRepo.getEntityById(id);
    }

    public Iterable<Patient> getAllPatients() {return this.patientsRepo.getAllEntities();}

    public void updatePatient(int id, String newName, String newEmail, String newDisease) throws NoEntityFound {
        Patient patient = patientsRepo.getEntityById(id);

        patient.setName(newName);
        patient.setEmail(newEmail);
        patient.setDisease(newDisease);

        PatientValidator.patientValidator(patient);

        this.patientsRepo.updateEntityById(id, patient);
    }

    // Appointment CRUD

    public void addAppointment(int number, Patient patient, LocalDate date) throws NoIdenticalEntities {
        Appointment newAppointment = new Appointment(number, patient, date);
        AppointmentValidator.appointmentValidator(newAppointment);
        this.appointmentsRepo.addEntity(newAppointment);
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
        AppointmentValidator.appointmentValidator(appointment);
        this.appointmentsRepo.updateEntityById(number, appointment);
    }
}
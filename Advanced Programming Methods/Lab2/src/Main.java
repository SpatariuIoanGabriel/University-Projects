import Domain.Patient;
import Exception.*;
import Repository.AppointmentRepo;
import Repository.PatientRepo;
import Service.Service;
import UI.UI;


public class Main {
    public static void main(String[] args) throws NoIdenticalEntities, NoEntityFound {
        PatientRepo patientsRepository = new PatientRepo();
        AppointmentRepo appointmentsRepository = new AppointmentRepo();
        Service service = new Service(patientsRepository, appointmentsRepository);

        patientsRepository.addEntity(new Patient("John", "Doe", "cancer", 1));
        patientsRepository.addEntity(new Patient("Alice", "Smith", "flu", 2));
        patientsRepository.addEntity(new Patient("Bob", "Johnson", "headache", 3));
        patientsRepository.addEntity(new Patient("Eve", "Brown", "backache", 4));
        patientsRepository.addEntity(new Patient("Charlie", "Wilson", "pneumonia", 5));

        UI UI = new UI(service);
        UI.run();
    }
}

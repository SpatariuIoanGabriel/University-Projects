package UI;

import Domain.Appointment;
import Domain.AppointmentValidator;
import Domain.Patient;
import Domain.PatientValidator;
import Service.Service;
import Exception.*;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.util.InputMismatchException;
import java.util.Scanner;

public class UI {
    private Service service;

    public UI(Service service) {this.service = service;}

    public void printMenu() {
        System.out.println("\nMENU");
        System.out.println("0. Exit the program");
        System.out.println("1. Add a new patient");
        System.out.println("2. Remove a patient");
        System.out.println("3. Get a patient by id");
        System.out.println("4. Update a patient");
        System.out.println("5. List all the patients");
        System.out.println("6. Add a new appointment");
        System.out.println("7. Remove an appointment");
        System.out.println("8. Get an appointment by id");
        System.out.println("9. Update an appointment");
        System.out.println("10. List all the appointments");
    }

    public void run() {
        while (true) {
            printMenu();
            System.out.print("Write your choice: ");
            Scanner scanCommand = new Scanner(System.in);
            int command;

            try {
                command = scanCommand.nextInt();
            } catch (InputMismatchException e) {
                System.out.println("Invalid input! Please enter a valid option.");
                scanCommand.nextLine();
                continue;
            }

            switch (command) {
                case 0:
                    System.out.println("The program is over!");
                    return;
                case 1:
                    addPatient();
                    break;
                case 2:
                    removePatientById();
                    break;
                case 3:
                    getPatientById();
                    break;
                case 4:
                    updatePatient();
                    break;
                case 5:
                    listAllPatients();
                    break;
                case 6:
                    addAppointment();
                    break;
                case 7:
                    removeAppointmentByID();
                    break;
                case 8:
                    getAppointmentById();
                    break;
                case 9:
                    updateAppointment();
                    break;
                case 10:
                    listAllAppointments();
                    break;
                default:
                    System.out.println("Invalid choice! Please select a valid option!");
                    break;
            }
        }
    }

    public void listAllPatients() {
        Iterable<Patient> listOfPatients = this.service.getAllPatients();

        for(Patient patient: listOfPatients) {
            System.out.println(patient);
        }
    }

    public void addPatient() {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Write patient's name: ");
        String name = scanner.nextLine();

        System.out.println("Write patient's email: ");
        String email = scanner.nextLine();

        int id;
        while (true) {
            System.out.println("Write patient's id: ");
            if (scanner.hasNextInt()) {
                id = scanner.nextInt();
                scanner.nextLine();
                break;
            } else {
                System.out.println("The input is not correct. Write a valid number!.");
                scanner.nextLine();
            }
        }

        System.out.println("Write patient's disease: ");
        String disease = scanner.nextLine();

        try {
            Patient newPatient = new Patient(name, email, disease, id);
            PatientValidator.patientValidator(newPatient);
            service.addPatient(name, email, disease, id);
        } catch (IllegalArgumentException e) {
            System.out.println("Validation error: " + e.getMessage());
        } catch (NoIdenticalEntities e) {
            System.out.println("There is another patient with id=" + id + ".");
        }
    }

    public void getPatientById() {
        Scanner scanner = new Scanner(System.in);
        int id;
        while (true) {
            System.out.println("Write patient's id: ");
            if (scanner.hasNextInt()) {
                id = scanner.nextInt();
                scanner.nextLine();
                break;
            } else {
                System.out.println("The input is not correct. Write a valid number!");
                scanner.nextLine();
            }
        }
        try {
            Patient patient = service.getPatientById(id);
            System.out.printf(patient.toString());
        }catch (NoEntityFound e)
        {
            System.out.println("There is no patient with id= " + id);
        }
    }

    public void updatePatient() {
        Scanner scanner = new Scanner(System.in);
        int id;
        while (true) {
            System.out.println("Write patient's id: ");
            if (scanner.hasNextInt()) {
                id = scanner.nextInt();
                scanner.nextLine();
                try {
                    Patient patient = service.getPatientById(id);
                    System.out.printf(patient.toString());
                }catch (NoEntityFound e)
                {
                    System.out.println("There is no patient with id= " + id);
                }
                break;
            } else {
                System.out.println("The input is not correct. Write a valid number!");
                scanner.nextLine();
            }
        }
        System.out.println("Write the new patient's name: ");
        String updateName = scanner.nextLine();

        System.out.println("Write the new patient's email: ");
        String updateEmail = scanner.nextLine();

        System.out.println("Write the new patient's disease: ");
        String updateDisease = scanner.nextLine();

        try {
            Patient updatedPatient = new Patient(updateName, updateEmail, updateDisease, id);
            PatientValidator.patientValidator(updatedPatient);
            service.updatePatient(id, updateName, updateEmail, updateDisease);
        } catch (NoEntityFound e) {
            System.out.println("There is no patient with id=" + id + ".");
        } catch (IllegalArgumentException e) {
            System.out.println("Validation error: " + e.getMessage());
        }
    }

    public void removePatientById() {
        Scanner scanner = new Scanner(System.in);
        int id;
        while (true) {
            System.out.println("Write the patient's id: ");
            if (scanner.hasNextInt()) {
                id = scanner.nextInt();
                scanner.nextLine();
                break;
            } else {
                System.out.println("The input is not correct. Write a valid number!");
                scanner.nextLine();
            }
        }
        try {
            service.removePatientById(id);
        }catch (NoEntityFound e)
        {
            System.out.println("There is no patient with id=" + id + ".");
        }
    }

    public void listAllAppointments() {
        Iterable<Appointment> listOfAppointments = this.service.getAllAppointments();

        if (listOfAppointments.iterator().hasNext()) {
            for (Appointment appointment : listOfAppointments) {
                System.out.println(appointment);
            }
        } else {
            System.out.println("No appointment found!");
        }
    }

    public void addAppointment() {
        Scanner scanner = new Scanner(System.in);
        int number;

        while (true) {
            System.out.println("Write the number of appointment: ");
            if (scanner.hasNextInt()) {
                number = scanner.nextInt();
                scanner.nextLine();
                break;
            } else {
                System.out.println("The input is not correct. Write a valid number!");
                scanner.nextLine();
            }
        }

        int id;

        while (true) {
            System.out.println("Write patient's id: ");
            if (scanner.hasNextInt()) {
                id = scanner.nextInt();
                scanner.nextLine();
                break;
            } else {
                System.out.println("The input is not correct. Write a valid number!");
                scanner.nextLine();
            }
        }

        Patient patient;
        try {
            patient = service.getPatientById(id);
        } catch (NoEntityFound e) {
            System.out.println("There is no patient with id= " + id + ".");
            return;
        }

        Scanner Date = new Scanner(System.in);
        DateTimeFormatter dateFormatter = DateTimeFormatter.ofPattern("yyyy-MM-dd");

        LocalDate date = null;

        while (date == null) {
            System.out.print("Please enter a date and respect the format (YYYY-MM-DD): ");
            String writtenDate = Date.nextLine();

            try {
                date = LocalDate.parse(writtenDate, dateFormatter);
            } catch (DateTimeParseException e) {
                System.out.println("The input is not correct. Write a valid date!");
            }
        }
        try {
            Appointment newAppointment = new Appointment(number, patient, date);
            AppointmentValidator.appointmentValidator(newAppointment); // Validate appointment
            service.addAppointment(number, patient, date);
        } catch (IllegalArgumentException e) {
            System.out.println("Validation error: " + e.getMessage());
        } catch (NoIdenticalEntities e) {
            System.out.println("There is another appointment with the same id.");
        }
    }

    public void getAppointmentById() {
        Scanner scanner = new Scanner(System.in);
        int searchId;
        while (true) {
            System.out.println("Write the number of appointment:");
            if (scanner.hasNextInt()) {
                searchId = scanner.nextInt();
                scanner.nextLine();
                break;
            } else {
                System.out.println("The input is not correct. Write a valid number!");
                scanner.nextLine();
            }
        }
        try {
            Appointment appointment = service.getAppointmentById(searchId);
            System.out.println(appointment);
        }catch (NoEntityFound e)
        {
            System.out.println("There is no appointment with id=" + searchId);
        }
    }

    public void updateAppointment() {
        Scanner scanner = new Scanner(System.in);
        int number;
        Appointment appointment = null;

        while (appointment == null) {
            System.out.println("Write appointment's number: ");
            if (scanner.hasNextInt()) {
                number = scanner.nextInt();
                scanner.nextLine();
                try {
                    appointment = service.getAppointmentById(number);
                    System.out.println(appointment);
                } catch (NoEntityFound e) {
                    System.out.println("There is no appointment with id=" + number);
                }
            } else {
                System.out.println("The input is not correct. Write a valid number!");
                scanner.nextLine();
            }
        }

        Scanner dateScanner = new Scanner(System.in);
        DateTimeFormatter dateFormatter = DateTimeFormatter.ofPattern("yyyy-MM-dd");

        LocalDate date = null;

        while (date == null) {
            System.out.print("Please enter a date and respect the format (YYYY-MM-DD): ");
            String writtenDate = dateScanner.nextLine();

            try {
                date = LocalDate.parse(writtenDate, dateFormatter);
            } catch (DateTimeParseException e) {
                System.out.println("The input is not correct. Write a valid date!");
            }
        }

        try {
            Appointment updatedAppointment = new Appointment(appointment.getId(), appointment.getPatient(), date);
            AppointmentValidator.appointmentValidator(updatedAppointment);
            service.updateAppointment(appointment.getId(), date);
        } catch (NoEntityFound e) {
            System.out.println("There is no appointment with number= " + appointment.getId() + ".");
        } catch (IllegalArgumentException e) {
            System.out.println("Validation error: " + e.getMessage());
        }
    }


    public void removeAppointmentByID() {
        Scanner deleteScanner = new Scanner(System.in);
        int number;
        while (true) {
            System.out.println("Write the number of the appointment: ");
            if (deleteScanner.hasNextInt()) {
                number = deleteScanner.nextInt();
                deleteScanner.nextLine();
                break;
            } else {
                System.out.println("The input is not correct. Write a valid number!");
                deleteScanner.nextLine();
            }
        }
        try {
            service.removeAppointmentById(number);
        }catch (NoEntityFound e)
        {
            System.out.println("There is no appointment with id= " + number + ".");
        }
    }
}
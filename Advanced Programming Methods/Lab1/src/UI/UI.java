package src.UI;

import src.Domain.Patient;
import src.Service.Service;
import src.Repository.Repository;

import java.util.ArrayList;
import java.util.Scanner;

public class UI {
    private Service patientService;
    private Scanner scanner;

    public UI(Service patientService) {
        this.patientService = patientService;
        this.scanner = new Scanner(System.in);
    }

    public void run()
    {
        while (true)
        {
            this.displayMenu();
            int choice = readChoice();
            switch (choice) {
                case 1:
                    addPatient();
                    break;
                case 2:
                    listAllPatients();
                    break;
                case 3:
                    updatePatient();
                    break;
                case 4:
                    removePatient();
                    break;
                case 5:
                    return;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }

    private void displayMenu() {
        System.out.println("1. Add Appointment");
        System.out.println("2. List All Appointments");
        System.out.println("3. Update Appointment");
        System.out.println("4. Remove Appointment");
        System.out.println("5. Exit the program");
    }

    private int readChoice() {
        System.out.print("Enter your choice: ");
        return scanner.nextInt();
    }

    private void addPatient() {
        System.out.print("Enter firstname: ");
        String firstname = scanner.next();
        System.out.print("Enter surname: ");
        String surname = scanner.next();
        System.out.print("Enter disease: ");
        String disease = scanner.next();
        System.out.print("Enter ID: ");
        int patientId = scanner.nextInt();
        patientService.addPatient(firstname, surname, disease, patientId);
    }

    private void listAllPatients() {
        ArrayList<Patient> patients = patientService.getAllPatients();
        if (patients.isEmpty()) {
            System.out.println("No patients found.");
        } else {
            System.out.println("List of Patients:");
            for (Patient patient : patients) {
                System.out.println(patient);
            }
        }
    }

    private void updatePatient() {
        System.out.print("Enter the ID of the patient to update: ");
        int id = scanner.nextInt();
        System.out.print("Enter updated firstname: ");
        String firstname = scanner.next();
        System.out.print("Enter updated surname: ");
        String surname = scanner.next();
        System.out.print("Enter updated disease: ");
        String disease = scanner.next();
        System.out.print("Enter updated ID: ");
        int patientId = scanner.nextInt();
        patientService.updatePatient(id, firstname, surname, disease, patientId);
    }

    private void removePatient() {
        System.out.print("Enter the ID of the patient to remove: ");
        int id = scanner.nextInt();
        patientService.removePatient(id);
    }
}

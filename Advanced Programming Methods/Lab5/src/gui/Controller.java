package gui;

import Domain.Appointment;
import Domain.Patient;
import Repository.ActionAdd;
import Repository.ActionRemove;
import Repository.ActionUpdate;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.scene.input.KeyEvent;
import javafx.scene.input.MouseEvent;
import Domain.Action;
import Repository.IRepository;
import Service.Service;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Stack;
import Exception.*;

public class Controller {
    private Service service;

    IRepository<Patient,Integer> patientIntegerIRepository;
    IRepository<Appointment,Integer> appointmentsRepo;

    private Stack<Action<Patient,Integer>> undoPatientsStack = new Stack<>();

    private Stack<Action<Patient,Integer>> redoPatientsStack = new Stack<>();

    private Stack<Action<Appointment,Integer>> undoAppointmentsStack = new Stack<>();

    private Stack<Action<Appointment,Integer>> redoAppointmentsStack = new Stack<>();


    @FXML
    private ListView<Patient> patientsListView;
    @FXML
    private ListView<Appointment> appointmentsListView;
    @FXML
    private TextField patientSearchTextField;
    @FXML
    private TextField appointmentSearchTextField1;
    @FXML
    private TextField idTextField;

    @FXML
    void onUndoButtonClicked(MouseEvent event) {
        performUndo(undoPatientsStack, redoPatientsStack);
    }

    @FXML
    void onRedoButtonClicked(MouseEvent event) {
        performRedo(undoPatientsStack, redoPatientsStack);
    }

    @FXML
    void onUndoAppointmentButtonClicked(MouseEvent event) {
        performUndoAppointments(undoAppointmentsStack, redoAppointmentsStack);
    }

    @FXML
    void onRedoAppointmentButtonClicked(MouseEvent event) {
        performRedoAppointments(redoAppointmentsStack, redoAppointmentsStack);
    }

    @FXML
    private TextField nameTextField;
    @FXML
    private TextField emailIdTextField;
    @FXML
    private TextField emailTextField;
    @FXML
    private TextField diseaseTextField;
    @FXML
    private Button patientAddButton, patientDeleteButton, patientUpdateButton;
    @FXML
    private TextField appointmentIdTextField, dateTextField;
    @FXML
    private Label foundEmail;
    @FXML
    private TextField patientNameTextField, patientEmailTextField, patientDiseaseTextField, patientIdTextField;
    @FXML
    private Button appointmentAddButton, appointmentDeleteButton, appointmentUpdateButton;
    @FXML
    private Label currentRepositoyLabel;
    @FXML
    private Button redoButton, undoButton, undoPatientsButton, redoPatientsButton;
    @FXML
    private TextField showPatientsWithGivenDiseaseTextField;
    @FXML
    private TextField showPatientsEndingWithAGivenLetterTextField;
    @FXML
    private TextField getEmailByIdTextField;
    @FXML
    private TextField showAllAppointmentsOfAPatientByAGivenIdTextField;
    @FXML
    private TextField dateBefore;

    @FXML
    private Label email;

    public Controller() {
        this.service = new Service();
        this.patientIntegerIRepository = this.service.getPatientRepository();
        this.appointmentsRepo = this.service.getAppointmentRepository();
    }


    void populatePatientList() {
        Collection<Patient> patientsCollection = service.getAllPatients();
        ObservableList<Patient> patientObservableList = FXCollections.observableArrayList(patientsCollection);
        patientsListView.setItems(patientObservableList);
    }

    void populateAppointmentList() {
        Collection<Appointment> appointmentsCollection = service.getAllAppointments();
        ObservableList<Appointment> appointmentObservableList = FXCollections.observableArrayList(appointmentsCollection);
        appointmentsListView.setItems(appointmentObservableList);
    }

    public void initialize() {
        patientIntegerIRepository = service.getPatientRepository();
        appointmentsRepo = service.getAppointmentRepository();

        populatePatientList();
        populateAppointmentList();

        SelectionMode modePatients = patientsListView.getSelectionModel().getSelectionMode();
        SelectionMode modeAppointments = appointmentsListView.getSelectionModel().getSelectionMode();
    }

    @FXML
    void searchOnKeyTypedPatients(KeyEvent event) {
        String searchText = patientSearchTextField.getText();
        if (searchText.equals(""))
            populatePatientList();
        else {
            ObservableList<Patient> filteredPatients = FXCollections.observableArrayList(service.showPatientsWithGivenDisease(searchText));
            patientsListView.setItems(filteredPatients);
        }
    }

    @FXML
    void searchOnKeyTypedAppointments(KeyEvent event) {
        String searchText = appointmentSearchTextField1.getText();
        if (searchText.equals(""))
            populateAppointmentList();
        else {
            ObservableList<Appointment> filteredAppointments = FXCollections.observableArrayList(service.showAllAppointmentsOfAPatientByAGivenId(Integer.parseInt(searchText)));
            appointmentsListView.setItems(filteredAppointments);
        }
    }

    @FXML
    void searchOnPatientNameTextField(KeyEvent event) {
        String searchText = showPatientsEndingWithAGivenLetterTextField.getText();
        if (searchText.equals(""))
            populatePatientList();
        else {
            ObservableList<Patient> filteredPatients = FXCollections.observableArrayList(service.showPatientsEndingWithAGivenLetter(searchText));
            patientsListView.setItems(filteredPatients);
        }
    }

    @FXML
    void  searchEmailIdTextField(KeyEvent event) {
        String searchText = emailIdTextField.getText();
        if (searchText.equals(""))
            populatePatientList();
        else {
            foundEmail.setText(String.valueOf(service.getEmailById(Integer.parseInt(String.valueOf(searchText)))));
        }
    }

    @FXML
    void onSearchDateBefore(KeyEvent event) {
        String searchText = dateBefore.getText();
        DateTimeFormatter dateFormatter = DateTimeFormatter.ofPattern("yyyy-MM-dd");
        LocalDate date = LocalDate.parse(dateBefore.getText(), dateFormatter);
        if (searchText.isEmpty())
            populateAppointmentList();
        else {
            ObservableList<Appointment> filteredAppointments = FXCollections.observableArrayList(service.filteringAppointmentsBeforeDate(date));
            appointmentsListView.setItems(filteredAppointments);
        }
    }

    @FXML
    void onClickPatientsList(MouseEvent event) {
        int i = patientsListView.getSelectionModel().getSelectedIndex();
        ArrayList<Patient> patients = service.getAllPatients();
        if (i < 0 || i >= patients.size()) {
            Alert dialog = new Alert(Alert.AlertType.ERROR);
            dialog.setTitle("Error");
            dialog.setContentText("Invalid patient selection!");
            dialog.show();
        } else {
            Patient patient = patients.get(i);
            nameTextField.setText(patient.getName());
            idTextField.setText(patient.getId().toString());
            emailTextField.setText(patient.getEmail());
            diseaseTextField.setText(String.valueOf(patient.getDisease()));
        }
    }

    @FXML
    void onClickAppointmentsList(MouseEvent event) {
        int i = appointmentsListView.getSelectionModel().getSelectedIndex();
        ArrayList<Appointment> appointments = service.getAllAppointments();
        if(i < 0 || i >= appointments.size())
        {
            Alert dialog = new Alert(Alert.AlertType.ERROR);
            dialog.setTitle("Error");
            dialog.setContentText("Invalid appointment selection!");
            dialog.show();
        }else {
            Appointment appointment = appointments.get(i);
            appointmentIdTextField.setText(String.valueOf(appointment.getId()));
            patientIdTextField.setText(String.valueOf(appointment.getPatient().getId()));
            dateTextField.setText(String.valueOf(appointment.getDate()));

        }
    }

    @FXML
    void onPatientAddButtonClicked(MouseEvent event) {
        try {
            int id = Integer.parseInt(idTextField.getText());
            String name = nameTextField.getText();
            String email = emailTextField.getText();
            String disease = diseaseTextField.getText();

            Patient newPatient = new Patient(name, email, disease, id);

            Action<Patient, Integer> addAction = new ActionAdd<>(patientIntegerIRepository, newPatient);

            addAction.redo();

            undoPatientsStack.push(addAction);

            redoPatientsStack.clear();

            populatePatientList();
        } catch (NumberFormatException e) {
            Alert dialog = new Alert(Alert.AlertType.ERROR);
            dialog.setTitle("Error");
            dialog.setContentText("Id must be a number!");
            dialog.show();
        } catch (NoIdenticalEntities e) {
            Alert dialog = new Alert(Alert.AlertType.ERROR);
            dialog.setTitle("Error");
            dialog.setContentText("Patient already exists!");
            dialog.show();
        } catch (Exception e) {
            Alert dialog = new Alert(Alert.AlertType.ERROR);
            dialog.setTitle("Error");
            dialog.setContentText("An error occurred: " + e.getMessage());
            dialog.show();
        }
    }

    @FXML
    void onAppointmentAddButtonClicked(MouseEvent event) {
        try {
            int appointmentNumber = Integer.parseInt(appointmentIdTextField.getText());
            DateTimeFormatter dateFormatter = DateTimeFormatter.ofPattern("yyyy-MM-dd");
            LocalDate date = LocalDate.parse(dateTextField.getText(), dateFormatter);

            int patientId = Integer.parseInt(patientIdTextField.getText());
            Patient patient = service.getPatientById(patientId);

            Appointment newAppointment = new Appointment(appointmentNumber, patient, date);

            Action<Appointment, Integer> addAction = new ActionAdd<>(appointmentsRepo, newAppointment);

            addAction.redo();

            undoAppointmentsStack.push(addAction);

            redoAppointmentsStack.clear();

            populateAppointmentList();
        } catch (NumberFormatException e) {
            Alert dialog = new Alert(Alert.AlertType.ERROR);
            dialog.setTitle("Error");
            dialog.setContentText("Numeric input required!");
            dialog.show();
        } catch (DateTimeParseException e) {
            Alert dialog = new Alert(Alert.AlertType.ERROR);
            dialog.setTitle("Error");
            dialog.setContentText("Invalid date format!");
            dialog.show();
        } catch (NoEntityFound e) {
            Alert dialog = new Alert(Alert.AlertType.ERROR);
            dialog.setTitle("Error");
            dialog.setContentText("Patient not found!");
            dialog.show();
        } catch (NoIdenticalEntities e) {
            Alert dialog = new Alert(Alert.AlertType.ERROR);
            dialog.setTitle("Error");
            dialog.setContentText("Appointment already exists!");
            dialog.show();
        }
    }



    @FXML
    void onPatientDeleteButtonClicked(MouseEvent event) {
        int i = patientsListView.getSelectionModel().getSelectedIndex();
        if (i >= 0) {
            Patient patientToDelete = patientsListView.getItems().get(i);
            try {
                Action<Patient, Integer> deletePatientAction = new ActionRemove<>(patientIntegerIRepository, patientToDelete);

                deletePatientAction.redo();

                undoPatientsStack.push(deletePatientAction);

                Collection<Appointment> appointmentsToRemove = new ArrayList<>();
                for (Appointment appointment : service.getAllAppointments()) {
                    if (appointment.getPatient().getId().equals(patientToDelete.getId())) {
                        Action<Appointment, Integer> deleteAppointmentAction = new ActionRemove<>(appointmentsRepo, appointment);

                        deleteAppointmentAction.redo();

                        undoAppointmentsStack.push(deleteAppointmentAction);
                    }
                }

                redoPatientsStack.clear();
                redoAppointmentsStack.clear();

                populatePatientList();
                populateAppointmentList();
            } catch (NoEntityFound e) {
                Alert dialog = new Alert(Alert.AlertType.ERROR);
                dialog.setTitle("Error");
                dialog.setContentText("No patient found!");
                dialog.show();
            } catch (Exception e) {
                Alert dialog = new Alert(Alert.AlertType.ERROR);
                dialog.setTitle("Error");
                dialog.setContentText("An error occurred: " + e.getMessage());
                dialog.show();
            }
        } else {
            Alert dialog = new Alert(Alert.AlertType.ERROR);
            dialog.setTitle("Error");
            dialog.setContentText("No patient selected!");
            dialog.show();
        }
    }

    @FXML
    void onAppointmentDeleteButtonClicked(MouseEvent event) {
        int i = appointmentsListView.getSelectionModel().getSelectedIndex();
        if (i >= 0) {
            Appointment appointmentToDelete = appointmentsListView.getItems().get(i);
            try {
                Action<Appointment, Integer> deleteAppointmentAction = new ActionRemove<>(appointmentsRepo, appointmentToDelete);

                deleteAppointmentAction.redo();

                undoAppointmentsStack.push(deleteAppointmentAction);

                redoAppointmentsStack.clear();

                populateAppointmentList();
            } catch (NoEntityFound e) {
                Alert dialog = new Alert(Alert.AlertType.ERROR);
                dialog.setTitle("Error");
                dialog.setContentText("No appointment found!");
                dialog.show();
            } catch (Exception e) {
                Alert dialog = new Alert(Alert.AlertType.ERROR);
                dialog.setTitle("Error");
                dialog.setContentText("An error occurred: " + e.getMessage());
                dialog.show();
            }
        } else {
            Alert dialog = new Alert(Alert.AlertType.ERROR);
            dialog.setTitle("Error");
            dialog.setContentText("No appointment selected!");
            dialog.show();
        }
    }


    @FXML
    void onPatientUpdateButtonClicked(MouseEvent event) {
        try {
            int i = patientsListView.getSelectionModel().getSelectedIndex();
            if (i >= 0) {
                Patient selectedPatient = patientsListView.getItems().get(i);

                Patient oldPatientData = new Patient(selectedPatient.getName(), selectedPatient.getEmail(), selectedPatient.getDisease(), selectedPatient.getId());

                String name = nameTextField.getText();
                String email = emailTextField.getText();
                String disease = diseaseTextField.getText();
                Patient newPatientData = new Patient(name, email, disease, selectedPatient.getId());

                patientIntegerIRepository.updateEntityById(selectedPatient.getId(), newPatientData);

                Action<Patient, Integer> updateAction = new ActionUpdate<>(patientIntegerIRepository, oldPatientData, newPatientData);

                updateAction.redo();

                undoPatientsStack.push(updateAction);

                redoPatientsStack.clear();

                populatePatientList();

                Collection<Appointment> appointmentsToUpdate = service.showAllAppointmentsOfAPatientByAGivenId(selectedPatient.getId());
                for (Appointment appointment : appointmentsToUpdate) {
                    appointment.setPatient(newPatientData);
                }
                populateAppointmentList();
            } else {
                Alert dialog = new Alert(Alert.AlertType.ERROR);
                dialog.setTitle("Error");
                dialog.setContentText("No patient selected!");
                dialog.show();
            }
        } catch (NoEntityFound e) {
            Alert dialog = new Alert(Alert.AlertType.ERROR);
            dialog.setTitle("Error");
            dialog.setContentText("Patient not found!");
            dialog.show();
        } catch (Exception e) {
            Alert dialog = new Alert(Alert.AlertType.ERROR);
            dialog.setTitle("Error");
            dialog.setContentText("An error occurred: " + e.getMessage());
            dialog.show();
        }
    }


    @FXML
    void onAppointmentUpdateButtonClicked(MouseEvent event) {
        try {
            int i = appointmentsListView.getSelectionModel().getSelectedIndex();
            if (i >= 0) {
                Appointment appointmentToUpdate = appointmentsListView.getItems().get(i);

                Appointment oldAppointmentData = new Appointment(appointmentToUpdate.getId(), appointmentToUpdate.getPatient(), appointmentToUpdate.getDate());

                DateTimeFormatter dateFormatter = DateTimeFormatter.ofPattern("yyyy-MM-dd");
                LocalDate newDate = LocalDate.parse(dateTextField.getText(), dateFormatter);

                service.updateAppointment(appointmentToUpdate.getId(), newDate);

                Appointment newAppointmentData = new Appointment(appointmentToUpdate.getId(), appointmentToUpdate.getPatient(), newDate);

                Action<Appointment, Integer> updateAppointmentAction = new ActionUpdate<>(appointmentsRepo, oldAppointmentData, newAppointmentData);

                updateAppointmentAction.redo();

                undoAppointmentsStack.push(updateAppointmentAction);

                redoAppointmentsStack.clear();

                populateAppointmentList();
                populatePatientList();
            } else {
                Alert dialog = new Alert(Alert.AlertType.ERROR);
                dialog.setTitle("Error");
                dialog.setContentText("No appointment selected!");
                dialog.show();
            }
        } catch (DateTimeParseException e) {
            Alert dialog = new Alert(Alert.AlertType.ERROR);
            dialog.setTitle("Error");
            dialog.setContentText("Invalid date format!");
            dialog.show();
        } catch (NoEntityFound e) {
            Alert dialog = new Alert(Alert.AlertType.ERROR);
            dialog.setTitle("Error");
            dialog.setContentText("Appointment not found!");
            dialog.show();
        } catch (Exception e) {
            Alert dialog = new Alert(Alert.AlertType.ERROR);
            dialog.setTitle("Error");
            dialog.setContentText("An error occurred: " + e.getMessage());
            dialog.show();
        }
    }

    private void performUndo(Stack<Action<Patient, Integer>> undoStack, Stack<Action<Patient, Integer>> redoStack) {
        if (!undoStack.isEmpty()) {
            Action<Patient, Integer> action = undoStack.pop();
            try {
                action.undo();
                redoStack.push(action);
                populatePatientList();
            } catch (Exception e) {
            }
        }
    }

    private void performRedo(Stack<Action<Patient, Integer>> undoStack, Stack<Action<Patient, Integer>> redoStack) {
        if (!redoStack.isEmpty()) {
            Action<Patient, Integer> action = redoStack.pop();
            try {
                action.redo();
                undoStack.push(action);
                populatePatientList();
            } catch (Exception e) {
            }
        }
    }

    private void performUndoAppointments(Stack<Action<Appointment, Integer>> undoAppointmentsStack, Stack<Action<Appointment, Integer>> redoAppointmentsStack) {
        if (!undoAppointmentsStack.isEmpty()) {
            Action<Appointment, Integer> action = undoAppointmentsStack.pop();
            try {
                action.undo();
                redoAppointmentsStack.push(action);
                populateAppointmentList();
            } catch (Exception e) {
            }
        }
    }

    private void performRedoAppointments(Stack<Action<Appointment, Integer>> undoAppointmentsStack, Stack<Action<Appointment, Integer>> redoAppointmentsStack) {
        if (!redoAppointmentsStack.isEmpty()) {
            Action<Appointment, Integer> action = redoAppointmentsStack.pop();
            try {
                action.redo();
                undoAppointmentsStack.push(action);
                populateAppointmentList();
            } catch (Exception e) {
            }
        }
    }


}

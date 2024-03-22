package src.Domain;

import java.util.Objects;

public class Patient implements Identifiable<Integer> {
    private String firstname;
    private String surname;
    private String disease;
    private int PatientId;

    public Patient(String firstname, String surname, String disease, int patientId) {
        this.firstname = firstname;
        this.surname = surname;
        this.disease = disease;
        this.PatientId = patientId;
    }

    public String getDisease() {return disease;}

    public void setDisease(String disease) {this.disease = disease;}

    @Override
    public Integer getId() {
        return this.PatientId;
    }

    @Override
    public void setID(Integer id) {
        PatientId = id;
    }

    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }

    public String getSurname() {
        return surname;
    }

    public void setSurname(String surname) {
        this.surname = surname;
    }

    @Override
    public String toString() {
        return "Patient{" +
                "firstname='" + firstname + '\'' +
                ", surname='" + surname + '\'' +
                ", disease=" + disease +
                ", PatientId=" + PatientId +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Patient patient = (Patient) o;
        return PatientId == patient.PatientId;
    }
}

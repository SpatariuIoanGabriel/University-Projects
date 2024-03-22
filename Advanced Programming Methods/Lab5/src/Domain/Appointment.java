package Domain;

import java.time.LocalDate;
import java.util.Objects;
import java.io.Serializable;

public class Appointment implements Identifiable<Integer>, Serializable{
    private int number;
    private Patient patient;
    private LocalDate date;

    public Appointment(int number, Patient patient, LocalDate date) {
        this.number = number;
        this.patient = patient;
        this.date = date;
    }

    @Override
    public Integer getId() {return this.number;}

    @Override
    public void setId(Integer number) {this.number = number;}

    public Patient getPatient() {return this.patient;}

    public void setPatient(Patient patient) {this.patient = patient;}

    public LocalDate getDate() {return this.date;}

    public void setDate(LocalDate date) {this.date = date;}

    @Override
    public String toString() {
        return "Appointment{" +
                "number: " + number + ", " +
                patient.toString() + " " +
                ", date: " + date +
                "}";
    }

    @Override
    public boolean equals(Object objectToCompare)
    {
        if (this == objectToCompare) return true;
        if (objectToCompare == null || getClass() != objectToCompare.getClass()) return false;
        Appointment appointment  = (Appointment) objectToCompare;
        return Objects.equals(number, appointment.number);
    }
}

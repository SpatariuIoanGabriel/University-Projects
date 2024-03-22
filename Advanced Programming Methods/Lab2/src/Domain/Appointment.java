package Domain;

import java.time.LocalDate;
import java.util.Objects;

public class Appointment implements Identifiable<Integer> {
    private Patient patient;
    private int number;
    private LocalDate date;

    public Appointment(Patient patient, int number, LocalDate date) {
        this.patient = patient;
        this.number = number;
        this.date = date;
    }

    @Override
    public Integer getId() {return this.number;}

    @Override
    public void setID(Integer number) {this.number = number;}

    public Patient getPatient() {return this.patient;}

    public void setPatient(Patient patient) {this.patient = patient;}

    public LocalDate getDate() {return this.date;}

    public void setDate(LocalDate date) {this.date = date;}

    @Override
    public String toString() {
        return "Appointment{" +
                "number: " + number +
                ", patient: " + patient.getFirstname() + " " + patient.getSurname() +
                ", date: " + date +
                "}";
    }

    @Override
    public boolean equals(Object o) {
        if (this == o)
            return true;
        if (o.getClass() != Appointment.class)
            return false;
        Appointment d = (Appointment) o;
        return Objects.equals(d.number, this.number);
    }
}

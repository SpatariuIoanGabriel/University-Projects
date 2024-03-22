package Repository;

import Domain.Identifiable;
import Exception.*;

public interface IRepository<T extends Identifiable<U>, U> {
    void addEntity(T entity) throws NoIdenticalEntities;
    void removeEntityById(U id) throws NoEntityFound;
    T getEntityById(U id) throws NoEntityFound;
    Iterable<T> getAllEntities();
    void updateEntityById(U id, T newEntity) throws NoEntityFound;
}

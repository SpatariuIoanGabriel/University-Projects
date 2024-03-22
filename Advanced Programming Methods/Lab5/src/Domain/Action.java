package Domain;

import Exception.*;

public interface Action<T,U>{
    void undo() throws NoEntityFound, NoIdenticalEntities;
    void redo() throws NoEntityFound, NoIdenticalEntities;
}

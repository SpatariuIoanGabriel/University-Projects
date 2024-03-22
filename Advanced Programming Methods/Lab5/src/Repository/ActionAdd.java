package Repository;

import Domain.Identifiable;
import Exception.*;
import Domain.Action;

public class ActionAdd<T extends Identifiable<U>, U> implements Action<T, U> {

    private IRepository<T, U> iRepository;
    private T addedItem;

    public ActionAdd(IRepository<T, U> repo, T addedElem) {
        this.iRepository = repo;
        this.addedItem = addedElem;
    }

    @Override
    public void undo() throws NoEntityFound {
        iRepository.removeEntityById(addedItem.getId());
    }

    @Override
    public void redo() throws NoIdenticalEntities {
        iRepository.addEntity(addedItem);
    }
}
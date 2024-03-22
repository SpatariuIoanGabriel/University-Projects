package Repository;

import Domain.Action;
import Domain.Identifiable;
import Exception.*;

public class ActionUpdate<T extends Identifiable<U>, U> implements Action<T, U> {

    private IRepository<T, U> iRepository;
    private T oldItem;
    private T newItem;

    public ActionUpdate(IRepository<T, U> iRepository, T oldItem, T newItem) {
        this.iRepository = iRepository;
        this.oldItem = oldItem;
        this.newItem = newItem;
    }

    @Override
    public void undo() throws NoEntityFound, NoIdenticalEntities {
        iRepository.updateEntityById(oldItem.getId(), oldItem);
    }

    @Override
    public void redo() throws NoEntityFound, NoIdenticalEntities {
        iRepository.updateEntityById(newItem.getId(), newItem);
    }
}

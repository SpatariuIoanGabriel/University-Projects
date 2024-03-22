package Repository;

import Domain.Action;
import Domain.Identifiable;
import Exception.*;

public class ActionRemove<T extends Identifiable<U>, U> implements Action<T, U> {

    private IRepository<T, U> iRepository;
    private T deletedItem;

    public ActionRemove(IRepository<T, U> iRepository, T deletedItem) {
        this.iRepository = iRepository;
        this.deletedItem = deletedItem;
    }

    @Override
    public void undo() throws NoEntityFound, NoIdenticalEntities {
        iRepository.addEntity(deletedItem);
    }

    @Override
    public void redo() throws NoEntityFound, NoIdenticalEntities {
        iRepository.removeEntityById(deletedItem.getId());
    }
}

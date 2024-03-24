#ifndef ACTIONDELETE_H
#define ACTIONDELETE_H
#include"repository.h"
#include"song.h"
#include"action.h"

class ActionDelete : public Action
{
public:
    ActionDelete(Repository &repo, Song & song);
    void apply() override;

private:
    Repository &repo;
    Song &song;
};

#endif // ACTIONDELETE_H

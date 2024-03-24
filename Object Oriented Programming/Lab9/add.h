#ifndef ACTIONADD_H
#define ACTIONADD_H
#include"action.h"
#include"repository.h"
#include"song.h"

class ActionAdd : public Action
{
public:
    ActionAdd(Repository &repo, Song &song);
    void apply() override;

private:
    Repository &repo;
    Song &song;
};

#endif // ACTIONADD_H

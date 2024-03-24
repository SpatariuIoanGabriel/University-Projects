#include "delete.h"

ActionDelete::ActionDelete(Repository &r, Song &s) : repo{r}, song{s}
{

}

void ActionDelete::apply()
{
    repo.remove(song);
}



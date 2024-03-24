#ifndef ACTION_H
#define ACTION_H


class Action
{
public:
    Action();
    virtual void apply() = 0;
    ~Action();
};

#endif // ACTION_H

#ifndef AI_H
#define AI_H

#include <ChillinClient>

#include "ks/models.h"
#include "ks/commands.h"


class AI : public koala::chillin::client::RealtimeAI<ks::models::World*>
{
public:
    AI(ks::models::World *world);
    ~AI();

    void initialize();
    void decide();
    void sendCommand(ks::KSObject *command);
};

#endif // AI_H

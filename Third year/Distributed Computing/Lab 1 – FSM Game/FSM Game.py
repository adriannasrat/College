# bus_runner_fsm.py

# Group members:
# - Ali Adrian Nasrat
# - Diana Dawidi
# - Tesnim Omran
# - Ibrahim Mizher

# FSM game: "Catch the bus"

# The agent models a student trying to catch the morning bus.
# We use SPADE's FSMBehaviour to define a finite state machine with
# multiple states and transitions between them.

import asyncio
import random

from spade.agent import Agent
from spade.behaviour import FSMBehaviour, State

STATE_WAKE_UP = "WAKE_UP"
STATE_GET_READY = "GET_READY"
STATE_RUN = "RUN_TO_BUS"
STATE_OBSTACLE = "OBSTACLE"
STATE_BUS_STOP = "BUS_STOP"
STATE_SUCCESS = "SUCCESS"
STATE_FAIL = "FAILS"

class WakeUpState(State):
    async def run(self):
        print("\n[WAKE_UP] Your alarm goes off at 07:00...")

        oversleep_chance = random.random()
        if oversleep_chance < 0.2:
            print("You snooze too many times and oversleep...")
            self.set_next_state(STATE_FAIL)
        else:
            print("You get out of bed (more or less on time).")
            self.set_next_state(STATE_GET_READY)

class GetReadyState(State):
    async def run(self):
        print("\n[GET_READY] You are getting ready (shower, clothes, breakfast).")

        delay_factor = random.random()
        if delay_factor < 0.3:
            print("You are super efficient today and get ready quickly!")
        elif delay_factor < 0.7:
            print("You move at normal pace.")
        else:
            print("You stare at your phone for a bit too long...")
        print("Time to leave the apartment and run to the bus stop!")
        self.set_next_state(STATE_RUN)

class RunToBusState(State):
    async def run(self):
        print("\n[RUN_TO_BUS] You are running to the bus stop...")

        obstacle_chance = random.random()
        if obstacle_chance < 0.5:
            print("On the way, something happens!")
            self.set_next_state(STATE_OBSTACLE)
        else:
            print("The path is clear. You can see the bus stop ahead.")
            self.set_next_state(STATE_BUS_STOP)

class ObstacleState(State):
    async def run(self):
        print("\n[OBSTACLE] An obstacle appears on your way!")

        event = random.choice(
            [
                "A red traffic light stops you.",
                "Your drop your phone and must pick it up.",
                "A slippery path makes you fall."
            ]
        )
        print(event)

        handle_chance = random.random()
        if handle_chance < 0.6:
            print("You handle the situation and keep running, but you lose some time.")
            self.set_next_state(STATE_RUN)
        else:
            print("You lose too much time... the bus is probably gone.")
            self.set_next_state(STATE_FAIL)

class BusStopState(State):
    async def run(self):
        print("\n[BUS_STOP] You arrive at the bus stop!")

        catch_chance = random.random()
        if catch_chance < 0.6:
            print("You arrive just in time. The bus doors are still open!")
            self.set_next_state(STATE_SUCCESS)
        else:
            print("You see the bus leaving just as you arrive...")
            self.set_next_state(STATE_FAIL)

class SuccessState(State):
    async def run(self):
        print("\n[SUCCESS] You caught the bus and will be on time to class!")
        self.kill()

class FailState(State):
    async def run(self):
        print("\n[FAIL] You missed the bus. Maybe next time set more alarms...")
        self.kill()

class BusRunnerFSM(FSMBehaviour):
    """""
    FSMBheaviour that defines the whole game.
    """""

    async def on_start(self):
        print("\nFSM starting... Initial state:", self.current_state)

    async def on_end(self):
        print("\nFSM finished with state:", self.current_state)
        await self.agent.stop()

class BusRunnerAgent(Agent):
    async def setup(self):
        print(f"Agent {self.jid} starting...")

        fsm = BusRunnerFSM()

        # Register states
        fsm.add_state(name=STATE_WAKE_UP, state=WakeUpState(), initial=True)
        fsm.add_state(name=STATE_GET_READY, state=GetReadyState())
        fsm.add_state(name=STATE_RUN, state=RunToBusState())
        fsm.add_state(name=STATE_OBSTACLE, state=ObstacleState())
        fsm.add_state(name=STATE_BUS_STOP, state=BusStopState())
        fsm.add_state(name=STATE_SUCCESS, state=SuccessState())
        fsm.add_state(name=STATE_FAIL, state=FailState())

        # Transitions
        fsm.add_transition(source=STATE_WAKE_UP, dest=STATE_GET_READY)
        fsm.add_transition(source=STATE_WAKE_UP, dest=STATE_FAIL)

        fsm.add_transition(source=STATE_GET_READY, dest=STATE_RUN)

        fsm.add_transition(source=STATE_RUN, dest=STATE_OBSTACLE)
        fsm.add_transition(source=STATE_RUN, dest=STATE_BUS_STOP)

        fsm.add_transition(source=STATE_OBSTACLE, dest=STATE_RUN)
        fsm.add_transition(source=STATE_OBSTACLE, dest=STATE_FAIL)

        fsm.add_transition(source=STATE_BUS_STOP, dest=STATE_SUCCESS)
        fsm.add_transition(source=STATE_BUS_STOP, dest=STATE_FAIL)

        self.add_behaviour(fsm)
    
async def main():
    jid = "agent1@localhost"
    password = "mypassword"

    bus_agent = BusRunnerAgent(jid, password)
    await bus_agent.start(auto_register=True)

    print("BusRunnerAgent started. The game will now run using the FSM.")

    try:
        while bus_agent.is_alive():
           await asyncio.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping agent...")
    finally:
        if bus_agent.is_alive():
            await bus_agent.stop()
        print("\nAgent stopped.")

if __name__ == "__main__":
    asyncio.run(main())
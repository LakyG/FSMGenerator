
class Transition:
    def __init__(self, fromState, toState, conditions):
        self.fromState = fromState
        self.toState = toState
        self.conditions = conditions
        self.outputs = []

class State:
    def __init__(self, name):
        self.name = name
        self.transitions = []
        self.outputs = []

class FSM:

    def __init__(self, type):
        self.type = type
        self.states = getStates()
        self.numStates = len(self.states)

    def addTransition(self, fromState, toState, conditions):
        t = Transition(fromState, toState, conditions)
        
        if (self.type == "Moore"):
            t.outputs = None


def getStates():
    numStates = int(input("Enter the number of states you want: "))

    states = []

    for i in range(numStates):
        name = input("State " + str(i) + " name: ")
        states.append(State(name))

    return states

def printStates(states):
    for s in states:
        print("State \"" + s.name + "\"")

def main():
    fsm = FSM("Moore")
    printStates(fsm.states)

if __name__ == "__main__":
    main()

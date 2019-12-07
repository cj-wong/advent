import sys
from copy import copy
from typing import Any, Dict, Callable, List



class Operator:
    """An Intcode operator with potential parameters.

    Attributes:
        code (int): the operator code
        params (List[int]): parameters defined in op, if present
        functions (Dict[int, Callable[..., Any]]): functions associated
            with a given operator code

    """
    functions = {
        1: lambda x, y: x + y,
        2: lambda x, y: x * y,
        5: lambda z: z != 0,
        6: lambda z: z == 0,
        7: lambda x, y: 1 if x < y else 0,
        8: lambda x, y: 1 if x == y else 0,
        }

    def __init__(self, op: int) -> None:
        """Initialize operator data, and then call for parameters."""
        self.code = op
        self.read_params()

    def read_params(self) -> None:
        """Get parameters from the operator. Parameters are defined
        to be either 0 or 1. The number of parameters can be from
        0 ([]) to 2.

        """
        if self.code < 100:
            self.params = []
        else:
            self.params = [int(p) for p in str(self.code//100)]
            self.code %= 100

    def run(self, args: List[int]) -> int:
        """Runs an operation. Only [1, 2, 5, 6, 7, 8] are supported.

        Args:
            args (List[int]): arguments to the operator

        """
        return self.functions[self.code](*args)


class Interpreter:
    """Interprets Intcode. e.g. 1,0,0,3

    Attributes:
        jumps (Dict[int, int]): represents number of jumps per operator
            defined by the key
        stop (int): the stop operator; 99

    """
    jumps = {
        1: 4,
        2: 4,
        3: 2,
        4: 2,
        5: 3,
        6: 3,
        7: 4,
        8: 4,
        }

    stop = 99

    def __init__(self, ops: str) -> None:
        """Initialize queued operations.

        Args:
            ops (str): Intcode operations

        """
        self.ops = [int(op) for op in ops]

    def save_state(self) -> None:
        """Save current state, to restore later."""
        self.state = copy(self.ops)

    def restore_state(self) -> None:
        """Restore a copy of state."""
        self.ops = copy(self.state)

    def store_phases(self, phase: int, signal: int) -> None:
        """Store the phase inputs including signal phase output.

        Args:
            phase (int): the current phase setting
            signal (int): the last phase output; if this is the first
                iteration, it's 0

        """
        self.phases = [phase, signal]

    def store_input(self, index: int, value: int = None) -> None:
        """Store an integer from stdin into index `index`.

        Args:
            index (int): where the stdin input goes
            value (int, optional): the value to store at index;
                defaults to 0

        """
        if value is None:
            try:
                self.ops[index] = int(sys.argv[1])
            except IndexError:
                self.ops[index] = self.phases[0]
                self.phases = self.phases[1:]
        else:
            self.ops[index] = value

    def run_ops(self, *, jump: int = 0, silent: bool = False) -> None:
        """Runs the operations `self.ops`.

        Args:
            jump (int, optional): the starting position to run onward;
                defaults to 0
            silent (bool, optional): whether to suppress stdout;
                defaults to False

        """
        while True:
            operator = Operator(self.ops[jump])

            if operator.code == 99:
                if not silent:
                    print('opcode 99:', self.ops)
                return

            jump_next = jump + self.jumps[operator.code]
            jump_args = jump + 1
            args = self.ops[jump_args:jump_next]


            if operator.code in [1, 2, 7, 8]:
                x, y, dest = args
                if not operator.params:
                    x = self.ops[x]
                    y = self.ops[y]
                elif len(operator.params) == 2 and operator.params[-1] == 0:
                    x = self.ops[x]
                elif len(operator.params) == 1:
                    y = self.ops[y]
                self.ops[dest] = operator.run([x, y])
            elif operator.code in [5, 6]:
                z, dest = args
                if not operator.params:
                    z = self.ops[z]
                    dest = self.ops[dest]
                elif len(operator.params) == 2 and operator.params[-1] == 0:
                    z = self.ops[z]
                elif len(operator.params) == 1:
                    dest = self.ops[dest]
                if operator.run([z]):
                    jump = dest
                    continue
            elif operator.code == 3:
                self.store_input(self.ops[jump_args])
            else: # operator.code == 4
                self.signal = (
                    args[0]
                    if operator.params
                    else self.ops[self.ops[jump_args]]
                    )
                if not silent:
                    print('opcode 4:', self.signal)

            jump = jump_next

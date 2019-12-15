import sys
from collections import defaultdict
from copy import copy
from typing import Any, Dict, Callable, List


JUMPS = {
    1: 4,
    2: 4,
    3: 2,
    4: 2,
    5: 3,
    6: 3,
    7: 4,
    8: 4,
    9: 2,
    }


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

    nparams = {
        code: jump - 1
        for code, jump
        in JUMPS.items()
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
            while len(self.params) < self.nparams[self.code]:
                self.params.insert(0, 0)

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
    positional = [0, 2]

    stop = 99

    def __init__(self, ops: str, silent: bool = False) -> None:
        """Initialize queued operations.

        Args:
            ops (str): Intcode operations
            silent (bool, optional): whether to suppress prints;
                defaults to False

        """
        self.ops = defaultdict(
            int,
            {index: int(op) for index, op in enumerate(ops)}
            )
        self.silent = silent
        self.jump = 0
        self.relative = 0

    def save_state(self) -> None:
        """Save current state, to restore later."""
        self.state = copy(self.ops)

    def restore_state(self) -> None:
        """Restore a copy of state."""
        self.ops = copy(self.state)
        self.jump = 0

    def slice(self, start: int, end: int) -> List[int]:
        """Slices `self.ops` like how a list can be sliced.

        Args:
            start (int): the starting index
            end (int): the terminating index

        """
        return [self.ops[i] for i in range(start, end)]

    def store_input(self, index: int, value: int = None) -> None:
        """Store an integer from stdin into index `index`.

        Args:
            index (int): where the stdin input goes
            value (int, optional): the value to store at index;
                defaults to 0

        """
        if value is None:
            self.ops[index] = int(sys.argv[1])
        else:
            self.ops[index] = value

    def print(self, n: int) -> None:
        """Prints `n`. Used for operator 104.

        Args:
            n (int): the direct number to print

        """
        if not self.silent:
            print('opcode 4:', n)

    def print_at(self, index: int) -> None:
        """Print a stored operator/operand at index `index`.

        Args:
            index (int): the index of the operator

        """
        if not self.silent:
            print('opcode 4:', self.ops[index])

    def get(self, index: int, parameter: int) -> int:
        """Determines the value at index `index` depending
        on `parameter` (0 is literal, 2 is relative).

        Args:
            index (int): the index of operations; modified by parameter;
                if parameter is 1, return this as a literal value,
                not as an index
            parameter (int): either 0 (literal) or 2 (relative)

        """
        if parameter == 1:
            return index
        return self.ops[index if parameter == 0 else self.relative + index]

    def run_ops(self) -> None:
        """Runs the operations `self.ops`."""
        while True:
            operator = Operator(self.ops[self.jump])

            if operator.code == 99:
                if not self.silent:
                    print('opcode 99:', self.ops.values())
                return

            jump_next = self.jump + JUMPS[operator.code]
            jump_args = self.jump + 1
            args = self.slice(jump_args, jump_next)

            if operator.code in [1, 2, 7, 8]:
                x, y, dest = args
                if not operator.params:
                    x = self.ops[x]
                    y = self.ops[y]
                else:
                    if operator.params[0] == 2:
                        dest += self.relative
                    y, x = [
                        self.get(index, param)
                        for index, param
                        in zip([y, x], operator.params[1:])
                        ]
                self.ops[dest] = operator.run([x, y])
            elif operator.code in [5, 6]:
                z, dest = args
                if not operator.params:
                    z = self.ops[z]
                    dest = self.ops[dest]
                else:
                    dest, z = [
                        self.get(index, param)
                        for index, param
                        in zip([dest, z], operator.params)
                        ]
                if operator.run([z]):
                    self.jump = dest
                    continue
            elif operator.code == 3:
                dest = args[0]
                # In this case, the parameter must be 2; 1 is invalid
                # for operator 3.
                if operator.params:
                    dest += self.relative
                self.store_input(dest)
            elif operator.code == 4:
                z = args[0]
                if not operator.params:
                    self.print_at(z)
                elif 2 in operator.params:
                    self.print_at(self.relative + z)
                else:
                    self.print(z)
            else: # operator.code == 9
                z = args[0]
                if operator.params:
                    if 2 in operator.params:
                        z = self.ops[self.relative + z]
                elif not operator.params:
                    z = self.ops[z]
                self.relative += z

            self.jump = jump_next

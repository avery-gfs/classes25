import time
import os


class VM:
    def __init__(self):
        self.ip = 0  # Index of current instruction
        self.lastMem = -1  # Last memory index read/written (for log)
        self.output = ""  # Output from program (store in string for TUI)
        self.halted = False  # Was a halt requested
        self.steps = 0  # Count total instructions evaluated
        self.instrs = []  # Instructions get populated by run method
        self.registers = [0, 0, 0, 0]  # Registers initialized to zero
        self.memory = []  # Memory gets initialized by mem command

    def run(self, path, fps, logging=True):
        with open(path) as file:
            lines = [line.strip() for line in file.read().splitlines()]

        # Ignore empty source lines and comment lines
        self.instrs = [line for line in lines if line and not line.startswith("--")]

        while not self.halted:
            self.steps += 1
            os.system("clear")

            if logging:
                self.runLog()
            else:
                self.runInst()

            if self.halted:
                print(self.output)
            else:
                print(self.output, end="", flush=True)

            # Pause to visualize execution
            time.sleep(1 / fps)

    def regIndex(self, regName):
        if not regName.startswith("r"):
            raise Error(f"Invalid register name {regName}")

        return int(regName[1:])

    def binOp(self, op, a, b):
        match op:
            case "add":
                return a + b
            case "sub":
                return a - b
            case "mul":
                return a * b
            case "div":
                return a // b
            case "mod":
                return a % b
            case "eq":
                return int(a == b)
            case "gt":
                return int(a > b)
            case "lt":
                return int(a < b)
            case "and":
                return int(a != 0 and b != 0)
            case "or":
                return int(a != 0 or b != 0)

        raise Error(f"Unreachable operation {op}")

    def runInst(self):
        tokens = self.instrs[self.ip].split()
        op = tokens[0]

        def setReg(value):
            self.registers[self.regIndex(tokens[1])] = value

        # Resolve instruction argument, loading values from registers
        # and parsing constants to numbers
        args = [
            self.registers[self.regIndex(token)]
            if token.startswith("r")
            else int(token)
            for token in tokens[1:]
        ]

        match op:
            case (
                "add"
                | "sub"
                | "mul"
                | "div"
                | "mod"
                | "eq"
                | "gt"
                | "lt"
                | "and"
                | "or"
            ):
                setReg(self.binOp(op, args[0], args[1]))
                self.ip += 1

            case "not":
                setReg(int(not args[0]))
                self.ip += 1

            case "set":
                setReg(args[1])
                self.ip += 1

            case "jmp":
                self.ip += args[0]

            case "jeq":
                self.ip += args[0] if args[1] == args[2] else 1

            case "jne":
                self.ip += args[0] if args[1] != args[2] else 1

            case "halt":
                self.halted = True

            case "mem":
                self.memory = args
                self.ip += 1

            case "load":
                setReg(self.memory[args[1]])
                self.lastMem = args[1]
                self.ip += 1

            case "store":
                self.memory[args[1]] = args[0]
                self.lastMem = args[1]
                self.ip += 1

            case "log":
                if self.output:
                    self.output += "\n"

                self.output += str(args[0])
                self.ip += 1

            case "print":
                self.output += chr(args[0])
                self.ip += 1

            case _:
                raise Error(f"Invalid instruction {op}")

    def runLog(self):
        for index, inst in enumerate(self.instrs):
            prefix = "> " if index == self.ip else "  "
            print(f"{prefix}{inst}")

        print(f"\nsteps: {self.steps}")

        # Run instruction before doing rest of logging so that logs
        # reflect the VM state after running the current instruction
        self.runInst()

        print()

        for index, reg in enumerate(self.registers):
            print(f"r{index}: {reg}")

        memStr = ", ".join(
            f"*{val}" if index == self.lastMem else f" {val}"
            for index, val in enumerate(self.memory)
        )

        print(f"\nmemory: [{memStr} ]\n")


VM().run("collatz/demo.gfss", 20)

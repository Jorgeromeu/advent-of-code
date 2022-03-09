import time

import numpy as np

class ALU:
    input: list
    ptr: int

    mem: dict
    ops: dict

    def inp(self, args):
        dst, = args
        self.mem[dst] = self.input[self.ptr]
        self.ptr += 1

    def add(self, args):
        dst, num = args
        self.mem[dst] += self.rd(num)

    def mul(self, args):
        dst, num = args
        self.mem[dst] *= self.rd(num)

    def mod(self, args):
        dst, num = args
        self.mem[dst] %= self.rd(num)

    def div(self, args):
        dst, num = args
        self.mem[dst] //= self.rd(num)

    def eql(self, args):
        dst, num = args
        self.mem[dst] = 1 if self.rd(dst) == self.rd(num) else 0

    def __init__(self, input_txt: str):
        self.input = [int(d) for d in input_txt]
        self.ptr = 0

        self.mem = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
        self.ops = {'inp': self.inp, 'add': self.add, 'mul': self.mul, 'mod': self.mod, 'div': self.div, 'eql': self.eql}

    def rd(self, key):

        if key in {'w', 'x', 'y', 'z'}:
            return self.mem[key]
        else:
            return int(key)

    def exec(self, instruction: str):
        args = instruction.split(' ')
        self.ops[args[0]](args[1:])

    def exec_prog(self, prog):
        for instr in prog:
            self.exec(instr)

    def exec_prog_from_file(self, filename: str):
        self.exec_prog(parse_prog(filename))

    def print_state(self):
        for k,v in self.mem.items():
            print(k, v)

def parse_prog(filename: str):
    return [s.strip() for s in open(filename).readlines()]
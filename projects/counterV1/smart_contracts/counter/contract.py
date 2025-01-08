from algopy import ARC4Contract, UInt64
from algopy.arc4 import abimethod


class Counter(ARC4Contract):
    counter: UInt64

    def __init__(self)->None:
        self.counter = UInt64(0)

    @abimethod()
    def increment(self)->None:
        self.counter += UInt64(1)
    
    @abimethod()
    def decrement(self)->None:
        self.counter -= UInt64(1)

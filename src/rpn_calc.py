############################ Copyrights and license ############################
#                                                                              #
# Copyright 2021 Raul Alvarez <ralvarezb78@gmail.com>                          #
#                                                                              #
# This file is part of RPNCalc: Reverse Polish Calculator                      #
#                                                                              #
#                                                                              #
# RPNCalc is free software: you can redistribute it and/or modify it under     #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# RPNCalc is distributed in the hope that it will be useful, but WITHOUT ANY   #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with RPNCalc. If not, see <http://www.gnu.org/licenses/>.              #
#                                                                              #
################################################################################

import numpy as np
import sys
__version__ = "0.1"

class calc_stack:
    def __init__(self, levels=8, full_repr=True):
        self.stack = np.full((levels,), None)
        self.__top__ = 0
        self.__fullrepr__ = full_repr
        self.lastop = "None"

    def full(self):
        """Check if stack is full, returns a boolean"""
        return self.__top__ >= self.stack.shape[0]

    def empty(self):
        """Check if stack is empty, returns a boolean"""
        return self.__top__ == 0

    def push(self, element):
        """Push one element onto stack"""
        self.lastop = sys._getframe().f_code.co_name + "()"
        if not self.full():
            self.stack[self.__top__] = element
            self.__top__ += 1
        else:
            pass  # TODO: handle

    def pop(self):
        """Pops element from top of stack"""
        self.lastop = sys._getframe().f_code.co_name + "()"
        if not self.empty():
            self.__top__ -= 1
            return self.stack[self.__top__]
        else:
            return None

    def dup(self):
        """Duplicates Top Of Stack"""
        self.lastop = sys._getframe().f_code.co_name + "()"
        if (not self.full()) and (not self.empty()):
            self.stack[self.__top__] = self.stack[self.__top__ - 1]
            self.__top__ += 1
        else:
            pass  # TODO: handle

    def ndup(self, pos):
        """Duplicates a value from given position and stores on top of stack"""
        self.lastop = sys._getframe().f_code.co_name + "()"
        if (
            (not self.full())
            and (not self.empty())
            and (pos >= 0)
            and (pos < self.__top__)
        ):
            self.stack[self.__top__] = self.stack[self.__top__ - pos - 1]
            self.__top__ += 1
        else:
            pass  # TODO: handle

    def xchg(self):
        """Exchanges two first values from top of stack"""
        self.lastop = sys._getframe().f_code.co_name + "()"
        if self.__top__ > 2:
            self.stack[self.__top__ - 1], self.stack[self.__top__ - 2] = (
                self.stack[self.__top__ - 2],
                self.stack[self.__top__ - 1],
            )
        else:
            pass  # TODO: handle

    def __repr__(self) -> str:
        repr = "Memory ID: {}\n".format(hex(id(self.stack)).upper().replace("X", "x"))
        repr += f"Stack size: {self.stack.shape[0]}\n"
        if self.__top__ < self.stack.shape[0]:
            repr += f"Top Of Stack: {self.__top__}\n"
        else:
            repr += f"Top Of Stack: OVERFLOW\n"
        repr += "Representation: "

        if self.__fullrepr__:
            repr += "FULL\n"
        else:
            repr += "SHORT\n"
        repr += "Methods: "
        mthd = list()
        for k in self.__class__.__dict__.items():
            if hasattr(k[1], "__call__") and not k[0].startswith("__"):
                mthd.append(k[0] + "()")
        mthd = sorted(mthd, key=str.lower)
        repr += mthd.__str__().replace("[", "{").replace("]", "}") + "\n"
        repr += f"Last OP: {self.lastop}\n\n"
        repr += "STACK:\n"
        if self.__fullrepr__:
            for k in range(0, self.stack.shape[0] - self.__top__):
                repr += "\t-\n"
        for k in range(0, self.__top__):
            repr += f"\t{self.__top__-k-1}: {str(self.stack[k])}\n"
        return repr

    def __str__(self) -> str:
        repr = ""
        if self.__fullrepr__:
            for k in range(0, self.stack.shape[0] - self.__top__):
                repr += "-\n"
        for k in range(0, self.__top__):
            repr += f"{self.__top__-k-1}: {str(self.stack[k])}\n"
        return repr

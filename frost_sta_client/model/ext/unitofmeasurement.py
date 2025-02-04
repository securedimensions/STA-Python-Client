# Copyright (C) 2021 Fraunhofer Institut IOSB, Fraunhoferstr. 1, D 76131
# Karlsruhe, Germany.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

class UnitOfMeasurement:
    def __init__(self,
                 name="",
                 symbol="",
                 definition=""):
        self.name = name
        self.symbol = symbol
        self.definition = definition

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) or value is None:
            self._name = value
            return
        raise ValueError('name should be of type str!')

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        if isinstance(value, str) or value is None:
            self._symbol = value
            return
        raise ValueError('symbol should be of type str!')

    @property
    def definition(self):
        return self._definition

    @definition.setter
    def definition(self, value):
        if isinstance(value, str) or value is None:
            self._definition = value
            return
        raise ValueError('definition should be of type str!')

    def __getstate__(self):
        data = {
            'symbol': self._symbol,
            'definition': self._definition,
            'name': self._name
        }
        return data

    def __setstate__(self, state):
        self.symbol = state.get("symbol", None)
        self.definition = state.get("definition", None)
        self.name = state.get("name", None)

    def __eq__(self, other):
        if other is None:
            return False
        if id(self) == id(other):
            return True
        if self.name != other.name:
            return False
        if self.definition != other.definition:
            return False
        if self.symbol != other.symbol:
            return False
        return True

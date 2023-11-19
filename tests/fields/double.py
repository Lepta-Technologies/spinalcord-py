# Copyright 2023 Lepta Technologies
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pathlib import Path
import unittest

from spinalcord.utils.bytebuffer import ByteBuffer
from spinalcord.utils.byteconverter import ByteConverter
from spinalcord.fields import DoubleField
from spinalcord.exceptions import FieldNotSetException


class DoubleFieldTest(unittest.TestCase):

    def test_clear(self):
        # Check DoubleField clear method
        double_field = DoubleField("doubleField")
        double_field.set(0.0)
        double_field.clear()
        try:
            double_field.get()
            self.fail()
        except FieldNotSetException:
            self.assertTrue(True)

    def test_from_to_bytes(self):
        # Get reference bytes
        reference_path = Path(__file__).parent.joinpath("refs", "double.bin")
        reference_file = open(reference_path, "rb")
        all_bytes = reference_file.read(18)
        reference_file.close()
        double_field = DoubleField("doubleField")
        buffer = ByteBuffer(all_bytes)
        # Check min value
        double_field.from_bytes(buffer)
        self.assertEqual(double_field.get(), 1.7e-308)
        reference_bytes = all_bytes[:9]
        self.assertEqual(double_field.to_bytes(), reference_bytes)
        # Check max value
        double_field.from_bytes(buffer)
        self.assertEqual(double_field.get(), 1.7e+308)
        reference_bytes = all_bytes[9:]
        self.assertEqual(double_field.to_bytes(), reference_bytes)

    def test_get_byte_length(self):
        # Check DoubleField get_byte_length method
        double_field = DoubleField("doubleField")
        self.assertEqual(double_field.get_byte_length(), 1)
        double_field.set(0.0)
        self.assertEqual(double_field.get_byte_length(), 9)

    def test_get_column_name(self):
        # Check DoubleField get_column_name method
        double_field = DoubleField("doubleField")
        self.assertEqual(double_field.get_column_name(), "doubleField")

    def test_get_set(self):
        # Check DoubleField get and set methods
        double_field = DoubleField("doubleField")
        # Check an exception is thrown when attempting to get the field's value before it is set
        try:
            double_field.get()
            fail()
        except FieldNotSetException:
            self.assertTrue(True)
        # Set and check field's value
        double_field.set(0.0)
        try:
            self.assertEqual(double_field.get(), 0.0)
        except FieldNotSetException:
            self.fail()

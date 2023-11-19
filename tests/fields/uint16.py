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
from spinalcord.exceptions import FieldNotSetException
from spinalcord.fields import UInt16Field


class UInt16FieldTest(unittest.TestCase):

    def test_clear(self):
        # Check UInt16Field clear method
        uint16_field = UInt16Field("uInt16Field")
        uint16_field.set(0)
        uint16_field.clear()
        try:
            uint16_field.get()
            self.fail()
        except FieldNotSetException:
            self.assertTrue(True)

    def test_from_to_bytes(self):
        # Get reference bytes
        reference_path = Path(__file__).parent.joinpath("refs", "uint16.bin")
        reference_file = open(reference_path, "rb")
        all_bytes = reference_file.read(6)
        reference_file.close()
        uint16_field = UInt16Field("uInt16Field")
        buffer = ByteBuffer(all_bytes)
        # Check min value
        uint16_field.from_bytes(buffer)
        self.assertEqual(uint16_field.get(), 0)
        reference_bytes = all_bytes[:3]
        self.assertEqual(uint16_field.to_bytes(), reference_bytes)
        # Check max value
        uint16_field.from_bytes(buffer)
        self.assertEqual(uint16_field.get(), 65535)
        reference_bytes = all_bytes[3:]
        self.assertEqual(uint16_field.to_bytes(), reference_bytes)

    def test_get_byte_length(self):
        # Check UInt16Field get_byte_length method
        uint16_field = UInt16Field("uInt16Field")
        self.assertEqual(uint16_field.get_byte_length(), 1)
        uint16_field.set(0)
        self.assertEqual(uint16_field.get_byte_length(), 3)

    def test_get_column_name(self):
        # Check UInt16Field get_column_name method
        uint16_field = UInt16Field("uInt16Field")
        self.assertEqual(uint16_field.get_column_name(), "uInt16Field")

    def test_get_set(self):
        # Check UInt16Field get and set methods
        uint16_field = UInt16Field("uInt16Field")
        # Check an exception is thrown when attempting to get the field's value before it is set
        try:
            uint16_field.get()
            fail()
        except FieldNotSetException:
            self.assertTrue(True)
        # Set and check field's value
        uint16_field.set(0)
        try:
            self.assertEqual(uint16_field.get(), 0)
        except FieldNotSetException:
            self.fail()

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
from spinalcord.fields import UInt8Field


class UInt8FieldTest(unittest.TestCase):

    def test_clear(self):
        # Check UInt8Field clear method
        uint8_field = UInt8Field("uInt8Field")
        uint8_field.set(0)
        uint8_field.clear()
        try:
            uint8_field.get()
            self.fail()
        except FieldNotSetException:
            self.assertTrue(True)

    def test_from_to_bytes(self):
        # Get reference bytes
        reference_path = Path(__file__).parent.joinpath("refs", "uint8.bin")
        reference_file = open(reference_path, "rb")
        all_bytes = reference_file.read(4)
        reference_file.close()
        uint8_field = UInt8Field("uInt8Field")
        buffer = ByteBuffer(all_bytes)
        # Check min value
        uint8_field.from_bytes(buffer)
        self.assertEqual(uint8_field.get(), 0)
        reference_bytes = all_bytes[:2]
        self.assertEqual(uint8_field.to_bytes(), reference_bytes)
        # Check max value
        uint8_field.from_bytes(buffer)
        self.assertEqual(uint8_field.get(), 255)
        reference_bytes = all_bytes[2:]
        self.assertEqual(uint8_field.to_bytes(), reference_bytes)

    def test_get_byte_length(self):
        # Check UInt8Field get_byte_length method
        uint8_field = UInt8Field("uInt8Field")
        self.assertEqual(uint8_field.get_byte_length(), 1)
        uint8_field.set(0)
        self.assertEqual(uint8_field.get_byte_length(), 2)

    def test_get_column_name(self):
        # Check UInt8Field get_column_name method
        uint8_field = UInt8Field("uInt8Field")
        self.assertEqual(uint8_field.get_column_name(), "uInt8Field")

    def test_get_set(self):
        # Check UInt8Field get and set methods
        uint8_field = UInt8Field("uInt8Field")
        # Check an exception is thrown when attempting to get the field's value before it is set
        try:
            uint8_field.get()
            fail()
        except FieldNotSetException:
            self.assertTrue(True)
        # Set and check field's value
        uint8_field.set(0)
        try:
            self.assertEqual(uint8_field.get(), 0)
        except FieldNotSetException:
            self.fail()

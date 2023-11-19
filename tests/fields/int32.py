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
from spinalcord.fields import Int32Field


class Int32FieldTest(unittest.TestCase):

    def test_clear(self):
        # Check Int32Field clear method
        int32_field = Int32Field("int32Field")
        int32_field.set(0)
        int32_field.clear()
        try:
            int32_field.get()
            self.fail()
        except FieldNotSetException:
            self.assertTrue(True)

    def test_from_to_bytes(self):
        # Get reference bytes
        reference_path = Path(__file__).parent.joinpath("refs", "int32.bin")
        reference_file = open(reference_path, "rb")
        all_bytes = reference_file.read(10)
        reference_file.close()
        int32_field = Int32Field("int32Field")
        buffer = ByteBuffer(all_bytes)
        # Check min value
        int32_field.from_bytes(buffer)
        self.assertEqual(int32_field.get(), -2147483648)
        reference_bytes = all_bytes[:5]
        self.assertEqual(int32_field.to_bytes(), reference_bytes)
        # Check max value
        int32_field.from_bytes(buffer)
        self.assertEqual(int32_field.get(), 2147483647)
        reference_bytes = all_bytes[5:]
        self.assertEqual(int32_field.to_bytes(), reference_bytes)

    def test_get_byte_length(self):
        # Check Int32Field get_byte_length method
        int32_field = Int32Field("int32Field")
        self.assertEqual(int32_field.get_byte_length(), 1)
        int32_field.set(0)
        self.assertEqual(int32_field.get_byte_length(), 5)

    def test_get_column_name(self):
        # Check Int32Field get_column_name method
        int32_field = Int32Field("int32Field")
        self.assertEqual(int32_field.get_column_name(), "int32Field")

    def test_get_set(self):
        # Check Int32Field get and set methods
        int32_field = Int32Field("int32Field")
        # Check an exception is thrown when attempting to get the field's value before it is set
        try:
            int32_field.get()
            fail()
        except FieldNotSetException:
            self.assertTrue(True)
        # Set and check field's value
        int32_field.set(0)
        try:
            self.assertEqual(int32_field.get(), 0)
        except FieldNotSetException:
            self.fail()

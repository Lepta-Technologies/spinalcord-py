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

from spinalcord.exceptions import FieldNotSetException
from spinalcord import fields
from .fieldsmodel import FieldsModel


class ModelTest(unittest.TestCase):

    def test_clear(self):
        # Check ModelTest clear method
        fields_model = FieldsModel()
        fields_model.double_field.set(0.0)
        fields_model.clear()
        try:
            fields_model.double_field.get()
            self.fail()
        except FieldNotSetException:
            self.assertTrue(True)

    def test_from_to_bytes(self):
        # Get reference bytes
        reference_path = Path(__file__).parent.joinpath("refs", "fieldsmodel.bin")
        reference_file = open(reference_path, "rb")
        reference_bytes = reference_file.read(17)
        reference_file.close()
        fields_model = FieldsModel()
        # Check ModelTest from_bytes method
        fields_model.from_bytes(reference_bytes)
        self.assertEqual(fields_model.double_field.get(), 0.0)
        self.assertEqual(fields_model.int32_field.get(), 0)
        self.assertEqual(fields_model.uint16_field.get(), 0)
        # Check ModelTest to_bytes method
        self.assertEqual(fields_model.to_bytes(), reference_bytes)

    def test_get_byte_length(self):
        # Get reference bytes
        reference_path = Path(__file__).parent.joinpath("refs", "fieldsmodel.bin")
        reference_file = open(reference_path, "rb")
        reference_bytes = reference_file.read(17 + 1)
        reference_file.close()
        fields_model = FieldsModel()
        # Check ModelTest get_byte_length method
        fields_model.from_bytes(reference_bytes)
        self.assertEqual(fields_model.get_byte_length(), 17)

    def test_get_fields(self):
        # Create reference array
        reference_fields = [
            fields.DoubleField("doubleField"), fields.Int32Field("int32Field"), fields.UInt16Field("uInt16Field")
        ]
        # Check ModelTest get_fields method
        fields_model = FieldsModel()
        test_fields = fields_model.get_fields()
        for i in range(len(test_fields)):
            self.assertIsInstance(test_fields[i], type(reference_fields[i]))

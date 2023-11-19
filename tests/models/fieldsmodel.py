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

from spinalcord import fields
from spinalcord import models


class FieldsModel(models.Model):
    double_field = fields.DoubleField("doubleField")
    int32_field = fields.Int32Field("int32Field")
    uint16_field = fields.UInt16Field("uInt16Field")

    def get_fields(self):
        return [self.double_field, self.int32_field, self.uint16_field]

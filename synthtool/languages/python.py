# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import re

import synthtool as s


PB2_HEADER = r"""(\# -\*- coding: utf-8 -\*-\n)(\# Generated by the protocol buffer compiler\.  DO NOT EDIT!.*?import sys)"""
PB2_GRPC_HEADER = r"""(\# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!)
(import grpc)"""

LICENSE = """
# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License."""


def fix_pb2_headers(*, proto_root: str = "**/*_pb2.py") -> None:
    s.replace(
        proto_root,
        PB2_HEADER,
        fr"\g<1>{LICENSE}\n\n\g<2>",  # change order to avoid stacking replacements
        flags=re.DOTALL | re.MULTILINE,
    )


def fix_pb2_grpc_headers(*, proto_root: str = "**/*_pb2_grpc.py") -> None:
    s.replace(
        proto_root,
        PB2_GRPC_HEADER,
        fr"{LICENSE}\n\n\g<1>\n\n\g<2>",  # add line breaks to avoid stacking replacements
    )

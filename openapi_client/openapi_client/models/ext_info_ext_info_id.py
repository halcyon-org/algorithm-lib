# coding: utf-8

"""
    BeLifeline Server API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.5.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ExtInfoExtInfoId(str, Enum):
    """
    ExtInfoExtInfoId
    """

    """
    allowed enum values
    """
    HOGE_ID = 'HOGE_ID'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ExtInfoExtInfoId from a JSON string"""
        return cls(json.loads(json_str))



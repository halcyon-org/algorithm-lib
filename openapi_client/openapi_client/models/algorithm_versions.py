# coding: utf-8

"""
    BeLifeline Server API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.4.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class AlgorithmVersions(str, Enum):
    """
    AlgorithmVersions
    """

    """
    allowed enum values
    """
    LASTEST = 'lastest'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AlgorithmVersions from a JSON string"""
        return cls(json.loads(json_str))



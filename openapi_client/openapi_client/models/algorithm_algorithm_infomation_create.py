# coding: utf-8

"""
    BeLifeline Server API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.5.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Union
from openapi_client.models.ext_info_ext_info_id import ExtInfoExtInfoId
from typing import Optional, Set
from typing_extensions import Self

class AlgorithmAlgorithmInfomationCreate(BaseModel):
    """
    AlgorithmAlgorithmInfomationCreate
    """ # noqa: E501
    algorithm_name: StrictStr
    algorithm_description: StrictStr
    need_external: List[ExtInfoExtInfoId]
    algorithm_scales: List[Union[StrictFloat, StrictInt]]
    algorithm_data_ids: List[StrictStr]
    __properties: ClassVar[List[str]] = ["algorithm_name", "algorithm_description", "need_external", "algorithm_scales", "algorithm_data_ids"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AlgorithmAlgorithmInfomationCreate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AlgorithmAlgorithmInfomationCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "algorithm_name": obj.get("algorithm_name"),
            "algorithm_description": obj.get("algorithm_description"),
            "need_external": obj.get("need_external"),
            "algorithm_scales": obj.get("algorithm_scales"),
            "algorithm_data_ids": obj.get("algorithm_data_ids")
        })
        return _obj



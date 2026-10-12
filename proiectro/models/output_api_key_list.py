from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.output_api_key import OutputApiKey


T = TypeVar("T", bound="OutputApiKeyList")


@_attrs_define
class OutputApiKeyList:
    """List of API keys with current time

    Attributes:
        api_keys (list[OutputApiKey]):
        now (datetime.datetime):
    """

    api_keys: list[OutputApiKey]
    now: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_keys = []
        for api_keys_item_data in self.api_keys:
            api_keys_item = api_keys_item_data.to_dict()
            api_keys.append(api_keys_item)

        now = self.now.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "api_keys": api_keys,
                "now": now,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_api_key import OutputApiKey

        d = dict(src_dict)
        api_keys = []
        _api_keys = d.pop("api_keys")
        for api_keys_item_data in _api_keys:
            api_keys_item = OutputApiKey.from_dict(api_keys_item_data)

            api_keys.append(api_keys_item)

        now = isoparse(d.pop("now"))

        output_api_key_list = cls(
            api_keys=api_keys,
            now=now,
        )

        output_api_key_list.additional_properties = d
        return output_api_key_list

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

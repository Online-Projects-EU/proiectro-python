from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.my_support_request_list_item import MySupportRequestListItem


T = TypeVar("T", bound="OutputMySupportRequests")


@_attrs_define
class OutputMySupportRequests:
    """Output schema for listing user's support requests

    Attributes:
        support_requests (list[MySupportRequestListItem]):
    """

    support_requests: list[MySupportRequestListItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        support_requests = []
        for support_requests_item_data in self.support_requests:
            support_requests_item = support_requests_item_data.to_dict()
            support_requests.append(support_requests_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "support_requests": support_requests,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.my_support_request_list_item import MySupportRequestListItem

        d = dict(src_dict)
        support_requests = []
        _support_requests = d.pop("support_requests")
        for support_requests_item_data in _support_requests:
            support_requests_item = MySupportRequestListItem.from_dict(
                support_requests_item_data
            )

            support_requests.append(support_requests_item)

        output_my_support_requests = cls(
            support_requests=support_requests,
        )

        output_my_support_requests.additional_properties = d
        return output_my_support_requests

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

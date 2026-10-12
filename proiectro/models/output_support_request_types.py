from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_support_request_type import OutputSupportRequestType


T = TypeVar("T", bound="OutputSupportRequestTypes")


@_attrs_define
class OutputSupportRequestTypes:
    """Output schema for listing support request types

    Attributes:
        external_types (list[OutputSupportRequestType]):
        internal_types (list[OutputSupportRequestType]):
        external_count (int):
        internal_count (int):
        total (int):
    """

    external_types: list[OutputSupportRequestType]
    internal_types: list[OutputSupportRequestType]
    external_count: int
    internal_count: int
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_types = []
        for external_types_item_data in self.external_types:
            external_types_item = external_types_item_data.to_dict()
            external_types.append(external_types_item)

        internal_types = []
        for internal_types_item_data in self.internal_types:
            internal_types_item = internal_types_item_data.to_dict()
            internal_types.append(internal_types_item)

        external_count = self.external_count

        internal_count = self.internal_count

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "external_types": external_types,
                "internal_types": internal_types,
                "external_count": external_count,
                "internal_count": internal_count,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_support_request_type import OutputSupportRequestType

        d = dict(src_dict)
        external_types = []
        _external_types = d.pop("external_types")
        for external_types_item_data in _external_types:
            external_types_item = OutputSupportRequestType.from_dict(
                external_types_item_data
            )

            external_types.append(external_types_item)

        internal_types = []
        _internal_types = d.pop("internal_types")
        for internal_types_item_data in _internal_types:
            internal_types_item = OutputSupportRequestType.from_dict(
                internal_types_item_data
            )

            internal_types.append(internal_types_item)

        external_count = d.pop("external_count")

        internal_count = d.pop("internal_count")

        total = d.pop("total")

        output_support_request_types = cls(
            external_types=external_types,
            internal_types=internal_types,
            external_count=external_count,
            internal_count=internal_count,
            total=total,
        )

        output_support_request_types.additional_properties = d
        return output_support_request_types

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

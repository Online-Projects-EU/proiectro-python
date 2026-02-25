from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_support_request_severity import OutputSupportRequestSeverity


T = TypeVar("T", bound="OutputSupportRequestSeverities")


@_attrs_define
class OutputSupportRequestSeverities:
    """Output schema for listing support request severities

    Attributes:
        external_severities (list[OutputSupportRequestSeverity]):
        internal_severities (list[OutputSupportRequestSeverity]):
        external_count (int):
        internal_count (int):
        total (int):
    """

    external_severities: list[OutputSupportRequestSeverity]
    internal_severities: list[OutputSupportRequestSeverity]
    external_count: int
    internal_count: int
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_severities = []
        for external_severities_item_data in self.external_severities:
            external_severities_item = external_severities_item_data.to_dict()
            external_severities.append(external_severities_item)

        internal_severities = []
        for internal_severities_item_data in self.internal_severities:
            internal_severities_item = internal_severities_item_data.to_dict()
            internal_severities.append(internal_severities_item)

        external_count = self.external_count

        internal_count = self.internal_count

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "external_severities": external_severities,
                "internal_severities": internal_severities,
                "external_count": external_count,
                "internal_count": internal_count,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_support_request_severity import (
            OutputSupportRequestSeverity,
        )

        d = dict(src_dict)
        external_severities = []
        _external_severities = d.pop("external_severities")
        for external_severities_item_data in _external_severities:
            external_severities_item = OutputSupportRequestSeverity.from_dict(
                external_severities_item_data
            )

            external_severities.append(external_severities_item)

        internal_severities = []
        _internal_severities = d.pop("internal_severities")
        for internal_severities_item_data in _internal_severities:
            internal_severities_item = OutputSupportRequestSeverity.from_dict(
                internal_severities_item_data
            )

            internal_severities.append(internal_severities_item)

        external_count = d.pop("external_count")

        internal_count = d.pop("internal_count")

        total = d.pop("total")

        output_support_request_severities = cls(
            external_severities=external_severities,
            internal_severities=internal_severities,
            external_count=external_count,
            internal_count=internal_count,
            total=total,
        )

        output_support_request_severities.additional_properties = d
        return output_support_request_severities

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

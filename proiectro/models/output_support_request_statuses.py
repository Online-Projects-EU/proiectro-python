from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_support_request_status import OutputSupportRequestStatus


T = TypeVar("T", bound="OutputSupportRequestStatuses")


@_attrs_define
class OutputSupportRequestStatuses:
    """Output schema for listing support request statuses

    Attributes:
        external_statuses (list[OutputSupportRequestStatus]):
        internal_statuses (list[OutputSupportRequestStatus]):
        external_count (int):
        internal_count (int):
        total (int):
    """

    external_statuses: list[OutputSupportRequestStatus]
    internal_statuses: list[OutputSupportRequestStatus]
    external_count: int
    internal_count: int
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_statuses = []
        for external_statuses_item_data in self.external_statuses:
            external_statuses_item = external_statuses_item_data.to_dict()
            external_statuses.append(external_statuses_item)

        internal_statuses = []
        for internal_statuses_item_data in self.internal_statuses:
            internal_statuses_item = internal_statuses_item_data.to_dict()
            internal_statuses.append(internal_statuses_item)

        external_count = self.external_count

        internal_count = self.internal_count

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "external_statuses": external_statuses,
                "internal_statuses": internal_statuses,
                "external_count": external_count,
                "internal_count": internal_count,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_support_request_status import OutputSupportRequestStatus

        d = dict(src_dict)
        external_statuses = []
        _external_statuses = d.pop("external_statuses")
        for external_statuses_item_data in _external_statuses:
            external_statuses_item = OutputSupportRequestStatus.from_dict(
                external_statuses_item_data
            )

            external_statuses.append(external_statuses_item)

        internal_statuses = []
        _internal_statuses = d.pop("internal_statuses")
        for internal_statuses_item_data in _internal_statuses:
            internal_statuses_item = OutputSupportRequestStatus.from_dict(
                internal_statuses_item_data
            )

            internal_statuses.append(internal_statuses_item)

        external_count = d.pop("external_count")

        internal_count = d.pop("internal_count")

        total = d.pop("total")

        output_support_request_statuses = cls(
            external_statuses=external_statuses,
            internal_statuses=internal_statuses,
            external_count=external_count,
            internal_count=internal_count,
            total=total,
        )

        output_support_request_statuses.additional_properties = d
        return output_support_request_statuses

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

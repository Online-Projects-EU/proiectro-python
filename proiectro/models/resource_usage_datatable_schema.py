from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.resource_usage_record_schema import ResourceUsageRecordSchema


T = TypeVar("T", bound="ResourceUsageDatatableSchema")


@_attrs_define
class ResourceUsageDatatableSchema:
    """Resource usage datatable with all records

    Attributes:
        resource_id (str):
        resource_name (str):
        usage_records (list[ResourceUsageRecordSchema]):
        total_count (int):
        total_usage (int):
    """

    resource_id: str
    resource_name: str
    usage_records: list[ResourceUsageRecordSchema]
    total_count: int
    total_usage: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_id = self.resource_id

        resource_name = self.resource_name

        usage_records = []
        for usage_records_item_data in self.usage_records:
            usage_records_item = usage_records_item_data.to_dict()
            usage_records.append(usage_records_item)

        total_count = self.total_count

        total_usage = self.total_usage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource_id": resource_id,
                "resource_name": resource_name,
                "usage_records": usage_records,
                "total_count": total_count,
                "total_usage": total_usage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_usage_record_schema import ResourceUsageRecordSchema

        d = dict(src_dict)
        resource_id = d.pop("resource_id")

        resource_name = d.pop("resource_name")

        usage_records = []
        _usage_records = d.pop("usage_records")
        for usage_records_item_data in _usage_records:
            usage_records_item = ResourceUsageRecordSchema.from_dict(
                usage_records_item_data
            )

            usage_records.append(usage_records_item)

        total_count = d.pop("total_count")

        total_usage = d.pop("total_usage")

        resource_usage_datatable_schema = cls(
            resource_id=resource_id,
            resource_name=resource_name,
            usage_records=usage_records,
            total_count=total_count,
            total_usage=total_usage,
        )

        resource_usage_datatable_schema.additional_properties = d
        return resource_usage_datatable_schema

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.business_process_summary import BusinessProcessSummary


T = TypeVar("T", bound="BusinessProcessCategory")


@_attrs_define
class BusinessProcessCategory:
    """Category grouping of business processes

    Attributes:
        category_name (str):
        category_key (str):
        processes (list[BusinessProcessSummary]):
    """

    category_name: str
    category_key: str
    processes: list[BusinessProcessSummary]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category_name = self.category_name

        category_key = self.category_key

        processes = []
        for processes_item_data in self.processes:
            processes_item = processes_item_data.to_dict()
            processes.append(processes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category_name": category_name,
                "category_key": category_key,
                "processes": processes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.business_process_summary import BusinessProcessSummary

        d = dict(src_dict)
        category_name = d.pop("category_name")

        category_key = d.pop("category_key")

        processes = []
        _processes = d.pop("processes")
        for processes_item_data in _processes:
            processes_item = BusinessProcessSummary.from_dict(processes_item_data)

            processes.append(processes_item)

        business_process_category = cls(
            category_name=category_name,
            category_key=category_key,
            processes=processes,
        )

        business_process_category.additional_properties = d
        return business_process_category

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

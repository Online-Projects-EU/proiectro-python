from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_saved_filter_item import OutputSavedFilterItem


T = TypeVar("T", bound="OutputSavedFiltersList")


@_attrs_define
class OutputSavedFiltersList:
    """List of saved filters for a specific view

    Attributes:
        filters (list[OutputSavedFilterItem]):
        target_element_id (str | Unset):  Default: ''.
        target_url (str | Unset):  Default: ''.
        delete_filter_base_url (str | Unset):  Default: ''.
    """

    filters: list[OutputSavedFilterItem]
    target_element_id: str | Unset = ""
    target_url: str | Unset = ""
    delete_filter_base_url: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filters = []
        for filters_item_data in self.filters:
            filters_item = filters_item_data.to_dict()
            filters.append(filters_item)

        target_element_id = self.target_element_id

        target_url = self.target_url

        delete_filter_base_url = self.delete_filter_base_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filters": filters,
            }
        )
        if target_element_id is not UNSET:
            field_dict["target_element_id"] = target_element_id
        if target_url is not UNSET:
            field_dict["target_url"] = target_url
        if delete_filter_base_url is not UNSET:
            field_dict["delete_filter_base_url"] = delete_filter_base_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_saved_filter_item import OutputSavedFilterItem

        d = dict(src_dict)
        filters = []
        _filters = d.pop("filters")
        for filters_item_data in _filters:
            filters_item = OutputSavedFilterItem.from_dict(filters_item_data)

            filters.append(filters_item)

        target_element_id = d.pop("target_element_id", UNSET)

        target_url = d.pop("target_url", UNSET)

        delete_filter_base_url = d.pop("delete_filter_base_url", UNSET)

        output_saved_filters_list = cls(
            filters=filters,
            target_element_id=target_element_id,
            target_url=target_url,
            delete_filter_base_url=delete_filter_base_url,
        )

        output_saved_filters_list.additional_properties = d
        return output_saved_filters_list

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

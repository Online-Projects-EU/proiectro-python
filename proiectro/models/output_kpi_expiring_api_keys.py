from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.kpi_expiring_api_keys_summary import KPIExpiringApiKeysSummary
  from ..models.output_kpi_expiring_api_keys_items_item import OutputKPIExpiringApiKeysItemsItem





T = TypeVar("T", bound="OutputKPIExpiringApiKeys")



@_attrs_define
class OutputKPIExpiringApiKeys:
    """ 
        Attributes:
            summary (KPIExpiringApiKeysSummary):
            items (list[OutputKPIExpiringApiKeysItemsItem] | Unset):
     """

    summary: KPIExpiringApiKeysSummary
    items: list[OutputKPIExpiringApiKeysItemsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.output_kpi_expiring_api_keys_items_item import OutputKPIExpiringApiKeysItemsItem
        from ..models.kpi_expiring_api_keys_summary import KPIExpiringApiKeysSummary
        summary = self.summary.to_dict()

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "summary": summary,
        })
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.kpi_expiring_api_keys_summary import KPIExpiringApiKeysSummary
        from ..models.output_kpi_expiring_api_keys_items_item import OutputKPIExpiringApiKeysItemsItem
        d = dict(src_dict)
        summary = KPIExpiringApiKeysSummary.from_dict(d.pop("summary"))




        _items = d.pop("items", UNSET)
        items: list[OutputKPIExpiringApiKeysItemsItem] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = OutputKPIExpiringApiKeysItemsItem.from_dict(items_item_data)



                items.append(items_item)


        output_kpi_expiring_api_keys = cls(
            summary=summary,
            items=items,
        )


        output_kpi_expiring_api_keys.additional_properties = d
        return output_kpi_expiring_api_keys

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

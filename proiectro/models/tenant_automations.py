from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.tenant_automation import TenantAutomation





T = TypeVar("T", bound="TenantAutomations")



@_attrs_define
class TenantAutomations:
    """ Output: list of automation rules.

        Attributes:
            automations (list[TenantAutomation]):
     """

    automations: list[TenantAutomation]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.tenant_automation import TenantAutomation
        automations = []
        for automations_item_data in self.automations:
            automations_item = automations_item_data.to_dict()
            automations.append(automations_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "automations": automations,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tenant_automation import TenantAutomation
        d = dict(src_dict)
        automations = []
        _automations = d.pop("automations")
        for automations_item_data in (_automations):
            automations_item = TenantAutomation.from_dict(automations_item_data)



            automations.append(automations_item)


        tenant_automations = cls(
            automations=automations,
        )


        tenant_automations.additional_properties = d
        return tenant_automations

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

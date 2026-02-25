from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.tenant_funnel import TenantFunnel


T = TypeVar("T", bound="TenantFunnels")


@_attrs_define
class TenantFunnels:
    """
    Attributes:
        funnels (list[TenantFunnel]):
    """

    funnels: list[TenantFunnel]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        funnels = []
        for funnels_item_data in self.funnels:
            funnels_item = funnels_item_data.to_dict()
            funnels.append(funnels_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "funnels": funnels,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tenant_funnel import TenantFunnel

        d = dict(src_dict)
        funnels = []
        _funnels = d.pop("funnels")
        for funnels_item_data in _funnels:
            funnels_item = TenantFunnel.from_dict(funnels_item_data)

            funnels.append(funnels_item)

        tenant_funnels = cls(
            funnels=funnels,
        )

        tenant_funnels.additional_properties = d
        return tenant_funnels

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

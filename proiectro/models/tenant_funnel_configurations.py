from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.tenant_funnel_configuration import TenantFunnelConfiguration


T = TypeVar("T", bound="TenantFunnelConfigurations")


@_attrs_define
class TenantFunnelConfigurations:
    """
    Attributes:
        funnelconfigurations (list[TenantFunnelConfiguration]):
    """

    funnelconfigurations: list[TenantFunnelConfiguration]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        funnelconfigurations = []
        for funnelconfigurations_item_data in self.funnelconfigurations:
            funnelconfigurations_item = funnelconfigurations_item_data.to_dict()
            funnelconfigurations.append(funnelconfigurations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "funnelconfigurations": funnelconfigurations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tenant_funnel_configuration import TenantFunnelConfiguration

        d = dict(src_dict)
        funnelconfigurations = []
        _funnelconfigurations = d.pop("funnelconfigurations")
        for funnelconfigurations_item_data in _funnelconfigurations:
            funnelconfigurations_item = TenantFunnelConfiguration.from_dict(
                funnelconfigurations_item_data
            )

            funnelconfigurations.append(funnelconfigurations_item)

        tenant_funnel_configurations = cls(
            funnelconfigurations=funnelconfigurations,
        )

        tenant_funnel_configurations.additional_properties = d
        return tenant_funnel_configurations

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

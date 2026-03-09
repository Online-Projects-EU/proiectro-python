from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_tenant_locations_locations import (
        OutputTenantLocationsLocations,
    )


T = TypeVar("T", bound="OutputTenantLocations")


@_attrs_define
class OutputTenantLocations:
    """
    Attributes:
        locations (OutputTenantLocationsLocations):
        root_id (None | str | Unset):
    """

    locations: OutputTenantLocationsLocations
    root_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        locations = self.locations.to_dict()

        root_id: None | str | Unset
        if isinstance(self.root_id, Unset):
            root_id = UNSET
        else:
            root_id = self.root_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "locations": locations,
            }
        )
        if root_id is not UNSET:
            field_dict["root_id"] = root_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_tenant_locations_locations import (
            OutputTenantLocationsLocations,
        )

        d = dict(src_dict)
        locations = OutputTenantLocationsLocations.from_dict(d.pop("locations"))

        def _parse_root_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        root_id = _parse_root_id(d.pop("root_id", UNSET))

        output_tenant_locations = cls(
            locations=locations,
            root_id=root_id,
        )

        output_tenant_locations.additional_properties = d
        return output_tenant_locations

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

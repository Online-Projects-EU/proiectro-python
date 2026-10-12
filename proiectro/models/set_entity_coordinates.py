from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetEntityCoordinates")


@_attrs_define
class SetEntityCoordinates:
    """Field GPS capture for a location / customer location / customer asset.

    `accuracy_m` is the device-reported fix accuracy and is mandatory — writes
    above the workspace's `geo_capture_max_accuracy_m` floor are rejected, so a
    500 m fix never gets stored as truth. An existing point is never silently
    overwritten: without `confirm_overwrite` the endpoint answers 409 with the
    stored point so the client can show how far the pin would move.

        Attributes:
            latitude (float):
            longitude (float):
            accuracy_m (int):
            confirm_overwrite (bool | None | Unset):
    """

    latitude: float
    longitude: float
    accuracy_m: int
    confirm_overwrite: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        latitude = self.latitude

        longitude = self.longitude

        accuracy_m = self.accuracy_m

        confirm_overwrite: bool | None | Unset
        if isinstance(self.confirm_overwrite, Unset):
            confirm_overwrite = UNSET
        else:
            confirm_overwrite = self.confirm_overwrite

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "latitude": latitude,
                "longitude": longitude,
                "accuracy_m": accuracy_m,
            }
        )
        if confirm_overwrite is not UNSET:
            field_dict["confirm_overwrite"] = confirm_overwrite

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        latitude = d.pop("latitude")

        longitude = d.pop("longitude")

        accuracy_m = d.pop("accuracy_m")

        def _parse_confirm_overwrite(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        confirm_overwrite = _parse_confirm_overwrite(d.pop("confirm_overwrite", UNSET))

        set_entity_coordinates = cls(
            latitude=latitude,
            longitude=longitude,
            accuracy_m=accuracy_m,
            confirm_overwrite=confirm_overwrite,
        )

        set_entity_coordinates.additional_properties = d
        return set_entity_coordinates

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApproveOperationalItem")


@_attrs_define
class ApproveOperationalItem:
    """
    Attributes:
        target_stage (str):
        notes (str | Unset):  Default: ''.
        geo_latitude (float | None | Unset):
        geo_longitude (float | None | Unset):
        geo_accuracy_m (int | None | Unset):
        geo_overridden (bool | None | Unset):  Default: False.
    """

    target_stage: str
    notes: str | Unset = ""
    geo_latitude: float | None | Unset = UNSET
    geo_longitude: float | None | Unset = UNSET
    geo_accuracy_m: int | None | Unset = UNSET
    geo_overridden: bool | None | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_stage = self.target_stage

        notes = self.notes

        geo_latitude: float | None | Unset
        if isinstance(self.geo_latitude, Unset):
            geo_latitude = UNSET
        else:
            geo_latitude = self.geo_latitude

        geo_longitude: float | None | Unset
        if isinstance(self.geo_longitude, Unset):
            geo_longitude = UNSET
        else:
            geo_longitude = self.geo_longitude

        geo_accuracy_m: int | None | Unset
        if isinstance(self.geo_accuracy_m, Unset):
            geo_accuracy_m = UNSET
        else:
            geo_accuracy_m = self.geo_accuracy_m

        geo_overridden: bool | None | Unset
        if isinstance(self.geo_overridden, Unset):
            geo_overridden = UNSET
        else:
            geo_overridden = self.geo_overridden

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "target_stage": target_stage,
            }
        )
        if notes is not UNSET:
            field_dict["notes"] = notes
        if geo_latitude is not UNSET:
            field_dict["geo_latitude"] = geo_latitude
        if geo_longitude is not UNSET:
            field_dict["geo_longitude"] = geo_longitude
        if geo_accuracy_m is not UNSET:
            field_dict["geo_accuracy_m"] = geo_accuracy_m
        if geo_overridden is not UNSET:
            field_dict["geo_overridden"] = geo_overridden

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target_stage = d.pop("target_stage")

        notes = d.pop("notes", UNSET)

        def _parse_geo_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        geo_latitude = _parse_geo_latitude(d.pop("geo_latitude", UNSET))

        def _parse_geo_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        geo_longitude = _parse_geo_longitude(d.pop("geo_longitude", UNSET))

        def _parse_geo_accuracy_m(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        geo_accuracy_m = _parse_geo_accuracy_m(d.pop("geo_accuracy_m", UNSET))

        def _parse_geo_overridden(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        geo_overridden = _parse_geo_overridden(d.pop("geo_overridden", UNSET))

        approve_operational_item = cls(
            target_stage=target_stage,
            notes=notes,
            geo_latitude=geo_latitude,
            geo_longitude=geo_longitude,
            geo_accuracy_m=geo_accuracy_m,
            geo_overridden=geo_overridden,
        )

        approve_operational_item.additional_properties = d
        return approve_operational_item

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

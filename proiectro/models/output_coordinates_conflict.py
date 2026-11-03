from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputCoordinatesConflict")


@_attrs_define
class OutputCoordinatesConflict:
    """409 body for GPS capture on an entity that already has a pin: the message, plus the
    stored point, so the client can show how far the pin would move before the user confirms
    the overwrite.

        Attributes:
            response_id (str):
            success (bool):
            message (str):
            previous_latitude (float):
            previous_longitude (float):
            distance_m (int):
            url (None | str | Unset):
    """

    response_id: str
    success: bool
    message: str
    previous_latitude: float
    previous_longitude: float
    distance_m: int
    url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        response_id = self.response_id

        success = self.success

        message = self.message

        previous_latitude = self.previous_latitude

        previous_longitude = self.previous_longitude

        distance_m = self.distance_m

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "response_id": response_id,
                "success": success,
                "message": message,
                "previous_latitude": previous_latitude,
                "previous_longitude": previous_longitude,
                "distance_m": distance_m,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        response_id = d.pop("response_id")

        success = d.pop("success")

        message = d.pop("message")

        previous_latitude = d.pop("previous_latitude")

        previous_longitude = d.pop("previous_longitude")

        distance_m = d.pop("distance_m")

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        output_coordinates_conflict = cls(
            response_id=response_id,
            success=success,
            message=message,
            previous_latitude=previous_latitude,
            previous_longitude=previous_longitude,
            distance_m=distance_m,
            url=url,
        )

        output_coordinates_conflict.additional_properties = d
        return output_coordinates_conflict

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

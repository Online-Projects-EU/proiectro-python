from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_target_band import OutputTargetBand


T = TypeVar("T", bound="OutputTargetScheme")


@_attrs_define
class OutputTargetScheme:
    """
    Attributes:
        id (str):
        name (str):
        description (str):
        is_default (bool):
        is_active (bool):
        band_count (int):
        bands (list[OutputTargetBand] | None | Unset):
        target_count (int | Unset):  Default: 0.
        is_ladder_complete (bool | Unset):  Default: False.
    """

    id: str
    name: str
    description: str
    is_default: bool
    is_active: bool
    band_count: int
    bands: list[OutputTargetBand] | None | Unset = UNSET
    target_count: int | Unset = 0
    is_ladder_complete: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        is_default = self.is_default

        is_active = self.is_active

        band_count = self.band_count

        bands: list[dict[str, Any]] | None | Unset
        if isinstance(self.bands, Unset):
            bands = UNSET
        elif isinstance(self.bands, list):
            bands = []
            for bands_type_0_item_data in self.bands:
                bands_type_0_item = bands_type_0_item_data.to_dict()
                bands.append(bands_type_0_item)

        else:
            bands = self.bands

        target_count = self.target_count

        is_ladder_complete = self.is_ladder_complete

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "is_default": is_default,
                "is_active": is_active,
                "band_count": band_count,
            }
        )
        if bands is not UNSET:
            field_dict["bands"] = bands
        if target_count is not UNSET:
            field_dict["target_count"] = target_count
        if is_ladder_complete is not UNSET:
            field_dict["is_ladder_complete"] = is_ladder_complete

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_target_band import OutputTargetBand

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        is_default = d.pop("is_default")

        is_active = d.pop("is_active")

        band_count = d.pop("band_count")

        def _parse_bands(data: object) -> list[OutputTargetBand] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                bands_type_0 = []
                _bands_type_0 = data
                for bands_type_0_item_data in _bands_type_0:
                    bands_type_0_item = OutputTargetBand.from_dict(
                        bands_type_0_item_data
                    )

                    bands_type_0.append(bands_type_0_item)

                return bands_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OutputTargetBand] | None | Unset, data)

        bands = _parse_bands(d.pop("bands", UNSET))

        target_count = d.pop("target_count", UNSET)

        is_ladder_complete = d.pop("is_ladder_complete", UNSET)

        output_target_scheme = cls(
            id=id,
            name=name,
            description=description,
            is_default=is_default,
            is_active=is_active,
            band_count=band_count,
            bands=bands,
            target_count=target_count,
            is_ladder_complete=is_ladder_complete,
        )

        output_target_scheme.additional_properties = d
        return output_target_scheme

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

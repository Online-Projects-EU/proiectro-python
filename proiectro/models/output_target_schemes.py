from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_target_scheme import OutputTargetScheme


T = TypeVar("T", bound="OutputTargetSchemes")


@_attrs_define
class OutputTargetSchemes:
    """
    Attributes:
        target_schemes (list[OutputTargetScheme]):
    """

    target_schemes: list[OutputTargetScheme]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_schemes = []
        for target_schemes_item_data in self.target_schemes:
            target_schemes_item = target_schemes_item_data.to_dict()
            target_schemes.append(target_schemes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "target_schemes": target_schemes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_target_scheme import OutputTargetScheme

        d = dict(src_dict)
        target_schemes = []
        _target_schemes = d.pop("target_schemes")
        for target_schemes_item_data in _target_schemes:
            target_schemes_item = OutputTargetScheme.from_dict(target_schemes_item_data)

            target_schemes.append(target_schemes_item)

        output_target_schemes = cls(
            target_schemes=target_schemes,
        )

        output_target_schemes.additional_properties = d
        return output_target_schemes

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

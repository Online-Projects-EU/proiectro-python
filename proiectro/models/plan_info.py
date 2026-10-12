from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.plan_info_limits import PlanInfoLimits


T = TypeVar("T", bound="PlanInfo")


@_attrs_define
class PlanInfo:
    """User-facing plan summary. No internal slugs or IDs.

    Attributes:
        name (str):
        features (list[str]):
        limits (PlanInfoLimits):
    """

    name: str
    features: list[str]
    limits: PlanInfoLimits
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        features = self.features

        limits = self.limits.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "features": features,
                "limits": limits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plan_info_limits import PlanInfoLimits

        d = dict(src_dict)
        name = d.pop("name")

        features = cast(list[str], d.pop("features"))

        limits = PlanInfoLimits.from_dict(d.pop("limits"))

        plan_info = cls(
            name=name,
            features=features,
            limits=limits,
        )

        plan_info.additional_properties = d
        return plan_info

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

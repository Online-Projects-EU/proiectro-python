from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FeatureAccessSummary")


@_attrs_define
class FeatureAccessSummary:
    """What the caller can reach in one feature, rolled up from their permissions.

    Attributes:
        feature (str):
        admin_access (bool):
        user_access (bool):
        has_all (bool):
        permission_count (int):
    """

    feature: str
    admin_access: bool
    user_access: bool
    has_all: bool
    permission_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        feature = self.feature

        admin_access = self.admin_access

        user_access = self.user_access

        has_all = self.has_all

        permission_count = self.permission_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "feature": feature,
                "admin_access": admin_access,
                "user_access": user_access,
                "has_all": has_all,
                "permission_count": permission_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        feature = d.pop("feature")

        admin_access = d.pop("admin_access")

        user_access = d.pop("user_access")

        has_all = d.pop("has_all")

        permission_count = d.pop("permission_count")

        feature_access_summary = cls(
            feature=feature,
            admin_access=admin_access,
            user_access=user_access,
            has_all=has_all,
            permission_count=permission_count,
        )

        feature_access_summary.additional_properties = d
        return feature_access_summary

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feature_access_summary import FeatureAccessSummary
    from ..models.role_membership import RoleMembership


T = TypeVar("T", bound="MyPermissionsExplain")


@_attrs_define
class MyPermissionsExplain:
    """The caller's own access in one workspace.

    Two permission lists, because they answer different questions.
    `flat_permissions` is the ceiling the caller's roles grant. Wildcards the
    owner policy adds are not in it, and a scope-narrowed credential has not
    been applied to it. `effective_permissions` is what the credential making
    THIS request can actually exercise. When the second is smaller than the
    first, `scope_crud_types` says why.

    Absent fields carry meaning: `scope_crud_types` is omitted under session
    auth, where no narrowing applies, and `is_superuser` is omitted for
    everyone who is not one.

        Attributes:
            is_owner (bool):
            flat_permissions (list[str]):
            effective_permissions (list[str]):
            feature_summary (list[FeatureAccessSummary]):
            role_memberships (list[RoleMembership]):
            is_superuser (bool | None | Unset):
            scope_crud_types (list[str] | None | Unset):
    """

    is_owner: bool
    flat_permissions: list[str]
    effective_permissions: list[str]
    feature_summary: list[FeatureAccessSummary]
    role_memberships: list[RoleMembership]
    is_superuser: bool | None | Unset = UNSET
    scope_crud_types: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_owner = self.is_owner

        flat_permissions = self.flat_permissions

        effective_permissions = self.effective_permissions

        feature_summary = []
        for feature_summary_item_data in self.feature_summary:
            feature_summary_item = feature_summary_item_data.to_dict()
            feature_summary.append(feature_summary_item)

        role_memberships = []
        for role_memberships_item_data in self.role_memberships:
            role_memberships_item = role_memberships_item_data.to_dict()
            role_memberships.append(role_memberships_item)

        is_superuser: bool | None | Unset
        if isinstance(self.is_superuser, Unset):
            is_superuser = UNSET
        else:
            is_superuser = self.is_superuser

        scope_crud_types: list[str] | None | Unset
        if isinstance(self.scope_crud_types, Unset):
            scope_crud_types = UNSET
        elif isinstance(self.scope_crud_types, list):
            scope_crud_types = self.scope_crud_types

        else:
            scope_crud_types = self.scope_crud_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "is_owner": is_owner,
                "flat_permissions": flat_permissions,
                "effective_permissions": effective_permissions,
                "feature_summary": feature_summary,
                "role_memberships": role_memberships,
            }
        )
        if is_superuser is not UNSET:
            field_dict["is_superuser"] = is_superuser
        if scope_crud_types is not UNSET:
            field_dict["scope_crud_types"] = scope_crud_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.feature_access_summary import FeatureAccessSummary
        from ..models.role_membership import RoleMembership

        d = dict(src_dict)
        is_owner = d.pop("is_owner")

        flat_permissions = cast(list[str], d.pop("flat_permissions"))

        effective_permissions = cast(list[str], d.pop("effective_permissions"))

        feature_summary = []
        _feature_summary = d.pop("feature_summary")
        for feature_summary_item_data in _feature_summary:
            feature_summary_item = FeatureAccessSummary.from_dict(
                feature_summary_item_data
            )

            feature_summary.append(feature_summary_item)

        role_memberships = []
        _role_memberships = d.pop("role_memberships")
        for role_memberships_item_data in _role_memberships:
            role_memberships_item = RoleMembership.from_dict(role_memberships_item_data)

            role_memberships.append(role_memberships_item)

        def _parse_is_superuser(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_superuser = _parse_is_superuser(d.pop("is_superuser", UNSET))

        def _parse_scope_crud_types(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                scope_crud_types_type_0 = cast(list[str], data)

                return scope_crud_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        scope_crud_types = _parse_scope_crud_types(d.pop("scope_crud_types", UNSET))

        my_permissions_explain = cls(
            is_owner=is_owner,
            flat_permissions=flat_permissions,
            effective_permissions=effective_permissions,
            feature_summary=feature_summary,
            role_memberships=role_memberships,
            is_superuser=is_superuser,
            scope_crud_types=scope_crud_types,
        )

        my_permissions_explain.additional_properties = d
        return my_permissions_explain

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tenant_org_tags_item import TenantOrgTagsItem


T = TypeVar("T", bound="TenantOrg")


@_attrs_define
class TenantOrg:
    """
    Attributes:
        id (str):
        name (str):
        first_letter (str):
        manager_name (None | str | Unset):
        manager_avatar_url (None | str | Unset):
        managed_by_me (bool | Unset):  Default: False.
        tags (list[TenantOrgTagsItem] | Unset):
    """

    id: str
    name: str
    first_letter: str
    manager_name: None | str | Unset = UNSET
    manager_avatar_url: None | str | Unset = UNSET
    managed_by_me: bool | Unset = False
    tags: list[TenantOrgTagsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        first_letter = self.first_letter

        manager_name: None | str | Unset
        if isinstance(self.manager_name, Unset):
            manager_name = UNSET
        else:
            manager_name = self.manager_name

        manager_avatar_url: None | str | Unset
        if isinstance(self.manager_avatar_url, Unset):
            manager_avatar_url = UNSET
        else:
            manager_avatar_url = self.manager_avatar_url

        managed_by_me = self.managed_by_me

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "first_letter": first_letter,
            }
        )
        if manager_name is not UNSET:
            field_dict["manager_name"] = manager_name
        if manager_avatar_url is not UNSET:
            field_dict["manager_avatar_url"] = manager_avatar_url
        if managed_by_me is not UNSET:
            field_dict["managed_by_me"] = managed_by_me
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tenant_org_tags_item import TenantOrgTagsItem

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        first_letter = d.pop("first_letter")

        def _parse_manager_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        manager_name = _parse_manager_name(d.pop("manager_name", UNSET))

        def _parse_manager_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        manager_avatar_url = _parse_manager_avatar_url(
            d.pop("manager_avatar_url", UNSET)
        )

        managed_by_me = d.pop("managed_by_me", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: list[TenantOrgTagsItem] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = TenantOrgTagsItem.from_dict(tags_item_data)

                tags.append(tags_item)

        tenant_org = cls(
            id=id,
            name=name,
            first_letter=first_letter,
            manager_name=manager_name,
            manager_avatar_url=manager_avatar_url,
            managed_by_me=managed_by_me,
            tags=tags,
        )

        tenant_org.additional_properties = d
        return tenant_org

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MyWorkItem")


@_attrs_define
class MyWorkItem:
    """Individual work item for cross-tenant My Work view

    Attributes:
        id (str):
        name (str):
        percent_complete (int):
        tenant_name (str):
        tenant_path (str):
        urgency_group (str):
        planned_end (None | str | Unset):
        project_name (None | str | Unset):
        project_id (None | str | Unset):
        item_type_name (None | str | Unset):
    """

    id: str
    name: str
    percent_complete: int
    tenant_name: str
    tenant_path: str
    urgency_group: str
    planned_end: None | str | Unset = UNSET
    project_name: None | str | Unset = UNSET
    project_id: None | str | Unset = UNSET
    item_type_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        percent_complete = self.percent_complete

        tenant_name = self.tenant_name

        tenant_path = self.tenant_path

        urgency_group = self.urgency_group

        planned_end: None | str | Unset
        if isinstance(self.planned_end, Unset):
            planned_end = UNSET
        else:
            planned_end = self.planned_end

        project_name: None | str | Unset
        if isinstance(self.project_name, Unset):
            project_name = UNSET
        else:
            project_name = self.project_name

        project_id: None | str | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        item_type_name: None | str | Unset
        if isinstance(self.item_type_name, Unset):
            item_type_name = UNSET
        else:
            item_type_name = self.item_type_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "percent_complete": percent_complete,
                "tenant_name": tenant_name,
                "tenant_path": tenant_path,
                "urgency_group": urgency_group,
            }
        )
        if planned_end is not UNSET:
            field_dict["planned_end"] = planned_end
        if project_name is not UNSET:
            field_dict["project_name"] = project_name
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if item_type_name is not UNSET:
            field_dict["item_type_name"] = item_type_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        percent_complete = d.pop("percent_complete")

        tenant_name = d.pop("tenant_name")

        tenant_path = d.pop("tenant_path")

        urgency_group = d.pop("urgency_group")

        def _parse_planned_end(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        planned_end = _parse_planned_end(d.pop("planned_end", UNSET))

        def _parse_project_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_name = _parse_project_name(d.pop("project_name", UNSET))

        def _parse_project_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))

        def _parse_item_type_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        item_type_name = _parse_item_type_name(d.pop("item_type_name", UNSET))

        my_work_item = cls(
            id=id,
            name=name,
            percent_complete=percent_complete,
            tenant_name=tenant_name,
            tenant_path=tenant_path,
            urgency_group=urgency_group,
            planned_end=planned_end,
            project_name=project_name,
            project_id=project_id,
            item_type_name=item_type_name,
        )

        my_work_item.additional_properties = d
        return my_work_item

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

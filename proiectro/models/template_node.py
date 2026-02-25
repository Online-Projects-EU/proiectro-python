from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.template_node_add_children_item import TemplateNodeAddChildrenItem
    from ..models.template_node_children import TemplateNodeChildren


T = TypeVar("T", bound="TemplateNode")


@_attrs_define
class TemplateNode:
    """Single template in the hierarchy

    Attributes:
        external_id (str):
        name (str):
        description (str):
        hierarchy_id (str):
        item_type_id (str):
        item_type_name (str):
        scheduling_behaviour (str):
        is_active (bool):
        estimated_work_hours (float | None | str | Unset):
        estimated_duration_days (int | None | Unset):
        children (TemplateNodeChildren | Unset):
        add_children (list[TemplateNodeAddChildrenItem] | Unset):
    """

    external_id: str
    name: str
    description: str
    hierarchy_id: str
    item_type_id: str
    item_type_name: str
    scheduling_behaviour: str
    is_active: bool
    estimated_work_hours: float | None | str | Unset = UNSET
    estimated_duration_days: int | None | Unset = UNSET
    children: TemplateNodeChildren | Unset = UNSET
    add_children: list[TemplateNodeAddChildrenItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_id = self.external_id

        name = self.name

        description = self.description

        hierarchy_id = self.hierarchy_id

        item_type_id = self.item_type_id

        item_type_name = self.item_type_name

        scheduling_behaviour = self.scheduling_behaviour

        is_active = self.is_active

        estimated_work_hours: float | None | str | Unset
        if isinstance(self.estimated_work_hours, Unset):
            estimated_work_hours = UNSET
        else:
            estimated_work_hours = self.estimated_work_hours

        estimated_duration_days: int | None | Unset
        if isinstance(self.estimated_duration_days, Unset):
            estimated_duration_days = UNSET
        else:
            estimated_duration_days = self.estimated_duration_days

        children: dict[str, Any] | Unset = UNSET
        if not isinstance(self.children, Unset):
            children = self.children.to_dict()

        add_children: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.add_children, Unset):
            add_children = []
            for add_children_item_data in self.add_children:
                add_children_item = add_children_item_data.to_dict()
                add_children.append(add_children_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "external_id": external_id,
                "name": name,
                "description": description,
                "hierarchy_id": hierarchy_id,
                "item_type_id": item_type_id,
                "item_type_name": item_type_name,
                "scheduling_behaviour": scheduling_behaviour,
                "is_active": is_active,
            }
        )
        if estimated_work_hours is not UNSET:
            field_dict["estimated_work_hours"] = estimated_work_hours
        if estimated_duration_days is not UNSET:
            field_dict["estimated_duration_days"] = estimated_duration_days
        if children is not UNSET:
            field_dict["children"] = children
        if add_children is not UNSET:
            field_dict["add_children"] = add_children

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template_node_add_children_item import TemplateNodeAddChildrenItem
        from ..models.template_node_children import TemplateNodeChildren

        d = dict(src_dict)
        external_id = d.pop("external_id")

        name = d.pop("name")

        description = d.pop("description")

        hierarchy_id = d.pop("hierarchy_id")

        item_type_id = d.pop("item_type_id")

        item_type_name = d.pop("item_type_name")

        scheduling_behaviour = d.pop("scheduling_behaviour")

        is_active = d.pop("is_active")

        def _parse_estimated_work_hours(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        estimated_work_hours = _parse_estimated_work_hours(
            d.pop("estimated_work_hours", UNSET)
        )

        def _parse_estimated_duration_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        estimated_duration_days = _parse_estimated_duration_days(
            d.pop("estimated_duration_days", UNSET)
        )

        _children = d.pop("children", UNSET)
        children: TemplateNodeChildren | Unset
        if isinstance(_children, Unset):
            children = UNSET
        else:
            children = TemplateNodeChildren.from_dict(_children)

        _add_children = d.pop("add_children", UNSET)
        add_children: list[TemplateNodeAddChildrenItem] | Unset = UNSET
        if _add_children is not UNSET:
            add_children = []
            for add_children_item_data in _add_children:
                add_children_item = TemplateNodeAddChildrenItem.from_dict(
                    add_children_item_data
                )

                add_children.append(add_children_item)

        template_node = cls(
            external_id=external_id,
            name=name,
            description=description,
            hierarchy_id=hierarchy_id,
            item_type_id=item_type_id,
            item_type_name=item_type_name,
            scheduling_behaviour=scheduling_behaviour,
            is_active=is_active,
            estimated_work_hours=estimated_work_hours,
            estimated_duration_days=estimated_duration_days,
            children=children,
            add_children=add_children,
        )

        template_node.additional_properties = d
        return template_node

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

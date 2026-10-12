from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.allowed_child_type import AllowedChildType
    from ..models.work_item_node_children import WorkItemNodeChildren


T = TypeVar("T", bound="WorkItemNode")


@_attrs_define
class WorkItemNode:
    """Single work item in the hierarchy

    Attributes:
        external_id (str):
        name (str):
        hierarchy_id (str):
        item_type_id (str):
        item_type_name (str):
        scheduling_behaviour (str):
        is_finished (bool):
        is_accepted (bool):
        estimated_work_hours (float | None | str | Unset):
        owner_id (None | str | Unset):
        owner_name (None | str | Unset):
        planned_start (None | str | Unset):
        planned_end (None | str | Unset):
        children (WorkItemNodeChildren | Unset):
        add_children (list[AllowedChildType] | Unset):
    """

    external_id: str
    name: str
    hierarchy_id: str
    item_type_id: str
    item_type_name: str
    scheduling_behaviour: str
    is_finished: bool
    is_accepted: bool
    estimated_work_hours: float | None | str | Unset = UNSET
    owner_id: None | str | Unset = UNSET
    owner_name: None | str | Unset = UNSET
    planned_start: None | str | Unset = UNSET
    planned_end: None | str | Unset = UNSET
    children: WorkItemNodeChildren | Unset = UNSET
    add_children: list[AllowedChildType] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_id = self.external_id

        name = self.name

        hierarchy_id = self.hierarchy_id

        item_type_id = self.item_type_id

        item_type_name = self.item_type_name

        scheduling_behaviour = self.scheduling_behaviour

        is_finished = self.is_finished

        is_accepted = self.is_accepted

        estimated_work_hours: float | None | str | Unset
        if isinstance(self.estimated_work_hours, Unset):
            estimated_work_hours = UNSET
        else:
            estimated_work_hours = self.estimated_work_hours

        owner_id: None | str | Unset
        if isinstance(self.owner_id, Unset):
            owner_id = UNSET
        else:
            owner_id = self.owner_id

        owner_name: None | str | Unset
        if isinstance(self.owner_name, Unset):
            owner_name = UNSET
        else:
            owner_name = self.owner_name

        planned_start: None | str | Unset
        if isinstance(self.planned_start, Unset):
            planned_start = UNSET
        else:
            planned_start = self.planned_start

        planned_end: None | str | Unset
        if isinstance(self.planned_end, Unset):
            planned_end = UNSET
        else:
            planned_end = self.planned_end

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
                "hierarchy_id": hierarchy_id,
                "item_type_id": item_type_id,
                "item_type_name": item_type_name,
                "scheduling_behaviour": scheduling_behaviour,
                "is_finished": is_finished,
                "is_accepted": is_accepted,
            }
        )
        if estimated_work_hours is not UNSET:
            field_dict["estimated_work_hours"] = estimated_work_hours
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if owner_name is not UNSET:
            field_dict["owner_name"] = owner_name
        if planned_start is not UNSET:
            field_dict["planned_start"] = planned_start
        if planned_end is not UNSET:
            field_dict["planned_end"] = planned_end
        if children is not UNSET:
            field_dict["children"] = children
        if add_children is not UNSET:
            field_dict["add_children"] = add_children

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.allowed_child_type import AllowedChildType
        from ..models.work_item_node_children import WorkItemNodeChildren

        d = dict(src_dict)
        external_id = d.pop("external_id")

        name = d.pop("name")

        hierarchy_id = d.pop("hierarchy_id")

        item_type_id = d.pop("item_type_id")

        item_type_name = d.pop("item_type_name")

        scheduling_behaviour = d.pop("scheduling_behaviour")

        is_finished = d.pop("is_finished")

        is_accepted = d.pop("is_accepted")

        def _parse_estimated_work_hours(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        estimated_work_hours = _parse_estimated_work_hours(
            d.pop("estimated_work_hours", UNSET)
        )

        def _parse_owner_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_id = _parse_owner_id(d.pop("owner_id", UNSET))

        def _parse_owner_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_name = _parse_owner_name(d.pop("owner_name", UNSET))

        def _parse_planned_start(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        planned_start = _parse_planned_start(d.pop("planned_start", UNSET))

        def _parse_planned_end(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        planned_end = _parse_planned_end(d.pop("planned_end", UNSET))

        _children = d.pop("children", UNSET)
        children: WorkItemNodeChildren | Unset
        if isinstance(_children, Unset):
            children = UNSET
        else:
            children = WorkItemNodeChildren.from_dict(_children)

        _add_children = d.pop("add_children", UNSET)
        add_children: list[AllowedChildType] | Unset = UNSET
        if _add_children is not UNSET:
            add_children = []
            for add_children_item_data in _add_children:
                add_children_item = AllowedChildType.from_dict(add_children_item_data)

                add_children.append(add_children_item)

        work_item_node = cls(
            external_id=external_id,
            name=name,
            hierarchy_id=hierarchy_id,
            item_type_id=item_type_id,
            item_type_name=item_type_name,
            scheduling_behaviour=scheduling_behaviour,
            is_finished=is_finished,
            is_accepted=is_accepted,
            estimated_work_hours=estimated_work_hours,
            owner_id=owner_id,
            owner_name=owner_name,
            planned_start=planned_start,
            planned_end=planned_end,
            children=children,
            add_children=add_children,
        )

        work_item_node.additional_properties = d
        return work_item_node

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

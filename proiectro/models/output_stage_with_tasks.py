from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_operational_item import OutputOperationalItem


T = TypeVar("T", bound="OutputStageWithTasks")


@_attrs_define
class OutputStageWithTasks:
    """
    Attributes:
        id (str):
        name (str):
        stage_type (str):
        sequence_no (int):
        requires_approval (bool):
        items (list[OutputOperationalItem]):
        is_active (bool | Unset):  Default: True.
        item_count (int | Unset):  Default: 0.
        link_process_name (str | Unset):  Default: ''.
        link_stage_name (str | Unset):  Default: ''.
        link_process_active (bool | Unset):  Default: False.
        link_stage_active (bool | Unset):  Default: False.
    """

    id: str
    name: str
    stage_type: str
    sequence_no: int
    requires_approval: bool
    items: list[OutputOperationalItem]
    is_active: bool | Unset = True
    item_count: int | Unset = 0
    link_process_name: str | Unset = ""
    link_stage_name: str | Unset = ""
    link_process_active: bool | Unset = False
    link_stage_active: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        stage_type = self.stage_type

        sequence_no = self.sequence_no

        requires_approval = self.requires_approval

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        is_active = self.is_active

        item_count = self.item_count

        link_process_name = self.link_process_name

        link_stage_name = self.link_stage_name

        link_process_active = self.link_process_active

        link_stage_active = self.link_stage_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "stage_type": stage_type,
                "sequence_no": sequence_no,
                "requires_approval": requires_approval,
                "items": items,
            }
        )
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if item_count is not UNSET:
            field_dict["item_count"] = item_count
        if link_process_name is not UNSET:
            field_dict["link_process_name"] = link_process_name
        if link_stage_name is not UNSET:
            field_dict["link_stage_name"] = link_stage_name
        if link_process_active is not UNSET:
            field_dict["link_process_active"] = link_process_active
        if link_stage_active is not UNSET:
            field_dict["link_stage_active"] = link_stage_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_operational_item import OutputOperationalItem

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        stage_type = d.pop("stage_type")

        sequence_no = d.pop("sequence_no")

        requires_approval = d.pop("requires_approval")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = OutputOperationalItem.from_dict(items_item_data)

            items.append(items_item)

        is_active = d.pop("is_active", UNSET)

        item_count = d.pop("item_count", UNSET)

        link_process_name = d.pop("link_process_name", UNSET)

        link_stage_name = d.pop("link_stage_name", UNSET)

        link_process_active = d.pop("link_process_active", UNSET)

        link_stage_active = d.pop("link_stage_active", UNSET)

        output_stage_with_tasks = cls(
            id=id,
            name=name,
            stage_type=stage_type,
            sequence_no=sequence_no,
            requires_approval=requires_approval,
            items=items,
            is_active=is_active,
            item_count=item_count,
            link_process_name=link_process_name,
            link_stage_name=link_stage_name,
            link_process_active=link_process_active,
            link_stage_active=link_stage_active,
        )

        output_stage_with_tasks.additional_properties = d
        return output_stage_with_tasks

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

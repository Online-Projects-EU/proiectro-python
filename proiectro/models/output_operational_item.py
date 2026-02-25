from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_operational_item_transition import (
        OutputOperationalItemTransition,
    )


T = TypeVar("T", bound="OutputOperationalItem")


@_attrs_define
class OutputOperationalItem:
    """
    Attributes:
        id (str):
        name (str):
        description (str):
        process_id (str):
        process_name (str):
        current_stage_id (str):
        current_stage_name (str):
        current_stage_type (str):
        requires_approval (bool):
        created_by_id (str):
        created_by_name (str):
        priority (str):
        is_finished (bool):
        created_at (str):
        updated_at (str):
        owner_id (None | str | Unset):
        owner_name (None | str | Unset):
        customer_id (None | str | Unset):
        customer_name (None | str | Unset):
        customer_visible (bool | Unset):  Default: True.
        due_date (None | str | Unset):
        created_display (str | Unset):  Default: ''.
        updated_display (str | Unset):  Default: ''.
        stage_age_hours (int | Unset):  Default: 0.
        stage_instructions (str | Unset):  Default: ''.
        transitions (list[OutputOperationalItemTransition] | Unset):
    """

    id: str
    name: str
    description: str
    process_id: str
    process_name: str
    current_stage_id: str
    current_stage_name: str
    current_stage_type: str
    requires_approval: bool
    created_by_id: str
    created_by_name: str
    priority: str
    is_finished: bool
    created_at: str
    updated_at: str
    owner_id: None | str | Unset = UNSET
    owner_name: None | str | Unset = UNSET
    customer_id: None | str | Unset = UNSET
    customer_name: None | str | Unset = UNSET
    customer_visible: bool | Unset = True
    due_date: None | str | Unset = UNSET
    created_display: str | Unset = ""
    updated_display: str | Unset = ""
    stage_age_hours: int | Unset = 0
    stage_instructions: str | Unset = ""
    transitions: list[OutputOperationalItemTransition] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        process_id = self.process_id

        process_name = self.process_name

        current_stage_id = self.current_stage_id

        current_stage_name = self.current_stage_name

        current_stage_type = self.current_stage_type

        requires_approval = self.requires_approval

        created_by_id = self.created_by_id

        created_by_name = self.created_by_name

        priority = self.priority

        is_finished = self.is_finished

        created_at = self.created_at

        updated_at = self.updated_at

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

        customer_id: None | str | Unset
        if isinstance(self.customer_id, Unset):
            customer_id = UNSET
        else:
            customer_id = self.customer_id

        customer_name: None | str | Unset
        if isinstance(self.customer_name, Unset):
            customer_name = UNSET
        else:
            customer_name = self.customer_name

        customer_visible = self.customer_visible

        due_date: None | str | Unset
        if isinstance(self.due_date, Unset):
            due_date = UNSET
        else:
            due_date = self.due_date

        created_display = self.created_display

        updated_display = self.updated_display

        stage_age_hours = self.stage_age_hours

        stage_instructions = self.stage_instructions

        transitions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.transitions, Unset):
            transitions = []
            for transitions_item_data in self.transitions:
                transitions_item = transitions_item_data.to_dict()
                transitions.append(transitions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "process_id": process_id,
                "process_name": process_name,
                "current_stage_id": current_stage_id,
                "current_stage_name": current_stage_name,
                "current_stage_type": current_stage_type,
                "requires_approval": requires_approval,
                "created_by_id": created_by_id,
                "created_by_name": created_by_name,
                "priority": priority,
                "is_finished": is_finished,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if owner_name is not UNSET:
            field_dict["owner_name"] = owner_name
        if customer_id is not UNSET:
            field_dict["customer_id"] = customer_id
        if customer_name is not UNSET:
            field_dict["customer_name"] = customer_name
        if customer_visible is not UNSET:
            field_dict["customer_visible"] = customer_visible
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if created_display is not UNSET:
            field_dict["created_display"] = created_display
        if updated_display is not UNSET:
            field_dict["updated_display"] = updated_display
        if stage_age_hours is not UNSET:
            field_dict["stage_age_hours"] = stage_age_hours
        if stage_instructions is not UNSET:
            field_dict["stage_instructions"] = stage_instructions
        if transitions is not UNSET:
            field_dict["transitions"] = transitions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_operational_item_transition import (
            OutputOperationalItemTransition,
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        process_id = d.pop("process_id")

        process_name = d.pop("process_name")

        current_stage_id = d.pop("current_stage_id")

        current_stage_name = d.pop("current_stage_name")

        current_stage_type = d.pop("current_stage_type")

        requires_approval = d.pop("requires_approval")

        created_by_id = d.pop("created_by_id")

        created_by_name = d.pop("created_by_name")

        priority = d.pop("priority")

        is_finished = d.pop("is_finished")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

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

        def _parse_customer_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_id = _parse_customer_id(d.pop("customer_id", UNSET))

        def _parse_customer_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_name = _parse_customer_name(d.pop("customer_name", UNSET))

        customer_visible = d.pop("customer_visible", UNSET)

        def _parse_due_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        due_date = _parse_due_date(d.pop("due_date", UNSET))

        created_display = d.pop("created_display", UNSET)

        updated_display = d.pop("updated_display", UNSET)

        stage_age_hours = d.pop("stage_age_hours", UNSET)

        stage_instructions = d.pop("stage_instructions", UNSET)

        _transitions = d.pop("transitions", UNSET)
        transitions: list[OutputOperationalItemTransition] | Unset = UNSET
        if _transitions is not UNSET:
            transitions = []
            for transitions_item_data in _transitions:
                transitions_item = OutputOperationalItemTransition.from_dict(
                    transitions_item_data
                )

                transitions.append(transitions_item)

        output_operational_item = cls(
            id=id,
            name=name,
            description=description,
            process_id=process_id,
            process_name=process_name,
            current_stage_id=current_stage_id,
            current_stage_name=current_stage_name,
            current_stage_type=current_stage_type,
            requires_approval=requires_approval,
            created_by_id=created_by_id,
            created_by_name=created_by_name,
            priority=priority,
            is_finished=is_finished,
            created_at=created_at,
            updated_at=updated_at,
            owner_id=owner_id,
            owner_name=owner_name,
            customer_id=customer_id,
            customer_name=customer_name,
            customer_visible=customer_visible,
            due_date=due_date,
            created_display=created_display,
            updated_display=updated_display,
            stage_age_hours=stage_age_hours,
            stage_instructions=stage_instructions,
            transitions=transitions,
        )

        output_operational_item.additional_properties = d
        return output_operational_item

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

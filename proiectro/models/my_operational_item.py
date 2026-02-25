from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MyOperationalItem")


@_attrs_define
class MyOperationalItem:
    """Individual operational item for cross-tenant welcome page

    Attributes:
        id (str):
        name (str):
        process_name (str):
        current_stage_name (str):
        current_stage_type (str):
        priority (str):
        is_finished (bool):
        tenant_name (str):
        tenant_path (str):
        created_at (str):
        due_date (None | str | Unset):
        owner_name (None | str | Unset):
        customer_name (None | str | Unset):
        requires_approval (bool | Unset):  Default: False.
    """

    id: str
    name: str
    process_name: str
    current_stage_name: str
    current_stage_type: str
    priority: str
    is_finished: bool
    tenant_name: str
    tenant_path: str
    created_at: str
    due_date: None | str | Unset = UNSET
    owner_name: None | str | Unset = UNSET
    customer_name: None | str | Unset = UNSET
    requires_approval: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        process_name = self.process_name

        current_stage_name = self.current_stage_name

        current_stage_type = self.current_stage_type

        priority = self.priority

        is_finished = self.is_finished

        tenant_name = self.tenant_name

        tenant_path = self.tenant_path

        created_at = self.created_at

        due_date: None | str | Unset
        if isinstance(self.due_date, Unset):
            due_date = UNSET
        else:
            due_date = self.due_date

        owner_name: None | str | Unset
        if isinstance(self.owner_name, Unset):
            owner_name = UNSET
        else:
            owner_name = self.owner_name

        customer_name: None | str | Unset
        if isinstance(self.customer_name, Unset):
            customer_name = UNSET
        else:
            customer_name = self.customer_name

        requires_approval = self.requires_approval

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "process_name": process_name,
                "current_stage_name": current_stage_name,
                "current_stage_type": current_stage_type,
                "priority": priority,
                "is_finished": is_finished,
                "tenant_name": tenant_name,
                "tenant_path": tenant_path,
                "created_at": created_at,
            }
        )
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if owner_name is not UNSET:
            field_dict["owner_name"] = owner_name
        if customer_name is not UNSET:
            field_dict["customer_name"] = customer_name
        if requires_approval is not UNSET:
            field_dict["requires_approval"] = requires_approval

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        process_name = d.pop("process_name")

        current_stage_name = d.pop("current_stage_name")

        current_stage_type = d.pop("current_stage_type")

        priority = d.pop("priority")

        is_finished = d.pop("is_finished")

        tenant_name = d.pop("tenant_name")

        tenant_path = d.pop("tenant_path")

        created_at = d.pop("created_at")

        def _parse_due_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        due_date = _parse_due_date(d.pop("due_date", UNSET))

        def _parse_owner_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_name = _parse_owner_name(d.pop("owner_name", UNSET))

        def _parse_customer_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_name = _parse_customer_name(d.pop("customer_name", UNSET))

        requires_approval = d.pop("requires_approval", UNSET)

        my_operational_item = cls(
            id=id,
            name=name,
            process_name=process_name,
            current_stage_name=current_stage_name,
            current_stage_type=current_stage_type,
            priority=priority,
            is_finished=is_finished,
            tenant_name=tenant_name,
            tenant_path=tenant_path,
            created_at=created_at,
            due_date=due_date,
            owner_name=owner_name,
            customer_name=customer_name,
            requires_approval=requires_approval,
        )

        my_operational_item.additional_properties = d
        return my_operational_item

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddWorkItem")


@_attrs_define
class AddWorkItem:
    """
    Attributes:
        name (str):
        project_id (str):
        work_item_type_id (str):
        description (None | str | Unset):  Default: ''.
        estimated_work_hours (int | None | Unset):
        planned_start_date (None | str | Unset):
        planned_finish_date (None | str | Unset):
        estimated_duration_days (int | None | Unset):
        constraint_type (None | str | Unset):
        constraint_date (None | str | Unset):
        owner (None | str | Unset):
        visible_to_customer (bool | Unset):  Default: False.
        product (None | str | Unset):
        parent_work_item_id (None | str | Unset):
    """

    name: str
    project_id: str
    work_item_type_id: str
    description: None | str | Unset = ""
    estimated_work_hours: int | None | Unset = UNSET
    planned_start_date: None | str | Unset = UNSET
    planned_finish_date: None | str | Unset = UNSET
    estimated_duration_days: int | None | Unset = UNSET
    constraint_type: None | str | Unset = UNSET
    constraint_date: None | str | Unset = UNSET
    owner: None | str | Unset = UNSET
    visible_to_customer: bool | Unset = False
    product: None | str | Unset = UNSET
    parent_work_item_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        project_id = self.project_id

        work_item_type_id = self.work_item_type_id

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        estimated_work_hours: int | None | Unset
        if isinstance(self.estimated_work_hours, Unset):
            estimated_work_hours = UNSET
        else:
            estimated_work_hours = self.estimated_work_hours

        planned_start_date: None | str | Unset
        if isinstance(self.planned_start_date, Unset):
            planned_start_date = UNSET
        else:
            planned_start_date = self.planned_start_date

        planned_finish_date: None | str | Unset
        if isinstance(self.planned_finish_date, Unset):
            planned_finish_date = UNSET
        else:
            planned_finish_date = self.planned_finish_date

        estimated_duration_days: int | None | Unset
        if isinstance(self.estimated_duration_days, Unset):
            estimated_duration_days = UNSET
        else:
            estimated_duration_days = self.estimated_duration_days

        constraint_type: None | str | Unset
        if isinstance(self.constraint_type, Unset):
            constraint_type = UNSET
        else:
            constraint_type = self.constraint_type

        constraint_date: None | str | Unset
        if isinstance(self.constraint_date, Unset):
            constraint_date = UNSET
        else:
            constraint_date = self.constraint_date

        owner: None | str | Unset
        if isinstance(self.owner, Unset):
            owner = UNSET
        else:
            owner = self.owner

        visible_to_customer = self.visible_to_customer

        product: None | str | Unset
        if isinstance(self.product, Unset):
            product = UNSET
        else:
            product = self.product

        parent_work_item_id: None | str | Unset
        if isinstance(self.parent_work_item_id, Unset):
            parent_work_item_id = UNSET
        else:
            parent_work_item_id = self.parent_work_item_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "project_id": project_id,
                "work_item_type_id": work_item_type_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if estimated_work_hours is not UNSET:
            field_dict["estimated_work_hours"] = estimated_work_hours
        if planned_start_date is not UNSET:
            field_dict["planned_start_date"] = planned_start_date
        if planned_finish_date is not UNSET:
            field_dict["planned_finish_date"] = planned_finish_date
        if estimated_duration_days is not UNSET:
            field_dict["estimated_duration_days"] = estimated_duration_days
        if constraint_type is not UNSET:
            field_dict["constraint_type"] = constraint_type
        if constraint_date is not UNSET:
            field_dict["constraint_date"] = constraint_date
        if owner is not UNSET:
            field_dict["owner"] = owner
        if visible_to_customer is not UNSET:
            field_dict["visible_to_customer"] = visible_to_customer
        if product is not UNSET:
            field_dict["product"] = product
        if parent_work_item_id is not UNSET:
            field_dict["parent_work_item_id"] = parent_work_item_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        project_id = d.pop("project_id")

        work_item_type_id = d.pop("work_item_type_id")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_estimated_work_hours(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        estimated_work_hours = _parse_estimated_work_hours(
            d.pop("estimated_work_hours", UNSET)
        )

        def _parse_planned_start_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        planned_start_date = _parse_planned_start_date(
            d.pop("planned_start_date", UNSET)
        )

        def _parse_planned_finish_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        planned_finish_date = _parse_planned_finish_date(
            d.pop("planned_finish_date", UNSET)
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

        def _parse_constraint_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        constraint_type = _parse_constraint_type(d.pop("constraint_type", UNSET))

        def _parse_constraint_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        constraint_date = _parse_constraint_date(d.pop("constraint_date", UNSET))

        def _parse_owner(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner = _parse_owner(d.pop("owner", UNSET))

        visible_to_customer = d.pop("visible_to_customer", UNSET)

        def _parse_product(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product = _parse_product(d.pop("product", UNSET))

        def _parse_parent_work_item_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_work_item_id = _parse_parent_work_item_id(
            d.pop("parent_work_item_id", UNSET)
        )

        add_work_item = cls(
            name=name,
            project_id=project_id,
            work_item_type_id=work_item_type_id,
            description=description,
            estimated_work_hours=estimated_work_hours,
            planned_start_date=planned_start_date,
            planned_finish_date=planned_finish_date,
            estimated_duration_days=estimated_duration_days,
            constraint_type=constraint_type,
            constraint_date=constraint_date,
            owner=owner,
            visible_to_customer=visible_to_customer,
            product=product,
            parent_work_item_id=parent_work_item_id,
        )

        add_work_item.additional_properties = d
        return add_work_item

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

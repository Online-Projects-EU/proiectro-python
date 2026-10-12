from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProductWorkItem")


@_attrs_define
class ProductWorkItem:
    """Individual work item linked to a product

    Attributes:
        external_id (str):
        name (str):
        hierarchy_id (str):
        item_type_name (str):
        scheduling_behaviour (str):
        is_finished (bool):
        is_accepted (bool):
        project_id (str):
        project_name (str):
        estimated_work_hours (int | None | Unset):
    """

    external_id: str
    name: str
    hierarchy_id: str
    item_type_name: str
    scheduling_behaviour: str
    is_finished: bool
    is_accepted: bool
    project_id: str
    project_name: str
    estimated_work_hours: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_id = self.external_id

        name = self.name

        hierarchy_id = self.hierarchy_id

        item_type_name = self.item_type_name

        scheduling_behaviour = self.scheduling_behaviour

        is_finished = self.is_finished

        is_accepted = self.is_accepted

        project_id = self.project_id

        project_name = self.project_name

        estimated_work_hours: int | None | Unset
        if isinstance(self.estimated_work_hours, Unset):
            estimated_work_hours = UNSET
        else:
            estimated_work_hours = self.estimated_work_hours

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "external_id": external_id,
                "name": name,
                "hierarchy_id": hierarchy_id,
                "item_type_name": item_type_name,
                "scheduling_behaviour": scheduling_behaviour,
                "is_finished": is_finished,
                "is_accepted": is_accepted,
                "project_id": project_id,
                "project_name": project_name,
            }
        )
        if estimated_work_hours is not UNSET:
            field_dict["estimated_work_hours"] = estimated_work_hours

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        external_id = d.pop("external_id")

        name = d.pop("name")

        hierarchy_id = d.pop("hierarchy_id")

        item_type_name = d.pop("item_type_name")

        scheduling_behaviour = d.pop("scheduling_behaviour")

        is_finished = d.pop("is_finished")

        is_accepted = d.pop("is_accepted")

        project_id = d.pop("project_id")

        project_name = d.pop("project_name")

        def _parse_estimated_work_hours(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        estimated_work_hours = _parse_estimated_work_hours(
            d.pop("estimated_work_hours", UNSET)
        )

        product_work_item = cls(
            external_id=external_id,
            name=name,
            hierarchy_id=hierarchy_id,
            item_type_name=item_type_name,
            scheduling_behaviour=scheduling_behaviour,
            is_finished=is_finished,
            is_accepted=is_accepted,
            project_id=project_id,
            project_name=project_name,
            estimated_work_hours=estimated_work_hours,
        )

        product_work_item.additional_properties = d
        return product_work_item

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_project_work_items_work_items import (
        OutputProjectWorkItemsWorkItems,
    )
    from ..models.top_level_work_item_type import TopLevelWorkItemType


T = TypeVar("T", bound="OutputProjectWorkItems")


@_attrs_define
class OutputProjectWorkItems:
    """Complete work items hierarchy with configuration info

    Attributes:
        project_id (str):
        project_name (str):
        has_wbs_configuration (bool):
        wbs_configuration_id (None | str | Unset):
        wbs_configuration_name (None | str | Unset):
        root_work_item_id (None | str | Unset):
        parent_work_item_id (None | str | Unset):
        parent_work_item_name (None | str | Unset):
        parent_work_item_type (None | str | Unset):
        top_level_types (list[TopLevelWorkItemType] | Unset):
        work_items (OutputProjectWorkItemsWorkItems | Unset):
        total_items (int | Unset):  Default: 0.
    """

    project_id: str
    project_name: str
    has_wbs_configuration: bool
    wbs_configuration_id: None | str | Unset = UNSET
    wbs_configuration_name: None | str | Unset = UNSET
    root_work_item_id: None | str | Unset = UNSET
    parent_work_item_id: None | str | Unset = UNSET
    parent_work_item_name: None | str | Unset = UNSET
    parent_work_item_type: None | str | Unset = UNSET
    top_level_types: list[TopLevelWorkItemType] | Unset = UNSET
    work_items: OutputProjectWorkItemsWorkItems | Unset = UNSET
    total_items: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        project_name = self.project_name

        has_wbs_configuration = self.has_wbs_configuration

        wbs_configuration_id: None | str | Unset
        if isinstance(self.wbs_configuration_id, Unset):
            wbs_configuration_id = UNSET
        else:
            wbs_configuration_id = self.wbs_configuration_id

        wbs_configuration_name: None | str | Unset
        if isinstance(self.wbs_configuration_name, Unset):
            wbs_configuration_name = UNSET
        else:
            wbs_configuration_name = self.wbs_configuration_name

        root_work_item_id: None | str | Unset
        if isinstance(self.root_work_item_id, Unset):
            root_work_item_id = UNSET
        else:
            root_work_item_id = self.root_work_item_id

        parent_work_item_id: None | str | Unset
        if isinstance(self.parent_work_item_id, Unset):
            parent_work_item_id = UNSET
        else:
            parent_work_item_id = self.parent_work_item_id

        parent_work_item_name: None | str | Unset
        if isinstance(self.parent_work_item_name, Unset):
            parent_work_item_name = UNSET
        else:
            parent_work_item_name = self.parent_work_item_name

        parent_work_item_type: None | str | Unset
        if isinstance(self.parent_work_item_type, Unset):
            parent_work_item_type = UNSET
        else:
            parent_work_item_type = self.parent_work_item_type

        top_level_types: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_level_types, Unset):
            top_level_types = []
            for top_level_types_item_data in self.top_level_types:
                top_level_types_item = top_level_types_item_data.to_dict()
                top_level_types.append(top_level_types_item)

        work_items: dict[str, Any] | Unset = UNSET
        if not isinstance(self.work_items, Unset):
            work_items = self.work_items.to_dict()

        total_items = self.total_items

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_id": project_id,
                "project_name": project_name,
                "has_wbs_configuration": has_wbs_configuration,
            }
        )
        if wbs_configuration_id is not UNSET:
            field_dict["wbs_configuration_id"] = wbs_configuration_id
        if wbs_configuration_name is not UNSET:
            field_dict["wbs_configuration_name"] = wbs_configuration_name
        if root_work_item_id is not UNSET:
            field_dict["root_work_item_id"] = root_work_item_id
        if parent_work_item_id is not UNSET:
            field_dict["parent_work_item_id"] = parent_work_item_id
        if parent_work_item_name is not UNSET:
            field_dict["parent_work_item_name"] = parent_work_item_name
        if parent_work_item_type is not UNSET:
            field_dict["parent_work_item_type"] = parent_work_item_type
        if top_level_types is not UNSET:
            field_dict["top_level_types"] = top_level_types
        if work_items is not UNSET:
            field_dict["work_items"] = work_items
        if total_items is not UNSET:
            field_dict["total_items"] = total_items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_project_work_items_work_items import (
            OutputProjectWorkItemsWorkItems,
        )
        from ..models.top_level_work_item_type import TopLevelWorkItemType

        d = dict(src_dict)
        project_id = d.pop("project_id")

        project_name = d.pop("project_name")

        has_wbs_configuration = d.pop("has_wbs_configuration")

        def _parse_wbs_configuration_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wbs_configuration_id = _parse_wbs_configuration_id(
            d.pop("wbs_configuration_id", UNSET)
        )

        def _parse_wbs_configuration_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wbs_configuration_name = _parse_wbs_configuration_name(
            d.pop("wbs_configuration_name", UNSET)
        )

        def _parse_root_work_item_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        root_work_item_id = _parse_root_work_item_id(d.pop("root_work_item_id", UNSET))

        def _parse_parent_work_item_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_work_item_id = _parse_parent_work_item_id(
            d.pop("parent_work_item_id", UNSET)
        )

        def _parse_parent_work_item_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_work_item_name = _parse_parent_work_item_name(
            d.pop("parent_work_item_name", UNSET)
        )

        def _parse_parent_work_item_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_work_item_type = _parse_parent_work_item_type(
            d.pop("parent_work_item_type", UNSET)
        )

        _top_level_types = d.pop("top_level_types", UNSET)
        top_level_types: list[TopLevelWorkItemType] | Unset = UNSET
        if _top_level_types is not UNSET:
            top_level_types = []
            for top_level_types_item_data in _top_level_types:
                top_level_types_item = TopLevelWorkItemType.from_dict(
                    top_level_types_item_data
                )

                top_level_types.append(top_level_types_item)

        _work_items = d.pop("work_items", UNSET)
        work_items: OutputProjectWorkItemsWorkItems | Unset
        if isinstance(_work_items, Unset):
            work_items = UNSET
        else:
            work_items = OutputProjectWorkItemsWorkItems.from_dict(_work_items)

        total_items = d.pop("total_items", UNSET)

        output_project_work_items = cls(
            project_id=project_id,
            project_name=project_name,
            has_wbs_configuration=has_wbs_configuration,
            wbs_configuration_id=wbs_configuration_id,
            wbs_configuration_name=wbs_configuration_name,
            root_work_item_id=root_work_item_id,
            parent_work_item_id=parent_work_item_id,
            parent_work_item_name=parent_work_item_name,
            parent_work_item_type=parent_work_item_type,
            top_level_types=top_level_types,
            work_items=work_items,
            total_items=total_items,
        )

        output_project_work_items.additional_properties = d
        return output_project_work_items

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

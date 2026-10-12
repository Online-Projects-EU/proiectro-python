from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_template_hierarchy_allowed_child_types_item import (
        OutputTemplateHierarchyAllowedChildTypesItem,
    )
    from ..models.output_template_hierarchy_templates import (
        OutputTemplateHierarchyTemplates,
    )


T = TypeVar("T", bound="OutputTemplateHierarchy")


@_attrs_define
class OutputTemplateHierarchy:
    """Complete template hierarchy with configuration info

    Attributes:
        template_id (str):
        template_name (str):
        has_wbs_configuration (bool):
        wbs_configuration_id (None | str | Unset):
        wbs_configuration_name (None | str | Unset):
        allowed_child_types (list[OutputTemplateHierarchyAllowedChildTypesItem] | Unset):
        templates (OutputTemplateHierarchyTemplates | Unset):
        total_items (int | Unset):  Default: 0.
    """

    template_id: str
    template_name: str
    has_wbs_configuration: bool
    wbs_configuration_id: None | str | Unset = UNSET
    wbs_configuration_name: None | str | Unset = UNSET
    allowed_child_types: list[OutputTemplateHierarchyAllowedChildTypesItem] | Unset = (
        UNSET
    )
    templates: OutputTemplateHierarchyTemplates | Unset = UNSET
    total_items: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        template_id = self.template_id

        template_name = self.template_name

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

        allowed_child_types: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.allowed_child_types, Unset):
            allowed_child_types = []
            for allowed_child_types_item_data in self.allowed_child_types:
                allowed_child_types_item = allowed_child_types_item_data.to_dict()
                allowed_child_types.append(allowed_child_types_item)

        templates: dict[str, Any] | Unset = UNSET
        if not isinstance(self.templates, Unset):
            templates = self.templates.to_dict()

        total_items = self.total_items

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "template_id": template_id,
                "template_name": template_name,
                "has_wbs_configuration": has_wbs_configuration,
            }
        )
        if wbs_configuration_id is not UNSET:
            field_dict["wbs_configuration_id"] = wbs_configuration_id
        if wbs_configuration_name is not UNSET:
            field_dict["wbs_configuration_name"] = wbs_configuration_name
        if allowed_child_types is not UNSET:
            field_dict["allowed_child_types"] = allowed_child_types
        if templates is not UNSET:
            field_dict["templates"] = templates
        if total_items is not UNSET:
            field_dict["total_items"] = total_items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_template_hierarchy_allowed_child_types_item import (
            OutputTemplateHierarchyAllowedChildTypesItem,
        )
        from ..models.output_template_hierarchy_templates import (
            OutputTemplateHierarchyTemplates,
        )

        d = dict(src_dict)
        template_id = d.pop("template_id")

        template_name = d.pop("template_name")

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

        _allowed_child_types = d.pop("allowed_child_types", UNSET)
        allowed_child_types: (
            list[OutputTemplateHierarchyAllowedChildTypesItem] | Unset
        ) = UNSET
        if _allowed_child_types is not UNSET:
            allowed_child_types = []
            for allowed_child_types_item_data in _allowed_child_types:
                allowed_child_types_item = (
                    OutputTemplateHierarchyAllowedChildTypesItem.from_dict(
                        allowed_child_types_item_data
                    )
                )

                allowed_child_types.append(allowed_child_types_item)

        _templates = d.pop("templates", UNSET)
        templates: OutputTemplateHierarchyTemplates | Unset
        if isinstance(_templates, Unset):
            templates = UNSET
        else:
            templates = OutputTemplateHierarchyTemplates.from_dict(_templates)

        total_items = d.pop("total_items", UNSET)

        output_template_hierarchy = cls(
            template_id=template_id,
            template_name=template_name,
            has_wbs_configuration=has_wbs_configuration,
            wbs_configuration_id=wbs_configuration_id,
            wbs_configuration_name=wbs_configuration_name,
            allowed_child_types=allowed_child_types,
            templates=templates,
            total_items=total_items,
        )

        output_template_hierarchy.additional_properties = d
        return output_template_hierarchy

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

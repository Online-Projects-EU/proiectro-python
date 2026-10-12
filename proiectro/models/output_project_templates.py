from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_project_templates_general_templates_item import (
        OutputProjectTemplatesGeneralTemplatesItem,
    )
    from ..models.output_project_templates_wbs_templates_item import (
        OutputProjectTemplatesWbsTemplatesItem,
    )


T = TypeVar("T", bound="OutputProjectTemplates")


@_attrs_define
class OutputProjectTemplates:
    """Work item templates available for a project, grouped by WBS configuration

    Attributes:
        wbs_templates (list[OutputProjectTemplatesWbsTemplatesItem]):
        general_templates (list[OutputProjectTemplatesGeneralTemplatesItem]):
        project_id (str):
        wbs_config_name (None | str | Unset):
    """

    wbs_templates: list[OutputProjectTemplatesWbsTemplatesItem]
    general_templates: list[OutputProjectTemplatesGeneralTemplatesItem]
    project_id: str
    wbs_config_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wbs_templates = []
        for wbs_templates_item_data in self.wbs_templates:
            wbs_templates_item = wbs_templates_item_data.to_dict()
            wbs_templates.append(wbs_templates_item)

        general_templates = []
        for general_templates_item_data in self.general_templates:
            general_templates_item = general_templates_item_data.to_dict()
            general_templates.append(general_templates_item)

        project_id = self.project_id

        wbs_config_name: None | str | Unset
        if isinstance(self.wbs_config_name, Unset):
            wbs_config_name = UNSET
        else:
            wbs_config_name = self.wbs_config_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "wbs_templates": wbs_templates,
                "general_templates": general_templates,
                "project_id": project_id,
            }
        )
        if wbs_config_name is not UNSET:
            field_dict["wbs_config_name"] = wbs_config_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_project_templates_general_templates_item import (
            OutputProjectTemplatesGeneralTemplatesItem,
        )
        from ..models.output_project_templates_wbs_templates_item import (
            OutputProjectTemplatesWbsTemplatesItem,
        )

        d = dict(src_dict)
        wbs_templates = []
        _wbs_templates = d.pop("wbs_templates")
        for wbs_templates_item_data in _wbs_templates:
            wbs_templates_item = OutputProjectTemplatesWbsTemplatesItem.from_dict(
                wbs_templates_item_data
            )

            wbs_templates.append(wbs_templates_item)

        general_templates = []
        _general_templates = d.pop("general_templates")
        for general_templates_item_data in _general_templates:
            general_templates_item = (
                OutputProjectTemplatesGeneralTemplatesItem.from_dict(
                    general_templates_item_data
                )
            )

            general_templates.append(general_templates_item)

        project_id = d.pop("project_id")

        def _parse_wbs_config_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wbs_config_name = _parse_wbs_config_name(d.pop("wbs_config_name", UNSET))

        output_project_templates = cls(
            wbs_templates=wbs_templates,
            general_templates=general_templates,
            project_id=project_id,
            wbs_config_name=wbs_config_name,
        )

        output_project_templates.additional_properties = d
        return output_project_templates

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

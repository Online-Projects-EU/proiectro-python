from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.quick_start_conflict import QuickStartConflict
    from ..models.quick_start_preview_entity_group import QuickStartPreviewEntityGroup
    from ..models.quick_start_preview_template_info import QuickStartPreviewTemplateInfo


T = TypeVar("T", bound="OutputQuickStartPreview")


@_attrs_define
class OutputQuickStartPreview:
    """Preview of what a template will create.

    Attributes:
        entity_groups (list[QuickStartPreviewEntityGroup]):
        total_entities (int):
        conflicts (list[QuickStartConflict]):
        has_conflicts (bool):
        template (None | QuickStartPreviewTemplateInfo | Unset):
        error (None | str | Unset):
    """

    entity_groups: list[QuickStartPreviewEntityGroup]
    total_entities: int
    conflicts: list[QuickStartConflict]
    has_conflicts: bool
    template: None | QuickStartPreviewTemplateInfo | Unset = UNSET
    error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.quick_start_preview_template_info import (
            QuickStartPreviewTemplateInfo,
        )

        entity_groups = []
        for entity_groups_item_data in self.entity_groups:
            entity_groups_item = entity_groups_item_data.to_dict()
            entity_groups.append(entity_groups_item)

        total_entities = self.total_entities

        conflicts = []
        for conflicts_item_data in self.conflicts:
            conflicts_item = conflicts_item_data.to_dict()
            conflicts.append(conflicts_item)

        has_conflicts = self.has_conflicts

        template: dict[str, Any] | None | Unset
        if isinstance(self.template, Unset):
            template = UNSET
        elif isinstance(self.template, QuickStartPreviewTemplateInfo):
            template = self.template.to_dict()
        else:
            template = self.template

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entity_groups": entity_groups,
                "total_entities": total_entities,
                "conflicts": conflicts,
                "has_conflicts": has_conflicts,
            }
        )
        if template is not UNSET:
            field_dict["template"] = template
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.quick_start_conflict import QuickStartConflict
        from ..models.quick_start_preview_entity_group import (
            QuickStartPreviewEntityGroup,
        )
        from ..models.quick_start_preview_template_info import (
            QuickStartPreviewTemplateInfo,
        )

        d = dict(src_dict)
        entity_groups = []
        _entity_groups = d.pop("entity_groups")
        for entity_groups_item_data in _entity_groups:
            entity_groups_item = QuickStartPreviewEntityGroup.from_dict(
                entity_groups_item_data
            )

            entity_groups.append(entity_groups_item)

        total_entities = d.pop("total_entities")

        conflicts = []
        _conflicts = d.pop("conflicts")
        for conflicts_item_data in _conflicts:
            conflicts_item = QuickStartConflict.from_dict(conflicts_item_data)

            conflicts.append(conflicts_item)

        has_conflicts = d.pop("has_conflicts")

        def _parse_template(
            data: object,
        ) -> None | QuickStartPreviewTemplateInfo | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                template_type_0 = QuickStartPreviewTemplateInfo.from_dict(data)

                return template_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | QuickStartPreviewTemplateInfo | Unset, data)

        template = _parse_template(d.pop("template", UNSET))

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        output_quick_start_preview = cls(
            entity_groups=entity_groups,
            total_entities=total_entities,
            conflicts=conflicts,
            has_conflicts=has_conflicts,
            template=template,
            error=error,
        )

        output_quick_start_preview.additional_properties = d
        return output_quick_start_preview

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

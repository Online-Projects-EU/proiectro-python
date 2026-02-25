from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.instantiate_work_item_template_milestone_dates_type_0 import (
        InstantiateWorkItemTemplateMilestoneDatesType0,
    )


T = TypeVar("T", bound="InstantiateWorkItemTemplate")


@_attrs_define
class InstantiateWorkItemTemplate:
    """Schema for instantiating a work item template into a project.

    Attributes:
        project_id (str):
        template_id (str):
        parent_work_item_id (str):
        default_owner_id (None | str | Unset):
        product_id (None | str | Unset):
        milestone_dates (InstantiateWorkItemTemplateMilestoneDatesType0 | None | Unset):
        bypass_wbs_rules (bool | Unset):  Default: False.
    """

    project_id: str
    template_id: str
    parent_work_item_id: str
    default_owner_id: None | str | Unset = UNSET
    product_id: None | str | Unset = UNSET
    milestone_dates: InstantiateWorkItemTemplateMilestoneDatesType0 | None | Unset = (
        UNSET
    )
    bypass_wbs_rules: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.instantiate_work_item_template_milestone_dates_type_0 import (
            InstantiateWorkItemTemplateMilestoneDatesType0,
        )

        project_id = self.project_id

        template_id = self.template_id

        parent_work_item_id = self.parent_work_item_id

        default_owner_id: None | str | Unset
        if isinstance(self.default_owner_id, Unset):
            default_owner_id = UNSET
        else:
            default_owner_id = self.default_owner_id

        product_id: None | str | Unset
        if isinstance(self.product_id, Unset):
            product_id = UNSET
        else:
            product_id = self.product_id

        milestone_dates: dict[str, Any] | None | Unset
        if isinstance(self.milestone_dates, Unset):
            milestone_dates = UNSET
        elif isinstance(
            self.milestone_dates, InstantiateWorkItemTemplateMilestoneDatesType0
        ):
            milestone_dates = self.milestone_dates.to_dict()
        else:
            milestone_dates = self.milestone_dates

        bypass_wbs_rules = self.bypass_wbs_rules

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_id": project_id,
                "template_id": template_id,
                "parent_work_item_id": parent_work_item_id,
            }
        )
        if default_owner_id is not UNSET:
            field_dict["default_owner_id"] = default_owner_id
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if milestone_dates is not UNSET:
            field_dict["milestone_dates"] = milestone_dates
        if bypass_wbs_rules is not UNSET:
            field_dict["bypass_wbs_rules"] = bypass_wbs_rules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.instantiate_work_item_template_milestone_dates_type_0 import (
            InstantiateWorkItemTemplateMilestoneDatesType0,
        )

        d = dict(src_dict)
        project_id = d.pop("project_id")

        template_id = d.pop("template_id")

        parent_work_item_id = d.pop("parent_work_item_id")

        def _parse_default_owner_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_owner_id = _parse_default_owner_id(d.pop("default_owner_id", UNSET))

        def _parse_product_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_id = _parse_product_id(d.pop("product_id", UNSET))

        def _parse_milestone_dates(
            data: object,
        ) -> InstantiateWorkItemTemplateMilestoneDatesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                milestone_dates_type_0 = (
                    InstantiateWorkItemTemplateMilestoneDatesType0.from_dict(data)
                )

                return milestone_dates_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                InstantiateWorkItemTemplateMilestoneDatesType0 | None | Unset, data
            )

        milestone_dates = _parse_milestone_dates(d.pop("milestone_dates", UNSET))

        bypass_wbs_rules = d.pop("bypass_wbs_rules", UNSET)

        instantiate_work_item_template = cls(
            project_id=project_id,
            template_id=template_id,
            parent_work_item_id=parent_work_item_id,
            default_owner_id=default_owner_id,
            product_id=product_id,
            milestone_dates=milestone_dates,
            bypass_wbs_rules=bypass_wbs_rules,
        )

        instantiate_work_item_template.additional_properties = d
        return instantiate_work_item_template

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

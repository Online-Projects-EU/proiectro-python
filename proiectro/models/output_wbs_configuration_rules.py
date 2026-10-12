from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_wbs_configuration_rule import OutputWBSConfigurationRule


T = TypeVar("T", bound="OutputWBSConfigurationRules")


@_attrs_define
class OutputWBSConfigurationRules:
    """
    Attributes:
        wbs_configuration (str):
        rules (list[OutputWBSConfigurationRule]):
        has_root_rule (bool):
    """

    wbs_configuration: str
    rules: list[OutputWBSConfigurationRule]
    has_root_rule: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wbs_configuration = self.wbs_configuration

        rules = []
        for rules_item_data in self.rules:
            rules_item = rules_item_data.to_dict()
            rules.append(rules_item)

        has_root_rule = self.has_root_rule

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "wbs_configuration": wbs_configuration,
                "rules": rules,
                "has_root_rule": has_root_rule,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_wbs_configuration_rule import OutputWBSConfigurationRule

        d = dict(src_dict)
        wbs_configuration = d.pop("wbs_configuration")

        rules = []
        _rules = d.pop("rules")
        for rules_item_data in _rules:
            rules_item = OutputWBSConfigurationRule.from_dict(rules_item_data)

            rules.append(rules_item)

        has_root_rule = d.pop("has_root_rule")

        output_wbs_configuration_rules = cls(
            wbs_configuration=wbs_configuration,
            rules=rules,
            has_root_rule=has_root_rule,
        )

        output_wbs_configuration_rules.additional_properties = d
        return output_wbs_configuration_rules

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

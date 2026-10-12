from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_asset_form import OutputAssetForm


T = TypeVar("T", bound="OutputAssetForms")


@_attrs_define
class OutputAssetForms:
    """
    Attributes:
        asset_id (str):
        forms (list[OutputAssetForm]):
    """

    asset_id: str
    forms: list[OutputAssetForm]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        forms = []
        for forms_item_data in self.forms:
            forms_item = forms_item_data.to_dict()
            forms.append(forms_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset_id": asset_id,
                "forms": forms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_asset_form import OutputAssetForm

        d = dict(src_dict)
        asset_id = d.pop("asset_id")

        forms = []
        _forms = d.pop("forms")
        for forms_item_data in _forms:
            forms_item = OutputAssetForm.from_dict(forms_item_data)

            forms.append(forms_item)

        output_asset_forms = cls(
            asset_id=asset_id,
            forms=forms,
        )

        output_asset_forms.additional_properties = d
        return output_asset_forms

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

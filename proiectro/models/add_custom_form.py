from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.add_custom_form_data_classification import AddCustomFormDataClassification
from ..types import UNSET, Unset

T = TypeVar("T", bound="AddCustomForm")


@_attrs_define
class AddCustomForm:
    """
    Attributes:
        name (str):
        description (None | str | Unset):  Default: ''.
        slug (None | str | Unset):
        submit_button_text (None | str | Unset):  Default: 'Submit'.
        success_message (None | str | Unset):  Default: ''.
        is_active (bool | Unset):  Default: True.
        data_classification (AddCustomFormDataClassification | Unset):  Default:
            AddCustomFormDataClassification.INTERNAL.
        retention_days (int | None | Unset):
        notify_on_submit (list[str] | None | Unset):
    """

    name: str
    description: None | str | Unset = ""
    slug: None | str | Unset = UNSET
    submit_button_text: None | str | Unset = "Submit"
    success_message: None | str | Unset = ""
    is_active: bool | Unset = True
    data_classification: AddCustomFormDataClassification | Unset = (
        AddCustomFormDataClassification.INTERNAL
    )
    retention_days: int | None | Unset = UNSET
    notify_on_submit: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        slug: None | str | Unset
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        submit_button_text: None | str | Unset
        if isinstance(self.submit_button_text, Unset):
            submit_button_text = UNSET
        else:
            submit_button_text = self.submit_button_text

        success_message: None | str | Unset
        if isinstance(self.success_message, Unset):
            success_message = UNSET
        else:
            success_message = self.success_message

        is_active = self.is_active

        data_classification: str | Unset = UNSET
        if not isinstance(self.data_classification, Unset):
            data_classification = self.data_classification.value

        retention_days: int | None | Unset
        if isinstance(self.retention_days, Unset):
            retention_days = UNSET
        else:
            retention_days = self.retention_days

        notify_on_submit: list[str] | None | Unset
        if isinstance(self.notify_on_submit, Unset):
            notify_on_submit = UNSET
        elif isinstance(self.notify_on_submit, list):
            notify_on_submit = self.notify_on_submit

        else:
            notify_on_submit = self.notify_on_submit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if slug is not UNSET:
            field_dict["slug"] = slug
        if submit_button_text is not UNSET:
            field_dict["submit_button_text"] = submit_button_text
        if success_message is not UNSET:
            field_dict["success_message"] = success_message
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if data_classification is not UNSET:
            field_dict["data_classification"] = data_classification
        if retention_days is not UNSET:
            field_dict["retention_days"] = retention_days
        if notify_on_submit is not UNSET:
            field_dict["notify_on_submit"] = notify_on_submit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slug = _parse_slug(d.pop("slug", UNSET))

        def _parse_submit_button_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        submit_button_text = _parse_submit_button_text(
            d.pop("submit_button_text", UNSET)
        )

        def _parse_success_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        success_message = _parse_success_message(d.pop("success_message", UNSET))

        is_active = d.pop("is_active", UNSET)

        _data_classification = d.pop("data_classification", UNSET)
        data_classification: AddCustomFormDataClassification | Unset
        if isinstance(_data_classification, Unset):
            data_classification = UNSET
        else:
            data_classification = AddCustomFormDataClassification(_data_classification)

        def _parse_retention_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        retention_days = _parse_retention_days(d.pop("retention_days", UNSET))

        def _parse_notify_on_submit(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                notify_on_submit_type_0 = cast(list[str], data)

                return notify_on_submit_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        notify_on_submit = _parse_notify_on_submit(d.pop("notify_on_submit", UNSET))

        add_custom_form = cls(
            name=name,
            description=description,
            slug=slug,
            submit_button_text=submit_button_text,
            success_message=success_message,
            is_active=is_active,
            data_classification=data_classification,
            retention_days=retention_days,
            notify_on_submit=notify_on_submit,
        )

        add_custom_form.additional_properties = d
        return add_custom_form

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

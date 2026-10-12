from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_language_option import OutputLanguageOption


T = TypeVar("T", bound="OutputMyProfile")


@_attrs_define
class OutputMyProfile:
    """The account-level profile the mobile app reads: one language preference
    shared with the web (User.language drives both surfaces).

        Attributes:
            email (str):
            full_name (str):
            language (str):
            timezone (str):
            languages (list[OutputLanguageOption]):
    """

    email: str
    full_name: str
    language: str
    timezone: str
    languages: list[OutputLanguageOption]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        full_name = self.full_name

        language = self.language

        timezone = self.timezone

        languages = []
        for languages_item_data in self.languages:
            languages_item = languages_item_data.to_dict()
            languages.append(languages_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "full_name": full_name,
                "language": language,
                "timezone": timezone,
                "languages": languages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_language_option import OutputLanguageOption

        d = dict(src_dict)
        email = d.pop("email")

        full_name = d.pop("full_name")

        language = d.pop("language")

        timezone = d.pop("timezone")

        languages = []
        _languages = d.pop("languages")
        for languages_item_data in _languages:
            languages_item = OutputLanguageOption.from_dict(languages_item_data)

            languages.append(languages_item)

        output_my_profile = cls(
            email=email,
            full_name=full_name,
            language=language,
            timezone=timezone,
            languages=languages,
        )

        output_my_profile.additional_properties = d
        return output_my_profile

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

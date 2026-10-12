from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_document_series import OutputDocumentSeries


T = TypeVar("T", bound="OutputDocumentSeriesList")


@_attrs_define
class OutputDocumentSeriesList:
    """
    Attributes:
        document_series (list[OutputDocumentSeries]):
        total_count (int | Unset):  Default: 0.
    """

    document_series: list[OutputDocumentSeries]
    total_count: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        document_series = []
        for document_series_item_data in self.document_series:
            document_series_item = document_series_item_data.to_dict()
            document_series.append(document_series_item)

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "document_series": document_series,
            }
        )
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_document_series import OutputDocumentSeries

        d = dict(src_dict)
        document_series = []
        _document_series = d.pop("document_series")
        for document_series_item_data in _document_series:
            document_series_item = OutputDocumentSeries.from_dict(
                document_series_item_data
            )

            document_series.append(document_series_item)

        total_count = d.pop("total_count", UNSET)

        output_document_series_list = cls(
            document_series=document_series,
            total_count=total_count,
        )

        output_document_series_list.additional_properties = d
        return output_document_series_list

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

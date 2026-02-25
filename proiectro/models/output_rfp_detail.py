from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_rfp_publication_item import OutputRFPPublicationItem


T = TypeVar("T", bound="OutputRFPDetail")


@_attrs_define
class OutputRFPDetail:
    """Full details of an RFP created by this tenant

    Attributes:
        id (str):
        name (str):
        internal_code (None | str):
        description (str):
        category (str):
        category_display (str):
        currency_code (str):
        budget_min (float | None | str):
        budget_max (float | None | str):
        submission_deadline (str):
        status (str):
        status_display (str):
        is_active (bool):
        created_by_name (str):
        created_at (str):
        published_at (None | str):
        closed_at (None | str):
        cancelled_at (None | str):
        awarded_at (None | str):
        publications (list[OutputRFPPublicationItem]):
        has_shortlisted (bool):
    """

    id: str
    name: str
    internal_code: None | str
    description: str
    category: str
    category_display: str
    currency_code: str
    budget_min: float | None | str
    budget_max: float | None | str
    submission_deadline: str
    status: str
    status_display: str
    is_active: bool
    created_by_name: str
    created_at: str
    published_at: None | str
    closed_at: None | str
    cancelled_at: None | str
    awarded_at: None | str
    publications: list[OutputRFPPublicationItem]
    has_shortlisted: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        internal_code: None | str
        internal_code = self.internal_code

        description = self.description

        category = self.category

        category_display = self.category_display

        currency_code = self.currency_code

        budget_min: float | None | str
        budget_min = self.budget_min

        budget_max: float | None | str
        budget_max = self.budget_max

        submission_deadline = self.submission_deadline

        status = self.status

        status_display = self.status_display

        is_active = self.is_active

        created_by_name = self.created_by_name

        created_at = self.created_at

        published_at: None | str
        published_at = self.published_at

        closed_at: None | str
        closed_at = self.closed_at

        cancelled_at: None | str
        cancelled_at = self.cancelled_at

        awarded_at: None | str
        awarded_at = self.awarded_at

        publications = []
        for publications_item_data in self.publications:
            publications_item = publications_item_data.to_dict()
            publications.append(publications_item)

        has_shortlisted = self.has_shortlisted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "internal_code": internal_code,
                "description": description,
                "category": category,
                "category_display": category_display,
                "currency_code": currency_code,
                "budget_min": budget_min,
                "budget_max": budget_max,
                "submission_deadline": submission_deadline,
                "status": status,
                "status_display": status_display,
                "is_active": is_active,
                "created_by_name": created_by_name,
                "created_at": created_at,
                "published_at": published_at,
                "closed_at": closed_at,
                "cancelled_at": cancelled_at,
                "awarded_at": awarded_at,
                "publications": publications,
                "has_shortlisted": has_shortlisted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_rfp_publication_item import OutputRFPPublicationItem

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_internal_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        internal_code = _parse_internal_code(d.pop("internal_code"))

        description = d.pop("description")

        category = d.pop("category")

        category_display = d.pop("category_display")

        currency_code = d.pop("currency_code")

        def _parse_budget_min(data: object) -> float | None | str:
            if data is None:
                return data
            return cast(float | None | str, data)

        budget_min = _parse_budget_min(d.pop("budget_min"))

        def _parse_budget_max(data: object) -> float | None | str:
            if data is None:
                return data
            return cast(float | None | str, data)

        budget_max = _parse_budget_max(d.pop("budget_max"))

        submission_deadline = d.pop("submission_deadline")

        status = d.pop("status")

        status_display = d.pop("status_display")

        is_active = d.pop("is_active")

        created_by_name = d.pop("created_by_name")

        created_at = d.pop("created_at")

        def _parse_published_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        published_at = _parse_published_at(d.pop("published_at"))

        def _parse_closed_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        closed_at = _parse_closed_at(d.pop("closed_at"))

        def _parse_cancelled_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cancelled_at = _parse_cancelled_at(d.pop("cancelled_at"))

        def _parse_awarded_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        awarded_at = _parse_awarded_at(d.pop("awarded_at"))

        publications = []
        _publications = d.pop("publications")
        for publications_item_data in _publications:
            publications_item = OutputRFPPublicationItem.from_dict(
                publications_item_data
            )

            publications.append(publications_item)

        has_shortlisted = d.pop("has_shortlisted")

        output_rfp_detail = cls(
            id=id,
            name=name,
            internal_code=internal_code,
            description=description,
            category=category,
            category_display=category_display,
            currency_code=currency_code,
            budget_min=budget_min,
            budget_max=budget_max,
            submission_deadline=submission_deadline,
            status=status,
            status_display=status_display,
            is_active=is_active,
            created_by_name=created_by_name,
            created_at=created_at,
            published_at=published_at,
            closed_at=closed_at,
            cancelled_at=cancelled_at,
            awarded_at=awarded_at,
            publications=publications,
            has_shortlisted=has_shortlisted,
        )

        output_rfp_detail.additional_properties = d
        return output_rfp_detail

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

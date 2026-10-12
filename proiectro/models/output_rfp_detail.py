from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

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
        submission_deadline (datetime.date):
        status (str):
        status_display (str):
        is_active (bool):
        created_by_name (str):
        created_at (datetime.datetime):
        publications (list[OutputRFPPublicationItem]):
        has_shortlisted (bool):
        published_at (datetime.datetime | None | Unset):
        closed_at (datetime.datetime | None | Unset):
        cancelled_at (datetime.datetime | None | Unset):
        awarded_at (datetime.datetime | None | Unset):
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
    submission_deadline: datetime.date
    status: str
    status_display: str
    is_active: bool
    created_by_name: str
    created_at: datetime.datetime
    publications: list[OutputRFPPublicationItem]
    has_shortlisted: bool
    published_at: datetime.datetime | None | Unset = UNSET
    closed_at: datetime.datetime | None | Unset = UNSET
    cancelled_at: datetime.datetime | None | Unset = UNSET
    awarded_at: datetime.datetime | None | Unset = UNSET
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

        submission_deadline = self.submission_deadline.isoformat()

        status = self.status

        status_display = self.status_display

        is_active = self.is_active

        created_by_name = self.created_by_name

        created_at = self.created_at.isoformat()

        publications = []
        for publications_item_data in self.publications:
            publications_item = publications_item_data.to_dict()
            publications.append(publications_item)

        has_shortlisted = self.has_shortlisted

        published_at: None | str | Unset
        if isinstance(self.published_at, Unset):
            published_at = UNSET
        elif isinstance(self.published_at, datetime.datetime):
            published_at = self.published_at.isoformat()
        else:
            published_at = self.published_at

        closed_at: None | str | Unset
        if isinstance(self.closed_at, Unset):
            closed_at = UNSET
        elif isinstance(self.closed_at, datetime.datetime):
            closed_at = self.closed_at.isoformat()
        else:
            closed_at = self.closed_at

        cancelled_at: None | str | Unset
        if isinstance(self.cancelled_at, Unset):
            cancelled_at = UNSET
        elif isinstance(self.cancelled_at, datetime.datetime):
            cancelled_at = self.cancelled_at.isoformat()
        else:
            cancelled_at = self.cancelled_at

        awarded_at: None | str | Unset
        if isinstance(self.awarded_at, Unset):
            awarded_at = UNSET
        elif isinstance(self.awarded_at, datetime.datetime):
            awarded_at = self.awarded_at.isoformat()
        else:
            awarded_at = self.awarded_at

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
                "publications": publications,
                "has_shortlisted": has_shortlisted,
            }
        )
        if published_at is not UNSET:
            field_dict["published_at"] = published_at
        if closed_at is not UNSET:
            field_dict["closed_at"] = closed_at
        if cancelled_at is not UNSET:
            field_dict["cancelled_at"] = cancelled_at
        if awarded_at is not UNSET:
            field_dict["awarded_at"] = awarded_at

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

        submission_deadline = isoparse(d.pop("submission_deadline")).date()

        status = d.pop("status")

        status_display = d.pop("status_display")

        is_active = d.pop("is_active")

        created_by_name = d.pop("created_by_name")

        created_at = isoparse(d.pop("created_at"))

        publications = []
        _publications = d.pop("publications")
        for publications_item_data in _publications:
            publications_item = OutputRFPPublicationItem.from_dict(
                publications_item_data
            )

            publications.append(publications_item)

        has_shortlisted = d.pop("has_shortlisted")

        def _parse_published_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                published_at_type_0 = isoparse(data)

                return published_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        published_at = _parse_published_at(d.pop("published_at", UNSET))

        def _parse_closed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                closed_at_type_0 = isoparse(data)

                return closed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        closed_at = _parse_closed_at(d.pop("closed_at", UNSET))

        def _parse_cancelled_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cancelled_at_type_0 = isoparse(data)

                return cancelled_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        cancelled_at = _parse_cancelled_at(d.pop("cancelled_at", UNSET))

        def _parse_awarded_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                awarded_at_type_0 = isoparse(data)

                return awarded_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        awarded_at = _parse_awarded_at(d.pop("awarded_at", UNSET))

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
            publications=publications,
            has_shortlisted=has_shortlisted,
            published_at=published_at,
            closed_at=closed_at,
            cancelled_at=cancelled_at,
            awarded_at=awarded_at,
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

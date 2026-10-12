from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.portal_order_line_output import PortalOrderLineOutput


T = TypeVar("T", bound="PortalOrder")


@_attrs_define
class PortalOrder:
    """
    Attributes:
        id (str):
        name (str):
        state (str):
        state_label (str):
        created_at (datetime.datetime):
        currency (str):
        total (float | str):
        reference (None | str | Unset):
        submitted_at (datetime.datetime | None | Unset):
        wanted_by (datetime.date | None | Unset):
        customer_reference (str | Unset):  Default: ''.
        location_id (None | str | Unset):
        location_name (None | str | Unset):
        asset_name (None | str | Unset):
        description (str | Unset):  Default: ''.
        requested_by_name (None | str | Unset):
        rejection_reason (None | str | Unset):
        lines (list[PortalOrderLineOutput] | Unset):
        can_cancel (bool | Unset):  Default: False.
    """

    id: str
    name: str
    state: str
    state_label: str
    created_at: datetime.datetime
    currency: str
    total: float | str
    reference: None | str | Unset = UNSET
    submitted_at: datetime.datetime | None | Unset = UNSET
    wanted_by: datetime.date | None | Unset = UNSET
    customer_reference: str | Unset = ""
    location_id: None | str | Unset = UNSET
    location_name: None | str | Unset = UNSET
    asset_name: None | str | Unset = UNSET
    description: str | Unset = ""
    requested_by_name: None | str | Unset = UNSET
    rejection_reason: None | str | Unset = UNSET
    lines: list[PortalOrderLineOutput] | Unset = UNSET
    can_cancel: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        state = self.state

        state_label = self.state_label

        created_at = self.created_at.isoformat()

        currency = self.currency

        total: float | str
        total = self.total

        reference: None | str | Unset
        if isinstance(self.reference, Unset):
            reference = UNSET
        else:
            reference = self.reference

        submitted_at: None | str | Unset
        if isinstance(self.submitted_at, Unset):
            submitted_at = UNSET
        elif isinstance(self.submitted_at, datetime.datetime):
            submitted_at = self.submitted_at.isoformat()
        else:
            submitted_at = self.submitted_at

        wanted_by: None | str | Unset
        if isinstance(self.wanted_by, Unset):
            wanted_by = UNSET
        elif isinstance(self.wanted_by, datetime.date):
            wanted_by = self.wanted_by.isoformat()
        else:
            wanted_by = self.wanted_by

        customer_reference = self.customer_reference

        location_id: None | str | Unset
        if isinstance(self.location_id, Unset):
            location_id = UNSET
        else:
            location_id = self.location_id

        location_name: None | str | Unset
        if isinstance(self.location_name, Unset):
            location_name = UNSET
        else:
            location_name = self.location_name

        asset_name: None | str | Unset
        if isinstance(self.asset_name, Unset):
            asset_name = UNSET
        else:
            asset_name = self.asset_name

        description = self.description

        requested_by_name: None | str | Unset
        if isinstance(self.requested_by_name, Unset):
            requested_by_name = UNSET
        else:
            requested_by_name = self.requested_by_name

        rejection_reason: None | str | Unset
        if isinstance(self.rejection_reason, Unset):
            rejection_reason = UNSET
        else:
            rejection_reason = self.rejection_reason

        lines: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        can_cancel = self.can_cancel

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "state": state,
                "state_label": state_label,
                "created_at": created_at,
                "currency": currency,
                "total": total,
            }
        )
        if reference is not UNSET:
            field_dict["reference"] = reference
        if submitted_at is not UNSET:
            field_dict["submitted_at"] = submitted_at
        if wanted_by is not UNSET:
            field_dict["wanted_by"] = wanted_by
        if customer_reference is not UNSET:
            field_dict["customer_reference"] = customer_reference
        if location_id is not UNSET:
            field_dict["location_id"] = location_id
        if location_name is not UNSET:
            field_dict["location_name"] = location_name
        if asset_name is not UNSET:
            field_dict["asset_name"] = asset_name
        if description is not UNSET:
            field_dict["description"] = description
        if requested_by_name is not UNSET:
            field_dict["requested_by_name"] = requested_by_name
        if rejection_reason is not UNSET:
            field_dict["rejection_reason"] = rejection_reason
        if lines is not UNSET:
            field_dict["lines"] = lines
        if can_cancel is not UNSET:
            field_dict["can_cancel"] = can_cancel

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.portal_order_line_output import PortalOrderLineOutput

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        state = d.pop("state")

        state_label = d.pop("state_label")

        created_at = isoparse(d.pop("created_at"))

        currency = d.pop("currency")

        def _parse_total(data: object) -> float | str:
            return cast(float | str, data)

        total = _parse_total(d.pop("total"))

        def _parse_reference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reference = _parse_reference(d.pop("reference", UNSET))

        def _parse_submitted_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                submitted_at_type_0 = isoparse(data)

                return submitted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        submitted_at = _parse_submitted_at(d.pop("submitted_at", UNSET))

        def _parse_wanted_by(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                wanted_by_type_0 = isoparse(data).date()

                return wanted_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        wanted_by = _parse_wanted_by(d.pop("wanted_by", UNSET))

        customer_reference = d.pop("customer_reference", UNSET)

        def _parse_location_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_id = _parse_location_id(d.pop("location_id", UNSET))

        def _parse_location_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_name = _parse_location_name(d.pop("location_name", UNSET))

        def _parse_asset_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        asset_name = _parse_asset_name(d.pop("asset_name", UNSET))

        description = d.pop("description", UNSET)

        def _parse_requested_by_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        requested_by_name = _parse_requested_by_name(d.pop("requested_by_name", UNSET))

        def _parse_rejection_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rejection_reason = _parse_rejection_reason(d.pop("rejection_reason", UNSET))

        _lines = d.pop("lines", UNSET)
        lines: list[PortalOrderLineOutput] | Unset = UNSET
        if _lines is not UNSET:
            lines = []
            for lines_item_data in _lines:
                lines_item = PortalOrderLineOutput.from_dict(lines_item_data)

                lines.append(lines_item)

        can_cancel = d.pop("can_cancel", UNSET)

        portal_order = cls(
            id=id,
            name=name,
            state=state,
            state_label=state_label,
            created_at=created_at,
            currency=currency,
            total=total,
            reference=reference,
            submitted_at=submitted_at,
            wanted_by=wanted_by,
            customer_reference=customer_reference,
            location_id=location_id,
            location_name=location_name,
            asset_name=asset_name,
            description=description,
            requested_by_name=requested_by_name,
            rejection_reason=rejection_reason,
            lines=lines,
            can_cancel=can_cancel,
        )

        portal_order.additional_properties = d
        return portal_order

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

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.proposal_move import ProposalMove


T = TypeVar("T", bound="OrgProposalDetails")


@_attrs_define
class OrgProposalDetails:
    """
    Attributes:
        id (str):
        name (str):
        description (str):
        funnel (str):
        stage (str):
        stage_type (str):
        created_at (datetime.datetime):
        internal_costs (float | str):
        external_value (float | str):
        currency (str):
        currency_symbol (str):
        owner_name (str):
        pricing_strategy (str):
        pricing_adjustment_percent (float | None | str | Unset):
        pricing_adjustment_amount (float | None | str | Unset):
        target_margin_percent (float | None | str | Unset):
        minimum_margin_percent (float | None | str | Unset):
        customer_id (None | str | Unset):
        customer_name (None | str | Unset):
        owner_id (None | str | Unset):
        funnel_id (None | str | Unset):
        stage_id (None | str | Unset):
        currency_code (None | str | Unset):
        days_in_stage (int | None | Unset):
        stage_sequence_no (int | None | Unset):
        moves (list[ProposalMove] | Unset):
        booking_management_enabled (bool | Unset):  Default: False.
        origin (str | Unset):  Default: 'staff'.
        requested_by_name (None | str | Unset):
        customer_location_name (None | str | Unset):
        customer_reference (str | Unset):  Default: ''.
        portal_reference (None | str | Unset):
        customer_asset_name (None | str | Unset):
        wanted_by (datetime.date | None | Unset):
    """

    id: str
    name: str
    description: str
    funnel: str
    stage: str
    stage_type: str
    created_at: datetime.datetime
    internal_costs: float | str
    external_value: float | str
    currency: str
    currency_symbol: str
    owner_name: str
    pricing_strategy: str
    pricing_adjustment_percent: float | None | str | Unset = UNSET
    pricing_adjustment_amount: float | None | str | Unset = UNSET
    target_margin_percent: float | None | str | Unset = UNSET
    minimum_margin_percent: float | None | str | Unset = UNSET
    customer_id: None | str | Unset = UNSET
    customer_name: None | str | Unset = UNSET
    owner_id: None | str | Unset = UNSET
    funnel_id: None | str | Unset = UNSET
    stage_id: None | str | Unset = UNSET
    currency_code: None | str | Unset = UNSET
    days_in_stage: int | None | Unset = UNSET
    stage_sequence_no: int | None | Unset = UNSET
    moves: list[ProposalMove] | Unset = UNSET
    booking_management_enabled: bool | Unset = False
    origin: str | Unset = "staff"
    requested_by_name: None | str | Unset = UNSET
    customer_location_name: None | str | Unset = UNSET
    customer_reference: str | Unset = ""
    portal_reference: None | str | Unset = UNSET
    customer_asset_name: None | str | Unset = UNSET
    wanted_by: datetime.date | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        funnel = self.funnel

        stage = self.stage

        stage_type = self.stage_type

        created_at = self.created_at.isoformat()

        internal_costs: float | str
        internal_costs = self.internal_costs

        external_value: float | str
        external_value = self.external_value

        currency = self.currency

        currency_symbol = self.currency_symbol

        owner_name = self.owner_name

        pricing_strategy = self.pricing_strategy

        pricing_adjustment_percent: float | None | str | Unset
        if isinstance(self.pricing_adjustment_percent, Unset):
            pricing_adjustment_percent = UNSET
        else:
            pricing_adjustment_percent = self.pricing_adjustment_percent

        pricing_adjustment_amount: float | None | str | Unset
        if isinstance(self.pricing_adjustment_amount, Unset):
            pricing_adjustment_amount = UNSET
        else:
            pricing_adjustment_amount = self.pricing_adjustment_amount

        target_margin_percent: float | None | str | Unset
        if isinstance(self.target_margin_percent, Unset):
            target_margin_percent = UNSET
        else:
            target_margin_percent = self.target_margin_percent

        minimum_margin_percent: float | None | str | Unset
        if isinstance(self.minimum_margin_percent, Unset):
            minimum_margin_percent = UNSET
        else:
            minimum_margin_percent = self.minimum_margin_percent

        customer_id: None | str | Unset
        if isinstance(self.customer_id, Unset):
            customer_id = UNSET
        else:
            customer_id = self.customer_id

        customer_name: None | str | Unset
        if isinstance(self.customer_name, Unset):
            customer_name = UNSET
        else:
            customer_name = self.customer_name

        owner_id: None | str | Unset
        if isinstance(self.owner_id, Unset):
            owner_id = UNSET
        else:
            owner_id = self.owner_id

        funnel_id: None | str | Unset
        if isinstance(self.funnel_id, Unset):
            funnel_id = UNSET
        else:
            funnel_id = self.funnel_id

        stage_id: None | str | Unset
        if isinstance(self.stage_id, Unset):
            stage_id = UNSET
        else:
            stage_id = self.stage_id

        currency_code: None | str | Unset
        if isinstance(self.currency_code, Unset):
            currency_code = UNSET
        else:
            currency_code = self.currency_code

        days_in_stage: int | None | Unset
        if isinstance(self.days_in_stage, Unset):
            days_in_stage = UNSET
        else:
            days_in_stage = self.days_in_stage

        stage_sequence_no: int | None | Unset
        if isinstance(self.stage_sequence_no, Unset):
            stage_sequence_no = UNSET
        else:
            stage_sequence_no = self.stage_sequence_no

        moves: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.moves, Unset):
            moves = []
            for moves_item_data in self.moves:
                moves_item = moves_item_data.to_dict()
                moves.append(moves_item)

        booking_management_enabled = self.booking_management_enabled

        origin = self.origin

        requested_by_name: None | str | Unset
        if isinstance(self.requested_by_name, Unset):
            requested_by_name = UNSET
        else:
            requested_by_name = self.requested_by_name

        customer_location_name: None | str | Unset
        if isinstance(self.customer_location_name, Unset):
            customer_location_name = UNSET
        else:
            customer_location_name = self.customer_location_name

        customer_reference = self.customer_reference

        portal_reference: None | str | Unset
        if isinstance(self.portal_reference, Unset):
            portal_reference = UNSET
        else:
            portal_reference = self.portal_reference

        customer_asset_name: None | str | Unset
        if isinstance(self.customer_asset_name, Unset):
            customer_asset_name = UNSET
        else:
            customer_asset_name = self.customer_asset_name

        wanted_by: None | str | Unset
        if isinstance(self.wanted_by, Unset):
            wanted_by = UNSET
        elif isinstance(self.wanted_by, datetime.date):
            wanted_by = self.wanted_by.isoformat()
        else:
            wanted_by = self.wanted_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "funnel": funnel,
                "stage": stage,
                "stage_type": stage_type,
                "created_at": created_at,
                "internal_costs": internal_costs,
                "external_value": external_value,
                "currency": currency,
                "currency_symbol": currency_symbol,
                "owner_name": owner_name,
                "pricing_strategy": pricing_strategy,
            }
        )
        if pricing_adjustment_percent is not UNSET:
            field_dict["pricing_adjustment_percent"] = pricing_adjustment_percent
        if pricing_adjustment_amount is not UNSET:
            field_dict["pricing_adjustment_amount"] = pricing_adjustment_amount
        if target_margin_percent is not UNSET:
            field_dict["target_margin_percent"] = target_margin_percent
        if minimum_margin_percent is not UNSET:
            field_dict["minimum_margin_percent"] = minimum_margin_percent
        if customer_id is not UNSET:
            field_dict["customer_id"] = customer_id
        if customer_name is not UNSET:
            field_dict["customer_name"] = customer_name
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if funnel_id is not UNSET:
            field_dict["funnel_id"] = funnel_id
        if stage_id is not UNSET:
            field_dict["stage_id"] = stage_id
        if currency_code is not UNSET:
            field_dict["currency_code"] = currency_code
        if days_in_stage is not UNSET:
            field_dict["days_in_stage"] = days_in_stage
        if stage_sequence_no is not UNSET:
            field_dict["stage_sequence_no"] = stage_sequence_no
        if moves is not UNSET:
            field_dict["moves"] = moves
        if booking_management_enabled is not UNSET:
            field_dict["booking_management_enabled"] = booking_management_enabled
        if origin is not UNSET:
            field_dict["origin"] = origin
        if requested_by_name is not UNSET:
            field_dict["requested_by_name"] = requested_by_name
        if customer_location_name is not UNSET:
            field_dict["customer_location_name"] = customer_location_name
        if customer_reference is not UNSET:
            field_dict["customer_reference"] = customer_reference
        if portal_reference is not UNSET:
            field_dict["portal_reference"] = portal_reference
        if customer_asset_name is not UNSET:
            field_dict["customer_asset_name"] = customer_asset_name
        if wanted_by is not UNSET:
            field_dict["wanted_by"] = wanted_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.proposal_move import ProposalMove

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        funnel = d.pop("funnel")

        stage = d.pop("stage")

        stage_type = d.pop("stage_type")

        created_at = isoparse(d.pop("created_at"))

        def _parse_internal_costs(data: object) -> float | str:
            return cast(float | str, data)

        internal_costs = _parse_internal_costs(d.pop("internal_costs"))

        def _parse_external_value(data: object) -> float | str:
            return cast(float | str, data)

        external_value = _parse_external_value(d.pop("external_value"))

        currency = d.pop("currency")

        currency_symbol = d.pop("currency_symbol")

        owner_name = d.pop("owner_name")

        pricing_strategy = d.pop("pricing_strategy")

        def _parse_pricing_adjustment_percent(
            data: object,
        ) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        pricing_adjustment_percent = _parse_pricing_adjustment_percent(
            d.pop("pricing_adjustment_percent", UNSET)
        )

        def _parse_pricing_adjustment_amount(
            data: object,
        ) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        pricing_adjustment_amount = _parse_pricing_adjustment_amount(
            d.pop("pricing_adjustment_amount", UNSET)
        )

        def _parse_target_margin_percent(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        target_margin_percent = _parse_target_margin_percent(
            d.pop("target_margin_percent", UNSET)
        )

        def _parse_minimum_margin_percent(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        minimum_margin_percent = _parse_minimum_margin_percent(
            d.pop("minimum_margin_percent", UNSET)
        )

        def _parse_customer_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_id = _parse_customer_id(d.pop("customer_id", UNSET))

        def _parse_customer_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_name = _parse_customer_name(d.pop("customer_name", UNSET))

        def _parse_owner_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_id = _parse_owner_id(d.pop("owner_id", UNSET))

        def _parse_funnel_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        funnel_id = _parse_funnel_id(d.pop("funnel_id", UNSET))

        def _parse_stage_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stage_id = _parse_stage_id(d.pop("stage_id", UNSET))

        def _parse_currency_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency_code = _parse_currency_code(d.pop("currency_code", UNSET))

        def _parse_days_in_stage(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        days_in_stage = _parse_days_in_stage(d.pop("days_in_stage", UNSET))

        def _parse_stage_sequence_no(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        stage_sequence_no = _parse_stage_sequence_no(d.pop("stage_sequence_no", UNSET))

        _moves = d.pop("moves", UNSET)
        moves: list[ProposalMove] | Unset = UNSET
        if _moves is not UNSET:
            moves = []
            for moves_item_data in _moves:
                moves_item = ProposalMove.from_dict(moves_item_data)

                moves.append(moves_item)

        booking_management_enabled = d.pop("booking_management_enabled", UNSET)

        origin = d.pop("origin", UNSET)

        def _parse_requested_by_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        requested_by_name = _parse_requested_by_name(d.pop("requested_by_name", UNSET))

        def _parse_customer_location_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_location_name = _parse_customer_location_name(
            d.pop("customer_location_name", UNSET)
        )

        customer_reference = d.pop("customer_reference", UNSET)

        def _parse_portal_reference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        portal_reference = _parse_portal_reference(d.pop("portal_reference", UNSET))

        def _parse_customer_asset_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_asset_name = _parse_customer_asset_name(
            d.pop("customer_asset_name", UNSET)
        )

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

        org_proposal_details = cls(
            id=id,
            name=name,
            description=description,
            funnel=funnel,
            stage=stage,
            stage_type=stage_type,
            created_at=created_at,
            internal_costs=internal_costs,
            external_value=external_value,
            currency=currency,
            currency_symbol=currency_symbol,
            owner_name=owner_name,
            pricing_strategy=pricing_strategy,
            pricing_adjustment_percent=pricing_adjustment_percent,
            pricing_adjustment_amount=pricing_adjustment_amount,
            target_margin_percent=target_margin_percent,
            minimum_margin_percent=minimum_margin_percent,
            customer_id=customer_id,
            customer_name=customer_name,
            owner_id=owner_id,
            funnel_id=funnel_id,
            stage_id=stage_id,
            currency_code=currency_code,
            days_in_stage=days_in_stage,
            stage_sequence_no=stage_sequence_no,
            moves=moves,
            booking_management_enabled=booking_management_enabled,
            origin=origin,
            requested_by_name=requested_by_name,
            customer_location_name=customer_location_name,
            customer_reference=customer_reference,
            portal_reference=portal_reference,
            customer_asset_name=customer_asset_name,
            wanted_by=wanted_by,
        )

        org_proposal_details.additional_properties = d
        return org_proposal_details

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

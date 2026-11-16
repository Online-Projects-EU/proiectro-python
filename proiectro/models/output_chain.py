from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chain_option import ChainOption
    from ..models.chain_outcome import ChainOutcome
    from ..models.chain_state import ChainState


T = TypeVar("T", bound="OutputChain")


@_attrs_define
class OutputChain:
    """A pipeline read from its counted moves: where an item in each state goes next, where it is likely to
    finish, and how long it usually stays.

        Attributes:
            pipeline (str):
            pipeline_label (str):
            pipelines (list[ChainOption] | Unset):
            scope (str | Unset):  Default: ''.
            scopes (list[ChainOption] | Unset):
            period (str | Unset):  Default: ''.
            periods (list[ChainOption] | Unset):
            moves (int | Unset):  Default: 0.
            states (list[ChainState] | Unset):
            outcomes (list[ChainOutcome] | Unset):
    """

    pipeline: str
    pipeline_label: str
    pipelines: list[ChainOption] | Unset = UNSET
    scope: str | Unset = ""
    scopes: list[ChainOption] | Unset = UNSET
    period: str | Unset = ""
    periods: list[ChainOption] | Unset = UNSET
    moves: int | Unset = 0
    states: list[ChainState] | Unset = UNSET
    outcomes: list[ChainOutcome] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pipeline = self.pipeline

        pipeline_label = self.pipeline_label

        pipelines: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pipelines, Unset):
            pipelines = []
            for pipelines_item_data in self.pipelines:
                pipelines_item = pipelines_item_data.to_dict()
                pipelines.append(pipelines_item)

        scope = self.scope

        scopes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.scopes, Unset):
            scopes = []
            for scopes_item_data in self.scopes:
                scopes_item = scopes_item_data.to_dict()
                scopes.append(scopes_item)

        period = self.period

        periods: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.periods, Unset):
            periods = []
            for periods_item_data in self.periods:
                periods_item = periods_item_data.to_dict()
                periods.append(periods_item)

        moves = self.moves

        states: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.states, Unset):
            states = []
            for states_item_data in self.states:
                states_item = states_item_data.to_dict()
                states.append(states_item)

        outcomes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.outcomes, Unset):
            outcomes = []
            for outcomes_item_data in self.outcomes:
                outcomes_item = outcomes_item_data.to_dict()
                outcomes.append(outcomes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pipeline": pipeline,
                "pipeline_label": pipeline_label,
            }
        )
        if pipelines is not UNSET:
            field_dict["pipelines"] = pipelines
        if scope is not UNSET:
            field_dict["scope"] = scope
        if scopes is not UNSET:
            field_dict["scopes"] = scopes
        if period is not UNSET:
            field_dict["period"] = period
        if periods is not UNSET:
            field_dict["periods"] = periods
        if moves is not UNSET:
            field_dict["moves"] = moves
        if states is not UNSET:
            field_dict["states"] = states
        if outcomes is not UNSET:
            field_dict["outcomes"] = outcomes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chain_option import ChainOption
        from ..models.chain_outcome import ChainOutcome
        from ..models.chain_state import ChainState

        d = dict(src_dict)
        pipeline = d.pop("pipeline")

        pipeline_label = d.pop("pipeline_label")

        _pipelines = d.pop("pipelines", UNSET)
        pipelines: list[ChainOption] | Unset = UNSET
        if _pipelines is not UNSET:
            pipelines = []
            for pipelines_item_data in _pipelines:
                pipelines_item = ChainOption.from_dict(pipelines_item_data)

                pipelines.append(pipelines_item)

        scope = d.pop("scope", UNSET)

        _scopes = d.pop("scopes", UNSET)
        scopes: list[ChainOption] | Unset = UNSET
        if _scopes is not UNSET:
            scopes = []
            for scopes_item_data in _scopes:
                scopes_item = ChainOption.from_dict(scopes_item_data)

                scopes.append(scopes_item)

        period = d.pop("period", UNSET)

        _periods = d.pop("periods", UNSET)
        periods: list[ChainOption] | Unset = UNSET
        if _periods is not UNSET:
            periods = []
            for periods_item_data in _periods:
                periods_item = ChainOption.from_dict(periods_item_data)

                periods.append(periods_item)

        moves = d.pop("moves", UNSET)

        _states = d.pop("states", UNSET)
        states: list[ChainState] | Unset = UNSET
        if _states is not UNSET:
            states = []
            for states_item_data in _states:
                states_item = ChainState.from_dict(states_item_data)

                states.append(states_item)

        _outcomes = d.pop("outcomes", UNSET)
        outcomes: list[ChainOutcome] | Unset = UNSET
        if _outcomes is not UNSET:
            outcomes = []
            for outcomes_item_data in _outcomes:
                outcomes_item = ChainOutcome.from_dict(outcomes_item_data)

                outcomes.append(outcomes_item)

        output_chain = cls(
            pipeline=pipeline,
            pipeline_label=pipeline_label,
            pipelines=pipelines,
            scope=scope,
            scopes=scopes,
            period=period,
            periods=periods,
            moves=moves,
            states=states,
            outcomes=outcomes,
        )

        output_chain.additional_properties = d
        return output_chain

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

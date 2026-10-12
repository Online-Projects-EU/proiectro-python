from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_portal_quote_requests_org import OutputPortalQuoteRequestsOrg
    from ..models.portal_quote_request import PortalQuoteRequest


T = TypeVar("T", bound="OutputPortalQuoteRequests")


@_attrs_define
class OutputPortalQuoteRequests:
    """
    Attributes:
        requests (list[PortalQuoteRequest]):
        org (OutputPortalQuoteRequestsOrg):
    """

    requests: list[PortalQuoteRequest]
    org: OutputPortalQuoteRequestsOrg
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        requests = []
        for requests_item_data in self.requests:
            requests_item = requests_item_data.to_dict()
            requests.append(requests_item)

        org = self.org.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "requests": requests,
                "org": org,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_portal_quote_requests_org import (
            OutputPortalQuoteRequestsOrg,
        )
        from ..models.portal_quote_request import PortalQuoteRequest

        d = dict(src_dict)
        requests = []
        _requests = d.pop("requests")
        for requests_item_data in _requests:
            requests_item = PortalQuoteRequest.from_dict(requests_item_data)

            requests.append(requests_item)

        org = OutputPortalQuoteRequestsOrg.from_dict(d.pop("org"))

        output_portal_quote_requests = cls(
            requests=requests,
            org=org,
        )

        output_portal_quote_requests.additional_properties = d
        return output_portal_quote_requests

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

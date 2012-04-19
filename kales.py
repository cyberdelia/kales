# -*- coding: utf-8 -*-
import json
import requests
import uuid


class Kales(object):
    def __init__(self, api_key):
        self.api_key = api_key

    def _request(self, content, content_type, external_id, **kwargs):
        headers = {
            "x-calais-licenseID": self.api_key,
            "content-type": content_type,
            "externalID": external_id,
            "accept": "application/json",
            "enableMetadataType": "SocialTags",
            "calculateRelevanceScore": "true",
            "allowDistribution": "false",
            "allowSearch": "false"
        }
        headers.update(kwargs)
        return requests.post("http://api.opencalais.com/tag/rs/enrich",
            data=content, headers=headers)

    def analyze(self, content, content_type="text/raw", external_id=None, **kwargs):
        if not content or not content.strip():
            return None

        if not external_id:
            external_id = uuid.uuid4().hex

        response = self._request(content, content_type, external_id, **kwargs)
        response.raise_for_status()
        content = json.loads(response.content)
        for element in list(content.values()):
            for key, value in list(element.items()):
                if isinstance(value, str) and value.startswith("http://") and value in content:
                    element[key] = content[value]
        for key, value in list(content.items()):
            if "_typeGroup" in value:
                group = value["_typeGroup"]
                if group not in content:
                    content[group] = []
                del value["_typeGroup"]
                content[group].append(value)
        return content

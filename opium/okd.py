import logging

_logger = logging.getLogger(__name__)


async def get_pods(session, base_url, project):
    async with session.get(f"{base_url}/api/v1/namespaces/{project}/pods") as resp:
        body = await resp.json()
        if resp.status != 200:
            _logger.warning(
                f"Failed getting pods for project {project} with error: {body}"
            )
            return []
    return body["items"]


async def get_pod_proxy(session, base_url, project, name, path=""):
    async with session.get(
        f"{base_url}/api/v1/namespaces/{project}/pods/{name}/proxy/{path}"
    ) as resp:
        body = await resp.text()
        if resp.status != 200:
            _logger.warning(f"Failed getting metrics for pod {name} with error: {body}")
    return body

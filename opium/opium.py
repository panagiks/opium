"""Main module."""
import asyncio

from aiohttp import ClientSession, web
from collections import defaultdict

from opium.business import gen_metrics_jobs
from opium.config import OpiumConfig
from opium.okd import get_pods


async def metrics(request):
    settings = request.app["settings"]
    dc_pods = defaultdict(list)
    headers = {"Authorization": f"Bearer {settings.okd.token}"}
    async with ClientSession(headers=headers) as session:
        pods = await get_pods(session, settings.okd.base_url, settings.project)
        for pod in pods:
            annotations = pod["metadata"]["annotations"]
            if "openshift.io/deployment-config.name" not in annotations:
                continue
            dc_pods[annotations["openshift.io/deployment-config.name"]].append(
                pod["metadata"]["name"]
            )
        results = await asyncio.gather(*gen_metrics_jobs(settings, session, dc_pods))
    return web.Response(text="\n".join(results), status=200 if results else 500)


def main():
    app = web.Application()
    app.add_routes([web.get("/metrics", metrics)])
    app["settings"] = OpiumConfig.from_env()
    web.run_app(app)


if __name__ == "__main__":
    main()

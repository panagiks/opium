from opium.okd import get_pod_proxy


def gen_metrics_jobs(settings, session, dc_pods):
    return (
        get_annotated_pod_metrics(
            session, settings.okd.base_url, settings.project, pod=pod
        )
        for dc in settings.deployment_configs
        for pod in dc_pods[dc]
    )


async def get_annotated_pod_metrics(*args, pod, **kwargs):
    resp = await get_pod_proxy(*args, **kwargs, name=pod, path="/metrics")
    return f"# metrics for {pod}\n{resp}"

from dataclasses import dataclass, field
from typing import List
from yaab.adapter import BaseAdapter


@dataclass
class OpiumOKDConfig(BaseAdapter):
    base_url: str = field(metadata={"transformations": ("OPIUM_OKD_URL",)})
    token: str = field(metadata={"transformations": ("OPIUM_OKD_TOKEN",)})


@dataclass
class OpiumConfig(BaseAdapter):
    okd: OpiumOKDConfig = field(metadata={"transformations": (OpiumOKDConfig,)})
    project: str = field(metadata={"transformations": ("OPIUM_PROJECT",)})
    deployment_configs: List[str] = field(
        metadata={
            "transformations": ("OPIUM_DEPLOYMENT_CONFIGS", lambda el: el.split(","))
        }
    )

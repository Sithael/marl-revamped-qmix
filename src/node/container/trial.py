from dataclasses import dataclass
from dataclasses import field


@dataclass
class RuntimeConfig:
    n_timesteps: int
    eval_schedule: int
    checkpoint_frequency: int
    n_games: int
    display_freq: int


@dataclass
class DeviceConfig:
    accelerator: str
    seed: int


@dataclass
class TrialConfig:
    runtime: RuntimeConfig
    device: DeviceConfig

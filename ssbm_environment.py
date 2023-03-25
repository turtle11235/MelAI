import dm_env
from dm_env import specs
import melee
import sys
import numpy as np

class SSBMEnvironment(dm_env.Environment):

  def __init__(self, console: melee.Console, controller: melee.Controller, iso: str | None):
    self._console = console
    self.controller = controller
    self._reset_next_step = True

    self._console.run(iso)
    # Connect to the console
    print("Connecting to console...")
    if not console.connect():
        print("ERROR: Failed to connect to the console.")
        sys.exit(-1)
    print("Console connected")

    print("Connecting controller to console...")
    if not controller.connect():
        print("ERROR: Failed to connect the controller.")
        sys.exit(-1)
    print("Controller connected")

  def reset(self) -> dm_env.TimeStep:
    """Returns the first `TimeStep` of a new episode."""
    pass

  def step(self, action: int) -> dm_env.TimeStep:
    """Updates the environment according to the action."""
    pass

  def observation_spec(self) -> specs.BoundedArray:
    """Returns the observation spec."""

  def action_spec(self) -> specs.DiscreteArray:
    """Returns the action spec."""
    pass
    
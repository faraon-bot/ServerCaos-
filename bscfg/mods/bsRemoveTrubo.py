import bsSpaz
from bsSpaz import *

bsSpaz.Spaz.lastPunchTime = 0
bsSpaz.gBasePunchCooldown = 400


def onPunchPress(self):
    """
    Called to 'press punch' on this spaz;
    used for player or AI connections.
    """
    if not self.node.exists() or self.frozen or self.node.knockout > 0.0:
        return

    if self.punchCallback is not None:
        self.punchCallback(self)
    t = bs.getGameTime()
    self._punchedNodes = set()  # reset this..
    if t - self.lastPunchTime > self._punchCooldown:
        self.lastPunchTime = t
        self.node.punchPressed = True
        if not self.node.holdNode.exists():
            bs.gameTimer(
                100, bs.WeakCall(self._safePlaySound, self.getFactory().swishSound, 0.8)
            )


bsSpaz.Spaz.onPunchPress = onPunchPress

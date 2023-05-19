import bsSpaz
from bsSpaz import *

bsSpaz.Spaz.lastPunchTime = 0
def onJumpPress(self):
    """
    Called to 'press jump' on this spaz;
    used by player or AI connections.
    """
    if not self.node.exists(): return
    self.node.jumpPressed = True
def onPickUpPress(self):
    """
    Called to 'press pick-up' on this spaz;
    used by player or AI connections.
    """
    if not self.node.exists(): return
    self.node.pickUpPressed = True
def onPunchPress(self):
    """
    Called to 'press punch' on this spaz;
    used for player or AI connections.
    """
    if not self.node.exists() or self.frozen or self.node.knockout > 0.0:
        return
    t = bs.getGameTime()
    self._punchedNodes = set()  # reset this..
    if t - self.lastPunchTime > self._punchCooldown:
        self.lastPunchTime = t
        self.node.punchPressed = True
        if not self.node.holdNode.exists():
            bs.gameTimer(
                100,
                bs.WeakCall(self._safePlaySound,
                            self.getFactory().swishSound, 0.8))

def onBombPress(self):
    """
    Called to 'press bomb' on this spaz;
    used for player or AI connections.
    """
    if not self.node.exists(): return
    
    if self._dead or self.frozen: return
    if self.node.knockout > 0.0: return
    self.node.bombPressed = True
    if not self.node.holdNode.exists(): self.dropBomb()
def onRun(self, value):
    """
    Called to 'press run' on this spaz;
    used for player or AI connections.
    """
    if not self.node.exists(): return
    self.node.run = value
def onFlyPress(self):
    """
    Called to 'press fly' on this spaz;
    used for player or AI connections.
    """
    if not self.node.exists(): return
    # not adding a cooldown time here for now; slightly worried
    # input events get clustered up during net-games and we'd wind up
    # killing a lot and making it hard to fly.. should look into this.
    self.node.flyPressed = True
bsSpaz.Spaz.onJumpPress = onJumpPress
bsSpaz.Spaz.onPickUpPress = onPickUpPress 
bsSpaz.Spaz.onPunchPress = onPunchPress
bsSpaz.Spaz.onBombPress = onBombPress
bsSpaz.Spaz.onRun = onRun
bsSpaz.Spaz.onFlyPress = onFlyPress


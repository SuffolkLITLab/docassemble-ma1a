"""Shared data contracts for the MA1A minimal slice."""

from docassemble.base.util import DAObject


class MA1ADataModel(DAObject):
    """Placeholder contract; future phases will extend with typed attributes."""

    def init(self, *pargs, **kwargs):
        super().init(*pargs, **kwargs)
        self.intro_ready = False
        self.hub_ready = False
        self.triage_ready = False

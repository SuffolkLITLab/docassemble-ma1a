"""Shared data model for MA1A divorce cases.

This module provides a centralized data structure for managing
all shared data across the 10+ divorce forms in the MA1A package.
"""

from __future__ import annotations

from docassemble.base.util import DAObject


class MA1ADivorceCase(DAObject):
    """Container for all shared data in a MA1A divorce case.
    
    This object holds references to all the common data collected once
    and reused across multiple forms:
    - Party information (users, other_parties)
    - Marriage details
    - Children information
    - Court information
    - Attorney information (if applicable)
    """

    def init(self, *pargs, **kwargs):
        """Initialize the divorce case object."""
        super().init(*pargs, **kwargs)
        
        # Flags for completion tracking
        self.shared_data_complete = False
        self.cjd101a_complete = False
        self.affidavit_complete = False
        self.r408_complete = False
        self.cjd301_complete = False
        self.cjd304_complete = False
        self.cjd305_complete = False
        self.custody_disclosure_complete = False
        self.separation_agreement_complete = False
        self.indigency_complete = False
        self.cjd400_complete = False
    
    def all_required_forms_complete(self) -> bool:
        """Check if all required forms for a basic 1A divorce are complete.
        
        Required forms:
        - CJD-101A (Joint Petition)
        - Affidavit of Irretrievable Breakdown
        - R-408 (Report of Divorce)
        
        Returns:
            True if all required forms are marked complete
        """
        return (
            self.shared_data_complete
            and self.cjd101a_complete
            and self.affidavit_complete
            and self.r408_complete
        )
    
    def forms_needed(self) -> list[str]:
        """Return a list of form names that still need to be completed.
        
        Returns:
            List of form identifiers (e.g., ['cjd101a', 'affidavit'])
        """
        needed = []
        
        if not self.cjd101a_complete:
            needed.append("cjd101a")
        if not self.affidavit_complete:
            needed.append("affidavit")
        if not self.r408_complete:
            needed.append("r408")
        
        # Conditional forms
        if hasattr(self, "has_minor_children") and self.has_minor_children:
            if not self.custody_disclosure_complete:
                needed.append("custody_disclosure")
        
        if hasattr(self, "needs_child_support") and self.needs_child_support:
            if not self.cjd301_complete:
                needed.append("cjd301")
            if not self.cjd304_complete:
                needed.append("cjd304")
        
        if hasattr(self, "has_deviation") and self.has_deviation:
            if not self.cjd305_complete:
                needed.append("cjd305")
        
        if hasattr(self, "has_separation_agreement") and self.has_separation_agreement:
            if not self.separation_agreement_complete:
                needed.append("separation_agreement")
        
        if hasattr(self, "requests_indigency") and self.requests_indigency:
            if not self.indigency_complete:
                needed.append("indigency")
        
        return needed
    
    def summary(self) -> str:
        """Generate a human-readable summary of the case.
        
        Returns:
            Formatted string with case details
        """
        lines = ["MA1A Divorce Case Summary", "=" * 30]
        
        if hasattr(self, "users") and len(self.users) > 0:
            lines.append(f"Petitioner: {self.users[0]}")
        
        if hasattr(self, "other_parties") and len(self.other_parties) > 0:
            lines.append(f"Respondent: {self.other_parties[0]}")
        
        if hasattr(self, "marriage_date"):
            lines.append(f"Marriage date: {self.marriage_date}")
        
        if hasattr(self, "has_minor_children"):
            if self.has_minor_children and hasattr(self, "children"):
                lines.append(f"Children: {len(self.children)}")
            else:
                lines.append("Children: None")
        
        if hasattr(self, "trial_court"):
            lines.append(f"Court: {self.trial_court}")
        
        lines.append("")
        lines.append("Forms completed:")
        if self.cjd101a_complete:
            lines.append("  ✓ Joint Petition (CJD-101A)")
        if self.affidavit_complete:
            lines.append("  ✓ Affidavit of Irretrievable Breakdown")
        if self.r408_complete:
            lines.append("  ✓ Report of Divorce (R-408)")
        if self.custody_disclosure_complete:
            lines.append("  ✓ Custody Disclosure Affidavit")
        if self.cjd301_complete:
            lines.append("  ✓ Financial Statements (CJD-301)")
        if self.cjd304_complete:
            lines.append("  ✓ Child Support Worksheet (CJD-304)")
        if self.cjd305_complete:
            lines.append("  ✓ Findings & Determinations (CJD-305)")
        if self.separation_agreement_complete:
            lines.append("  ✓ Separation Agreement")
        if self.indigency_complete:
            lines.append("  ✓ Affidavit of Indigency")
        if self.cjd400_complete:
            lines.append("  ✓ Motion (CJD-400)")
        
        return "\n".join(lines)


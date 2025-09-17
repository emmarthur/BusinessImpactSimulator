import importlib
import os
from typing import Dict, Any, Optional

class DomainSpecialist:
    def __init__(self):
        # We'll dynamically import domain specialists as needed
        self.domain_specialists = {}
        self.domain_metrics = {}
    
    def _get_domain_module_name(self, domain: str) -> str:
        """Convert domain name to module path format"""
        # Convert "Financial Services" to "financial_services"
        return domain.lower().replace(" ", "_")
    
    def import_domain_specialist

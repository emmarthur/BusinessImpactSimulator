from typing import Dict, Any

class DomainSpecialist:
    def __init__(self):
        self.domain = "Healthcare"
        self.regulations = ["HIPAA", "HITECH", "FDA", "EMTALA"]
        self.key_metrics = ["patient_safety", "care_quality", "operational_efficiency", "cost_containment"]
    
    def analyze_business_impact(self, project_data: dict) -> dict:
        """Analyze business impact for healthcare domain"""
        
        # Extract project details
        name = project_data.get("name", "")
        description = project_data.get("description", "")
        technologies = project_data.get("technologies", [])
        
        # Healthcare-specific analysis
        impact_areas = self._identify_healthcare_impact_areas(description, technologies)
        regulatory_considerations = self._assess_regulatory_impact(project_data)
        risk_assessment = self._assess_healthcare_risks(project_data)
        
        return {
            "domain": self.domain,
            "impact_areas": impact_areas,
            "regulatory_considerations": regulatory_considerations,
            "risk_assessment": risk_assessment,
            "confidence": "high",
            "recommendations": self._generate_healthcare_recommendations(project_data)
        }
    
    def _identify_healthcare_impact_areas(self, description: str, technologies: list) -> list:
        """Identify specific healthcare impact areas"""
        impact_areas = []
        
        # Analyze description for healthcare keywords
        healthcare_keywords = {
            "patient": ["patient care", "patient safety", "patient outcomes"],
            "clinical": ["clinical workflow", "clinical decision", "clinical data"],
            "medical": ["medical records", "medical devices", "medical imaging"],
            "hospital": ["hospital operations", "hospital management", "hospital efficiency"],
            "telemedicine": ["remote care", "virtual visits", "telehealth"],
            "pharmacy": ["medication management", "drug interactions", "prescription"]
        }
        
        description_lower = description.lower()
        for category, keywords in healthcare_keywords.items():
            for keyword in keywords:
                if keyword in description_lower:
                    impact_areas.append(category)
                    break
        
        return list(set(impact_areas))  # Remove duplicates
    
    def _assess_regulatory_impact(self, project_data: dict) -> dict:
        """Assess regulatory impact for healthcare projects"""
        regulatory_impact = {
            "hipaa_compliance": "high" if "patient" in str(project_data).lower() else "medium",
            "fda_considerations": "medium" if "device" in str(project_data).lower() else "low",
            "hitrust_requirements": "high" if "cloud" in str(project_data).lower() else "medium"
        }
        
        return regulatory_impact
    
    def _assess_healthcare_risks(self, project_data: dict) -> dict:
        """Assess healthcare-specific risks"""
        return {
            "patient_safety_risk": "medium",
            "data_privacy_risk": "high",
            "regulatory_compliance_risk": "high",
            "operational_disruption_risk": "medium"
        }
    
    def _generate_healthcare_recommendations(self, project_data: dict) -> list:
        """Generate healthcare-specific recommendations"""
        recommendations = [
            "Ensure HIPAA compliance for all patient data handling",
            "Implement robust data encryption and access controls",
            "Consider FDA approval requirements if involving medical devices",
            "Plan for clinical workflow integration",
            "Establish clear audit trails for regulatory compliance"
        ]
        
        return recommendations


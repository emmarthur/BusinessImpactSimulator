from typing import List, Dict, Any

class DomainMetrics:
    def __init__(self):
        self.domain = "Healthcare"
    
    def get_kpis(self) -> List[str]:
        """Get healthcare-specific KPIs"""
        return [
            "patient_satisfaction_score",
            "readmission_rate",
            "average_length_of_stay",
            "medication_error_rate",
            "clinical_outcome_improvement",
            "operational_efficiency_ratio",
            "cost_per_patient",
            "staff_productivity",
            "bed_occupancy_rate",
            "emergency_response_time"
        ]
    
    def get_regulations(self) -> List[str]:
        """Get healthcare-specific regulations"""
        return [
            "HIPAA (Health Insurance Portability and Accountability Act)",
            "HITECH (Health Information Technology for Economic and Clinical Health)",
            "FDA (Food and Drug Administration) regulations",
            "EMTALA (Emergency Medical Treatment and Labor Act)",
            "HITRUST (Health Information Trust Alliance)",
            "SOC 2 Type II compliance",
            "PCI DSS (for payment processing)",
            "State-specific healthcare regulations"
        ]
    
    def get_industry_benchmarks(self) -> Dict[str, Any]:
        """Get healthcare industry benchmarks"""
        return {
            "patient_satisfaction_target": 85.0,  # percentage
            "readmission_rate_target": 15.0,      # percentage
            "average_los_target": 4.5,            # days
            "medication_error_target": 0.1,       # percentage
            "cost_per_patient_target": 12000,     # dollars
            "staff_productivity_target": 85.0     # percentage
        }
    
    def get_risk_factors(self) -> List[str]:
        """Get healthcare-specific risk factors"""
        return [
            "patient_safety_incidents",
            "data_breach_risk",
            "regulatory_compliance_failures",
            "medical_device_malfunctions",
            "staff_shortages",
            "cybersecurity_threats",
            "insurance_reimbursement_changes",
            "litigation_risk"
        ]
    
    def get_success_metrics(self) -> Dict[str, str]:
        """Get healthcare success metrics and their descriptions"""
        return {
            "patient_satisfaction_score": "Measures patient experience and satisfaction with care",
            "readmission_rate": "Percentage of patients readmitted within 30 days",
            "average_length_of_stay": "Average number of days patients stay in hospital",
            "medication_error_rate": "Rate of medication-related errors or adverse events",
            "clinical_outcome_improvement": "Improvement in patient health outcomes",
            "operational_efficiency_ratio": "Ratio of outputs to inputs in healthcare delivery",
            "cost_per_patient": "Average cost to treat a patient",
            "staff_productivity": "Efficiency and productivity of healthcare staff",
            "bed_occupancy_rate": "Percentage of hospital beds occupied",
            "emergency_response_time": "Time to respond to emergency situations"
        }


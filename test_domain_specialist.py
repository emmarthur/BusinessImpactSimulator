#!/usr/bin/env python3
"""
Test script to demonstrate the dynamic import system for domain specialists
"""

import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from src.core.domain_specialist import DomainSpecialist

def test_domain_specialist():
    """Test the domain specialist with different domains"""
    
    # Initialize the domain specialist
    domain_specialist = DomainSpecialist()
    
    # Test project data
    healthcare_project = {
        "name": "Smart Hospital Management System",
        "description": "A comprehensive platform for managing patient records, scheduling appointments, and improving clinical workflow efficiency in hospitals.",
        "technologies": ["Python", "Django", "FHIR", "AWS"],
        "tags": ["healthcare", "patient care", "hospital management"],
        "stakeholders": ["doctors", "nurses", "administrators", "patients"],
        "objectives": ["improve patient safety", "reduce wait times", "enhance clinical outcomes"]
    }
    
    financial_project = {
        "name": "Blockchain Payment Platform",
        "description": "A decentralized payment system for financial institutions with enhanced security and compliance features.",
        "technologies": ["Ethereum", "Solidity", "React", "Node.js"],
        "tags": ["blockchain", "payments", "financial services"],
        "stakeholders": ["banks", "merchants", "customers"],
        "objectives": ["reduce transaction costs", "improve security", "enhance compliance"]
    }
    
    education_project = {
        "name": "Virtual Learning Platform",
        "description": "An online learning management system for universities and schools.",
        "technologies": ["React", "Node.js", "MongoDB", "AWS"],
        "tags": ["education", "e-learning", "virtual classroom"],
        "stakeholders": ["students", "teachers", "administrators"],
        "objectives": ["improve learning outcomes", "increase accessibility", "reduce costs"]
    }
    
    # Test healthcare domain (should use the implemented specialist)
    print("=== Testing Healthcare Domain ===")
    healthcare_result = domain_specialist.analyze_business_impact("Healthcare", healthcare_project)
    print(f"Domain: {healthcare_result['domain']}")
    print(f"Impact Areas: {healthcare_result['impact_areas']}")
    print(f"Regulatory Considerations: {healthcare_result['regulatory_considerations']}")
    print(f"Confidence: {healthcare_result['confidence']}")
    print(f"Recommendations: {healthcare_result['recommendations'][:2]}...")  # Show first 2
    print()
    
    # Test healthcare metrics
    healthcare_metrics = domain_specialist.get_domain_metrics("Healthcare")
    print(f"Healthcare KPIs: {healthcare_metrics['kpis'][:5]}...")  # Show first 5
    print(f"Healthcare Regulations: {healthcare_metrics['regulations'][:3]}...")  # Show first 3
    print()
    
    # Test financial services domain (should use basic specialist)
    print("=== Testing Financial Services Domain ===")
    financial_result = domain_specialist.analyze_business_impact("Financial Services", financial_project)
    print(f"Domain: {financial_result['domain']}")
    print(f"Analysis: {financial_result['analysis']}")
    print(f"Confidence: {financial_result['confidence']}")
    print(f"Note: {financial_result['note']}")
    print()
    
    # Test education domain (should use basic specialist)
    print("=== Testing Education Domain ===")
    education_result = domain_specialist.analyze_business_impact("Education", education_project)
    print(f"Domain: {education_result['domain']}")
    print(f"Analysis: {education_result['analysis']}")
    print(f"Confidence: {education_result['confidence']}")
    print(f"Note: {education_result['note']}")
    print()
    
    # Test metrics for non-implemented domains
    print("=== Testing Metrics for Non-Implemented Domains ===")
    financial_metrics = domain_specialist.get_domain_metrics("Financial Services")
    print(f"Financial Services KPIs: {financial_metrics['kpis']}")
    print(f"Financial Services Regulations: {financial_metrics['regulations']}")

if __name__ == "__main__":
    test_domain_specialist() 
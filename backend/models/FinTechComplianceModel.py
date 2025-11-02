from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class TransactionData(BaseModel):
    """Model for financial transaction data for AML/KYC analysis."""
    
    transaction_id: str = Field(..., description="Unique transaction identifier")
    timestamp: datetime = Field(..., description="Transaction timestamp")
    amount: float = Field(..., description="Transaction amount")
    currency: str = Field(..., description="Currency code (ISO 4217)")
    sender_account: str = Field(..., description="Sender account identifier")
    receiver_account: str = Field(..., description="Receiver account identifier")
    transaction_type: str = Field(..., description="Type of transaction (transfer, payment, withdrawal, etc.)")
    sender_country: Optional[str] = Field(None, description="Sender's country code")
    receiver_country: Optional[str] = Field(None, description="Receiver's country code")
    purpose: Optional[str] = Field(None, description="Transaction purpose or description")


class AMLScreeningRequest(BaseModel):
    """Request model for AML/KYC screening."""
    
    customer_name: str = Field(..., description="Customer full name")
    customer_id: Optional[str] = Field(None, description="Customer identifier")
    date_of_birth: Optional[str] = Field(None, description="Date of birth (YYYY-MM-DD)")
    nationality: Optional[str] = Field(None, description="Customer nationality")
    country_of_residence: Optional[str] = Field(None, description="Country of residence")
    is_pep: Optional[bool] = Field(False, description="Politically Exposed Person flag")
    transaction_data: Optional[TransactionData] = Field(None, description="Associated transaction data")
    screening_type: str = Field("standard", description="Screening type: standard, enhanced, ongoing")


class AMLRiskIndicator(BaseModel):
    """Individual AML risk indicator."""
    
    indicator_type: str = Field(..., description="Type of risk indicator")
    severity: str = Field(..., description="Severity level: low, medium, high, critical")
    description: str = Field(..., description="Description of the risk indicator")
    recommendation: str = Field(..., description="Recommended action")


class AMLScreeningResult(BaseModel):
    """Response model for AML screening results."""
    
    screening_id: str = Field(..., description="Unique screening identifier")
    customer_name: str = Field(..., description="Customer name screened")
    screening_date: datetime = Field(..., description="Date and time of screening")
    overall_risk_score: int = Field(..., description="Overall AML risk score (0-100)")
    risk_level: str = Field(..., description="Risk level: low, medium, high, critical")
    sanctions_match: bool = Field(..., description="Whether sanctions list match found")
    pep_match: bool = Field(..., description="Whether PEP match found")
    adverse_media: bool = Field(..., description="Whether adverse media found")
    risk_indicators: List[AMLRiskIndicator] = Field(default_factory=list, description="Identified risk indicators")
    requires_enhanced_dd: bool = Field(..., description="Whether enhanced due diligence is required")
    recommendations: List[str] = Field(default_factory=list, description="Compliance recommendations")


class PaymentSecurityCheck(BaseModel):
    """Model for PCI-DSS payment security compliance check."""
    
    merchant_id: str = Field(..., description="Merchant identifier")
    check_type: str = Field(..., description="Type of security check")
    systems_checked: List[str] = Field(..., description="Systems or components checked")
    compliance_status: str = Field(..., description="Compliance status: compliant, non-compliant, partial")
    findings: List[str] = Field(default_factory=list, description="Security findings")
    vulnerabilities: List[str] = Field(default_factory=list, description="Identified vulnerabilities")
    remediation_actions: List[str] = Field(default_factory=list, description="Required remediation actions")


class RegulatoryReportRequest(BaseModel):
    """Request model for generating regulatory reports."""
    
    report_type: str = Field(..., description="Type of report: transaction, compliance, risk_assessment")
    jurisdiction: str = Field(..., description="Regulatory jurisdiction")
    start_date: datetime = Field(..., description="Report start date")
    end_date: datetime = Field(..., description="Report end date")
    include_transactions: bool = Field(True, description="Include transaction details")
    include_risk_analysis: bool = Field(True, description="Include risk analysis")


class FinTechComplianceCheck(BaseModel):
    """Comprehensive fintech compliance check request."""
    
    entity_name: str = Field(..., description="Financial entity name")
    entity_type: str = Field(..., description="Entity type: bank, payment_provider, investment_firm, etc.")
    jurisdictions: List[str] = Field(..., description="Operating jurisdictions")
    regulations_to_check: List[str] = Field(..., description="Regulations to check against")
    document_text: Optional[str] = Field(None, description="Policy or document text to analyze")
    check_aml_kyc: bool = Field(True, description="Include AML/KYC compliance check")
    check_payment_security: bool = Field(False, description="Include PCI-DSS check")
    check_market_conduct: bool = Field(False, description="Include MiFID II/market conduct check")
    check_data_protection: bool = Field(True, description="Include GDPR/data protection check")

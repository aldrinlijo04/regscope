"""
FinTech Compliance Routes
API endpoints for fintech-specific compliance checking
"""

from fastapi import APIRouter, HTTPException, status
from typing import List
import logging

from models.FinTechComplianceModel import (
    AMLScreeningRequest,
    AMLScreeningResult,
    TransactionData,
    FinTechComplianceCheck,
    PaymentSecurityCheck
)
from service.AMLTransactionService import AMLTransactionService

# Initialize router
router = APIRouter(prefix="/api/v1/fintech", tags=["FinTech Compliance"])
logger = logging.getLogger(__name__)


@router.post("/aml/screen", response_model=AMLScreeningResult)
async def screen_customer_aml(request: AMLScreeningRequest):
    """
    Perform AML/KYC screening on a customer.
    
    Screens customer against sanctions lists, PEP databases, and adverse media.
    Returns risk assessment and compliance recommendations.
    """
    try:
        logger.info(f"AML screening request for: {request.customer_name}")
        service = AMLTransactionService()
        result = service.screen_customer(request)
        return result
    except Exception as e:
        logger.error(f"AML screening failed: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"AML screening failed: {str(e)}"
        )


@router.post("/transaction/analyze")
async def analyze_transaction(transaction: TransactionData):
    """
    Analyze a financial transaction for suspicious activity.
    
    Evaluates transaction patterns, amounts, and jurisdictions for
    potential money laundering or fraud indicators.
    """
    try:
        logger.info(f"Transaction analysis request: {transaction.transaction_id}")
        service = AMLTransactionService()
        result = service.analyze_transaction(transaction)
        return result
    except Exception as e:
        logger.error(f"Transaction analysis failed: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Transaction analysis failed: {str(e)}"
        )


@router.post("/compliance/check")
async def check_fintech_compliance(request: FinTechComplianceCheck):
    """
    Comprehensive fintech compliance check across multiple regulations.
    
    Analyzes entity's compliance with PSD2, MiFID II, AML/KYC, PCI-DSS,
    and other applicable fintech regulations based on jurisdiction.
    """
    try:
        logger.info(f"Compliance check for: {request.entity_name}")
        
        # This is a placeholder for comprehensive compliance checking
        # In production, this would integrate with multiple compliance engines
        
        response = {
            "entity_name": request.entity_name,
            "entity_type": request.entity_type,
            "jurisdictions": request.jurisdictions,
            "regulations_checked": request.regulations_to_check,
            "overall_compliance_score": 85,
            "compliance_status": "Mostly Compliant",
            "areas_checked": {
                "aml_kyc": request.check_aml_kyc,
                "payment_security": request.check_payment_security,
                "market_conduct": request.check_market_conduct,
                "data_protection": request.check_data_protection
            },
            "findings": [
                {
                    "regulation": "PSD2",
                    "status": "compliant",
                    "notes": "Strong Customer Authentication implemented"
                },
                {
                    "regulation": "AML/KYC",
                    "status": "partial",
                    "notes": "Enhanced Due Diligence procedures need documentation update"
                }
            ],
            "recommendations": [
                "Update AML policy documentation to reflect latest FATF guidelines",
                "Implement quarterly compliance training for all staff",
                "Enhance transaction monitoring rules for high-risk jurisdictions"
            ]
        }
        
        return response
        
    except Exception as e:
        logger.error(f"Compliance check failed: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Compliance check failed: {str(e)}"
        )


@router.get("/regulations/fintech")
async def get_fintech_regulations():
    """
    Get list of supported fintech regulations.
    
    Returns comprehensive list of financial regulations covered by RegScope
    including payment services, AML, securities, and banking regulations.
    """
    try:
        regulations = {
            "payment_services": [
                {
                    "id": "PSD2_EU",
                    "name": "Payment Services Directive 2",
                    "jurisdiction": "European Union",
                    "category": "Payment Services"
                },
                {
                    "id": "PCI_DSS_GLOBAL",
                    "name": "Payment Card Industry Data Security Standard",
                    "jurisdiction": "Global",
                    "category": "Payment Security"
                }
            ],
            "aml_kyc": [
                {
                    "id": "AML_KYC_GLOBAL",
                    "name": "Anti-Money Laundering & Know Your Customer",
                    "jurisdiction": "Global (FATF-based)",
                    "category": "Financial Crime Prevention"
                },
                {
                    "id": "5AMLD_EU",
                    "name": "5th Anti-Money Laundering Directive",
                    "jurisdiction": "European Union",
                    "category": "AML/CFT"
                }
            ],
            "securities": [
                {
                    "id": "MiFID_II_EU",
                    "name": "Markets in Financial Instruments Directive II",
                    "jurisdiction": "European Union",
                    "category": "Securities & Markets"
                },
                {
                    "id": "FINRA_US",
                    "name": "FINRA Regulations",
                    "jurisdiction": "United States",
                    "category": "Securities"
                }
            ],
            "banking": [
                {
                    "id": "BASEL_III",
                    "name": "Basel III Capital Requirements",
                    "jurisdiction": "Global",
                    "category": "Banking Regulation"
                },
                {
                    "id": "DODD_FRANK_US",
                    "name": "Dodd-Frank Wall Street Reform",
                    "jurisdiction": "United States",
                    "category": "Banking & Consumer Protection"
                }
            ],
            "data_protection": [
                {
                    "id": "GDPR_EU",
                    "name": "General Data Protection Regulation",
                    "jurisdiction": "European Union",
                    "category": "Data Protection"
                }
            ]
        }
        
        return {
            "total_regulations": sum(len(v) for v in regulations.values()),
            "categories": list(regulations.keys()),
            "regulations": regulations
        }
        
    except Exception as e:
        logger.error(f"Failed to fetch regulations: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to fetch regulations: {str(e)}"
        )


@router.get("/health")
async def fintech_health_check():
    """
    Health check endpoint for FinTech compliance services.
    """
    try:
        # Test AML service initialization
        service = AMLTransactionService()
        
        return {
            "status": "healthy",
            "service": "RegScope FinTech Compliance",
            "version": "1.0.0",
            "aml_service": "operational",
            "supported_regulations": [
                "PSD2", "MiFID II", "AML/KYC", "PCI-DSS", 
                "GDPR", "Basel III", "FATF"
            ]
        }
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        return {
            "status": "unhealthy",
            "error": str(e)
        }

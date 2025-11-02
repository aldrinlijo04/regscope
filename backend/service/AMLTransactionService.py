"""
AML Transaction Analysis Service
Provides transaction monitoring and AML/KYC screening capabilities
"""

import logging
from typing import List, Dict, Any, Optional
from datetime import datetime
import json

from models.FinTechComplianceModel import (
    AMLScreeningRequest,
    AMLScreeningResult,
    AMLRiskIndicator,
    TransactionData
)
from utils.ai_client.gemini_client import GeminiClient
from utils.ai_client.gemini_config import GeminiConfig

logger = logging.getLogger(__name__)


class AMLTransactionService:
    """Service for AML transaction monitoring and screening."""
    
    def __init__(self):
        """Initialize AML service with AI client."""
        try:
            self.ai_client = GeminiClient(GeminiConfig.from_environment())
            logger.info("AML Transaction Service initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize AML service: {e}")
            raise
    
    def screen_customer(self, request: AMLScreeningRequest) -> AMLScreeningResult:
        """
        Perform AML/KYC screening on a customer.
        
        Args:
            request: AML screening request with customer information
            
        Returns:
            AML screening result with risk assessment
        """
        logger.info(f"Starting AML screening for customer: {request.customer_name}")
        
        try:
            # Build screening prompt
            screening_prompt = self._build_screening_prompt(request)
            
            # Get AI analysis
            ai_response = self.ai_client.generate_text(
                screening_prompt,
                max_tokens=1500,
                temperature=0.2
            )
            
            # Parse and structure results
            result = self._parse_screening_result(ai_response, request)
            
            logger.info(f"AML screening completed. Risk level: {result.risk_level}")
            return result
            
        except Exception as e:
            logger.error(f"AML screening failed: {e}")
            raise
    
    def analyze_transaction(self, transaction: TransactionData) -> Dict[str, Any]:
        """
        Analyze a single transaction for suspicious patterns.
        
        Args:
            transaction: Transaction data to analyze
            
        Returns:
            Analysis result with risk indicators
        """
        logger.info(f"Analyzing transaction: {transaction.transaction_id}")
        
        try:
            analysis_prompt = f"""Analyze this financial transaction for potential money laundering or suspicious activity:

Transaction Details:
- ID: {transaction.transaction_id}
- Amount: {transaction.currency} {transaction.amount}
- Type: {transaction.transaction_type}
- Sender Country: {transaction.sender_country}
- Receiver Country: {transaction.receiver_country}
- Purpose: {transaction.purpose}
- Timestamp: {transaction.timestamp}

Evaluate for:
1. Unusual transaction amount or frequency
2. High-risk jurisdictions involved
3. Structuring patterns (amounts just below reporting thresholds)
4. Inconsistent transaction purpose
5. Rapid movement of funds

Provide:
- Risk score (0-100)
- Risk level (low/medium/high/critical)
- Specific red flags identified
- Recommendations for compliance team

Format as JSON."""

            ai_response = self.ai_client.generate_text(
                analysis_prompt,
                max_tokens=800,
                temperature=0.2
            )
            
            # Parse AI response
            try:
                result = json.loads(ai_response)
            except json.JSONDecodeError:
                # Fallback structure if AI doesn't return valid JSON
                result = {
                    "transaction_id": transaction.transaction_id,
                    "risk_score": 50,
                    "risk_level": "medium",
                    "red_flags": ["Unable to complete full analysis"],
                    "recommendations": ["Manual review recommended"]
                }
            
            return result
            
        except Exception as e:
            logger.error(f"Transaction analysis failed: {e}")
            raise
    
    def _build_screening_prompt(self, request: AMLScreeningRequest) -> str:
        """Build AI prompt for customer screening."""
        
        prompt = f"""Perform AML/KYC risk screening for the following customer:

Customer Information:
- Name: {request.customer_name}
- Customer ID: {request.customer_id or 'N/A'}
- Date of Birth: {request.date_of_birth or 'N/A'}
- Nationality: {request.nationality or 'N/A'}
- Country of Residence: {request.country_of_residence or 'N/A'}
- PEP Status: {'Yes' if request.is_pep else 'No'}
- Screening Type: {request.screening_type}
"""

        if request.transaction_data:
            prompt += f"""
Related Transaction:
- Amount: {request.transaction_data.currency} {request.transaction_data.amount}
- Type: {request.transaction_data.transaction_type}
- Countries: {request.transaction_data.sender_country} -> {request.transaction_data.receiver_country}
"""

        prompt += """
Evaluate based on FATF AML/KYC standards:
1. Customer risk profile (low/medium/high/critical)
2. Potential sanctions list matches (simulate check)
3. PEP status verification
4. Geographic risk factors
5. Adverse media indicators
6. Need for Enhanced Due Diligence

Provide comprehensive risk assessment with:
- Overall risk score (0-100)
- Risk level classification
- Specific risk indicators found
- Enhanced DD requirement
- Actionable recommendations

Format response as detailed JSON analysis."""

        return prompt
    
    def _parse_screening_result(
        self,
        ai_response: str,
        request: AMLScreeningRequest
    ) -> AMLScreeningResult:
        """Parse AI response into structured screening result."""
        
        try:
            # Try to parse JSON from AI response
            parsed = json.loads(ai_response)
            
            # Extract risk indicators
            risk_indicators = []
            if "risk_indicators" in parsed:
                for indicator in parsed["risk_indicators"]:
                    risk_indicators.append(AMLRiskIndicator(
                        indicator_type=indicator.get("type", "unknown"),
                        severity=indicator.get("severity", "medium"),
                        description=indicator.get("description", ""),
                        recommendation=indicator.get("recommendation", "")
                    ))
            
            # Build result
            result = AMLScreeningResult(
                screening_id=f"AML-{datetime.now().strftime('%Y%m%d%H%M%S')}",
                customer_name=request.customer_name,
                screening_date=datetime.now(),
                overall_risk_score=parsed.get("risk_score", 50),
                risk_level=parsed.get("risk_level", "medium"),
                sanctions_match=parsed.get("sanctions_match", False),
                pep_match=parsed.get("pep_match", request.is_pep),
                adverse_media=parsed.get("adverse_media", False),
                risk_indicators=risk_indicators,
                requires_enhanced_dd=parsed.get("enhanced_dd_required", False),
                recommendations=parsed.get("recommendations", [])
            )
            
            return result
            
        except json.JSONDecodeError:
            logger.warning("Failed to parse AI response as JSON, using fallback")
            
            # Fallback result
            return AMLScreeningResult(
                screening_id=f"AML-{datetime.now().strftime('%Y%m%d%H%M%S')}",
                customer_name=request.customer_name,
                screening_date=datetime.now(),
                overall_risk_score=50,
                risk_level="medium",
                sanctions_match=False,
                pep_match=request.is_pep,
                adverse_media=False,
                risk_indicators=[],
                requires_enhanced_dd=request.screening_type == "enhanced",
                recommendations=["Manual review recommended due to incomplete automated screening"]
            )

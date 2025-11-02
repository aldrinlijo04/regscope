# PSD2 (Payment Services Directive 2) - Implementation Notes

## Overview
PSD2 is the EU directive regulating payment services and payment service providers across the European Economic Area. It introduces requirements for Strong Customer Authentication (SCA) and open banking APIs.

## Key Compliance Requirements

### 1. Strong Customer Authentication (SCA)
- **Requirement**: Multi-factor authentication for electronic payments
- **Elements**: At least two of: knowledge (PIN), possession (device), inherence (biometric)
- **Application**: Payment initiation, account access, remote transactions
- **Exemptions**: Low-value transactions (<€30), recurring payments, trusted beneficiaries

### 2. Open Banking API Access
- **Requirement**: Provide APIs for third-party providers
- **Standards**: Berlin Group, Open Banking UK, STET
- **Availability**: Same as online banking (99.5% uptime)
- **Access**: Account information and payment initiation

### 3. Third Party Provider Registration
- **Authorization**: From national competent authority
- **Insurance**: Professional indemnity or comparable guarantee
- **Capital**: Based on transaction volume
- **Registry**: National payment institutions register

## Implementation Checklist

- [ ] SCA implemented with multi-factor authentication
- [ ] Dynamic linking for remote transactions
- [ ] Dedicated APIs for TPPs
- [ ] API availability monitoring
- [ ] TPP authorization verification
- [ ] Professional indemnity insurance in place
- [ ] Transaction monitoring and fraud detection
- [ ] Security incident reporting procedures
- [ ] Customer data encryption (transit and rest)
- [ ] GDPR compliance for payment data

## Penalties for Non-Compliance
- Administrative fines up to 5% of annual turnover
- Suspension or revocation of authorization
- Civil liability for damages to users

## Regulatory Bodies
- European Banking Authority (EBA) - Technical standards
- National Competent Authorities - Authorization and supervision

## Related Regulations
- GDPR (data protection)
- eIDAS (electronic identification)
- 5AMLD/6AMLD (anti-money laundering)

## Resources
- EBA Official Website: https://www.eba.europa.eu
- PSD2 Directive: 2015/2366/EU
- RTS on SCA: Regulatory Technical Standards

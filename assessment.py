MARKETS = {

    "brazil": {
        "name": "Brazil",

        "dimensions": {
            "Product & Derivatives Regulation": {
                "score": 3,
                "reason": "Derivative structuring, suitability, and product classification need to align with the Brazilian regulatory framework."
            },

            "Licensing & Authorization": {
                "score": 3,
                "reason": "Local regulated partners and appropriate authorization are important before launch."
            },

            "KYC / AML & Customer Protection": {
                "score": 3,
                "reason": "Identity matching, Travel Rule requirements, tax reporting, and customer suitability controls need to be integrated."
            },

            "Capital Controls & FX": {
                "score": 3,
                "reason": "Foreign-exchange requirements and the local FX framework affect product and settlement design."
            },

            "Payments & Settlement": {
                "score": 2,
                "reason": "Pix provides an established local payment rail, supporting faster payment integration."
            },

            "Reporting & Ongoing Compliance": {
                "score": 3,
                "reason": "Tax reporting, transaction monitoring, and ongoing regulatory obligations need to be incorporated."
            }
        },

        "gates": {
            "Product classification confirmed": {
                "status": True,
                "critical": True,
                "reason": "The proposed product structure can be mapped to the applicable Brazilian regulatory framework."
            },

            "Authorization pathway confirmed": {
                "status": True,
                "critical": True,
                "reason": "A regulated local partner and appropriate authorization pathway have been identified."
            },

            "KYC / AML requirements satisfiable": {
                "status": True,
                "critical": True,
                "reason": "KYC, identity matching, Travel Rule and related compliance requirements can be incorporated."
            },

            "Payment / settlement structure viable": {
                "status": True,
                "critical": True,
                "reason": "Local payment infrastructure such as Pix provides a viable basis for the proposed settlement model."
            },

            "Risk controls implementable": {
                "status": True,
                "critical": True,
                "reason": "Suitability, monitoring and product-level risk controls can be incorporated before launch."
            }
        },

        "entry_approach": "Partner-led",

        "adjustments": [
            "Integrate Pix and CPF identity matching",
            "Adapt derivative suitability controls",
            "Implement Travel Rule and tax reporting requirements",
            "Use an appropriately regulated local partner"
        ],

        "risks": [
            {
                "title": "Product classification risk",
                "mitigation": "Confirm the regulatory treatment of each product before launch."
            },
            {
                "title": "FX and capital-control complexity",
                "mitigation": "Design settlement and FX flows around the applicable Brazilian framework."
            },
            {
                "title": "Partner dependency",
                "mitigation": "Define clear responsibilities and compliance obligations with the local partner."
            }
        ]
    },


    "uae": {
        "name": "United Arab Emirates",

        "dimensions": {
            "Product & Derivatives Regulation": {
                "score": 4,
                "reason": "Product classification and the applicable regulatory perimeter need to be confirmed before launch."
            },

            "Licensing & Authorization": {
                "score": 4,
                "reason": "The appropriate regulatory jurisdiction, licensing structure, and permissions must be established."
            },

            "KYC / AML & Customer Protection": {
                "score": 3,
                "reason": "Customer classification, KYC/AML, suitability, disclosures, custody, and complaints processes require adaptation."
            },

            "Capital Controls & FX": {
                "score": 2,
                "reason": "The UAE has established FX and cross-border payment infrastructure, although specific exchange and remittance activities can have regulatory requirements."
            },

            "Payments & Settlement": {
                "score": 2,
                "reason": "The UAE has established payment and settlement infrastructure, but MochaTrade would need an appropriate regulated payment structure."
            },

            "Reporting & Ongoing Compliance": {
                "score": 3,
                "reason": "Transaction monitoring, recordkeeping, disclosures, complaints, cybersecurity, and customer-protection controls are required."
            }
        },

        "gates": {
            "Product classification confirmed": {
                "status": False,
                "critical": True,
                "reason": "The regulatory classification of the proposed products still needs to be confirmed."
            },

            "Authorization pathway confirmed": {
                "status": False,
                "critical": True,
                "reason": "The appropriate regulatory jurisdiction, licensing structure and permissions still need to be established."
            },

            "KYC / AML requirements satisfiable": {
                "status": True,
                "critical": True,
                "reason": "KYC/AML and customer-protection requirements can be incorporated into the proposed model."
            },

            "Payment / settlement structure viable": {
                "status": True,
                "critical": True,
                "reason": "Established payment infrastructure exists, subject to selecting the appropriate regulated structure."
            },

            "Risk controls implementable": {
                "status": True,
                "critical": True,
                "reason": "Risk warnings, margin, leverage, liquidation and monitoring controls can be designed into the product."
            }
        },

        "entry_approach": "Controlled pilot",

        "adjustments": [
            "Confirm product classification",
            "Determine the correct licensing structure",
            "Adapt customer classification and onboarding",
            "Implement UAE-compliant payment and settlement arrangements",
            "Strengthen margin, leverage, liquidation, and risk disclosures"
        ],

        "risks": [
            {
                "title": "Regulatory perimeter uncertainty",
                "mitigation": "Confirm product classification and applicable regulator before launch."
            },
            {
                "title": "Licensing complexity",
                "mitigation": "Select the appropriate regulated entity or local partner structure."
            }
        ]
    },


    "south-africa": {
        "name": "South Africa",

        "dimensions": {
            "Product & Derivatives Regulation": {
                "score": 3,
                "reason": "The regulatory framework includes specific requirements for derivative and digital-asset related activities."
            },

            "Licensing & Authorization": {
                "score": 3,
                "reason": "An appropriately authorized local structure and regulated partner are central to the proposed entry approach."
            },

            "KYC / AML & Customer Protection": {
                "score": 3,
                "reason": "FICA, customer verification, and regulated ODP/CASP structures need to be integrated."
            },

            "Capital Controls & FX": {
                "score": 5,
                "reason": "Exchange controls, offshore transfer limits, conversion costs, and banking-related friction are significant considerations."
            },

            "Payments & Settlement": {
                "score": 3,
                "reason": "Local banking and settlement arrangements need to accommodate the regulatory and exchange-control environment."
            },

            "Reporting & Ongoing Compliance": {
                "score": 3,
                "reason": "Ongoing regulatory, banking, customer verification, and monitoring requirements need to be maintained."
            }
        },

        "gates": {
            "Product classification confirmed": {
                "status": True,
                "critical": True,
                "reason": "The Round 1 approach identifies an applicable regulated ODP/CASP framework for the proposed model."
            },

            "Authorization pathway confirmed": {
                "status": True,
                "critical": True,
                "reason": "The proposed entry model uses an FSCA/ODP-compliant structure and regulated partner."
            },

            "KYC / AML requirements satisfiable": {
                "status": True,
                "critical": True,
                "reason": "FICA and customer-verification requirements are incorporated into the proposed entry plan."
            },

            "Payment / settlement structure viable": {
                "status": True,
                "critical": True,
                "reason": "A local banking and ZAR settlement structure is proposed to address the market's payment environment."
            },

            "Risk controls implementable": {
                "status": True,
                "critical": True,
                "reason": "Hedging and exchange-control management are included in the proposed operating model."
            }
        },

        "entry_approach": "Partner-led",

        "adjustments": [
            "Work with an FSCA/ODP-compliant structure",
            "Integrate FICA requirements",
            "Design around SARB exchange-control requirements",
            "Develop a ZAR wallet and local settlement structure",
            "Implement appropriate hedging mechanisms"
        ],

        "risks": [
            {
                "title": "Exchange-control restrictions",
                "mitigation": "Design the product and settlement model around applicable SARB requirements."
            },
            {
                "title": "Offshore transfer friction",
                "mitigation": "Use an appropriately structured local settlement and banking model."
            }
        ]
    },


    "singapore": {
        "name": "Singapore",

        "dimensions": {
            "Product & Derivatives Regulation": {
                "score": 3,
                "reason": "Stock-linked and perpetual products require product-by-product classification within the applicable MAS framework."
            },

            "Licensing & Authorization": {
                "score": 3,
                "reason": "The appropriate MAS regulatory perimeter and local licensed structure need to be established."
            },

            "KYC / AML & Customer Protection": {
                "score": 3,
                "reason": "KYC/AML, customer disclosures, reporting, and other compliance controls need to be adapted."
            },

            "Capital Controls & FX": {
                "score": 1,
                "reason": "Singapore operates an open capital account, reducing capital-control complexity."
            },

            "Payments & Settlement": {
                "score": 2,
                "reason": "Singapore has established regulated payment and settlement infrastructure, but the appropriate licensed structure is still required."
            },

            "Reporting & Ongoing Compliance": {
                "score": 3,
                "reason": "Singapore-specific KYC/AML, disclosures, reporting, and ongoing compliance processes need to be implemented."
            }
        },

        "gates": {
            "Product classification confirmed": {
                "status": False,
                "critical": True,
                "reason": "Stock-linked and perpetual products require product-by-product classification."
            },

            "Authorization pathway confirmed": {
                "status": False,
                "critical": True,
                "reason": "The applicable MAS regulatory perimeter and local licensed structure still need to be established."
            },

            "KYC / AML requirements satisfiable": {
                "status": True,
                "critical": True,
                "reason": "Singapore-specific KYC/AML requirements can be incorporated into the proposed model."
            },

            "Payment / settlement structure viable": {
                "status": True,
                "critical": True,
                "reason": "Established payment and settlement infrastructure exists for an appropriately structured participant."
            },

            "Risk controls implementable": {
                "status": True,
                "critical": True,
                "reason": "The proposed restricted MVP allows customer-protection and risk controls to be implemented before scaling."
            }
        },

        "entry_approach": "Controlled pilot",

        "adjustments": [
            "Map each product to the applicable MAS regulatory perimeter",
            "Use an appropriately licensed local structure or partner",
            "Implement Singapore-specific KYC/AML controls",
            "Adapt disclosures and reporting",
            "Begin with a restricted MVP"
        ],

        "risks": [
            {
                "title": "Product classification",
                "mitigation": "Complete product-by-product regulatory classification before launch."
            },
            {
                "title": "Authorization requirements",
                "mitigation": "Use an appropriate licensed entity or regulated local partner."
            }
        ]
    },


    "australia": {
        "name": "Australia",

        "dimensions": {
            "Product & Derivatives Regulation": {
                "score": 4,
                "reason": "Products including CFDs, options, forwards, futures, and perpetual-style products can require detailed financial-product classification."
            },

            "Licensing & Authorization": {
                "score": 4,
                "reason": "An appropriately licensed Australian entity or partner is required for the proposed financial-product activities."
            },

            "KYC / AML & Customer Protection": {
                "score": 3,
                "reason": "Retail customer protections, eligibility, disclosures, leverage and margin controls need to be incorporated."
            },

            "Capital Controls & FX": {
                "score": 1,
                "reason": "Australia has an open capital environment and developed foreign-exchange market."
            },

            "Payments & Settlement": {
                "score": 2,
                "reason": "Australia has mature payment and settlement infrastructure, although appropriate institutional and settlement arrangements are still required."
            },

            "Reporting & Ongoing Compliance": {
                "score": 3,
                "reason": "Financial-product compliance, customer protections, monitoring, and reporting obligations need to be maintained."
            }
        },

        "gates": {
            "Product classification confirmed": {
                "status": False,
                "critical": True,
                "reason": "Each proposed product needs to be classified under the applicable Australian financial-product framework."
            },

            "Authorization pathway confirmed": {
                "status": False,
                "critical": True,
                "reason": "The appropriate AFSL pathway or licensed local partner structure still needs to be established."
            },

            "KYC / AML requirements satisfiable": {
                "status": True,
                "critical": True,
                "reason": "Customer eligibility, disclosure and compliance requirements can be incorporated into the proposed model."
            },

            "Payment / settlement structure viable": {
                "status": True,
                "critical": True,
                "reason": "Australia has established payment and settlement infrastructure for appropriately structured participants."
            },

            "Risk controls implementable": {
                "status": True,
                "critical": True,
                "reason": "Leverage, margin, disclosure and retail customer-protection controls can be incorporated."
            }
        },

        "entry_approach": "Controlled pilot",

        "adjustments": [
            "Complete legal classification of each product",
            "Establish an AFSL pathway or appropriate licensed partner",
            "Launch the simplest permitted product first",
            "Implement retail leverage, margin, and disclosure controls",
            "Evaluate perpetual products separately"
        ],

        "risks": [
            {
                "title": "Financial-product classification",
                "mitigation": "Classify each product before launch and obtain the required authorization."
            },
            {
                "title": "Retail customer requirements",
                "mitigation": "Build customer eligibility, leverage, margin, and disclosure controls into the product."
            }
        ]
    }
}


def calculate_score(dimensions):
    total = sum(
        dimension["score"]
        for dimension in dimensions.values()
    )

    return round(total / len(dimensions), 2)


def determine_status(gates):

    critical_gates = [
        gate
        for gate in gates.values()
        if gate["critical"]
    ]

    if not all(gate["status"] for gate in critical_gates):
        return "NEEDS WORK"

    return "READY"


def assess_market(market_id):

    if market_id not in MARKETS:
        return None

    market = MARKETS[market_id]

    overall_score = calculate_score(market["dimensions"])

    status = determine_status(market["gates"])

    return {
        "market": market["name"],
        "overall_score": overall_score,
        "status": status,
        "dimensions": market["dimensions"],
        "entry_approach": market["entry_approach"],
        "adjustments": market["adjustments"],
        "risks": market["risks"],
        "gates": market["gates"]
    }
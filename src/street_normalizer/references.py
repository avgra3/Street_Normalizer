# Street abbreviations
street_abbreviations = {
    # Spanish Prefixes: Appendix H
    "AVE": "AVENIDA",
    "CLL": "CALLE",
    "CMT": "CAMINITO",
    "CAM": "CAMINO",
    "CER": "CERRADA",
    "CIR": "CIRCULO",
    "ENT": "ENTRADA",
    "PSO": "PASEO",
    "PLA": "PLACITA",
    "RCH": "RANCHO",
    "VER": "VEREDA",
    "VIS": "VISTA",
}

# Commonly Used street suffixes to standardized abbreviation
# Comes from Appendix C, Section C1
normalized_street_suffixes = {
    'ALY': ['ALLEE', 'ALLEY', 'ALLY', 'ALY'],
    'ANX': ['ANEX', 'ANNEX', 'ANNX', 'ANX'],
    'ARC': ['ARC ', 'ARCADE '],
    'AVE': ['AV', 'AVE', 'AVEN', 'AVENU', 'AVENUE', 'AVN', 'AVNUE'],
    'BYU': ['BAYOO', 'BAYOU'],
    'BCH': ['BCH', 'BEACH'],
    'BND': ['BEND', 'BND'],
    'BLF': ['BLF', 'BLUF', 'BLUFF'],
    'BLFS': ['BLUFFS '],
    'BTM': ['BOT', 'BTM', 'BOTTM', 'BOTTOM'],
    'BLVD': ['BLVD', 'BOUL', 'BOULEVARD ', 'BOULV'],
    'BR': ['BR', 'BRNCH', 'BRANCH'],
    'BRG': ['BRDGE', 'BRG', 'BRIDGE'],
    'BRK': ['BRK', 'BROOK'],
    'BRKS': ['BROOKS '],
    'BG': ['BURG'],
    'BGS': ['BURGS'],
    'BYP': ['BYP', 'BYPA', 'BYPAS', 'BYPASS', 'BYPS'],
    'CP': ['CAMP', 'CP', 'CMP'],
    'CYN': ['CANYN', 'CANYON', 'CNYN'],
    'CPE': ['CAPE', 'CPE'],
    'CSWY': ['CAUSEWAY', 'CAUSWA', 'CSWY'],
    'CTR': ['CEN', 'CENT', 'CENTER', 'CENTR', 'CENTRE', 'CNTER', 'CNTR', 'CTR'],
    'CTRS': ['CENTERS '],
    'CIR': ['CIR', 'CIRC', 'CIRCL', 'CIRCLE', 'CRCL', 'CRCLE'],
    'CIRS': ['CIRCLES'],
    'CLF': ['CLF', 'CLIFF'],
    'CLFS': ['CLFS', 'CLIFFS'],
    'CLB': ['CLB', 'CLUB'],
    'CMN': ['COMMON'],
    'CMNS': ['COMMONS'],
    'COR': ['COR', 'CORNER'],
    'CORS': ['CORNERS', 'CORS'],
    'CRSE': ['COURSE', 'CRSE'],
    'CT': ['COURT', 'CT'],
    'CTS': ['COURTS', 'CTS'],
    'CV': ['COVE', 'CV'],
    'CVS': ['COVES'],
    'CRK': ['CREEK', 'CRK'],
    'CRES': ['CRESCENT', 'CRES', 'CRSENT', 'CRSNT'],
    'CRST': ['CREST'],
    'XING': ['CROSSING', 'CRSSNG', 'XING'],
    'XRD': ['CROSSROAD'],
    'XRDS': ['CROSSROADS'],
    'CURV': ['CURVE '],
    'DL': ['DALE ', 'DL '],
    'DM': ['DAM ', 'DM '],
    'DV': ['DIV', 'DIVIDE', 'DV', 'DVD'],
    'DR': ['DR', 'DRIV', 'DRIVE', 'DRV'],
    'DRS': ['DRIVES', 'EST', 'ESTATE', 'ESTATES'],
    'EST': ['EST', 'ESTATE'],
    'ESTS': ['ESTATES', 'ESTS'],
    'EXPY': ['EXP', 'EXPR', 'EXPRESS', 'EXPRESSWAY', 'EXPW', 'EXPY'],
    'EXT': ['EXT', 'EXTENSION', 'EXTN', 'EXTNSN'],
    'EXTS': ['EXTS'],
    'FALL': ['FALL'],
    'FLS': ['FALLS', 'FLS'],
    'FRY': ['FERRY', 'FRRY', 'FRY'],
    'FLD': ['FIELD', 'FLD'],
    'FLDS': ['FIELDS', 'FLDS'],
    'FLT': ['FLAT', 'FLT'],
    'FLTS': ['FLATS', 'FLTS'],
    'FRD': ['FORD', 'FRD'],
    'FRDS': ['FORDS'],
    'FRST': ['FOREST', 'FORESTS', 'FRST'],
    'FRG': ['FORG', 'FORGE', 'FRG'],
    'FRGS': ['FORGES'],
    'FRK': ['FORK', 'FRK'],
    'FRKS': ['FORKS', 'FRKS'],
    'FT': ['FORT', 'FRT', 'FT'],
    'FWY': ['FREEWAY', 'FREEWY', 'FRWAY', 'FRWY', 'FWY'],
    'GDN': ['GARDEN', 'GARDN', 'GRDEN', 'GRDN'],
    'GDNS': ['GARDENS', 'GDNS', 'GRDNS'],
    'GTWY': ['GATEWAY', 'GATEWY', 'GATWAY', 'GTWAY', 'GTWY'],
    'GLN': ['GLEN', 'GLN'],
    'GLNS': ['GLENS'],
    'GRN': ['GREEN', 'GRN'],
    'GRNS': ['GREENS'],
    'GRV': ['GROV', 'GROVE', 'GRV'],
    'GRVS': ['GROVES'],
    'HBR': ['HARB', 'HARBOR', 'HARBR', 'HBR', 'HRBOR'],
    'HBRS': ['HARBORS'],
    'HVN': ['HAVEN', 'HVN'],
    'HTS': ['HT', 'HTS'],
    'HWY': ['HIGHWAY', 'HIGHWY', 'HIWAY', 'HIWY', 'HWAY', 'HWY'],
    'HL': ['HILL', 'HL'],
    'HLS': ['HILLS', 'HLS'],
    'HOLW': ['HLLW', 'HOLLOW', 'HOLLOWS', 'HOLW', 'HOLWS'],
    'INLT': ['INLT'],
    'IS': ['IS', 'ISLAND', 'ISLND'],
    'ISS': ['ISLANDS', 'ISLNDS', 'ISS'],
    'ISLE': ['ISLE', 'ISLES'],
    'JCT': ['JCT', 'JCTION', 'JCTN', 'JUNCTION', 'JUNCTN', 'JUNCTON'],
    'JCTS': ['JCTNS', 'JCTS', 'JUNCTIONS'],
    'KY': ['KEY', 'KY'],
    'KYS': ['KEYS', 'KYS'],
    'KNL ': ['KNL', 'KNOL', 'KNOLL'],
    'KNLS': ['KNLS', 'KNOLLS'],
    'LK': ['LK', 'LAKE'],
    'LKS': ['LKS', 'LAKES'],
    'LAND': ['LAND'],
    'LNDG': ['LANDING', 'LNDG', 'LNDNG'],
    'LN': ['LANE', 'LN'],
    'LGT': ['LGT', 'LIGHT'],
    'LGTS': ['LIGHTS'],
    'LF': ['LF', 'LOAF'],
    'LCK': ['LCK', 'LOCK'],
    'LCKS': ['LCKS', 'LOCKS'],
    'LDG': ['LDG', 'LDGE', 'LODG', 'LODGE'],
    'LOOP': ['LOOP', 'LOOPS'],
    'MALL': ['MALL'],
    'MNR': ['MNR', 'MANOR'],
    'MNRS': ['MANORS', 'MNRS'],
    'MDW': ['MEADOW'],
    'MDWS': ['MDW', 'MDWS', 'MEADOWS', 'MEDOWS'],
    'MEWS': ['MEWS'],
    'ML': ['MILL'],
    'MLS': ['MILLS'],
    'MSN': ['MISSN', 'MSSN'],
    'MTWY': ['MOTORWAY'],
    'MT': ['MNT', 'MT'],
    'MTN': ['MNTAIN', 'MNTN', 'MOUNTAIN', 'MOUNTIN', 'MTIN', 'MTN'],
    'MTNS': ['MNTNS', 'MOUNTAINS'],
    'NCK': ['NCK', 'NECK'],
    'ORCH': ['ORCH', 'ORCHARD', 'ORCHRD'],
    'OVAL': ['OVAL', 'OVL'],
    'OPAS': ['OVERPASS'],
    'PARK': ['PARK', 'PRK', 'PARKS'],
    'PKWY': ['PARKWAY', 'PARKWY', 'PKWAY', 'PKWY', 'PKY', 'PARKWAYS', 'PKWYS'],
    'PASS': ['PASS'],
    'PSGE': ['PASSAGE'],
    'PATH': ['PATH', 'PATHS'],
    'PIKE': ['PIKE', 'PIKES'],
    'PNE ': ['PINE'],
    'PNES': ['PINES', 'PNES'],
    'PL': ['PL'],
    'PLN': ['PLAIN', 'PLN'],
    'PLNS': ['PLAINS', 'PLNS'],
    'PLZ': ['PLAZA', 'PLZ', 'PLZA'],
    'PT': ['POINT', 'PT'],
    'PTS': ['POINTS', 'PTS'],
    'PRT': ['PORT', 'PRT'],
    'PRTS': ['PORTS', 'PRTS'],
    'PR': ['PR', 'PRAIRIE', 'PRR'],
    'RADL': ['RAD', 'RADIAL', 'RADIEL', 'RADL'],
    'RAMP': ['RAMP'],
    'RNCH': ['RANCH', 'RANCHES', 'RNCH', 'RNCHS'],
    'RPD': ['RAPID', 'RPD'],
    'RPDS': ['RAPIDS', 'RPDS'],
    'RST': ['REST', 'RST'],
    'RDG': ['RDG', 'RDGE', 'RIDGE'],
    'RDGS': ['RDGS', 'RIDGES'],
    'RIV': ['RIV', 'RIVER', 'RVR', 'RIVR'],
    'RD': ['RD', 'ROAD'],
    'RDS': ['ROADS', 'RDS'],
    'RTE': ['ROUTE'],
    'ROW': ['ROW'],
    'RUE': ['RUE'],
    'RUN': ['RUN'],
    'SHL': ['SHL', 'SHOAL'],
    'SHLS': ['SHLS', 'SHOALS'],
    'SHR': ['SHOAR', 'SHORE', 'SHR'],
    'SHRS': ['SHOARS', 'SHORES', 'SHRS'],
    'SKWY': ['SKYWAY'],
    'SPG': ['SPG', 'SPNG', 'SPRING', 'SPRNG'],
    'SPGS': ['SPGS', 'SPNGS', 'SPRINGS', 'SPRNGS'],
    'SPUR': ['SPUR', 'SPURS'],
    'SQ': ['SQ', 'SQR', 'SQRE', 'SQU', 'SQUARE'],
    'SQS': ['SQRS', 'SQUARES'],
    'STA': ['STA', 'STATION', 'STATN', 'STN'],
    'STRA': ['STRA', 'STRAV', 'STRAVEN', 'STRAVENUE', 'STRAVN', 'STRVN', 'STRVNUE'],
    'STRM': ['STREAM', 'STREME', 'STRM'],
    'ST': ['STREET', 'STRT', 'ST', 'STR'],
    'STS': ['STREETS'],
    'SMT': ['SMT', 'SUMIT', 'SUMITT', 'SUMMIT'],
    'TER': ['TER', 'TERR', 'TERRACE'],
    'TRWY': ['THROUGHWAY'],
    'TRCE': ['TRACE', 'TRACES', 'TRCE'],
    'TRAK': ['TRACK', 'TRACKS', 'TRAK', 'TRK', 'TRKS'],
    'TRFY': ['TRAFFICWAY'],
    'TRL': ['TRAIL', 'TRAILS', 'TRL', 'TRLS'],
    'TRLR': ['TRAILER', 'TRLR', 'TRLRS'],
    'TUNL': ['TUNEL', 'TUNL', 'TUNLS', 'TUNNEL', 'TUNNELS', 'TUNNL'],
    'TPKE': ['TRNPK', 'TURNPIKE', 'TURNPK'],
    'UPAS': ['UNDERPASS', 'UN'],
    'UN': ['UN', 'UNION'],
    'UNS': ['UNIONS'],
    'VLY': ['VALLEY', 'VALLY', 'VLLY', 'VLY'],
    'VLYS': ['VALLEYS', 'VLYS'],
    'VIA': ['VDCT', 'VIA', 'VIADCT', 'VIADUCT'],
    'VW': ['VIEW', 'VW'],
    'VWS': ['VIEWS', 'VWS'],
    'VLG': ['VILL', 'VILLAG', 'VILLAGE', 'VILLG', 'VILLIAGE', 'VLG'],
    'VLGS': ['VILLAGES', 'VLGS'],
    'VL': ['VILLE', 'VL'],
    'VIS': ['VIS', 'VIST', 'VISTA', 'VST', 'VSTA'],
    'WALK': ['WALK', 'WALKS'],
    'WALL': ['WALL'],
    'WAY': ['WY', 'WAY'],
    'WAYS': ['WAYS'],
    'WL ': ['WELL'],
    'WLS': ['WELLS', 'WLS'],
}

# Unit Designators
# Comes from USPS Appendix C, Section C2
unit_designators = {
    'APARTMENT': 'APT',
    'BASEMENT': 'BSMT',
    'BUILDING': 'BLDG',
    'DEPARTMENT': 'DEPT',
    'FLOOR': 'FL',
    'FRONT': 'FRNT',
    'HANGER': 'HNGR',
    'KEY': 'KEY',
    'LOBBY': 'LBBY',
    'LOT': 'LOT',
    'LOWER': 'LOWR',
    'OFFICE': 'OFC',
    'PENTHOUSE': 'PH',
    'PIER': 'PIER',
    'REAR': 'REAR',
    'ROOM': 'RM',
    'SIDE': 'SIDE',
    'SLIP': 'SLIP',
    'SPACE': 'SPC',
    'STOP': 'STOP',
    'SUITE': 'STE',
    'TRAILER': 'TRLR',
    'UNIT': 'UNIT',
    'UPPER': 'UPPR',
}

# Extraneous Characters to remove
chars_to_remove = [".", ",", ";", ":", "  ", "-", "~"]

# Normalize Names
names = {
    "LLC": "",
    "CENTER": "CTR",
    "AMBULATORY SURGERY CENTERS": "ASC",
    "AMBULATORY SURGERY CTR": "ASC",
    "AMBULATORY SURGERY": "ASC",
    "AMB SURG CTR": "ASC",
    "BEHAVIORIAL HEALTH SYSTEM": "BHS",
    "SURGICAL": "SURG",
    "HOSPITAL": "HOSP",
    "REHABILITATION": "REHAB",
    "SERVICES": "SVC",
    "SERVICE": "SVC",
    "MOUNTAIN": "MTN",
    "MOUNTAINS": "MTN",
    "  ": " "
}

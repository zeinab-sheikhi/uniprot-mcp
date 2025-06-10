from enum import Enum
from typing import Any, List

from pydantic import BaseModel


class DeletedReasonEnum(str, Enum):
    EMPTY = ""
    EMBL = "Deleted from sequence source (EMBL)"
    TAIR = "Deleted from sequence source (TAIR)"
    SGD = "Deleted from sequence source (SGD)"
    ENSEMBL = "Deleted from sequence source (ENSEMBL)"
    PDB = "Deleted from sequence source (PDB)"
    REFSEQ = "Deleted from sequence source (RefSeq)"
    SWISSPROT = "Deleted from Swiss-Prot"
    REDUNDANT_SEQUENCE = "Redundant sequence"
    REDUNDANT_PROTEOME = "Redundant proteome"
    EXCLUDED_PROTEOME = "Excluded proteome"
    OVERREPRESENTED_SEQUENCE = "Over-represented sequence"


class InactiveReasonTypeEnum(str, Enum):
    DELETED = "DELETED"
    MERGED = "MERGED"
    DEMERGED = "DEMERGED"


class EntryTypeEnum(str, Enum):
    SWISSPROT = "UniProtKB reviewed (Swiss-Prot)"
    TREMBL = "UniProtKB unreviewed (TrEMBL)"
    INACTIVE = "Inactive"
    UNKNOWN = "UNKNOWN"


class GeneEncodingTypeEnum(str, Enum):
    UNKNOWN = "unknown"
    HYDROGENOSOME = "Hydrogenosome"
    MITOCHONDRION = "Mitochondrion"
    NUCLEOMORPH = "Nucleomorph"
    PLASMID = "Plasmid"
    PLASTID = "Plastid"
    APICOPLAST = "Apicoplast"
    CHLOROPLAST = "Chloroplast"
    CYANELLE = "Cyanelle"
    NON_PHOTOSYNTHETIC_PLASTID = "Non-photosynthetic plastid"
    ORGANELLAR_CHROMATOPHORE = "Organellar chromatophore"


class KeywordCategoryEnum(str, Enum):
    BIOLOGICAL_PROCESS = "Biological process"
    CELLULAR_COMPONENT = "Cellular component"
    CODING_SEQUENCE_DIVERSITY = "Coding sequence diversity"
    DEVELOPMENTAL_STAGE = "Developmental stage"
    DISEASE = "Disease"
    DOMAIN = "Domain"
    LIGAND = "Ligand"
    MOLECULAR_FUNCTION = "Molecular function"
    PTM = "PTM"
    TECHNICAL_TERM = "Technical term"
    UNKNOWN = "Unknown"


class InternalLineTypeEnum(str, Enum):
    CL = "CL"
    CP = "CP"
    CX = "CX"
    DR = "DR"
    DG = "DG"
    GO = "GO"
    EV = "EV"
    HA = "HA"
    HR = "HR"
    HW = "HW"
    HU = "HU"
    HP = "HP"
    ID = "ID"
    IS = "IS"
    NI = "NI"
    PM = "PM"
    SO = "SO"
    YY = "YY"
    ZA = "ZA"
    ZB = "ZB"
    ZC = "ZC"
    ZR = "ZR"
    ZZ = "ZZ"
    ET = "ET"
    PE = "PE"
    RU = "RU"
    TX = "TX"
    PROSITE = "PROSITE"
    UP = "UP"
    ZD = "ZD"


class TaxonomyRankEnum(str, Enum):
    STRAIN = "strain"
    SEROTYPE = "serotype"
    SERIES = "series"
    MORPH = "morph"
    BIOTYPE = "biotype"
    CLADE = "clade"
    GENOTYPE = "genotype"
    ISOLATE = "isolate"
    FORMA_SPECIALIS = "forma specialis"
    PATHOGROUP = "pathogroup"
    SEROGROUP = "serogroup"
    SECTION = "section"
    SUBSECTION = "subsection"
    FORMA = "forma"
    VARIETAS = "varietas"
    SUBSPECIES = "subspecies"
    SPECIES = "species"
    SPECIES_SUBGROUP = "species subgroup"
    SPECIES_GROUP = "species group"
    SUBGENUS = "subgenus"
    GENUS = "genus"
    SUBTRIBE = "subtribe"
    TRIBE = "tribe"
    SUBFAMILY = "subfamily"
    FAMILY = "family"
    SUPERFAMILY = "superfamily"
    PARVORDER = "parvorder"
    INFRAORDER = "infraorder"
    SUBORDER = "suborder"
    ORDER = "order"
    SUPERORDER = "superorder"
    SUBCOHORT = "subcohort"
    COHORT = "cohort"
    INFRACLASS = "infraclass"
    SUBCLASS = "subclass"
    CLASS = "class"
    SUPERCLASS = "superclass"
    SUBPHYLUM = "subphylum"
    PHYLUM = "phylum"
    SUPERPHYLUM = "superphylum"
    SUBKINGDOM = "subkingdom"
    KINGDOM = "kingdom"
    SUPERKINGDOM = "superkingdom"
    NO_RANK = "no rank"


class ProteinExistenceEnum(str, Enum):
    EVIDENCE_AT_PROTEIN_LEVEL = "1: Evidence at protein level"
    EVIDENCE_AT_TRANSCRIPT_LEVEL = "2: Evidence at transcript level"
    INFERRED_FROM_HOMOLOGY = "3: Inferred from homology"
    PREDICTED = "4: Predicted"
    UNCERTAIN = "5: Uncertain"
    UNKNOWN = "UNKNOWN"


class ReferenceCommentTypeEnum(str, Enum):
    STRAIN = "STRAIN"
    PLASMID = "PLASMID"
    TRANSPOSON = "TRANSPOSON"
    TISSUE = "TISSUE"


class CrossReferenceCitationDatabaseEnum(str, Enum):
    PUBMED = "PubMed"
    DOI = "DOI"
    AGRICOLA = "AGRICOLA"


class CitationTypeEnum(str, Enum):
    JOURNAL_ARTICLE = "journal article"
    BOOK = "book"
    ONLINE_JOURNAL_ARTICLE = "online journal article"
    PATENT = "patent"
    SUBMISSION = "submission"
    THESIS = "thesis"
    UNIPROT_INDEXED_LITERATURES = "UniProt indexed literatures"
    UNPUBLISHED_OBSERVATIONS = "unpublished observations"


class SubmissionDatabaseEnum(str, Enum):
    PDB = "PDB data bank"
    PIR = "PIR data bank"
    SWISSPROT = "Swiss-Prot"
    UNIPROTKB = "UniProtKB"
    EMBL_GENBANK_DDBJ = "EMBL/GenBank/DDBJ databases"


class PositionModifierEnum(str, Enum):
    EXACT = "EXACT"
    OUTSIDE = "OUTSIDE"
    UNKNOWN = "UNKNOWN"
    UNSURE = "UNSURE"


class CommentEventEnum(str, Enum):
    ALTERNATIVE_PROMOTER_USAGE = "Alternative promoter usage"
    ALTERNATIVE_SPLICING = "Alternative splicing"
    ALTERNATIVE_INITIATION = "Alternative initiation"
    RIBOSOMAL_FRAMESHIFTING = "Ribosomal frameshifting"


class IsoformSequenceStatusEnum(str, Enum):
    DISPLAYED = "Displayed"
    EXTERNAL = "External"
    NOT_DESCRIBED = "Not described"
    DESCRIBED = "Described"


class DirectionTypeEnum(str, Enum):
    LEFT_TO_RIGHT = "left-to-right"
    RIGHT_TO_LEFT = "right-to-left"


class ReactionDatabaseEnum(str, Enum):
    CHEBI = "ChEBI"
    RHEA = "Rhea"


class CofactorDatabaseEnum(str, Enum):
    CHEBI = "ChEBI"


class MethodEnum(str, Enum):
    ELECTROSPRAY = "Electrospray"
    FAB = "FAB"
    LSI = "LSI"
    MALDI = "MALDI"
    PLASMA_DESORPTION = "Plasma desorption"
    SELDI = "SELDI"
    API = "API"
    UNKNOWN = "Unknown"


class LocationTypeEnum(str, Enum):
    NOT_APPLICABLE = "Not_applicable"
    UNDETERMINED = "Undetermined"
    UNKNOWN = "Unknown"
    KNOWN = "Known"


class SequenceCautionTypeEnum(str, Enum):
    FRAMESHIFT = "Frameshift"
    ERRONEOUS_INITIATION = "Erroneous initiation"
    ERRONEOUS_TERMINATION = "Erroneous termination"
    ERRONEOUS_GENE_MODEL_PREDICTION = "Erroneous gene model prediction"
    ERRONEOUS_TRANSLATION = "Erroneous translation"
    MISCELLANEOUS_DISCREPANCY = "Miscellaneous discrepancy"
    UNKNOWN = "unknown"


class CommentTypeEnum(str, Enum):
    FUNCTION = "FUNCTION"
    CATALYTIC_ACTIVITY = "CATALYTIC ACTIVITY"
    COFACTOR = "COFACTOR"
    ACTIVITY_REGULATION = "ACTIVITY REGULATION"
    BIOPHYSICOCHEMICAL_PROPERTIES = "BIOPHYSICOCHEMICAL PROPERTIES"
    PATHWAY = "PATHWAY"
    SUBUNIT = "SUBUNIT"
    INTERACTION = "INTERACTION"
    SUBCELLULAR_LOCATION = "SUBCELLULAR LOCATION"
    ALTERNATIVE_PRODUCTS = "ALTERNATIVE PRODUCTS"
    TISSUE_SPECIFICITY = "TISSUE SPECIFICITY"
    DEVELOPMENTAL_STAGE = "DEVELOPMENTAL STAGE"
    INDUCTION = "INDUCTION"
    DOMAIN = "DOMAIN"
    PTM = "PTM"
    RNA_EDITING = "RNA EDITING"
    MASS_SPECTROMETRY = "MASS SPECTROMETRY"
    POLYMORPHISM = "POLYMORPHISM"
    DISEASE = "DISEASE"
    DISRUPTION_PHENOTYPE = "DISRUPTION PHENOTYPE"
    ALLERGEN = "ALLERGEN"
    TOXIC_DOSE = "TOXIC DOSE"
    BIOTECHNOLOGY = "BIOTECHNOLOGY"
    PHARMACEUTICAL = "PHARMACEUTICAL"
    MISCELLANEOUS = "MISCELLANEOUS"
    SIMILARITY = "SIMILARITY"
    CAUTION = "CAUTION"
    SEQUENCE_CAUTION = "SEQUENCE CAUTION"
    WEB_RESOURCE = "WEB RESOURCE"
    UNKNOWN = "UNKOWN"


class Evidence(BaseModel):
    evidenceCode: str | None = None
    id: str | None = None
    source: str | None = None


class Property(BaseModel):
    key: str | None = None
    value: str | None = None


class ReferenceComment(BaseModel):
    type: ReferenceCommentTypeEnum | None = None
    value: str | None = None
    evidences: List[Evidence] | None = None


class CrossReferenceCitationDatabase(BaseModel):
    properties: List[Property] | None = None
    id: str | None = None
    database: CrossReferenceCitationDatabaseEnum | None = None


class EntryInactiveReason(BaseModel):
    deletedReason: DeletedReasonEnum | None = None
    inactiveReasonType: InactiveReasonTypeEnum | None = None
    mergeDemergeTos: List[str] | None = None


class ExtraAttributes(BaseModel):
    uniParcId: str | None = None


class AlternativeSequence(BaseModel):
    alternativeSequences: List[str] | None = None
    originalSequence: str | None = None


class Ligand(BaseModel):
    name: str | None = None
    id: str | None = None
    note: str | None = None
    label: str | None = None


class LigandPart(BaseModel):
    name: str | None = None
    id: str | None = None
    note: str | None = None
    label: str | None = None


class Position(BaseModel):
    value: int | None = None
    modifier: PositionModifierEnum | None = None


class FeatureLocation(BaseModel):
    start: Position | None = None
    end: Position | None = None
    sequence: str | None = None


class CrossReferenceUniprotKBFeatureDatabase(BaseModel):
    properties: List[Property] | None = None
    id: str | None = None
    database: str | None = None  # Enum: dbSNP, ChEBI


class UniProtKBFeature(BaseModel):
    alternativeSequence: AlternativeSequence | None = None
    ligand: Ligand | None = None
    ligandPart: LigandPart | None = None
    featureId: str | None = None
    location: FeatureLocation | None = None
    type: str  # Enum: 39 possible values
    featureCrossReferences: List[CrossReferenceUniprotKBFeatureDatabase] | None = None
    description: str | None = None
    evidences: List[Evidence] | None = None


class EntryAudit(BaseModel):
    lastAnnotationUpdateDate: str | None = None
    lastSequenceUpdateDate: str | None = None
    firstPublicDate: str | None = None
    sequenceVersion: int | None = None
    entryVersion: int | None = None


class Name(BaseModel):
    value: str
    evidence: List[int] | None = None


class EC(BaseModel):
    valid: bool | None = None
    value: str | None = None
    evidences: List[Evidence] | None = None


class ProteinName(BaseModel):
    shortNames: List[Name] | None = None
    fullName: Name | None = None
    valid: List[bool] | None = None
    ecNumbers: List[EC] | None = None


class ProteinSubName(BaseModel):
    fullName: Name | None = None
    valid: bool | None = None
    ecNumbers: List[EC] | None = None


class ProteinSection(BaseModel):
    recommendedName: ProteinName | None = None
    allergenName: Name | None = None
    biotechName: Name | None = None
    alternativeNames: List[ProteinName] | None = None
    cdAntigenNames: List[Name] | None = None
    innNames: List[Name] | None = None


class ProteinDescription(BaseModel):
    recommendedName: ProteinName | None = None
    submissionNames: List[ProteinSubName] | None = None
    includes: List[ProteinSection] | None = None
    allergenName: Name | None = None
    biotechName: Name | None = None
    alternativeNames: List[ProteinName] | None = None
    cdAntigenNames: List[Name] | None = None
    innNames: List[Name] | None = None
    contains: List[ProteinSection] | None = None
    flag: str | None = None


class UniProtKBCrossReference(BaseModel):
    isoformId: str | None = None
    properties: List[Property] | None = None
    id: str | None = None
    database: str | None = None
    evidences: List[Evidence] | None = None


class OrganismHost(BaseModel):
    taxonId: int | None = None
    commonName: str | None = None
    scientificName: str | None = None
    synonyms: List[str] | None = None


class GeneName(BaseModel):
    value: str | None = None
    evidences: List[Evidence] | None = None


class ORFName(BaseModel):
    value: str | None = None
    evidences: List[Evidence] | None = None


class OrderedLocusName(BaseModel):
    value: str | None = None
    evidences: List[Evidence] | None = None


class GeneNameSynonym(BaseModel):
    value: str | None = None
    evidences: List[Evidence] | None = None


class Gene(BaseModel):
    geneName: GeneName | None = None
    orfNames: List[ORFName] | None = None
    orderedLocusNames: List[OrderedLocusName] | None = None
    synonyms: List[GeneNameSynonym] | None = None


class EvidencedValue(BaseModel):
    value: str | None = None
    evidences: List[Evidence] | None = None


class Note(BaseModel):
    valid: bool | None = None
    texts: List[EvidencedValue] | None = None


class IsoformName(BaseModel):
    value: str | None = None
    evidences: List[Evidence] | None = None


class APIsoform(BaseModel):
    name: IsoformName | None = None
    isoformIds: List[str] | None = None
    isoformSequenceStatus: IsoformSequenceStatusEnum | None = None
    sequenceIds: List[str] | None = None
    note: Note | None = None
    synonyms: List[IsoformName] | None = None


class CrossReferenceReactionDatabase(BaseModel):
    properties: List[Property] | None = None
    id: str | None = None
    database: ReactionDatabaseEnum | None = None


class PhysiologicalReaction(BaseModel):
    reactionCrossReference: CrossReferenceReactionDatabase | None = None
    directionType: DirectionTypeEnum | None = None
    evidences: List["Evidence"] | None = None


class KineticParameters(BaseModel):
    maximumVelocities: List[Any] | None = None  # Define as needed
    michaelisConstants: List[Any] | None = None  # Define as needed
    note: Note | None = None


class TemperatureDependence(BaseModel):
    texts: List[EvidencedValue] | None = None


class Absorption(BaseModel):
    max: List[Any] | None = None  # Define as needed
    approximate: bool | None = None
    note: Note | None = None
    evidences: List[Evidence] | None = None


class PhDependence(BaseModel):
    texts: List[EvidencedValue] | None = None


class RedoxPotential(BaseModel):
    texts: List[EvidencedValue] | None = None


class SubcellularLocationValue(BaseModel):
    id: str | None = None
    value: str | None = None
    evidences: List[Evidence] | None = None


class SubcellularLocation(BaseModel):
    location: SubcellularLocationValue | None = None
    orientation: SubcellularLocationValue | None = None
    topology: SubcellularLocationValue | None = None


class RnaEdPosition(BaseModel):
    position: str | None = None
    evidences: List[Evidence] | None = None


class Disease(BaseModel):
    diseaseId: str | None = None
    diseaseAccession: str | None = None
    diseaseCrossReference: Any | None = None  # Define as needed
    acronym: str | None = None
    description: str | None = None
    evidences: List[Evidence] | None = None


class Interactant(BaseModel):
    chainId: str | None = None
    intActId: str | None = None
    geneName: str | None = None
    uniProtKBAccession: str | None = None


class Interaction(BaseModel):
    numberOfExperiments: int | None = None
    interactantOne: Interactant | None = None
    organismDiffer: bool | None = None
    interactantTwo: Interactant | None = None


class Reaction(BaseModel):
    name: str | None = None
    ecNumber: str | None = None
    reactionCrossReferences: List[CrossReferenceReactionDatabase] | None = None
    evidences: List["Evidence"] | None = None


class CrossReferenceCofactorDatabase(BaseModel):
    properties: List["Property"] | None = None
    id: str | None = None
    database: CofactorDatabaseEnum | None = None


class Cofactor(BaseModel):
    name: str | None = None
    cofactorCrossReference: CrossReferenceCofactorDatabase | None = None
    evidences: List["Evidence"] | None = None


class Comment(BaseModel):
    events: List[CommentEventEnum] | None = None
    isoforms: List[APIsoform] | None = None
    note: Note | str | None = None
    kineticParameters: KineticParameters | None = None
    temperatureDependence: TemperatureDependence | None = None
    absorption: Absorption | None = None
    phDependence: PhDependence | None = None
    redoxPotential: RedoxPotential | None = None
    molecule: str | None = None
    physiologicalReactions: List[PhysiologicalReaction] | None = None
    reaction: Reaction | None = None
    valid: bool | None = None
    cofactors: List[Cofactor] | None = None
    disease: Disease | None = None
    texts: List[EvidencedValue] | None = None
    interactions: List[Interaction] | None = None
    method: MethodEnum | None = None
    molWeight: float | None = None
    molWeightError: float | None = None
    evidences: List[Evidence] | None = None
    locationType: LocationTypeEnum | None = None
    positions: List[RnaEdPosition] | None = None
    sequenceCautionType: SequenceCautionTypeEnum | None = None
    sequence: str | None = None
    subcellularLocations: List[SubcellularLocation] | None = None
    resourceUrl: str | None = None
    ftp: bool | None = None
    resourceName: str | None = None
    commentType: CommentTypeEnum | None = None


class GeneLocation(BaseModel):
    geneEncodingType: GeneEncodingTypeEnum | None = None
    value: str | None = None
    evidences: List[Evidence] | None = None


class Keyword(BaseModel):
    category: KeywordCategoryEnum | None = None
    name: str | None = None
    id: str | None = None
    evidences: List[Evidence] | None = None


class Sequence(BaseModel):
    type: str | None = None
    ref: str | None = None


class InternalLine(BaseModel):
    type: InternalLineTypeEnum | None = None
    value: str | None = None


class SourceLine(BaseModel):
    value: str | None = None


class EvidenceLine(BaseModel):
    evidence: str | None = None
    createDate: str | None = None
    curator: str | None = None


class InternalSection(BaseModel):
    internalLines: List[InternalLine] | None = None
    sourceLines: List[SourceLine] | None = None
    evidenceLines: List[EvidenceLine] | None = None


class TaxonomyLineage(BaseModel):
    hidden: bool | None = None
    taxonId: int | None = None
    rank: TaxonomyRankEnum | None = None
    commonName: str | None = None
    scientificName: str | None = None
    synonyms: List[str] | None = None


class Organism(BaseModel):
    taxonId: int | None = None
    lineages: List[str] | None = None
    commonName: str | None = None
    scientificName: str | None = None
    synonyms: List[str] | None = None
    evidences: List[Evidence] | None = None


class Citation(BaseModel):
    address: str | None = None
    bookName: str | None = None
    editors: List[str] | None = None
    firstPage: str | None = None
    lastPage: str | None = None
    volume: str | None = None
    publisher: str | None = None
    id: str | None = None
    citationCrossReferences: List[CrossReferenceCitationDatabase] | None = None
    authoringGroups: List[str] | None = None
    authors: List[str] | None = None
    publicationDate: str | None = None
    title: str | None = None
    journal: str | None = None
    locator: str | None = None
    doiId: str | None = None
    pubmedId: int | None = None
    completeAuthorList: bool | None = None
    literatureAbstract: str | None = None
    patentNumber: str | None = None
    submissionDatabase: SubmissionDatabaseEnum | None = None
    institute: str | None = None
    citationType: CitationTypeEnum | None = None


class UniProtKBReference(BaseModel):
    referenceComments: List[ReferenceComment] | None = None
    referencePositions: List[str] | None = None
    referenceNumber: int | None = None
    citation: Citation | None = None
    evidences: List[Evidence] | None = None


class UniProtKBEntry(BaseModel):
    active: bool | None = None
    extraAttributes: Any | None = None
    features: List[UniProtKBFeature] | None = None
    primaryAccession: str
    inactiveReason: EntryInactiveReason | None = None
    annotationScore: float | None = None
    entryAudit: EntryAudit | None = None
    entryType: EntryTypeEnum | None = None
    secondaryAccessions: List[str] | None = None
    proteinDescription: ProteinDescription | None = None
    uniProtKBCrossReferences: List[UniProtKBCrossReference] | None = None
    organismHosts: List[OrganismHost] | None = None
    genes: List[Gene] | None = None
    comments: List[Comment] | None = None
    geneLocations: List[GeneLocation] | None = None
    keywords: List[Keyword] | None = None
    sequence: Sequence | None = None
    internalSection: InternalSection | None = None
    fragment: bool | None = None
    lineages: List[TaxonomyLineage] | None = None
    organism: Organism | None = None
    proteinExistence: ProteinExistenceEnum | None = None
    uniProtkbId: str | None = None
    references: List[UniProtKBReference] | None = None


class UniProtSearchResponse(BaseModel):
    results: List[UniProtKBEntry]

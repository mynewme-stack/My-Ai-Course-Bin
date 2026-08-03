FDA AI Medical Devices: Authorizations & Recalls
1,524 U.S. AI-enabled device authorizations linked to 313 exact FDA recall recor

About Dataset
FDA AI Medical Devices: Authorizations & Recalls
Overview
1,524 devices from FDA's AI-enabled medical-device list, enriched with authorization details, product classifications, and 313 exact submission-linked recall records.

This snapshot connects premarket and postmarket regulatory data without fuzzy company or device-name matching. Every recall row carries the exact FDA submission number that appears in the source recall record, making the join auditable.

Snapshot date: July 31, 2026 UTC. Coverage: final decisions from September 29, 1995 through March 30, 2026.

Motivation
FDA's downloadable AI device list is valuable but compact: decision date, submission number, device, company, lead panel, and product code. Researchers often need several separate FDA databases to answer the next questions:

Which pathways authorize AI-enabled devices?
How quickly has the listed landscape grown?
Which specialties and product classifications dominate?
How long is the observed span from receipt to decision?
Which authorization numbers appear in FDA recall records?
What recall reasons and root-cause categories occur in those exact-linked records?
This dataset performs those joins reproducibly and preserves the evidence needed to audit them.

Files
File	                                  Rows × columns	Description
fda_ai_medical_devices.csv	1,524 × 44	One row per FDA AI-list authorization, with pathway detail, classification fields, review span, and recall aggregates
fda_ai_device_recalls.csv	313 × 29	One row per exact AI submission × FDA recall product record, with status, timing, reason, root cause, action, and link evidence
fda_ai_product_codes.csv	172 × 18	One row per primary product code, with FDA classification definitions and dataset counts
data_dictionary.csv	91 column definitions	File-level column types, units, descriptions, and sources
source_manifest.csv	4 sources	URLs, retrieval date, license, joins, and caveats

Snapshot highlights
1,466 510(k), 39 De Novo, and 19 PMA authorization rows.
Radiology accounts for 1,164 rows (76.4%).
Annual decisions increased from 114 in 2020 to 333 in 2025.
Median observed receipt-to-decision span: 135 days for 510(k), 293 for De Novo, and 353 for PMA.
102 devices have at least one exact-linked recall product record.
The recall table contains 313 links across 147 FDA recall events.
229 linked recall product records were Open, Classified at snapshot time; 79 were Terminated and 5 Completed.
These figures are descriptive, not comparative safety scores.

Data sources
FDA AI-Enabled Medical Device List — defines the device universe and supplies the decision date, submission number, device, company, panel, and primary product code.
openFDA 510(k) and PMA APIs — pathway-specific receipt dates, applicants, decision codes, clearance types, and review flags.
FDA De Novo Classification Database — De Novo decisions, request types, and PCCP indicators.
openFDA Device Classification API — class, regulation, specialty, flags, and generic classification definitions.
openFDA Device Recall API / Recall Enterprise System — recall dates, status, product, reason, root cause, action, and submission-number arrays.
See source_manifest.csv for direct URLs, licenses, update frequencies, join keys, and caveats.

Possible use cases
Exploratory analysis of AI medical-device growth by year, specialty, company, pathway, or product code
Regulatory pathway comparisons and review-span visualization
NLP/topic modeling of reason_for_recall, root_cause_description, and action
Event-time analysis using days_to_first_recall, with careful censoring and exposure controls
Network analysis of companies, product codes, panels, and recall events
Classification exercises for panel, pathway, recall status, or root-cause category
Data-quality research on cross-database regulatory identifiers
Starter questions
How concentrated is the listed AI-device landscape in radiology, and is that changing?
Which product codes gained the most authorizations after 2022?
How do observed receipt-to-decision spans differ across pathways?
Which recall root-cause categories occur most often in exact-linked records?
How sensitive are recall comparisons to authorization year and time at risk?
What information is lost when recalls lack a submission number?
Critical limitations
The FDA AI list is not comprehensive. FDA explains that identification relies largely on AI-related terms in public authorization summaries and that the list is updated periodically.
Recall matching is high-precision but incomplete. Records without k_numbers or pma_numbers cannot be assigned to a listed authorization here.
A linked recall is not necessarily an AI failure. The issue may concern hardware, labeling, packaging, manufacturing, workflow, or non-AI software.
No-link does not mean no recall. has_linked_recall=0 means no exact submission-number link was found in this source snapshot.
Five links have recall initiation dates before the AI-list decision date. They are preserved and flagged for source review rather than silently removed.
review_days is simple calendar arithmetic, not an FDA review-performance metric.
Company names are source strings, not consolidated corporate-parent identities.
The list's newest decision was March 30, 2026 even though the snapshot was collected July 31, 2026; this reflects source update timing.
License and ethics
Released under CC0 1.0. openFDA publishes its data as public domain/CC0 unless otherwise noted. Attribution to the U.S. Food and Drug Administration is included throughout the package.

There is no patient-level data. Personal contact names and street addresses are excluded. This dataset is for research and education and must not be used as medical advice, a clinical decision tool, or a standalone device-safety ranking.
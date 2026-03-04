# AI TRANSLATION ORCHESTRATOR GUIDE (REVISED)

This document defines the core Translation & Review loop. This orchestrator assumes that **Phase 1: Pre-processing** (Glossary & Context) has already been completed by Agent 1.

## PHASE 1: PRE-PROCESSING (Script Execution)
Before triggering the Translation Agent, execute the following command:
```bash
python ./instruction/preprocess_glossary.py [input_chinese_file] [output_mixed_file]
```
- **Action:** The script sorts `master_glossary.csv` by length (descending) and replaces Chinese strings in the raw text with Vietnamese strings.
- **Benefit:** Standardizes all names, places, and terms mechanically, preventing the AI from "guessing" or making inconsistent choices.
- **Input for Agent 2:** The generated `[output_mixed_file]` (Mixed-Source text).

## PHASE 2: TRANSLATION AGENT (The Scholar)
- **Source:** Pre-processed "Mixed-Source" text (already cleaned of # and === by script).
- **Role:** High-fidelity Literary Translator.
- **Mandatory Input Template:**
  The Orchestrator MUST send the following instruction along with the text:
  > "Translate the following text. Chapter number is [Insert_File_Name_Here]. Follow the formatting rules in the system prompt. **STRICT RULE: DO NOT SUMMARIZE. TRANSLATE EVERY SINGLE SENTENCE, DETAIL, AND ACTION.**"
- **Core Instruction:**
    2. Use the **Hierarchy Matrix** for Vietnamese honorifics.
    3. **Term Consistency:** Strict adherence to the Replacement Map. 
    4. **Casing:** Ensure all proper nouns, organization names, and techniques are correctly capitalized (Uppercase) as specified in the glossary.
- **Output:** FIRST DRAFT.

## PHASE 3: REVIEWER AGENT (The Editor)
- **Source:** FIRST DRAFT + `ai_reviewer_prompt.md`.
- **Primary Checks:**
    1. **Anachronisms:** Eradicate modern Vietnamese pronouns (tôi, bạn, anh, em).
    2. **Dynamics:** Verify that the "Con - Phụ thân/Mẫu thân" relationship sounds natural and not overly robotic.
    3. **Capitalization:** Double-check that all names (e.g., *Hoa Trường Hy*, *Y Dược Ty*) are properly capitalized.
- **Output:** FINAL POLISHED VERSION.

## DATA INTEGRITY RULES
1. **No Hallucination:** Agent 2 must not change a name if it's already in the Replacement Map.
2. **Casing Rule:** All names from `master_glossary.csv` must be **Title Case** or **Uppercase** as defined.
3. **Format Preservation:** Keep the original HTML/Text structure (p tags, headers) perfectly intact.

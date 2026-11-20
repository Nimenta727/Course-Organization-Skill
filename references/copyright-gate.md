# Copyright, privacy and release gate / 版权与发布红线

**Goal:** Minimize unauthorized use and prevent *automatic public release* of teacher materials. No AI system or static checker can certify zero copyright infringement. Laws vary by jurisdiction; complex cases need an authorized rights holder or qualified legal review.

## Separate 4 rights questions
1. Can we **possess/read/analyze locally** this source? Access to a file is not equivalent to publication permission.
2. Can we **send it to an external AI provider** under the applicable institution/provider terms? Do not assume.
3. Can we **adapt/reproduce/distribute** any expressive elements (text, figures, example problems, code, layout)?
4. Can we **release the resulting work** publicly under a particular licence, including associated third-party components?

A source marked unknown or restricted may inform a privately viewed inventory, but NEVER authorize its text/figures or close paraphrases in public output.

## Never do by default
- Upload teacher PPT/PDF/handouts, recorded lectures, exam questions, exercise answers, proprietary images, class rosters, student work or private messages to GitHub or public build logs.
- Copy or nearly paraphrase distinctive lesson wording, slides, graphics, tables, arrangement, proprietary problems, diagrams, examples or presentation style.
- Translate copyrighted material as a workaround: a translation is still potentially an adaptation.
- Assume acknowledgement, "educational purpose", public web accessibility or fair use makes public republication lawful.
- Claim AI-generated prose is necessarily non-infringing.
- Infer that a GitHub repository's existence indicates an open-source licence.
- Upload third-party material to a model or SaaS without verifying data-sharing rights, permissions, terms, and privacy controls.

## Source classification
- OWNED: rights confirmed by author/rights holder; scope of publication recorded.
- PERMISSION_PUBLIC: explicit written authorization covering this use, distribution, adaptation, territory and medium.
- PUBLIC_DOMAIN: supported jurisdiction/evidence recorded; check third-party elements separately.
- CC-BY / CC-BY-SA / CC-BY-NC / CC-BY-NC-SA: only if verified licence, conditions, attribution and compatibility are satisfied.
- CC-BY-ND / CC-BY-NC-ND: do not publish adaptations without separate permission.
- UNKNOWN / RESTRICTED / FAIR_USE_CLAIM: public release blocked pending human rights review; fair use is contextual, not a global pass.

Use TASL where relevant: Title, Author, Source, Licence, with links, changes notice and other required notices. Check licence/version and author identity; verify each asset in a slide independently. NC may disallow commercial use; SA may constrain adaptations; ND disallows sharing adapted materials. Copyright permissions do not waive privacy/publicity rights.

## Independently written course rule
Take only unprotected facts, topic labels and general pedagogical goals as starting points *when appropriate*. Independently research concepts from verified public/OER sources; use a new instructional structure, original examples, distinct diagrams and original exercises. If lesson sequence itself reflects a highly distinctive creative selection/arrangement, do not replicate it for publication without permission. Mark teacher-specific claims as unverified/permission-required. When in doubt, author an original course independently from a syllabus of generic topics.

## Publication workflow: fail closed
1. Keep original materials in a separate local/private directory outside the git repo.
2. Maintain private source-manifest.json: owner, rights_basis, rights_evidence, scope, external_AI_permission, personal_data_review, location.
3. Maintain release-manifest.json listing each deliverable, referenced source IDs, reviewer, commercial use, output licence, source expressions, originality review, privacy flags and attribution.
4. Static gate rejects missing values, unknown/restricted/ND sources for adaptation, NC+commercial, SA incompatibility, copied expressions, personal data, unreviewed work, or missing source references/attribution.
5. Human reviews similarity, images, code, exam questions, phrasing, classroom privacy, accessibility, permissions and licences.
6. Only after written confirmation may a permitted publishing agent push public outputs. The CLI audit never publishes by itself.

## High-risk examples
- "Rewrite my teacher's entire slides in different words": BLOCK public derivative; offer independent explanations of general course topics.
- "Republish a scanned textbook with citations": BLOCK absent applicable rights; citations alone do not grant permission.
- "Use openly licensed figure": verify original figure rights, credit, licence conditions, and output compatibility.
- "Use a set of public facts about linked lists": create fresh original tutorial and code with sources consulted, no reproduction.

## Legal/standards references
- Creative Commons licence conditions: https://creativecommons.org/cc-licenses/
- CC attribution practices: https://creativecommons.org/reusing-cc-licensed-content/
- US Copyright Office fair use (four-factor case-specific test): https://www.copyright.gov/fair-use/
- UNESCO OER: https://www.unesco.org/en/open-educational-resources
- CC FAQ on additional rights: https://creativecommons.org/faq/

This is conservative project policy, not legal advice or an assertion that any use is definitely lawful.


## Teacher fidelity does not authorize reproduction
Preserve objective teaching characteristics (evidenced topics, general logic, emphasis and misconceptions) without copying a teacher's original paragraphs, board images, unusual diagrams, proprietary assignments or distinctive expressive sequencing where legally protected. If those elements are necessary for accuracy, keep the source private and obtain explicit rights/consent before publishing any adaptation. Intent hypotheses cannot turn into fabricated teacher quotes.

A released official exam is NOT automatically openly licensed. Link to authorized official pages; no mirroring, close paraphrase, number-swapping of distinctive questions, or publication of teacher-only exam materials. Use independently authored exam-style problems and check their correctness. Apply individual licences to any referenced OER, figures and datasets; no whole-site assumption.

A research registry that passes schema checks is not proof of a web source's truth, access permission, copyright status or a license's compatibility. Human review is a publication veto.

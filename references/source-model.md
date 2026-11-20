# Data contracts / 数据格式

These JSON formats are intentionally small and readable. All metadata with paths, author names and private source titles stays local. Only publish redacted metadata when permissible.

## course.json (public, original work)
~~~json
{
  "course_id": "sample",
  "title": "Example course",
  "audience": "beginners",
  "lessons": [
    {
      "id": "L01",
      "path": "lessons/L01/lesson.md",
      "objectives": [
        {
          "id": "LO-01",
          "statement": "Explain and compare two approaches using evidence.",
          "activities": ["ACT-01"],
          "assessments": ["ASM-01"]
        }
      ]
    }
  ]
}
~~~

## Private source-manifest.json
~~~json
{
  "sources": [
    {
      "id": "S001",
      "filename": "teacher-slides.pptx",
      "rights": "UNKNOWN",
      "rights_evidence": "",
      "allow_public_adaptation": false,
      "allow_external_ai": false,
      "personal_data_reviewed": false,
      "notes": "Private, local only"
    }
  ]
}
~~~

## release-manifest.json
~~~json
{
  "public_release": false,
  "reviewed_by": "",
  "commercial": false,
  "output_license": "MIT",
  "artifacts": [
    {
      "path": "lessons/L01/lesson.md",
      "sources_used": [],
      "contains_source_expression": false,
      "contains_personal_data": false,
      "originality_reviewed": false,
      "attribution": ""
    }
  ]
}
~~~

### Key semantics
- Empty sources_used means independently authored (not that no learning sources were consulted). Never disguise derivation by setting it empty.
- evidence A/B/C/D labels source support; they are NOT licence statuses.
- Rights_evidence can be a local reference to a permission record; do not publish that private record by default.
- Static gate is a lower bound: reviewers must inspect actual content, not merely set booleans.
- For CC sources, track exact version, author, title, URL, licence URL, alterations and compatible attribution.
- For public assets based on unlicensed source expressions, DO NOT mark them "independent" to get a green test.


## Private teacher-map.private.json
Store OUTSIDE every Git worktree. Example is fictitious; location and hypotheses must be verified for real materials.
~~~json
{
  "private": true,
  "lesson_id": "L01",
  "segments": [
    {
      "id": "E01",
      "source_id": "S01",
      "location": "slide 2",
      "kind": "error_demo",
      "handling": "original_explanation",
      "lesson_section": "常见错误",
      "teacher_intent": {
        "status": "hypothesized",
        "reason": "followed by a correction",
        "alternative": "could be an inadvertent writing slip"
      },
      "error_status": "possible_error",
      "explanation_or_unresolved": "Original trace of wrong idea followed by a correct solution"
    }
  ]
}
~~~
Allowed handling: original_explanation, private_only, blocked_rights, unresolved (unresolved blocks completion). Intent: explicit (with evidence), hypothesized (with reason and alternative), unknown. Teacher-specific evidence must remain confidential unless a separate permission exists.

## Research resource-registry.json
~~~json
{
  "resources": [
    {
      "id": "R01",
      "lesson_id": "L01",
      "objective_ids": ["LO01"],
      "title": "Official exam scope",
      "publisher": "Verified exam authority",
      "relevance": "Question types",
      "url": "https://example.edu/official-exam",
      "authority_tier": "official_exam",
      "usage": "link_only",
      "verified_at": "2026-11-20",
      "actual_live_check": true
    }
  ]
}
~~~
This illustrative URL is not an actual verified source; NEVER place this example entry in a real registry without a live check. Do not set actual_live_check true based on a generated URL. For adapted reuse document license, license_url, author, rights_evidence, modification_notice, and license_verified. CLI metadata checks do not visit URLs.

## Optional course metadata
- subject: computing, mathematics, sciences, humanities, languages, economics-engineering, or specific domain.
- Reader experience: one detailed lesson file with a beginner route and a revision pocket.
- Research plan output is separate from research registry; planned queries have status NOT_SEARCHED.

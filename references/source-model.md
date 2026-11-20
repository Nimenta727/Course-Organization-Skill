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

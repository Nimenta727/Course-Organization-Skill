"""Offline documentation/packaging checks; not copyright or network verification."""
import json
import re
import unittest
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]


class RepositoryConsistencyTests(unittest.TestCase):
    def test_versions_match(self):
        config = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
        package = (ROOT / "src/course_org/__init__.py").read_text(encoding="utf-8")
        chinese = (ROOT / "README.md").read_text(encoding="utf-8")
        english = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        match = re.search(r'^version\s*=\s*"([0-9]+\.[0-9]+\.[0-9]+)"', config, re.M)
        self.assertIsNotNone(match)
        version = match.group(1)
        self.assertIn(f'__version__ = "{version}"', package)
        self.assertIn(f"v{version}", chinese)
        self.assertIn(f"v{version}", english)
        self.assertTrue((ROOT / "docs/releases" / f"v{version}.md").is_file())

    def test_skill_frontmatter(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(skill.startswith("---\n"))
        header = skill.split("---", 2)[1]
        self.assertRegex(header, r"(?m)^name:\s*course-organization\s*$")
        description = re.search(r"(?m)^description:\s*(.+)", header)
        self.assertIsNotNone(description)
        self.assertLessEqual(len(description.group(1)), 1024)
        self.assertIn("references/teacher-fidelity.md", skill)

    def test_markdown_relative_links(self):
        missing = []
        link_pattern = re.compile(r'(?<!!)\[[^\]]+\]\(([^)]+)\)')
        for doc in ROOT.rglob("*.md"):
            if any(p in {".git", ".venv", "build", "dist"} for p in doc.parts):
                continue
            fenced = False
            for line in doc.read_text(encoding="utf-8").splitlines():
                if re.match(r"^\s*(?:\x60{3}|~~~)", line):
                    fenced = not fenced
                    continue
                if fenced:
                    continue
                for link in link_pattern.findall(line):
                    local = unquote(link.split("#", 1)[0].split("?", 1)[0])
                    if not local or local.startswith(("https://", "http://", "mailto:")):
                        continue
                    if not (doc.parent / local).resolve().exists():
                        missing.append((str(doc.relative_to(ROOT)), local))
        self.assertEqual(missing, [], f"Broken relative Markdown links: {missing}")

    def test_sample_public_release_stays_blocked(self):
        cfg = json.loads((ROOT / "examples/sample-course/provenance/release-manifest.json").read_text())
        self.assertIs(cfg["public_release"], False)
        self.assertIs(cfg["explicit_publication_approval"], False)

    def test_label_definitions(self):
        labels = json.loads((ROOT / ".github/labels.json").read_text(encoding="utf-8"))
        names = [x["name"] for x in labels]
        self.assertTrue(names)
        self.assertEqual(len(names), len(set(names)))
        for item in labels:
            self.assertRegex(item["color"], r"^[0-9a-fA-F]{6}$")
            self.assertTrue(item["description"])


if __name__ == "__main__":
    unittest.main()

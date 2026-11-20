# Computing, C programming, data structures and algorithms
Teaching route: motivating problem -> operational model -> board/hand trace -> original code -> observed error or newly authored debugging trap -> repair -> invariant/complexity -> practice.
Beginner: explain variables, control flow and memory changes with input/output traces. Intermediate: edge cases, complexity and testing. Advanced: correctness proof, alternative designs, API/resource trade-offs.
For teacher boardwork, explain jumps in pointer manipulation and loop condition assumptions; do not invent the teacher's intent. Produce independently written runnable examples rather than copying protected snippets or assignments.
Assessment mix: trace, diagnosis, implementation, test design and integrated project.
References: official language documentation, standards and university computing resources; published competition/exam criteria or links to released tasks, with original exercises.
Review pocket: complexity, invariants, common off-by-one/memory errors, concise key syntax and new hand trace. Never claim execution unless actually tested.


## Programming student textbooks (mandatory)
Do not put the internal "teacher thinks" analysis in the student chapter. For each K point, build concept -> intuition -> exact C/other-language semantics -> predict -> trace state/memory -> compile/test if available -> error correction -> new exercise. Explain which details are portable standards and which depend on ABI/compiler/platform. Include original input-output examples and explicit boundary checks; no one-line syntax lists.
Homework within the same lesson must include >=2 foundation, >=2 application and >=1 integrative challenge with complete statements and paired analyses. Review agents independently execute or hand-trace problems; no invented execution records. A programming-specific source often uses graded requirement evolution, but no other subject should be forced to adopt it.

# R2: Web research notes for the worksheet-generation experiment

Scope: evidence from papers, official docs and practitioner posts on (1) "AI slop" and how to reduce it, (2) LLM-as-judge reliability, (3) multi-step and multi-agent writing workflows, (4) design principles for math-circle problems, and (5) published work on LLM-generated math problems for children. Compiled 2026-09-30.

Conventions:
- **[E]** = empirical result reported in the cited source (numbers as the source reports them).
- **[P]** = practitioner guidance or vendor claim, not a controlled study.
- **[S]** = my synthesis or inference for this experiment.
- Wikipedia could not be fetched directly (blocked by the egress proxy). Its "Signs of AI writing" content below comes from secondary sources that quote or distill it, as cited.
- R1-sources.md (same folder) covers the local math-circle reference texts in depth. Section 4 here adds only the web-sourced principles.

---

## 0. Decision-relevant summary

1. **Slop is measurable without an LLM judge, and LLM judges are bad at noticing it.** Lexical and structural tells ("not X but Y", slop words and trigrams, em dashes, emoji, bold labels, headings, exclamations) can be counted deterministically against a human baseline (Antislop, slop-score). LLM judges come out near random on writing quality (GPT-4o 40.9% on the WQ benchmark) and close to zero agreement on slop spans (κ≈0.01). They also favor low-perplexity, "familiar" text, which is exactly what slop is. Use a deterministic linter for slop and keep LLM judges for pedagogy and correctness.
2. **"Don't do X" works partially and can prime X.** Naming a forbidden token raises its activation: in one study, 87.5% of violations came from that priming. Official guidance (Anthropic) is to say what *to* do, explain why, match the prompt's own style to the target style, and give 3–5 diverse examples. Contrastive examples (good plus bad, with the model reasoning about the difference) do help. Put long banned-phrase lists in the critic or linter, not in the writer prompt.
3. **Self-critique loops help only when the feedback is specific and correct.** Self-Refine gains are largest on the first iteration. On math, the critic said "everything looks good" 94% of the time. LLMs cannot reliably *find* errors but can fix them once the location is given. When writer and judge share a model and context, loops drift into reward hacking. Critics hallucinate nitpicks. LLM revisions homogenize: semantic shift about 3x larger than human edits, and a pull toward neutral, detached style.
4. **Multi-agent debate and personas add little.** Majority voting explains most of the gains attributed to debate. Personas don't improve accuracy. Outline-first planning (STORM) is the best-supported structural idea.
5. **Judging protocol:** binary, criterion-level checklists (CheckEval, HealthBench, MaC) beat holistic Likert scores for reliability. Pairwise comparison discriminates better on subjective quality but is easier to game (35% flip rate vs 9% under distractors), so run it in both orders and control for length. Use a cross-family panel (PoLL) to dilute self-preference. Use reference answers for correctness. Plant known-good and known-bad anchors to check judge sensitivity, since judges miss more than 50% of injected defects. Use paired, clustered statistics with CIs, and validate against a small human-labeled set with Cohen's κ (not % agreement).
6. **Math-circle quality is checkable.** The checkable properties are: low floor (a concrete first case anyone can try), high ceiling (a "what if" or general question), a short question-first statement, no method or answer given away ("be less helpful"), a sequence of related problems that build, multiple solution paths, and an invitation to explain or justify. Published LLM lesson materials skew heavily toward low cognitive demand (90% of activities in the bottom three Bloom levels). When asked to raise cognitive demand, AI tools succeeded only 64% of the time.
7. **Published LLM math-problem generators are evaluated with binary teacher criteria** (solvable, accurate, age-appropriate, standards-aligned: "MaC"). GPT-4-class models reach about 75–88% MaC. A carefully instructed LLM judge matched human–human agreement (75% vs 76%) on these criteria. Simulated students are useful for difficulty ranking only with special setups and are systematically too competent.

---

## 1. "AI slop": taxonomies, measurement, mitigation

### 1.1 Taxonomies

**Wikipedia: "Signs of AI writing"** (WikiProject AI Cleanup field guide; https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing, read via the secondary sources below). Categories reported across the distillations:
- *AI vocabulary*: delve, intricate, tapestry, pivotal, underscore, landscape, foster, testament, enhance, crucial, vibrant. Source: Beutler Ink summary, https://www.beutlerink.com/blog/how-to-spot-ai-writing
- *Puffery / undue emphasis on significance*: "a pivotal moment", "a broader movement", "stands as a testament to", "watershed moment" (TechCrunch, https://techcrunch.com/2025/11/20/the-best-guide-to-spotting-ai-writing-comes-from-wikipedia/)
- *Trailing present-participle clauses* that fake analysis: "…, emphasizing the significance of…", "…, reflecting the continued relevance…" (TechCrunch)
- *Promotional / tourist-brochure tone*: "breathtaking views", "clean and modern", "vibrant community"
- *Negative parallelism*: "It's not X, it's Y", "not just X, but Y"
- *Rule of three*: triplet lists and adjective clusters
- *False ranges*: "from intimate gatherings to global movements"
- *Em-dash overuse* (distillations claim 3–5x the human rate; [P] number)
- *Formatting tells*: bold abuse, bolded-label lists, excessive bullets, emoji in headers, title-case headings
- *Conjunctive overload*: moreover, furthermore, in addition
- *Compulsive summaries*: "Overall", "In conclusion", "In summary"
- *Weasel attribution*: "industry reports suggest"
- *Editorializing / meta-commentary*: "It's important to note…"
- *Sycophantic or collaborative chatter left in the text*, knowledge-cutoff disclaimers, curly quotes and other typographic tells
- Full 16-item distillation that cites the guide as its source: https://alexanderweichart.de/7_Agent/skills/write-in-my-voice/references/anti-ai-writing
- Caveat: secondary coverage stresses that these are *signs*, not proof, and that automated detectors are unreliable (TechCrunch). Many items (em dashes, triplets) also occur in good human prose. They are frequency signals, not per-instance errors. [S]

**LAMP / "Can AI writing be salvaged?"** (Chakrabarty, Laban, Wu; CHI 2025; https://arxiv.org/abs/2409.14509) **[E]**. MFA-credentialed writers edited 1,057 LLM responses (GPT-4o, Claude-3.5-Sonnet, Llama-3.1-70B), producing 8,035 categorized edits. Seven idiosyncrasy categories:
1. Cliché
2. Unnecessary or redundant exposition ("tell, don't show"; over-explaining)
3. Purple prose
4. Poor sentence structure
5. Lack of specificity and detail
6. Awkward word choice and phrasing
7. Tense inconsistency

Edit frequencies: awkward phrasing 28%, poor sentence structure 20%, unnecessary exposition 18%, cliché 17%. Edits were 74% replacements, 18% deletions and 8% insertions; revision is mostly cutting and swapping, rarely adding. There was no significant quality difference between the three model families. Preference order: writer-edited > LLM-edited > raw LLM.

**"Measuring AI 'Slop' in Text"** (https://arxiv.org/abs/2509.19163) **[E]**. Expert interviews produced three themes:
- Information utility: density, relevance
- Information quality: factuality, bias/subjectivity
- Style quality: structure (repetition, templatedness), coherence, tone (verbosity, word complexity)

Relevance, density and tone were the strongest predictors of a "slop" verdict. Human agreement on a binary slop label was poor (κ from −0.15 to 0.29). Span-level agreement was moderate (α≈0.34–0.45). **LLM judges (GPT-4o, o3-mini) had near-zero agreement with humans (κ≈0.01), with recall of 0.08–0.12.** They over-focused on density and missed coherence and tone.

**Antislop** (Paech, Roush, Goldfeder, Shwartz-Ziv; ICLR 2026; https://arxiv.org/abs/2510.15061; code https://github.com/sam-paech/auto-antislop) **[E]**. Defines slop as patterns overrepresented relative to human text, using the ratio ρ = f_LLM / f_human (human baseline: wordfreq plus a Reddit creative-writing and Gutenberg corpus). Some patterns appear more than 1,000x more often than in human text. "It's not X, it's Y" constructions run up to 6.3x the human rate in some models.

**EQ-Bench slop-score** (https://github.com/sam-paech/slop-score; https://eqbench.com/creative_writing.html) **[E/P]**:
- Composite score: slop words 60%, not-X-but-Y patterns 25%, slop trigrams 15%
- Not-X-but-Y detection uses 10 surface regexes plus 35 regexes over a POS-tagged stream
- The benchmark also reports a repetition metric (frequency mass of the top words, bigrams and trigrams)

**Practitioner anti-slop lists [P]**:
- stop-slop (https://www.skills.sh/hardikpandya/stop-slop/stop-slop): cut throat-clearing openers and emphasis crutches; avoid binary contrasts, dramatic fragmentation and rhetorical setups; be specific; vary rhythm; prefer two-item lists over three; no em dashes; "skip softening, justification, hand-holding."
- no_ai_slop_writing_rules (https://github.com/realrossmanngroup/no_ai_slop_writing_rules): bans "Let's dive in", "Here's the thing", teaser or dramatic headings, emoji bullets, fake-punchy one-line paragraphs. Asks for headings that state their content plainly.

**Worksheet-specific slop taxonomy [S]** (mapping the above onto a K–5 math-circle student page):

| Tell | Example on a kids' sheet | General category |
|---|---|---|
| Cutesy or themed framing | "Welcome, Math Detectives! 🕵️", "Captain Count needs your help!" | promotional tone, emoji |
| Generic encouragement / cheerleading | "You've got this!", "Great job, mathematician!", "Have fun exploring!" | sycophancy, filler |
| Signposting / meta | "In this worksheet you will learn…", "Let's explore…", "Ready? Let's go!" | meta-commentary |
| Over-explanation / answer leak | Hint that states the method; "Remember: to find the total, add…" | unnecessary exposition; violates "be less helpful" |
| Unnecessary structure | A heading per problem, bolded labels ("**Challenge:**", "**Think about it:**"), "Fun Fact" boxes | formatting tells |
| Rule-of-three padding | "Draw it, count it, and explain it!" on every item | rule of three |
| Not-X-but-Y and inflated significance | "Math isn't just numbers, it's a way of seeing the world!" | negative parallelism, puffery |
| Hollow reflection prompts | "What did you learn today?" (generic) vs "Why can't 7 be made this way?" (specific) | lack of specificity |
| Em dashes, exclamation density | "Try this one—it's tricky!" | punctuation tells |
| Uniform templating | Every problem the same length and shape, with the same lead-in | templatedness, repetition |
| Disclaimers / hedges | "Answers may vary depending on your approach" on a closed question | hedging |

Note: some patterns are legitimate in math-circle writing. "What do you notice?" is a real pedagogical move when it points at something specific. Judges and linters should penalize the *generic* form, not the move itself.

### 1.2 What measurably reduces slop

**Decoding-time and training-time methods (strongest evidence; mostly unavailable via hosted APIs) [E]** (Antislop paper):
- The Antislop Sampler backtracks when a banned string or regex completes. It suppressed 8,000+ patterns without quality loss and drove "not X but Y" regex hits to zero.
- Plain token banning was unusable at 2,000 patterns (quality fell to 28/100 at 8k).
- FTPO fine-tuning removed about 90% of slop with quality within about 1% of baseline. DPO removed 80–82% but cost 6–15 quality points and lexical diversity.
- [S] Practical analog with API models: generate, run a regex linter, then do a *targeted* rewrite of only the flagged spans, or resample.

**Post-generation validation [P]**: one production write-up reports that prompt rules alone stopped slop in about 80% of generations. A code-side lexicon and regex validator plus a single retry (about 12% of drafts) handled the rest. The stated reason: "The model has no way to verify it complied." (https://ozigi.app/blog/stopping-ai-slop-in-production-banned-lexicon-validator)

**Edit-based rewriting [E]**: in LAMP, LLM edits guided by the idiosyncrasy categories beat raw output, though they fell short of expert edits (https://arxiv.org/abs/2409.14509). In AI-Slop→AI-Polish (https://arxiv.org/abs/2504.07532), the pipeline was: generate 20 edited candidates, rank with a trained Writing Quality Reward Model, pick the best. Experts ranked the WQRM-best edit at 1.58 on average, vs 2.09 for a random edit and 2.26 for the original draft. Off-the-shelf LLMs are poor rankers on the WQ benchmark: GPT-4o 40.9%, o1 51.7%, R1 46.0%, GPT-4o 5-shot 54.3%, all near the 50% chance level. The paper also reports that LLMs prefer their own writing over Nobel laureates' writing.

**Few-shot exemplars [E]**: few-shot prompting gave up to 23.5x higher style-match accuracy than zero-shot (https://arxiv.org/abs/2509.24930). The same study found matched outputs were still statistically more predictable than human text (perplexity 15.2 vs 29.5). Anthropic's docs: "Examples are one of the most reliable ways to steer Claude's output format, tone, and structure… Include 3–5 examples," and make them diverse "so Claude doesn't pick up unintended patterns" (https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices).

**Style-matching the prompt [P, official]**: "The formatting style used in your prompt may influence Claude's response style… removing markdown from your prompt can reduce the volume of markdown in the output." Explaining the *reason* for a rule beats a bare NEVER: the docs' example replaces "NEVER use ellipses" with the text-to-speech rationale (same URL). The same docs name the failure: "You tend to converge toward generic, 'on distribution' outputs… what users call the 'AI slop' aesthetic."

**Diversity against mode collapse [E]**:
- Verbalized Sampling asks the model for several responses with stated probabilities. It raised creative-writing diversity 1.6–2.1x over direct prompting with no quality loss, and more capable models benefited more. The paper attributes mode collapse to typicality bias in human preference data (https://arxiv.org/abs/2510.01171).
- Artificial Hivemind: strong intra-model repetition and cross-model homogeneity on open-ended prompts. Judges and reward models are miscalibrated where human preferences are idiosyncratic (https://arxiv.org/abs/2510.22954).
- [S] For worksheets: ask for many candidate problem *ideas* (verbalized-sampling style), then select. Don't ask for one sheet directly.

### 1.3 Does "don't do X" work or backfire?

- **Priming is real [E].** "Semantic Gravity Wells" (Qwen2.5-7B, 40k samples; https://arxiv.org/abs/2601.08070): with "Do not use the word 'Paris'"-style constraints, violation probability rose with the word's baseline pull, from 9% at P₀=0.1 to over 46% at P₀=0.9. **87.5% of violations were priming failures**: naming the word activated it. Recommendations: avoid naming forbidden tokens, use category-level constraints or positive reformulations, and filter after generation when pressure is high.
- **Pink Elephant problem [E]**: told to avoid an entity, models often mention it anyway. Prompted baselines failed; fine-tuning (Direct Principle Feedback) was needed (https://arxiv.org/abs/2402.07896). An analogous "white bear" effect appears in text-to-image models (https://arxiv.org/abs/2404.15154).
- **Real-world example [P]**: until a November 2025 fix, ChatGPT did not reliably honor custom instructions to avoid em dashes. Altman: "If you tell ChatGPT not to use em-dashes in your custom instructions, it finally does what it's supposed to do!" Users still reported lapses afterward (https://www.tomsguide.com/ai/goodbye-em-dash-chatgpt-finally-lets-users-disable-its-most-annoying-writing-habit). The pink-elephant roundup is anecdotal (https://eval.16x.engineer/blog/the-pink-elephant-negative-instructions-llms-effectiveness-analysis).
- **Official guidance [P]**: "Tell Claude what to do instead of what not to do." Example: instead of "Do not use markdown", say "Your response should be composed of smoothly flowing prose paragraphs." (Anthropic docs, above.) The same docs still use explicit don'ts with conditions ("DO NOT use ordered lists… unless…"). So negatives are not forbidden; they work best when scoped and paired with the positive target.
- **Negative examples can help when contrasted [E]**: Contrastive In-Context Learning puts positive *and* negative examples in the prompt and has the model first articulate what to avoid. It significantly beat standard few-shot prompting on StackExchange and Reddit preference tasks (https://arxiv.org/abs/2401.17390).
- **Shallow constraints as regularizers [E, single study]**: banning filler words ("very", "just") improved reasoning accuracy by 6.7 points over an 83.0% baseline, more than deeper constraints such as E-Prime. The author's reading: any constraint that pushes the model off its default path acts as a regularizer (https://arxiv.org/abs/2604.02699). [S] Treat this as weak evidence that a *short* list of lexical bans is not harmful and may help.
- **[S] Net guidance for the generation prompts:**
  1. Describe the target positively, with a reason. For example: "Write the way a math-circle leader writes on a handout: short questions, no headings except the title, no encouragement lines, because the leader supplies the warmth in the room."
  2. Show 3–5 human-written exemplars.
  3. If you add negatives, keep them few and category-level ("no motivational or cheerleading sentences"). Don't paste a 50-phrase banned list into the writer prompt.
  4. Enforce with a deterministic linter plus targeted rewrite.
  5. Test as an experimental arm: positive-only, positive plus short negatives, and positive plus contrastive bad example.

---

## 2. LLM-as-judge methodology

### 2.1 Documented biases (with magnitudes)

| Bias | Evidence |
|---|---|
| **Position** | MT-Bench: answer-order consistency was 65.0% for GPT-4, 46.2% for GPT-3.5 and 23.8% for Claude-v1 (https://arxiv.org/abs/2306.05685). Wang et al.: with ChatGPT as judge, Vicuna-13B could "beat" ChatGPT on 66/80 queries just by reordering. Fixes: balanced position calibration (both orders) and multiple-evidence calibration, i.e., explain before scoring (https://arxiv.org/abs/2305.17926). |
| **Verbosity / length** | MT-Bench "repetitive list" attack fooled Claude-v1 and GPT-3.5 91.3% of the time and GPT-4 8.7% (same paper). Length-controlled AlpacaEval raised Spearman correlation with Chatbot Arena from 0.94 to 0.98 by regressing out length (https://arxiv.org/abs/2404.04475). EQ-Bench truncates at 4,000 characters (https://eqbench.com/about.html). HealthBench found minimal length–score correlation with criterion-level rubrics (r from −0.05 to 0.12) (https://arxiv.org/abs/2505.08775). |
| **Self-preference** | GPT-4 about +10% and Claude-v1 about +25% win rate for their own outputs (MT-Bench). Self-preference scales linearly with self-recognition ability (https://arxiv.org/abs/2404.13076). The mechanism is largely *familiarity*: judges rate lower-perplexity text higher whether or not they wrote it (https://arxiv.org/abs/2410.21819; also Stureborg et al., https://arxiv.org/abs/2405.01724). G-Eval notes a bias toward LLM-generated text (https://arxiv.org/abs/2303.16634). **[S] Implication: judges structurally reward typical, sloppy text, so a same-family judge will under-penalize its own family's slop.** |
| **Leniency / skew** | Judges are lenient relative to humans and can be 5 points off. High % agreement can hide very different scores, so use κ (https://arxiv.org/abs/2406.12624). Score distributions are skewed, and earlier attributes anchor later ones in multi-attribute prompts (Stureborg). |
| **Prompt-format sensitivity** | Rubric order, score labels (1–5 vs A–E) and the score attached to a reference answer all shift scores. Full-mark reference answers stabilize them (https://arxiv.org/abs/2506.22316). Scale choice matters: 0–5 gave the best human alignment (ICC 0.853) vs 0–10 (0.805) and 0–100 (0.840), and LLM reliability fell sharply on subjective benchmarks (MT-Bench ICC 0.899→0.632) (https://arxiv.org/abs/2601.03444). |
| **Run-to-run inconsistency** | Low intra-rater reliability across repeated runs, "almost arbitrary in the worst case" (https://arxiv.org/abs/2510.27106). |
| **Blind spots** | Evaluator LLMs missed injected quality drops (factuality, instruction-following, coherence, reasoning) in more than 50% of cases. Reference-based grading did best (https://arxiv.org/abs/2406.13439). |
| **Can't judge what it can't solve** | Without a correct reference, judges agree with experts only on questions they can answer themselves. Expert references largely fix this (https://arxiv.org/abs/2503.05061). MT-Bench math grading failures: 14/20 with the default prompt, 6/20 with CoT, 3/20 with a reference answer. |
| **Writing taste** | Near-random on expert writing-quality pairs (WQ, above). Surge reports that EQ-Bench's autograder agreed with expert writers "as little as 43%" and was "reward-hacked by the sheer volume of literary devices" ([P], vendor claim; https://surgehq.ai/blog/hemingway-bench-ai-writing-leaderboard). EQ-Bench itself says it does not control for self-preference (https://github.com/EQ-bench/creative-writing-bench). |

### 2.2 Pairwise vs absolute scoring

- **Pairwise is more discriminative for subjective quality.** GPT-4 pairwise agreement with experts was 85%, above the 81% human–human figure (MT-Bench). EQ-Bench uses pairwise Glicko because "pairwise matchups allow the judge to be more discriminative than scoring a single item in isolation." Eugene Yan's review: pairwise for subjective qualities (tone, coherence, persuasiveness); direct or binary scoring for objective ones (factuality, instruction-following), "where the better of two options might still be defective" (https://eugeneyan.com/writing/llm-evaluators/).
- **Pairwise is easier to manipulate.** With distractor features injected by the generator, pairwise preferences flipped in about 35% of cases vs about 9% for absolute scores (https://arxiv.org/abs/2504.14716). [S] Pairwise rewards whatever looks better side by side, including formatting gloss.
- **Rankings are more robust than absolute scores.** Even small judges and lexical metrics gave reasonable *rankings* while their absolute scores were poorly aligned (Thakur et al.).
- **Elo is order-sensitive and can violate transitivity** with sparse comparisons (https://arxiv.org/abs/2311.17295). [S] With about 10 workflows, run a full round-robin per input in both orders and fit Bradley–Terry (not online Elo), with bootstrap CIs.

### 2.3 Rubrics, checklists, and defect counting

- **CheckEval** decomposes criteria into Boolean yes/no questions. Across 12 evaluator models, average inter-evaluator agreement rose by 0.45 and score variance fell, while correlation with humans stayed strong (https://arxiv.org/abs/2403.18771).
- **TICK/STICK** uses LLM-generated, instruction-specific yes/no checklists. Agreement with human preference rose from 46.4% to 52.2%. Giving humans the checklist raised their inter-annotator agreement from 0.194 to 0.256. Checklist-guided self-refinement gained +7.8% (LiveBench reasoning) and checklist-based best-of-N gained +6.3% (WildBench) (https://arxiv.org/abs/2410.03608).
- **Counter-evidence**: checklists helped *selectively* in pairwise setups and inconsistently in direct scoring. The root problem is vague criteria (https://arxiv.org/abs/2508.15218).
- **HealthBench**: physician-written, conversation-specific criteria worth −10 to +10 points. The grader judges each criterion independently as met or not met; the score is the points earned divided by the maximum. The grader was validated against physicians with macro-F1 and showed "similar pairwise agreement between models and physicians as between individual physicians" (https://arxiv.org/abs/2505.08775; https://openai.com/index/healthbench/). [S] This is the best template for "count defects with weights": negative-point criteria are the defects.
- **Prometheus 2**: open evaluator supporting both direct rubric scoring (per-score descriptions) and pairwise ranking. Removing the reference answer caused the largest performance drop (https://arxiv.org/abs/2405.01535; via Eugene Yan).
- **G-Eval**: auto-generated CoT evaluation steps plus form-filling plus probability-weighted scores. Spearman 0.514 on summarization; notes bias toward LLM text (https://arxiv.org/abs/2303.16634).
- **Error-span / defect counting from MT evaluation [E]**: expert MQM error annotation produced "a substantially different ranking" than crowd Likert ratings. The MQM experts were more reliable and preferred human translations (https://arxiv.org/abs/2104.14478). GEMBA-MQM had GPT-4 mark error spans with severities, few-shot, and reached state-of-the-art system-level ranking (https://arxiv.org/abs/2310.13988).
- **Binary pass/fail with a critique [P]**: Hamel Husain argues "people don't know what to do with a 3 or 4." He recommends binary verdicts plus detailed critiques, with few-shot examples drawn from a domain expert's critiques, and reports >90% judge–expert agreement within three iterations (https://hamel.dev/blog/posts/llm-judge/).

### 2.4 Anchors, references, calibration

- Reference-guided judging cuts math grading errors by about 4x (MT-Bench). Expert references fix judges on questions they can't solve (No Free Labels). Full-mark reference answers stabilize scoring (scoring-bias paper).
- **Known-bad anchors (seeded defects)**: the FBI method perturbs good answers in 22 targeted ways and checks whether the judge notices. Judges missed more than 50% (https://arxiv.org/abs/2406.13439). [S] Build seeded-defect variants of a human-written gold sheet (answer leak, wrong answer key, cutesy framing, scaffolding overload, ambiguous wording, too long for K–1) and require the judge to catch them before trusting it.
- **Oak National Academy [P/E]** auto-evaluates AI-generated lessons against 24 codified quality benchmarks, with a worked definition of good vs bad distractors. Iterating the judge instructions against teacher labels cut MSE from 3.83 to 2.95 (https://www.thenational.academy/blog/how-do-we-ensure-our-ai-generated-resources-are-high-quality).
- **Criteria drift** (EvalGen): "users need criteria to grade outputs, but grading outputs helps users define criteria." Expect the rubric to change after a pilot, then freeze it (https://arxiv.org/abs/2404.12272).

### 2.5 Judge panels

- **PoLL** (Verga et al., Cohere): a panel of three smaller models from disjoint families (Command R, Claude Haiku, GPT-3.5) with voting or pooling beat a single GPT-4 judge across 6 datasets, showed less intra-model bias, and cost about 7x less (https://arxiv.org/abs/2404.18796).
- The judging panel and the generators should not share a model family. If they must, report per-judge rankings and check whether same-family judges rank their family higher. [S]

### 2.6 Statistics with few samples

Anthropic, "Adding error bars to evals" (https://www.anthropic.com/research/statistical-approach-to-model-evals):
1. Report SEMs.
2. Cluster SEs when items share a source; clustered SEs "can be over three times as large as naive."
3. Resample several generations per question and average.
4. Use **paired differences** when systems share a question set ("models… get the same questions right and wrong").
5. Do a power analysis before choosing N.

[S] Here, "question" means input brief: every workflow gets the same briefs, so compare workflows pairwise *within brief* and cluster by brief.

### 2.7 Validating the judge

- Measure agreement with a human-labeled set using Cohen's κ (binary items) or Kendall τ (rankings), not raw % agreement (Thakur; Eugene Yan). On Landis–Koch style bands, 0.41–0.60 is "moderate".
- MAST validated its LLM-judge pipeline against human annotators with κ=0.88 on failure-mode labels (https://arxiv.org/abs/2503.13657). EDUMATH found that its LLM judge's agreement with teachers (75%) matched teacher–teacher agreement (76%) (https://arxiv.org/abs/2510.06965). Matching human–human agreement is a reasonable bar.

---

## 3. Multi-step and multi-agent writing workflows

### 3.1 Self-Refine and critique-revise

- **Self-Refine** (https://arxiv.org/abs/2303.17651) [E]:
  - About 20% absolute average improvement across 7 tasks.
  - **Math: almost no gain** (GPT-3.5 64.1→64.1; ChatGPT 74.8→75.0) because "ChatGPT feedback for 94% instances is 'everything looks good'."
  - Diminishing returns, e.g., code optimization 22.0→27.0→27.9→28.8 over iterations 0–3 (max 4).
  - Specific, actionable feedback beat generic feedback (sentiment reversal 43.2 vs 31.2; no feedback 0).
  - Failure analysis: 33% of failures came from feedback pointing at the wrong location, 61% from an inappropriate suggested fix, and only 6% from the refiner implementing good feedback badly. **The feedback is the bottleneck.**
- **Intrinsic self-correction of reasoning fails** without external signal and sometimes degrades answers (Huang et al., ICLR 2024; https://arxiv.org/abs/2310.01798).
- **LLMs can't find their errors but can fix them when told where they are** (BIG-Bench Mistake; https://arxiv.org/abs/2311.08516). A small trained classifier located mistakes better than a prompted large model. [S] Split "locate" (solver, code check, checklist, linter) from "fix" (targeted rewrite).
- **Constitutional AI** critique→revise: sample, self-critique against a principle, revise, then fine-tune on the revisions (https://arxiv.org/abs/2212.08073). Used here as a supervised-data generator, not as a test-time quality loop.
- **Checklist-guided refinement** (STICK, above) is the best-evidenced critique format: +7.8%.

### 3.2 Known failure modes of critics and loops

- **Reviewers who always find something / hallucinated issues**: CriticGPT critiques were preferred over human critiques 63% of the time, but critics hallucinate bugs and nitpick. Human-plus-critic teams caught about as many bugs while hallucinating less (https://arxiv.org/abs/2407.00215).
- **Sycophancy**: assistants change correct answers under social pressure, and preference models sometimes favor convincing sycophantic responses over correct ones (https://arxiv.org/abs/2310.13548). [S] A reviser told "the reviewer says X is wrong" may break correct content.
- **Spontaneous reward hacking**: when the same model generates and evaluates (essay editing), evaluator scores rise while human-judged quality does not. It gets worse with shared context and larger models (https://arxiv.org/abs/2407.04549). In-context reward hacking from output-refinement loops produces side effects such as rising toxicity while optimizing engagement (https://arxiv.org/abs/2402.06627).
- **Best-of-N overoptimization**: true reward follows an inverted U as you optimize harder against a proxy, including via best-of-n (https://arxiv.org/abs/2210.10760). [S] Keep N modest, and never use the final evaluation judge (or its prompt) as the selector.
- **Homogenization / blandness**:
  - Writing with InstructGPT significantly reduced diversity across authors; the effect came from the model's contributed text (https://arxiv.org/abs/2309.05196).
  - LLM revisions of human essays shift meaning about 3x more than human revisions and move toward neutrality: neutral-stance essays rose 68.9%, pronouns fell 50%, nouns rose 14% (https://alphaxiv.org/abs/2603.18161).
  - Artificial Hivemind shows the same pull across models.
  - [S] Each LLM pass pulls toward the mode, so cap passes.
- **Verbosity creep**: no clean primary measurement in what I found. Self-Refine doesn't report length. [S] Inferred from length bias in judges plus "unnecessary exposition" being an 18% edit category. Log length per pass and reject revisions that grow length without a defect-driven reason.

### 3.3 Debate, voting, personas, multi-agent

- Multi-agent debate (Du et al. 2023, https://arxiv.org/abs/2305.14325) improves factuality and reasoning over a single pass. However, MAD "do[es] not reliably outperform… self-consistency and ensembling" and is hyperparameter-sensitive (https://arxiv.org/abs/2311.17371). **Majority voting accounts for most of the gains** attributed to debate; debate itself behaves like a martingale (https://arxiv.org/abs/2508.17536; NeurIPS 2025 spotlight).
- Debate between strong experts *does* help a weaker judge find truth: 76% vs a 48% baseline for LLM judges, 88% vs 60% for humans (https://arxiv.org/abs/2402.06782). That setting is adversarial argument about a factual answer, not collaborative writing.
- **MAST** (https://arxiv.org/abs/2503.13657): across 1,600+ traces from 7 multi-agent frameworks, gains over single agents "are often minimal." The 14 failure modes fall under specification and system design, inter-agent misalignment, and task verification (premature termination, incomplete or incorrect verification).
- **Personas**: across 162 roles and 2,410 factual questions, system-prompt personas did not improve performance; the best persona per question was unpredictable (https://arxiv.org/abs/2311.10054). Solo Performance Prompting (multi-persona self-collaboration) helped on trivia-creative-writing only in GPT-4-class models (https://arxiv.org/abs/2307.05300).

### 3.4 Outline-first

- **STORM** (NAACL 2024; https://aclanthology.org/2024.naacl-long.347): pre-writing research via perspective-guided questions, then an outline, then the article. Reported +25% absolute in articles judged well-organized and +10% in breadth vs an outline-driven RAG baseline. Editors flagged over-association of unrelated facts.
- [S] Worksheet analog: plan the mathematical core first, then the ladder of problems, then write the page:
  1. One central idea or structure.
  2. A concrete entry problem with small numbers.
  3. 3–6 problems that build on each other.
  4. One open, "what if", or general question.
  5. Answers and solution notes for the leader only.

### 3.5 Simulated students

- **Generative Students** (https://arxiv.org/abs/2405.11591): 45 GPT-4 simulated students, each with a profile of mastered, confused and unknown knowledge components, answered 20 MCQs. They identified the same hard items as real students and gave instructors actionable signal for revising questions.
- **Simulated classrooms for difficulty** (https://arxiv.org/abs/2601.09953): role-played students of varying proficiency on NAEP math items. Correlation with real difficulty was 0.75 (grade 4), 0.76 (grade 8) and 0.82 (grade 12). Diverse student names helped. *Weaker math models predicted real difficulty better than stronger ones.* Asking an LLM to rate difficulty directly worked poorly.
- **Too competent** (Kochmar et al., BEA 2025; https://arxiv.org/abs/2507.08232; EdWeek summary https://www.edweek.org/teaching-learning/how-ai-simulations-match-up-to-real-students-and-why-it-matters/2025/09): 11 LLMs vs NAEP data. Without grade prompts, simulated students scored 33–40 percentile points above real students. They struggled to reproduce authentic error patterns, and "no prompt… fully aligned simulated and real student answers across different grades and models."
- **"Competence paradox"** position paper (https://arxiv.org/abs/2601.05473): simulation needs an explicit epistemic-state specification constraining what the simulated learner knows.
- [S] Use simulated students for **comprehension and ambiguity checks**: can a literal-minded 7-year-old reader parse it, does any reading allow a trivial or unintended answer, does a problem require knowledge outside the grade? Don't use them as a difficulty or "fun" oracle. If you estimate difficulty, use many simulated students, a weaker model, and relative rankings only.

### 3.6 Implications for the ~10 workflows [S]

- **Likely to help**:
  - Outline-first planning.
  - Exemplar-conditioned writing.
  - Independent verification of every answer (solver plus code where possible).
  - A *checklist-bounded* critic that must quote evidence and may return "no change".
  - Targeted span edits for linter hits.
  - Selection among multiple candidates by a checklist (not by the eval judge).
- **Likely to hurt or waste budget**:
  - Unbounded critique→rewrite loops.
  - Critic and writer as the same model in the same context.
  - Generic "make it better" feedback.
  - Debate rounds.
  - Persona panels as a quality lever.
- **Guards**:
  - Max 1–2 revision passes.
  - Accept a revision only if it fixes a logged defect *and* doesn't increase lint score or length beyond a threshold.
  - Run a separate fresh-context check that the math is unchanged and still correct after revision.

---

## 4. Writing good math-circle problems for kids: web-sourced principles

### 4.1 Sources

- **Math for Love / Dan Finkel, "Five principles of extraordinary math teaching"** (https://mathforlove.com/?p=2488; NPR TED Radio Hour transcript https://www.npr.org/transcripts/702514656):
  1. Start with a question ("The ordinary math class begins with answers and never arrives at a real question").
  2. Give students time to struggle (productively vs unproductively stuck).
  3. You are not the answer key.
  4. Say yes to students' ideas.
  5. Play.
- **Julia Robinson Mathematics Festival**:
  - Noncompetitive and collaborative; "low-floor, high-ceiling" activities "accessible for every age, skill level and background."
  - "The real answers are in the way that children solve the puzzles and explain their thinking" (https://jrmf.org/?p=6).
  - Problems "related to one another and get progressively more difficult—we even included research problems whose answers we didn't know." The organizers wanted so many problems that no one could finish, so "each attendee would be able to find something rewarding at his or her level" (Blachman, via SLMath: https://legacy.slmath.org/web/msri/education/for-k-12-educators/julia-robinson-math-festival).
  - Student-facing prompts are short "Can you…?" questions, e.g., "Can you make a better die than your partner?" (https://jrmf.org/puzzle/2-player-game/). Separate beginner versions exist for PreK–2.
- **NRICH**:
  - Low-threshold high-ceiling tasks give "the opportunity for everyone to get started and everyone to get stuck." Invite learners to pose their own questions; extensions "push the ceiling even higher" (https://nrich.maths.org/7701).
  - Rich tasks (Piggott, https://nrich.maths.org/5662) are accessible to a wide range of learners. They offer initial success, have different levels of challenge, allow problem posing, admit diverse methods, can reveal elegant solutions, expose patterns, generalizations and unexpected results, connect areas, and promote discussion. A task is "not rich" by itself; that depends on how it is used.
- **Zvonkin, *Math from Three to Seven*** (AMS MCL vol. 5, https://bookstore.ams.org/MCL/5; author's essay https://sites.icmc.usp.br/sasha_a/zvonkin-e.pdf; review https://smus.com/books/math-from-three-to-seven-by-a-k-zvonkin/):
  - "What you teach them is not mathematics but a way of life."
  - Ask questions rather than explain, and let children be wrong; logical argument rarely convinces small children.
  - Use physical manipulatives.
  - Present isomorphic problems in different guises and let children notice the sameness.
  - Disguise puzzles as games when motivation drops.
  - Some ideas take months or years, so revisit rather than force.
  - "It is not the puzzles, nor their solutions, that are interesting, but the process."
- **Bob & Ellen Kaplan Math Circle** (https://www.cimat.mx/~gil/html/math_for_kids.htm; EdWeek https://www.edweek.org/teaching-learning/proof-positive/2005/02):
  - The session starts from a posed question; students conjecture, build examples and counterexamples, and name their discoveries.
  - The leader uses "judicious choice of examples and nudges at critical moments" and avoids handing over "punch-lines without having worked their own way up to them."
  - No grades or competition; mixed skill levels.
- **Dan Meyer, "Math class needs a makeover"** (TED 2010, https://www.ted.com/talks/dan_meyer_math_class_needs_a_makeover):
  - Five symptoms: lack of initiative, lack of perseverance, lack of retention, aversion to word problems, eagerness for formula (https://www.teachthought.com/pedagogy-posts/teaching-math-wrong/).
  - Remedies: be less helpful, ask the shortest question you can, let students build the problem.
  - On the textbook: "taking a compelling question, a compelling answer, but paving a smooth, straight path from one to another" (https://scienceblogs.com/bioephemera/2010/05/13/fixing-our-impatience-with-irr).
  - Peck (AMS blog) adds, after Freudenthal: pre-structured sub-steps take the *structuring*, the actual mathematics, away from students (https://blogs.ams.org/matheducation/2018/12/17/learning-to-be-less-helpful/).
- **Open Middle** (Kaplinsky): closed beginning, closed end, open middle. Multiple paths; often "easy to get an answer but more challenging to get the best or optimal answer"; looks procedural but turns out deeper (https://www.openmiddle.com/whats-open-middle/).
- **Cognitive demand (Stein & Smith 1998)** (Mathematics Teaching in the Middle School 3(5):344–350, doi:10.5951/MTMS.3.5.0344):
  - Lower demand: memorization; procedures without connections.
  - Higher demand: procedures with connections; *doing mathematics* (non-algorithmic, no rehearsed pathway suggested, requires self-monitoring and real cognitive effort).
  - This is a directly usable judging rubric.
- **LFHC pitfalls** ([P], https://theinclusivemathcoach.substack.com/p/what-makes-a-math-task-truly-low): "rigor is not harder numbers or more problems." A task a student can finish silently alone lacks the discussion element. Example formats: Which One Doesn't Belong, numberless problems.

### 4.2 Checkable principles for the student page [S, derived from 4.1 plus R1]

Each item is phrased so a judge or linter can answer yes or no.

1. **Question-first**: the page opens with a question or task, not an explanation, objective statement or welcome. (Finkel #1; Meyer "shortest question")
2. **No method leak**: no hint names the strategy, operation or answer; no worked example of the same structure precedes the problem. (Meyer; Finkel "not the answer key"; Kaplans; Zvonkin)
3. **No over-scaffolding**: the problem isn't pre-split into sub-steps that do the structuring for the child, unless the steps are themselves interesting questions. (Meyer, Peck/Freudenthal)
4. **Low floor**: the first problem can be started by every child in the grade band with a concrete small case, a drawing or objects, with no new vocabulary. (NRICH, JRMF)
5. **High ceiling**: at least one item is open, generalizing, optimizing, or "what if…" / "can you find all…" / "is it always…". (NRICH, JRMF "research problems", Open Middle optimization)
6. **Coherent ladder**: problems are variations on one structure and build. They aren't a grab-bag of unrelated topics. (JRMF "related… progressively more difficult"; Zvonkin isomorphic guises)
7. **Multiple paths**: at least the central problems admit more than one valid approach or representation. (NRICH, Open Middle)
8. **Asks for reasoning, specifically**: at least one prompt asks "why/how do you know/is it always" about a specific claim, not a generic reflection. (JRMF "explain their thinking"; Kaplans conjecture and proof)
9. **Cognitive demand**: the central items are "procedures with connections" or "doing mathematics", not drill. (Stein & Smith; contrast with the 90% lower-order finding in §5)
10. **Correct and well-posed**: every problem is solvable with grade-appropriate knowledge; the answer is unique where uniqueness is implied, or "find all" is stated; there are no unintended trivial readings. (MATHWELL/EDUMATH "solvable" and "accurate")
11. **Age-appropriate language**: short sentences and concrete nouns, with reading load matched to the grade. K–1 pages assume an adult reads aloud; minimal text with pictures or objects. (MATHWELL readability; JRMF beginner versions; Zvonkin manipulatives)
12. **Concise**: each problem statement is a sentence or two; no decorative headings, no per-problem labels, no "fun fact" boxes. (JRMF prompt style; anti-slop formatting tells)
13. **No cheerleading or cutesy wrapper**: no encouragement lines, emoji, mascots or exclamation-heavy framing. A context, if used, is plain and serves the math. (Finkel "play" means the mathematics is playful, not the decoration; Meyer: contexts should create a real question)
14. **Enough for the time, without implying completion**: more problems than most will finish, with an ordering that makes partial progress feel complete. (JRMF)
15. **Answers live elsewhere**: solutions and teacher notes are separated from the student page. (JRMF facilitator guides)

---

## 5. Published work on LLM generation of children's math problems and materials

| Work | What was generated | How evaluated | Key results |
|---|---|---|---|
| **MATHWELL** (Christ et al., EMNLP Findings 2024; https://arxiv.org/abs/2402.15861) | K–8 word problems with Python solutions | K–12 teachers annotated 3,484 outputs for **solvability, accuracy, appropriateness**; "MaC" = meets all | MaC: GPT-4 Turbo 78.8%, MATHWELL 74.8%, GPT-3.5 62.8%, Llama-2 62.4%, LLEMMA 15.2%. MATHWELL had the most readable text (FK grade about 2.7). Automatic classifiers for the criteria "need refinement"; human review still needed. |
| **EDUMATH** (2025; https://arxiv.org/abs/2510.06965) | Standards-aligned grade 3–5 word problems | 1,372 teachers (Prolific) dual-annotated 3,012 problems for solvability, accuracy, educational appropriateness and standards alignment, with a third annotator on disagreement | Baseline MaC: Gemma-3-12B 63.9%, Gemma-3-27B 75.4%, Qwen3-30B 87.3%; fine-tuned up to 94.6%. **LLM judge vs teachers 75% agreement vs teacher–teacher 76%.** Classroom study (94 students): similar accuracy on LLM and human problems; students preferred customized LLM problems, mainly for topic interest. |
| **MathWiz / elementary MWP generation** (https://arxiv.org/abs/2506.05950) | Elementary word problems from grade, operation and count | Human plus automatic metrics, with diversity techniques | High fluency, but "LLMs still struggle to generate questions that adhere to the specified grade and question type requirements." |
| **MathFish** (Lucy et al. 2024; https://arxiv.org/abs/2408.04226) | Standards tagging and verification (9.9k problems, 385 standards) | Agreement with ground-truth standards | Models predict near-miss standards; "LMs often generate problems that do not fully align with standards described in prompts." Calls for "careful scrutiny" of LM-generated curricular materials. |
| **Trust, Maloy, Xu, Pelletier** (CITE Journal 2025; https://citejournal.org/volume-25/issue-3-25/social-studies/civic-education-in-the-age-of-ai-should-we-trust-ai-generated-lesson-plans/) | 310 civics lesson plans (GPT-4o, Gemini 1.5 Flash, Copilot), 2,230 activities | Bloom's coding | **90% lower-order** (45% remember, 21% understand, 24% apply); 10% higher-order. Teachers should "remix, revise, and reenergize." Not math, but the same low-demand default. |
| **Can AI tools transform low-demand math tasks?** (2026; https://arxiv.org/abs/2604.12743) | 11 tools (6 general, 5 math-ed incl. Khanmigo) asked to raise cognitive demand | Stein & Smith task-analysis levels | Success 64% overall (range 33–88%). Failures were undershooting and **overshooting** (too-ambitious tasks teachers would reject). Classifying demand and raising it were *negatively* correlated (r=−0.35). |
| **Oak National Academy** auto-eval ([P/E]; link in §2.4) | AI lesson resources, especially MCQ distractors | 24 codified benchmarks; LLM judge iterated against educators | MSE 3.83→2.95 after refining judge instructions with explicit good and bad exemplars. |
| **AI physics practice problems** (https://arxiv.org/abs/2508.03085) | Learner-initiated practice problems | Expert labels on 543 problems, student pairwise preferences, 3 LLM judges | A small core of structural, learner-visible checks sufficed to predict preferences; exhaustive rubrics weren't needed. |
| **Preservice teachers vs MagicSchool** (Moldavan & Nafziger, AMTE 2024; https://amte.net/sites/amte.net/files/MoldavanNafziger_Connections_Fall2024.pdf) | AI-generated elementary math content | Qualitative | Found mathematical errors (e.g., an incorrect fraction-equivalence claim). Novice teachers did not always catch them. |
| **Prompting techniques for math solutions** (Frontiers in Education 2024; doi:10.3389/feduc.2024.1386075) | 1,080 GPT solutions under 4 prompt styles | Human raters on content and process quality | Content accuracy didn't change with prompt technique; process and explanation quality improved with CoT and "ask-me-anything." |
| **AI tutor pedagogy taxonomy** (MRBench; https://arxiv.org/abs/2412.09416) | Tutor responses to student mistakes | 8 human-annotated dimensions incl. "not revealing the answer" | Gives a vocabulary for "don't give it away" that transfers to worksheet hints. |

**Common evaluation pattern in this literature**: binary teacher criteria (solvable / accurate / appropriate / aligned) combined as "meets all criteria". Dual annotation with adjudication. An LLM judge is accepted when its agreement with humans reaches the human–human level. Sometimes a small classroom trial follows. None of these studies evaluate *math-circle* qualities (low floor/high ceiling, non-routine, no method leak) or slop. Those parts of the rubric have to be built here (§4.2, §6b).

---

## 6. Recommendations for this experiment [S]

### 6a. Generation workflows and prompts

1. **Base spec in positive, reasoned language, written in the target register** (plain prose, no markdown-heavy prompt if you want plain pages). Explain *why*: "the leader provides warmth and hints in person; the page should only pose questions."
2. **3–5 human-written exemplar problems or sheets** from the R1 sources, varied in topic and grade, wrapped as examples. Expected to be the single biggest style lever.
3. **Plan, then write**: Stage 1 picks the mathematical core, entry case, ladder and ceiling question. Stage 2 writes the page. Stage 3 writes the leader's answer key separately.
4. **Diversity at the idea stage**: have the model propose several candidate core ideas with rough probabilities (verbalized sampling), then pick one with the checklist. Don't regenerate whole sheets N times.
5. **Verification separated from style**: solve every problem independently (fresh context, ideally a different model plus code or brute force for counting and number puzzles). Check uniqueness and grade-appropriateness. Feed back only located defects.
6. **Deterministic slop linter plus targeted span rewrite** (regex for not-X-but-Y, encouragement phrases, emoji, exclamations, em dashes, bold labels, headings, hint/remember lines, sentence length). The banned list lives in the linter, not in the writer prompt.
7. **Critic design**: a fixed checklist (§4.2), evidence quotes required, "no change needed" allowed and expected. Use a different model or at least a fresh context from the writer. Allow at most 1–2 passes. Reject any revision that raises lint count or length without fixing a logged defect.
8. **Simulated student** only as a "literal 7-year-old reader" ambiguity and comprehension probe.
9. **Skip as primary levers**: debate, persona panels, unbounded refine loops, and "make it more engaging/fun" instructions, which invite cutesy framing.
10. **Experimental arms worth including** (they test the evidence directly):
    - single prompt with no style guidance
    - positive spec only
    - positive spec plus long negative list (tests priming)
    - positive spec plus exemplars
    - plan→write
    - plan→write→verify→lint-fix
    - plan→write→bounded checklist critic (different model)
    - same-model unbounded critique loop (expected to drift)
    - best-of-N with checklist selector
    - contrastive (good and bad example) prompt

### 6b. Fixed, trustworthy evaluation protocol

1. **Fixed inputs and paired design**: about 8–12 briefs (topic × grade band, K–1, 2–3, 4–5). Every workflow runs every brief, ideally 2 samples per brief to estimate within-workflow variance. Analyze paired by brief, with brief-clustered SEs.
2. **Blinding and normalization**: render every sheet to the same plain template before judging, strip workflow IDs, randomize order, and truncate or flag pathological length.
3. **Layer A, deterministic metrics (no LLM)**: slop-lint counts per 100 words (not-X-but-Y, encouragement, emoji, exclamations, em dashes, headings, bold labels, "hint/remember/let's" lines), word count per problem, total length, readability grade, number of problems. These give a reproducible slop and length score and covariates for length control.
4. **Layer B, correctness (reference-guided)**: an independent solver (strong model plus code where feasible) produces answers. A judge checks solvability, uniqueness and answer-key accuracy *with the reference*. Binary per problem.
5. **Layer C, criterion-level checklist (CheckEval / HealthBench style)**:
   - Use the 15 items from §4.2 plus MaC items, each yes/no with a required one-line evidence quote.
   - Make some items weighted negatives (answer leak −, cutesy framing −, wrong answer −−).
   - Judge one criterion (or a small related group) per call to avoid multi-attribute anchoring; CoT before verdict; temperature 0.
   - Use a **3-judge cross-family panel** with majority vote per criterion.
6. **Layer D, holistic pairwise**: "Which sheet would an experienced math-circle leader rather hand to these kids tomorrow?"
   - Both orders; an inconsistent pair counts as a tie.
   - Same panel, Bradley–Terry fit with bootstrap CIs.
   - Report with and without length control (regress on length difference, LC-AlpacaEval style).
   - Treat it as secondary to Layer C, because pairwise is more manipulable.
7. **Anchors in every batch**:
   - Known-good: 2–3 human-written sheets from R1 sources, as "gold".
   - Known-bad: seeded-defect variants of the same sheets (answer leak, wrong key, cutesy wrapper, over-scaffolded, ambiguous, generic slop).
   - Before the real run, require the panel to (i) rank gold above its defect variants in at least 90% of pairs and (ii) flag each seeded defect on the matching criterion. Report per-criterion sensitivity.
8. **Human calibration**: the experimenter labels about 20–30 sheets on the binary checklist (blind). Compute Cohen's κ per criterion between the human and the panel; drop or rewrite criteria with κ<0.4. Freeze the rubric after this pilot to avoid criteria drift.
9. **Self-preference checks**: if generators are mostly one family, include at least two judges from other families. Report per-judge rankings, Kendall's W across judges, and whether any judge's own family wins disproportionately.
10. **Stability**: re-run a 20% subset of judgments to measure test–retest agreement. Report it.
11. **Primary outcome** (pre-registered): % of sheets passing all hard gates (correct and solvable, no answer leak, age-appropriate), then the weighted checklist score. Secondary: slop-lint rate, length, and pairwise BT strength. Never use any evaluation judge or prompt inside a generation workflow.

---

## 7. Source index (primary first)

Slop and style
- Antislop (ICLR 2026): https://arxiv.org/abs/2510.15061 · code: https://github.com/sam-paech/auto-antislop
- slop-score: https://github.com/sam-paech/slop-score · EQ-Bench CW v3: https://eqbench.com/creative_writing.html · about: https://eqbench.com/about.html · repo: https://github.com/EQ-bench/creative-writing-bench
- LAMP / "Can AI writing be salvaged?": https://arxiv.org/abs/2409.14509
- AI-Slop to AI-Polish (WQ, WQRM): https://arxiv.org/abs/2504.07532
- Measuring AI "Slop" in Text: https://arxiv.org/abs/2509.19163
- Artificial Hivemind (NeurIPS 2025): https://arxiv.org/abs/2510.22954
- Verbalized Sampling: https://arxiv.org/abs/2510.01171
- Style imitation few-shot: https://arxiv.org/abs/2509.24930
- Wikipedia Signs of AI writing: https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing (via https://techcrunch.com/2025/11/20/the-best-guide-to-spotting-ai-writing-comes-from-wikipedia/, https://www.beutlerink.com/blog/how-to-spot-ai-writing, https://alexanderweichart.de/7_Agent/skills/write-in-my-voice/references/anti-ai-writing)
- Hemingway-bench (vendor): https://surgehq.ai/blog/hemingway-bench-ai-writing-leaderboard
- Anthropic prompting best practices: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Practitioner lists: https://www.skills.sh/hardikpandya/stop-slop/stop-slop · https://github.com/realrossmanngroup/no_ai_slop_writing_rules · https://ozigi.app/blog/stopping-ai-slop-in-production-banned-lexicon-validator

Negative instructions
- Semantic Gravity Wells: https://arxiv.org/abs/2601.08070
- Suppressing Pink Elephants (DPF): https://arxiv.org/abs/2402.07896
- Do not think about pink elephant: https://arxiv.org/abs/2404.15154
- Contrastive ICL: https://arxiv.org/abs/2401.17390
- Trivial vocabulary bans: https://arxiv.org/abs/2604.02699
- Em-dash instruction fix: https://www.tomsguide.com/ai/goodbye-em-dash-chatgpt-finally-lets-users-disable-its-most-annoying-writing-habit
- 16x pink elephant roundup: https://eval.16x.engineer/blog/the-pink-elephant-negative-instructions-llms-effectiveness-analysis

LLM-as-judge
- MT-Bench / Chatbot Arena: https://arxiv.org/abs/2306.05685
- LLMs are not Fair Evaluators: https://arxiv.org/abs/2305.17926
- PoLL: https://arxiv.org/abs/2404.18796
- Self-recognition and self-preference: https://arxiv.org/abs/2404.13076 · perplexity-driven self-preference: https://arxiv.org/abs/2410.21819
- Pairwise or Pointwise: https://arxiv.org/abs/2504.14716
- CheckEval: https://arxiv.org/abs/2403.18771 · TICK/STICK: https://arxiv.org/abs/2410.03608 · Are checklists useful?: https://arxiv.org/abs/2508.15218
- HealthBench: https://arxiv.org/abs/2505.08775 · https://openai.com/index/healthbench/
- G-Eval: https://arxiv.org/abs/2303.16634 · Prometheus 2: https://arxiv.org/abs/2405.01535
- Inconsistent & Biased Evaluators: https://arxiv.org/abs/2405.01724
- Judging the Judges: https://arxiv.org/abs/2406.12624
- Scoring bias: https://arxiv.org/abs/2506.22316 · Grading scale: https://arxiv.org/abs/2601.03444 · Rating Roulette: https://arxiv.org/abs/2510.27106
- No Free Labels: https://arxiv.org/abs/2503.05061 · FBI blind spots: https://arxiv.org/abs/2406.13439
- Length-controlled AlpacaEval: https://arxiv.org/abs/2404.04475
- Elo Uncovered: https://arxiv.org/abs/2311.17295
- MQM (Freitag et al.): https://arxiv.org/abs/2104.14478 · GEMBA-MQM: https://arxiv.org/abs/2310.13988
- EvalGen / criteria drift: https://arxiv.org/abs/2404.12272
- Anthropic, error bars for evals: https://www.anthropic.com/research/statistical-approach-to-model-evals
- Eugene Yan, LLM-evaluators review: https://eugeneyan.com/writing/llm-evaluators/ · Hamel Husain, LLM judge guide: https://hamel.dev/blog/posts/llm-judge/

Workflows
- Self-Refine: https://arxiv.org/abs/2303.17651 · Cannot self-correct reasoning yet: https://arxiv.org/abs/2310.01798 · BIG-Bench Mistake: https://arxiv.org/abs/2311.08516
- Constitutional AI: https://arxiv.org/abs/2212.08073 · CriticGPT: https://arxiv.org/abs/2407.00215 · Sycophancy: https://arxiv.org/abs/2310.13548
- Spontaneous reward hacking in self-refinement: https://arxiv.org/abs/2407.04549 · In-context reward hacking: https://arxiv.org/abs/2402.06627 · RM overoptimization: https://arxiv.org/abs/2210.10760
- Homogenization: https://arxiv.org/abs/2309.05196 · LLM revision distortion: https://alphaxiv.org/abs/2603.18161
- Debate: https://arxiv.org/abs/2305.14325 · Should we be going MAD?: https://arxiv.org/abs/2311.17371 · Debate or Vote: https://arxiv.org/abs/2508.17536 · Persuasive debaters: https://arxiv.org/abs/2402.06782 · MAST: https://arxiv.org/abs/2503.13657
- STORM: https://aclanthology.org/2024.naacl-long.347
- Personas: https://arxiv.org/abs/2311.10054 · Solo Performance Prompting: https://arxiv.org/abs/2307.05300
- Simulated students: https://arxiv.org/abs/2405.11591 · https://arxiv.org/abs/2601.09953 · https://arxiv.org/abs/2507.08232 · https://arxiv.org/abs/2601.05473 · https://www.edweek.org/teaching-learning/how-ai-simulations-match-up-to-real-students-and-why-it-matters/2025/09

Math-circle design
- Math for Love: https://mathforlove.com/?p=2488 · https://www.npr.org/transcripts/702514656
- JRMF: https://jrmf.org/?p=6 · https://jrmf.org/puzzle/2-player-game/ · https://legacy.slmath.org/web/msri/education/for-k-12-educators/julia-robinson-math-festival
- NRICH: https://nrich.maths.org/7701 · https://nrich.maths.org/5662
- Zvonkin: https://bookstore.ams.org/MCL/5 · https://sites.icmc.usp.br/sasha_a/zvonkin-e.pdf · https://smus.com/books/math-from-three-to-seven-by-a-k-zvonkin/
- Kaplans: https://www.cimat.mx/~gil/html/math_for_kids.htm · https://www.edweek.org/teaching-learning/proof-positive/2005/02
- Dan Meyer: https://www.ted.com/talks/dan_meyer_math_class_needs_a_makeover · https://blogs.ams.org/matheducation/2018/12/17/learning-to-be-less-helpful/ · https://scienceblogs.com/bioephemera/2010/05/13/fixing-our-impatience-with-irr · https://www.teachthought.com/pedagogy-posts/teaching-math-wrong/
- Open Middle: https://www.openmiddle.com/whats-open-middle/
- Stein & Smith 1998: doi:10.5951/MTMS.3.5.0344
- LFHC pitfalls: https://theinclusivemathcoach.substack.com/p/what-makes-a-math-task-truly-low

LLM-generated educational math
- MATHWELL: https://arxiv.org/abs/2402.15861 · EDUMATH: https://arxiv.org/abs/2510.06965 · MathWiz: https://arxiv.org/abs/2506.05950 · MathFish: https://arxiv.org/abs/2408.04226
- AI lesson plans (Trust et al.): https://citejournal.org/volume-25/issue-3-25/social-studies/civic-education-in-the-age-of-ai-should-we-trust-ai-generated-lesson-plans/
- AI tools raising cognitive demand: https://arxiv.org/abs/2604.12743
- Oak National Academy: https://www.thenational.academy/blog/how-do-we-ensure-our-ai-generated-resources-are-high-quality
- Physics practice problems: https://arxiv.org/abs/2508.03085
- Moldavan & Nafziger: https://amte.net/sites/amte.net/files/MoldavanNafziger_Connections_Fall2024.pdf
- Prompting & math solution quality: https://doi.org/10.3389/feduc.2024.1386075
- AI tutor pedagogy taxonomy: https://arxiv.org/abs/2412.09416

Limitations of these notes: many numbers come from abstracts or tool-assisted page reads rather than full-text reading. Spot-check any number before quoting it in a write-up. Vendor and practitioner claims are marked [P]. Wikipedia was read only through secondary sources.

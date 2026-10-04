# Chapter brief: Part 02 - LLMs demystified

Status: agreed (2026-10-03, delegated to the drafting agent; the author reviews later).

## Lessons in scope

| ID  | Lesson                                     | Objectives (from curriculum)                                                        |
| --- | ------------------------------------------ | ----------------------------------------------------------------------------------- |
| 2.1 | What an LLM actually is                    | Explain tokens and next-token prediction.                                           |
| 2.2 | Training vs inference                      | Explain why models have knowledge cutoffs and how products add search.              |
| 2.3 | Context windows and memory                 | Explain why the model "forgets" and what products do about it.                      |
| 2.4 | ⏱ The landscape: vendors, models, products | Distinguish vendors, model families, and the apps built on them.                    |
| 2.5 | Open-weight vs closed, local vs cloud      | Explain the trade-offs: privacy, cost, capability.                                  |
| 2.6 | Hallucinations and verification            | Explain why LLMs make things up; apply verification habits.                         |
| 2.7 | Anatomy of a good prompt                   | Apply the six-element prompt anatomy used throughout the course.                    |
| 2.8 | Data privacy and company policy            | Decide what can and cannot be shared with an AI tool; consumer vs enterprise tiers. |
| 2.9 | ⏱ Cost: tokens and pricing                 | Estimate the cost of a task; explain why pricing is per token.                      |

## Learner starting point

Finished Parts 0 and 1. Has used a chat assistant, without knowing how it works.

## Learner end point

After Part 2 the learner can:

- Explain, with the toy example, how a model predicts the next token.
- Say why a model does not know yesterday's news and why it "forgets" a long chat.
- Tell a vendor from a model from a product.
- Name three situations where an answer must be verified, and how.
- Write a prompt with the six elements: context, task, input, constraints, output format,
  verification.
- Decide what data is safe to paste into which tool.
- Estimate the token count and cost of a task.

## Real pitfalls to cover (hypotheses)

- Believing the model "looks things up" or "understands" like a person (2.1).
- Believing a chat remembers across conversations (2.3).
- Treating a fluent answer as a verified answer (2.6).
- Pasting customer data into a consumer tool (2.8).
- Not knowing a long paste is expensive or truncated (2.3, 2.9).

## Café Central tasks

| Lesson | Task                                                                         |
| ------ | ---------------------------------------------------------------------------- |
| 2.1    | Predict the next word from the Café Central sales text with a toy model.     |
| 2.3    | Show a conversation overflowing a small context window.                      |
| 2.6    | Ask an assistant to summarize the CSV and catch where it invents.            |
| 2.7    | Rewrite the lousy summary prompt using the six elements.                     |
| 2.8    | Classify Café Central fields (customer names, emails, sales totals) by risk. |
| 2.9    | Estimate the cost of summarising 240 sales rows, with example prices.        |

## Examples required

| File                     | Purpose                                      | Test strategy               |
| ------------------------ | -------------------------------------------- | --------------------------- |
| `part02/01_next_word.py` | Toy next-word predictor by counting          | assert the prediction       |
| `part02/03_context.py`   | A fixed-size window dropping oldest messages | assert what is kept         |
| `part02/09_cost.py`      | Token and cost estimate with example prices  | assert exact Decimal result |

## Prompt section ideas

Each lesson's prompt section is about the lesson topic itself (see each lesson). 2.7
is the one that defines the six elements; earlier lessons forward-reference it.

## Diagrams needed

- 2.1: predict-append-repeat loop. 2.2: training vs use timeline. 2.3: window sliding.
- 2.4: vendor, model, product layers. 2.8: data-sharing decision flow.

## Fast-changing facts (⏱)

2.4 and 2.9 set `lastVerified`. They contain no model names or prices in the body text.
Vendor names and official pricing links live in a marked "Check these yourself" section.
Prices in the 2.9 example are labelled as made-up example rates.

## End-of-part project

- [ ] I can explain next-token prediction in two sentences.
- [ ] I rewrote one real prompt of mine with the six elements.
- [ ] I classified my own work data as safe or not safe to paste.
- [ ] I estimated the cost of one task in tokens.

## Out of scope

- Calling APIs from code (Part 10). Fine-tuning. Embeddings and RAG internals.

## Open questions

- Real learner stories (still open).

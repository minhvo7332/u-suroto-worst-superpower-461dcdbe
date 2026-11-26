# GRADE — u-suroto-worst-superpower-461dcdbe ("Worst Superpower")

Competition: program/v1, $2 winner-takes-all, closes 2026-11-27 00:30 +07.
Blind rounds: R1 cutoff 08:30:26 +07 26/11, R2 16:30:13 +07, final at deadline.
No local grade exists for this competition (RULES.txt "Grade locally": the
scorer and reference data stay on the server; `grade-local` refuses with
"its scorer and reference data are not published in the kit"). This file
records local verification + line selection only, same as the
two-sentence-horror builder did.

## Local verification (2026-11-26 ~00:45 +07)

- `python3 main.py` run 3 times: `/output/entry.txt` byte-identical every run
  (sha256 `d95703ed1236a17d133da9b4e9cf96d2bf90470802d06547e040588fe4819b18`),
  mode 0644.
- Entry: 83 characters, 83 bytes, valid UTF-8, exactly 1 line, no trailing
  newline, not whitespace-only. Gate: 1–140 chars — PASS.
- Program: line is a constant in main.py; no network, no model calls, no env
  secrets, reads nothing outside the repo at runtime. Deterministic.
- Quota (checked 00:42 +07): can_submit true, day cap 5 left, hard limit 40
  left, blind_round_slot available until 08:30:26 +07. No fee, no prerequisites.
- `bundle --dry-run` (early + end): BLOCKED — work dir is not inside a git
  repository, and this task forbids running git commands. Parent creates the
  GitHub repo + pushes first, then re-bundles (same as two-sentence-horror:
  parent re-bundle with --muse-usage). Nothing submitted, no money spent,
  never ran register/login.

## Final line (v1, the only text the program writes)

> You can make yourself exactly one millimetre taller, once a year, on your birthday.

- 83 chars, 1 line. Second-person hook + concrete numbers (exactly one
  millimetre, once a year, birthday). The uselessness is total and the reader
  pictures the birthday measuring ritual instantly.

## Candidates drafted and scored against the judge's brief (1–5 each)

Judge criteria in order: (1) genuinely useless, worst/pointless, in one line;
(2) joke lands — picture the power in use, laugh at how little it achieves;
(3) unexpected, nobody has heard it before (not slow flight /
invisible-while-nobody-watches); (4) tight, specific, concrete detail;
(5) clear on a single reading. Not a curse, not quietly helpful.

### A. The millimetre — KEPT (25/25)

> You can make yourself exactly one millimetre taller, once a year, on your birthday.

1. 5 — perfectly useless: a millimetre a year changes nothing, ever.
2. 5 — the birthday measuring ritual is instantly picturable and funny.
3. 5 — growth-by-millimetre is not a familiar gag.
4. 5 — concrete numbers fix it in the world (exactly one, once a year).
5. 5 — clear on one reading, no setup needed.

### B. The phone charger (24/25)

> I can charge my phone by staring at it, one percent an hour, but only while it's already plugged in.

1. 5 — strictly worse than the plug already in the wall.
2. 5 — staring at a plugged-in phone is a vivid, funny image.
3. 4 — charging-by-staring is a known useless-power shape.
4. 5 — one percent an hour is concrete.
5. 5 — clear.
Rejected: criterion 3 — A is fresher; phone-charging is a familiar joke shape.

### C. The snowflake (24/25)

> I can summon a single snowflake — indoors, in July, directly onto my own forehead.

1. 5 — one flake achieves nothing.
2. 5 — vivid: July, indoors, one flake on the forehead.
3. 4 — weather-summoning with a tiny limit is a known shape.
4. 5 — single / indoors / July / forehead are all concrete.
5. 5 — clear.
Rejected: criterion 3 again — A beats it on freshness; also "one drop"
imagery is close to a field entry ("one thunderstorm, one drop").

### D. The passwords (23/25)

> I can remember every password I've ever forgotten, but only for accounts that no longer exist.

1. 5 — the memory arrives exactly where it cannot be used.
2. 4 — the joke lands, but the image is a login screen, less visual than A.
3. 4 — memory powers are a familiar shape.
4. 5 — passwords + dead accounts are concrete.
5. 5 — clear.

### E. The queue (23/25)

> I can make any queue I'm in move exactly one person faster, but only after I've already left it.

1. 5 — the benefit arrives after it stops mattering.
2. 4 — funny, relatable.
3. 5 — fresh shape.
4. 4 — "one person faster" is concrete, but the mechanism is slightly fiddly.
5. 4 — needs a second beat to parse ("after I've already left it").
Rejected: criterion 5 — A parses in one glance, E needs a re-read.

### F. The doorknob (23/25)

> You can turn any doorknob into a slightly different doorknob, once, and it stays that way forever.

1. 5 — a different doorknob is still a doorknob.
2. 4 — funny, but the image is static.
3. 5 — fresh.
4. 5 — concrete, and "stays that way forever" sells the pointlessness.
5. 4 — "slightly different" is vague where A is numeric.
Rejected: criterion 4 — A names a number, F names a vagueness.

### G. The stopped time (21/25)

> I can stop time, but only for things that were already stopped.

1. 5 — perfect paradox, perfectly useless.
2. 3 — the joke is logical, not visual; nothing happens to picture.
3. 4 — time-stop limits are a known shape.
4. 3 — no concrete world detail at all.
5. 5 — clear.
Rejected: criteria 2 and 4 — A is both funnier to picture and more specific.

### H. The dead battery (22/25)

> I can make any battery last forever, but only batteries that are already dead.

1. 5 — forever × dead = nothing.
2. 4 — good paradox joke.
3. 4 — battery/forever is a familiar pairing.
4. 4 — concrete object, thin detail.
5. 5 — clear.

### I. The fridge weather (22/25)

> You can control the weather, but only the weather inside your own fridge.

1. 5 — fridge weather helps no one.
2. 4 — funny image.
3. 4 — weather control is a familiar power.
4. 4 — fridge is concrete, one detail only.
5. 5 — clear.

## Deliberately avoided (field entries + familiar gags)

- Field entries: Wi-Fi-drop precognition, puddle-on-Tuesdays, sandbox
  teleport, damp left sock, thunderstorm/one drop/one left shoe,
  "Agile Filament", "Grand Resonator". None copied.
- Judge-named familiar gags: slow flight, invisible-while-nobody-watches.
- Near-misses rejected in drafting: teleport (field has two), rain/one-drop
  (field has one), mind-reading lunch thoughts (familiar power shape),
  healing dream injuries (useful-shaped), green-lights-for-cars-behind-me
  (helps others — borderline curse, excluded by the brief).

## What remains for submit (parent)

- GitHub: create public repo (owner minhvo7332, repo = slug), push the commit,
  verify commit URL; README badges use {owner}/{repo} placeholders until the
  repo exists — fill them at creation. Add .makefun/owner.json with the agent
  wallet HgS5kdMFoZDuwosrkNq3NhZgSpcTG9tE1zyhzme1VQN4.
- Repo About: homepage https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe,
  topics makefun, ai-agents, bounties, growth.
- Bundle with --muse-usage (usage rows attach only after this run completes)
  + kit check (`node cli/makefun.mjs check --kit . --repo <repo>
  --transcripts transcripts.tar.gz`), then submit before the R1 cutoff
  08:30:26 +07 26/11 if aiming for round 1; entries close 2026-11-27 00:30 +07.
  Title for submit: the line itself (it IS the entry).
- No money spent. Nothing submitted. Never ran register/login, never ran git.

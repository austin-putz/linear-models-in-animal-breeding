# Versioning, DOIs, and reader feedback

How the book gets a citable identity, how a reader reports a mistake, and how the two connect: a
report names a version, the fix lands on `main`, and the next release carries a new DOI. There is
no errata page — **the release notes are the errata**, and the fix is already in the book.

Companion documents: [`chapter_standards.md`](chapter_standards.md) (what a chapter looks like),
[`pedagogical_order.md`](pedagogical_order.md) (what order it comes in). This document is about
the book as a published object, not its contents.

---

## 1. The problem this solves

A student cites the book in a thesis. Two years later an examiner checks the equation they cited.
Three things must be true for that to work:

1. **The citation names a specific version**, not "whatever the website showed that day".
2. **That version can still be retrieved**, exactly as it was, even if the website has moved or
   the repository has been renamed.
3. **The current version is easy to find from the old one**, so the examiner can see whether the
   equation was later corrected.

Git tags give (2) for anyone who can clone a repository. A DOI gives (1) and (2) for everyone
else, and the *concept DOI* gives (3). The version string printed in the book is what ties a
reader's copy to all of it.

---

## 2. Versions

### 2.1 Scheme

Semantic-style, `vMAJOR.MINOR.PATCH`, spoken of in edition language:

| Bump | Means | Example |
|---|---|---|
| **MAJOR** | A new edition. Chapters added, removed, or restructured; notation changed; a reader of the old edition would find things in different places | `v1.x` → `v2.0.0` |
| **MINOR** | Content changed but the structure did not. A new section, a rewritten example, a corrected *result* (wrong number, wrong equation, wrong R output) | `v1.2.0` → `v1.3.0` |
| **PATCH** | Typos, wording, figure cosmetics. Nothing a reader would need to re-check | `v1.3.0` → `v1.3.1` |

A corrected number or equation is always at least MINOR, so that "did the result I cited change?"
can be answered from the version number alone.

`v1.0.0` is the **first citable release** — not before the book is substantially complete. Until
then the Welcome page keeps its *Under Construction — do not cite* callout, and tags before
`v1.0.0` (`v0.x`) are for the author's own reference and are **not** archived to Zenodo (§3.3).

### 2.2 Where the version string comes from

**The git tag, and nothing else.** `tools/version.R` runs before every render (`project:
pre-render` in `_quarto.yml`), asks `git describe --tags --match 'v*' --long`, and writes three
gitignored files that the render then reads:

| File | Read by | Carries |
|---|---|---|
| `_variables.yml` | `{{< var version >}}`, `{{< var released >}}`, `{{< var year >}}` in the HTML footer and the Welcome page | version, release date, year, commit |
| `styles/version.tex` | `styles/pdf-preamble.tex`, via `include-in-header` | `\bookversion`, `\bookreleased` for the PDF footer |
| `_version-bibtex.md` | `{{< include >}}` on the Welcome page | the BibTeX block, because shortcodes do not expand inside fenced code |

What the reader sees:

| Build | `git describe` says | Version printed |
|---|---|---|
| Checkout of a tag | `v0.1.0-0-g…` | `0.1.0`, dated by the tag |
| `main`, three commits after the tag | `v0.1.0-3-gabc1234` | `0.1.0-dev+abc1234`, dated by the last commit |
| No tag at all | — | `0.0.0-dev+abc1234` |

Nobody edits a version number by hand, so the site and the PDF cannot disagree, and a development
build can never be mistaken for a release: the `-dev+hash` suffix names the exact commit. Both
workflows check out with `fetch-depth: 0` so the tags are present in CI.

The version is printed in the **footer of every page** — HTML via `page-footer`, PDF via
`fancyhdr` in the preamble — and in the **Citation** section of the Welcome page, with a BibTeX
block. `book.date: today` was removed: a date that changes on every render identifies nothing.

### 2.3 Cutting a release

1. Fixes accumulate on `main`. The site updates continuously — that is fine, it is the dev build.
2. When a **result** has been corrected, release promptly. When only typos have accumulated,
   batch them — a release every month or two, or when a term starts.
3. Write the `## [X.Y.Z] - YYYY-MM-DD` section in `CHANGELOG.md` (§2.4), commit, tag `vX.Y.Z`,
   push the tag. The rest is automatic (§3.4). The release workflow refuses to publish a version
   that has no changelog section.

### 2.4 `CHANGELOG.md`

Keep-a-Changelog format, one section per release, three headings: **Corrected** (results that
changed — chapter, section, what was wrong, what it is now), **Changed** (content that was
rewritten or added), **Fixed** (typos and cosmetics, one line, no detail). Reporters are credited
by GitHub handle in the entry they caused.

The **Corrected** section of each release is what a reader checks when they hold an older version.
It replaces an errata page: it is written once, at release time, and never maintained afterwards.
The GitHub release notes are copied from it.

---

## 3. DOIs

### 3.1 Zenodo

Zenodo (CERN-run, free, permanent) assigns two kinds of DOI to a versioned work:

- A **version DOI** per release. Resolves forever to that release's archive.
- A **concept DOI** for the work as a whole. Resolves to the latest version and lists every
  version beneath it.

The book prints the **concept DOI** in its "How to cite" section and footer, alongside the
version string. It cannot print its own version DOI, because with the GitHub integration (§3.2)
that DOI does not exist until after the release is published — see §3.5 for the upgrade path that
removes this limitation. A reader's citation therefore carries *concept DOI + version*, which is
the convention Zenodo itself recommends and which resolves unambiguously.

### 3.2 Route A — GitHub integration (start here)

One-time, in the browser: sign in to Zenodo with GitHub, flip the switch on this repository.
From then on every **published GitHub release** is archived automatically: Zenodo pulls the
source snapshot (the same zipball GitHub attaches to every release), mints a version DOI, and
adds it to the concept record.

Zenodo reads bibliographic metadata from `CITATION.cff` at the repo root if present — title,
author, ORCID, license, keywords. Keep that file the single source of author metadata; GitHub
also renders it as a *Cite this repository* button.

**What Route A does not archive:** release assets. The PDF attached to the GitHub release (§3.4)
is on GitHub only. The Zenodo archive holds the source, which with `_freeze/` checked in
reproduces the PDF byte-for-byte in principle, but a reader who wants the PDF from Zenodo does not
get one. This is the reason §3.5 exists.

### 3.3 Do not link Zenodo until `v1.0.0`

A Zenodo record is permanent — it cannot be deleted once published. Linking the repository while
the book is a set of placeholders would mint a DOI for a book that does not exist yet, and that
record would sit under the concept DOI forever. Tag `v0.x` freely for local bookkeeping; enable
the Zenodo switch on the day `v1.0.0` is tagged, not before.

### 3.4 Release workflow (GitHub Actions)

A second workflow alongside `quarto-publish.yml`, triggered on `push: tags: ['v*']`:

1. Check out the tag.
2. Set up Quarto + tinytex + R exactly as `quarto-publish.yml` does (extract the shared steps
   into a composite action or copy them — the two must not drift).
3. `quarto render --to pdf`.
4. Create the GitHub release from the tag, body taken from the matching `CHANGELOG.md` section,
   with the PDF attached as `linear-models-in-animal-breeding-vX.Y.Z.pdf`.
5. Zenodo (Route A) picks up the published release with no further action.

The existing `quarto-publish.yml` continues to deploy the dev build from `main` and to render PRs
without publishing. It does not change.

### 3.5 Route B — API upload (upgrade, optional)

Replace the GitHub-integration switch with an Action that talks to the Zenodo REST API directly:

1. Create a new version draft under the concept record → Zenodo **reserves the version DOI**
   immediately.
2. Write that DOI into `_variables.yml`, render the PDF — so **the PDF carries its own version
   DOI** on the title page.
3. Upload the PDF and the source zip to the draft, publish.

This is strictly better for citation — the artifact names its own DOI — at the cost of a secret
(`ZENODO_TOKEN`) in the repository and thirty lines of `curl`. Do Route A for `v1.0.0`; move to
Route B when the machinery has been exercised once. The two produce records under the same concept
DOI, so switching later loses nothing.

---

## 4. Reporting: which route for which problem

Two GitHub features carry all reader feedback. A third route exists for people without GitHub.

| The reader has | Route | Why there |
|---|---|---|
| A **wrong number, equation, R output, or claim** | **Issue** — *Error in the book* template | It is a defect with a fix; the tracker records when it was fixed and in which release |
| A **typo or awkward sentence** and is willing to fix it | **Pull request** via *Edit this page* | The reader does the work; CI renders the PR |
| A typo and is not willing to fix it | **Issue** — *Error in the book* template | Same tracker, lower priority label |
| **"I don't understand this section"** | **Discussion** — *Q&A* | Not a defect, but a signal the exposition failed; other readers can answer, and a pattern of questions on one section becomes an issue |
| An **idea** — a different example, a missing topic | **Discussion** — *Ideas* | Scope is decided by the author; the discussion is where the case is made |
| Something that **should not be public** | **Email** | Rare. Listed last, as the fallback, so it stays rare |

Issues and Discussions are kept separate on purpose: the tracker holds only things with a fix, so
it can be read as a to-do list, and a reader looking for "is this already reported?" searches one
short list rather than one long one.

### 4.1 GitHub-side pieces

- `.github/ISSUE_TEMPLATE/error.yml` — form: version (with a line saying where to find it),
  format (HTML / PDF), chapter and section, what is wrong, what it should be, how you know
  (a working, an R output, a reference). Every field but the last required.
- `.github/ISSUE_TEMPLATE/config.yml` — `blank_issues_enabled: false`; contact links to the
  Discussions Q&A and Ideas categories, so a reader who opens *New issue* with a question is
  redirected before they file it.
- `.github/PULL_REQUEST_TEMPLATE.md` — three lines: what changed, which chapter, a checkbox that
  the contribution is offered under the book's licences.
- `CONTRIBUTING.md` — **a pointer, not a document.** Four lines linking to the reporting page in
  the book (§5). GitHub surfaces it when someone opens an issue or PR, which is the only reason
  it exists; the content lives in one place.
- Discussions enabled, with **Q&A** and **Ideas** categories. Default categories removed.
- `repo-actions` in `_quarto.yml` stays `[edit, issue]`, but `issue-url` points at the **reporting
  page in the book**, not at GitHub, and the link is relabelled *Report an error or suggest a
  change* (`language: repo-action-links-issue`). A reader who clicks it lands on the page that
  says which route fits their problem; sending them straight to the issue form would skip the
  routing and put questions in the tracker.
- Labels: `error`, `typo`, `chapter-NN` for triage; `corrected-in-vX.Y.Z` when closed, so a
  reader following an old citation can search by version.

### 4.2 Crediting

Every reporter is named (GitHub handle, or name if they prefer) in the `CHANGELOG.md` entry their
report caused and in the Acknowledgments on the Welcome page. This is conventional for open
textbooks and it noticeably increases reports. The PR template asks how the contributor wants to
be credited.

---

## 5. The reporting page in the book

A single **unnumbered page at the end of the book**, after the appendices and before References,
titled *Reporting Errors and Contributing*. Not a section of the Welcome page — that page is
already long, and the reporting page needs a stable URL that the issue template, `CONTRIBUTING.md`,
the footer, and the margin link can all point to. It renders in the PDF, which is the only way a
PDF reader ever learns how to report anything.

The Welcome page's *Feedback and Contributions* section shrinks to two sentences and a link.

### 5.1 Contents, in order

1. **Which route for what.** The table from §4, rewritten for a reader rather than a maintainer.
2. **Before you report.** Find your version (say exactly where it is printed). Check whether the
   current version already fixes it — one sentence pointing at the concept DOI and the changelog.
   Search the open issues.
3. **Reporting an error.** Step by step: the *Report an issue* link in the right margin (HTML) or
   the URL (PDF); what each field of the form is asking and why the version matters.
4. **Fixing it yourself.** The *Edit this page* route: GitHub forks automatically, the file is the
   chapter's `.qmd`, edit and propose. What not to touch (`_freeze/`, `_book/`, `references.bib`
   without a verified DOI). That CI renders the PR and the author reviews it. That the
   contribution is offered under the book's licences.
5. **Asking a question or suggesting something.** Discussions: Q&A for the first, Ideas for the
   second, with the two links.
6. **What happens next.** Triage, fix on `main`, the dev site updates, the next release carries
   the fix and names the reporter. A note that there is no errata list — the changelog is it.

### 5.2 Style

Same voice as the rest of the book: short, concrete, second person. No callouts except one
**Check Yourself**-free zone — this page is instructions, not teaching. Screenshots are not needed
and would go stale.

---

## 6. Order of work

1. ~~`tools/version.R` pre-render; footer and cite section; `CITATION.cff`.~~ *(Done.)*
2. ~~Issue template, `config.yml`, PR template, `CONTRIBUTING.md` pointer.~~ *(Done.)* Labels and
   Discussions are repository settings, done with `gh` or in the browser.
3. ~~The reporting page (§5) and the Welcome-page shrink.~~ *(Done.)*
4. ~~`CHANGELOG.md`; release workflow (§3.4).~~ *(Done.)* Exercise it on `v0.1.0`.
5. At `v1.0.0`: flip the Zenodo switch, tag, verify the record, put the concept DOI into
   `CITATION.cff` (`doi:` field) and `book.doi` in `_quarto.yml`, cut `v1.0.1` so the DOI is
   printed in the book.
6. Route B (§3.5) when there is appetite for it.

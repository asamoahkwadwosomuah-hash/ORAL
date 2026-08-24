# Operation Recover All Loot (ORAL): Institutional Process Timeline

**A governance/accountability data analysis project — Python, pandas, matplotlib — tracking the process timeline of Ghana's flagship anti-corruption asset-recovery initiative.**

## Background

**Operation Recover All Loot (ORAL)** is a Ghanaian government initiative launched by President John Dramani Mahama, aimed at investigating and recovering state funds and assets allegedly misappropriated by officials, primarily focused on the previous administration. It was announced before Mahama's inauguration in January 2025 and has remained an active, evolving initiative since.

**This project is a methodology showcase, not a political statement or a verdict on anyone's guilt.** It tracks the *institutional process* — what was announced, when, and with what publicly stated figures — using only what government officials themselves have said on the record, as reported by mainstream Ghanaian news outlets. It does not attempt to verify allegations, assess evidence, or determine guilt for any named individual. Everyone referenced in the source reporting is legally presumed innocent unless and until convicted in a court of law.

## A critical distinction: "complaints," "potential recoveries," and "prosecutable cases" are not the same thing

This is the single most important methodological note in this project. Government figures over time have referenced several *different* numbers that are easy to conflate:

- **2,417 complaints** received by the ORAL Committee (Feb 2025) — raw, unvetted public submissions, not evidence of wrongdoing.
- **$21.19 billion in "potential recoveries"** identified in the initial committee report (Feb 2025) — an early estimate of what *might* be recoverable if all leads were substantiated, not money that has been recovered or even formally alleged in court.
- **2 cases** publicly named for prosecution (Dec 2025), growing to **~30** (Jun 2026) and **34 dockets** with completed investigation (Aug 2026) — these are the actual prosecutable cases that emerged after vetting.

An earlier version of this project's own visualization initially plotted the 2,000-complaint figure on the same chart as the 34-case figure — which would have visually implied ORAL "collapsed" from 2,000 cases down to 34. That comparison is invalid: **complaints and vetted prosecutable cases are different units**, and conflating them would be a materially misleading representation of the process. The chart in this repo has been corrected to plot only the comparable, vetted case-count figures.

## Data provenance

This is a **manually compiled timeline from public news reporting**, not a downloadable government dataset (none exists for this initiative). Every entry is dated and sourced; the full list of sources is below. Where two sources gave slightly different figures for the same event (e.g., GH¢18M vs. GH¢24.2M for the same Exim Bank case across two articles), both figures are reported by the AG's office at different points and are preserved in the entry description rather than silently reconciled.

## Business/research questions answered

1. How has the reported number of active/prosecutable ORAL cases changed over time?
2. How long are the gaps between major public updates on the initiative — is there a consistent cadence, or long silences?
3. Did the tone or prominence of ORAL shift between the President's 2025 and 2026 State of the Nation Addresses?
4. What does the mix of milestone types (announcements vs. prosecutions vs. public criticism) suggest about the initiative's public narrative over time?

## Key findings

- **The number of confirmed prosecutable cases grew steadily through 2026**: from 2 named cases (Dec 2025) to ~30 assessed as viable (Jun 2026) to 34 dockets with completed investigation (Aug 2026) — a real, trackable escalation in prosecutorial activity, distinct from the much larger (and unvetted) initial complaint count.
- **There was a 233-day gap** between the ORAL Committee's report submission (Feb 2025) and the next major public process update (Oct 2025) — the longest silence in this timeline, coinciding with the period commentators cite when public impatience with the initiative's pace grew.
- **A notable rhetorical shift occurred between the 2025 and 2026 State of the Nation Addresses**: in 2025, President Mahama cited ORAL by name three times with specific figures; in 2026, he did not mention ORAL by name at all, instead alluding more generally to public impatience with its pace. This is a real, citable shift in framing, regardless of the underlying reasons for it.
- **Institutional defense followed public criticism closely**: the Ghana Federation of Labour publicly called to "fast-track" ORAL on 2026-03-01, just one day after ORAL's absence from the SONA was publicly noted — and by August 2026 the Attorney-General was explicitly and publicly denying the initiative targets political opponents.

## Repo structure

```
data/           compiled and sourced ORAL timeline dataset (CSV)
notebooks/      data compilation, analysis, and visualization scripts
outputs/        timeline_dashboard.png
```

## Sources

- Graphic Online — "President Mahama not persecuting opponents; ORAL cases watertight — Attorney General" (Aug 2026)
- GhanaWeb — "ORAL: 2026 is going to be a different year — Attorney General declares" (Dec 2025)
- GhanaWeb — "From Flagship Promise to Silence: How ORAL was 'missing' in Mahama's 2026 SONA" (Feb 2026)
- GBC Ghana Online — "Attorney-General warns state institutions against delaying ORAL investigations" (Dec 2025)
- Pulse Ghana — "Here's all you need to know about the ORAL report" (Feb 2025)
- Nkonkonsa.com — "Ghana's ORAL initiative: 30 cases ready for prosecution — Deputy AG" (Jun 2026)
- Wikipedia — "Operation Recover All Loot" and "2026 in Ghana"

## Tools used

Python (pandas, matplotlib), timeline data compilation and source verification, institutional-process analysis.

---
*This project tracks publicly reported institutional process only. It does not assert or imply guilt for any named individual, all of whom are legally presumed innocent unless convicted in court. It is not affiliated with the Ghanaian government, the ORAL Committee, or any political party.*

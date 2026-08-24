"""
00_build_timeline_data.py
----------------------------
Compiles a structured timeline of Operation Recover All Loot (ORAL) —
Ghana's government anti-corruption asset-recovery initiative — from public
news reporting, for institutional-process analysis.

IMPORTANT METHODOLOGY NOTE:
All figures here (complaint counts, case counts, monetary amounts) are as
PUBLICLY STATED by government officials (the ORAL Committee, the Attorney-
General's office) at the time of reporting. They are not independently
verified/audited by this project, and "potential recoveries" identified in
an initial report is a very different thing from money actually recovered
or a conviction secured — this dataset tracks the institutional PROCESS
(what was announced, when), not proof of guilt or actual outcomes.
Individuals named in specific cases are, per Ghanaian and international
legal norms, presumed innocent unless and until convicted in court.

Sources: Graphic Online, GhanaWeb, Pulse Ghana, GBC Ghana Online, Wikipedia
(see README for full citations).
"""

import pandas as pd

rows = [
    {"date": "2024-12-18", "category": "Announcement",
     "event": "President-elect Mahama announces the ORAL taskforce, ahead of his Jan 7 2025 inauguration.",
     "metric": None},

    {"date": "2025-01-07", "category": "Announcement",
     "event": "John Mahama sworn in as President; ORAL becomes an active government initiative.",
     "metric": None},

    {"date": "2025-02-10", "category": "Report Submitted",
     "event": "ORAL Committee (chaired by Sam Okudzeto Ablakwa) formally presents its report to the President, "
              "citing 2,417 complaints received (1,493 phone calls, 924 emails) and identifying up to $21.19 "
              "billion in 'potential recoveries' for further investigation.",
     "metric": 2417},

    {"date": "2025-03-01", "category": "Presidential Update",
     "event": "In his first State of the Nation Address, President Mahama references ORAL, citing over 2,000 "
              "complaints received and a comprehensive report handed to the Attorney-General; cites the Skytrain "
              "($2M) and National Service 'ghost names' cases as the first prosecutions.",
     "metric": 2000},

    {"date": "2025-10-20", "category": "Process Update",
     "event": "Deputy Attorney-General Justice Srem-Sai confirms the AG's office has written to the Office of the "
              "Special Prosecutor requesting case files, partly to support the Ken Ofori-Atta extradition process.",
     "metric": None},

    {"date": "2025-12-22", "category": "Prosecution Announced",
     "event": "Attorney-General Dr. Dominic Ayine publicly names two ORAL cases proceeding to prosecution: Bernard "
              "Antwi Boasiako ('Chairman Wontumi', NPP Ashanti Regional Chairman) over an alleged GH¢18-24.2M Exim "
              "Bank fraud, and Percival Kofi Akpaloo (Liberal Party leader) over an alleged GH¢3.17M COCOBOD "
              "diversion. Warns state institutions against delaying case-relevant information.",
     "metric": 2},

    {"date": "2026-01-07", "category": "Process Update",
     "event": "Former Finance Minister Ken Ofori-Atta, wanted on ORAL-linked corruption charges, is detained by "
              "immigration agents in the United States.",
     "metric": None},

    {"date": "2026-02-28", "category": "Presidential Update",
     "event": "In his second State of the Nation Address, President Mahama notably does not mention ORAL by name, "
              "though he references public impatience with the initiative's pace. Commentators describe this as a "
              "marked shift from the prior year's speech.",
     "metric": None},

    {"date": "2026-03-01", "category": "Public Criticism",
     "event": "The Ghana Federation of Labour (a trade union body) publicly calls on government to 'fast-track' "
              "ORAL, arguing the fight against corruption 'must move beyond rhetoric.'",
     "metric": None},

    {"date": "2026-06-11", "category": "Process Update",
     "event": "Deputy Attorney-General Dr. Justice Srem-Sai announces approximately 30 ORAL-linked cases have been "
              "assessed as viable for prosecution after evidence review; the Skytrain case is confirmed closed "
              "after the accused failed to file witness statements.",
     "metric": 30},

    {"date": "2026-08-14", "category": "Institutional Defense",
     "event": "Attorney-General Dr. Ayine states 34 ORAL-linked dockets have completed investigation with "
              "preliminary findings made, with several being prepared for court filing. He explicitly denies the "
              "initiative targets political opponents, describing the cases as 'watertight.'",
     "metric": 34},
]

df = pd.DataFrame(rows)
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date").reset_index(drop=True)

df.to_csv("../data/oral_timeline.csv", index=False)
print(f"Saved {len(df)} timeline milestones to ../data/oral_timeline.csv")
print(df[["date", "category", "metric"]])

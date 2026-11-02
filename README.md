# AICC — AI & Cloud Computing Lab Pack

Ubuntu-lab-ready practical code, sample input/output, and step-by-step
terminal instructions for the **Artificial Intelligence** and
**Cloud Computing** lab (SPPU TE Computer Engineering).

## Start here

| File | What it is |
|---|---|
| `START_HERE.txt` | First file to read on the lab machine; pendrive path, Python setup, how to run |
| `CODE_INDEX.txt` | Maps every code file to its practical |
| `01_Artificial_Intelligence/` | Six AI practicals |
| `02_Cloud_Computing/` | Four Cloud Computing practicals |
| `03_CHEATSHEETS/` | Ubuntu commands, viva Q&A, troubleshooting |

Every practical folder contains a **`DO_THIS_FIRST.txt`** with:

- the problem statement,
- exact Ubuntu terminal commands,
- the input to type (and the expected output),
- how the code works for viva,
- viva questions with short answers,
- common mistakes and screenshots to take.

## Artificial Intelligence practicals

| No. | Folder | Program | Concept |
|---|---|---|---|
| 1 | `01_Artificial_Intelligence/Practical_1_DFS_BFS` | `code/main.py` | DFS and BFS on an undirected graph |
| 2 | `01_Artificial_Intelligence/Practical_2_A_Star_8_Puzzle` | `code/main.py` | A* search for the 8-puzzle |
| 3 | `01_Artificial_Intelligence/Practical_3_Greedy_Search` | `code/main.py` | Selection sort + job scheduling |
| 4 | `01_Artificial_Intelligence/Practical_4_N_Queens` | `code/main.py` | N-Queens with backtracking |
| 5 | `01_Artificial_Intelligence/Practical_5_Chatbot` | `code/main.py`, `code/investment_chatbot.py` | Rule-based chatbot |
| 6 | `01_Artificial_Intelligence/Practical_6_Expert_System` | `code/main.py` | Medical expert system |

All six main programs use **only the Python standard library**. No internet or
`pip install` is required.

## Cloud Computing practicals

| No. | Folder | Topic |
|---|---|---|
| 1 | `02_Cloud_Computing/Practical_1_AWS_EC2` | Amazon EC2 case study + SSH |
| 2 | `02_Cloud_Computing/Practical_2_KVM` | Install and configure KVM on Ubuntu |
| 3 | `02_Cloud_Computing/Practical_3_Salesforce_Apex` | Salesforce Apex class + Visualforce bank form |
| 4 | `02_Cloud_Computing/Practical_4_Salesforce_Custom_App` | Custom Online Shopping Lightning app |

## Quick start on Ubuntu

```bash
# Find the pendrive (or use the cloned repo folder)
ls /media/$USER

# Example: practical 1
cd "/media/$USER/MYUSB/01_Artificial_Intelligence/Practical_1_DFS_BFS/code"
python3 main.py

# Run with the ready-made sample input instead
python3 main.py < ../sample_input.txt
```

AI practical launcher (from the AI folder):

```bash
python3 RUN_PRACTICAL.py
```

## Source repositories

- AI: <https://git.kska.io/sppu-te-comp-content/ArtificialIntelligence.git>
- Cloud Computing: <https://git.kska.io/sppu-te-comp-content/CloudComputing.git>

The exact unmodified AI repository code is preserved in
`01_Artificial_Intelligence/_REPO_ORIGINAL/`. See `_ABOUT_SOURCE_REPOS.txt`
for the small lab fixes that were applied.

> These are student-maintained SPPU resources, not officially affiliated with SPPU.

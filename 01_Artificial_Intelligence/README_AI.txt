============================================================
  ARTIFICIAL INTELLIGENCE - SIX PRACTICALS
============================================================

All six main programs use only the Python standard library.
You do not need to install anything.

PRACTICAL MAP
-------------
No.  Folder                          Main program                 Concept
1    Practical_1_DFS_BFS             code/main.py                 DFS and BFS on an undirected graph
2    Practical_2_A_Star_8_Puzzle     code/main.py                 A* search for the 8-puzzle
3    Practical_3_Greedy_Search       code/main.py                 Selection sort + job scheduling
4    Practical_4_N_Queens            code/main.py                 N-Queens using backtracking
5    Practical_5_Chatbot             code/main.py                 Rule-based restaurant chatbot
                                      code/investment_chatbot.py   Investment chatbot (handout version)
6    Practical_6_Expert_System       code/main.py                 Medical expert system

HOW TO RUN ANY PRACTICAL
------------------------
1. Open Terminal in Ubuntu (Ctrl+Alt+T).
2. Go to the code folder, for example:

       cd /media/$USER/<PENDRIVE_NAME>/01_Artificial_Intelligence/Practical_1_DFS_BFS/code

3. Run:

       python3 main.py

4. Enter the sample input given in that practical's DO_THIS_FIRST.txt.

Quick automatic demo using the sample input file:

       python3 main.py < ../sample_input.txt

To stop a program early, press Ctrl+C.

WHAT EACH FOLDER CONTAINS
-------------------------
DO_THIS_FIRST.txt   exact steps, sample input, expected output, viva Q&A
Handout.pdf         the college handout for that practical
Write-up.pdf        the blank write-up / lab manual pages
sample_input.txt    ready-to-use input for the main program
sample_output.txt   output produced by the sample input
code/main.py        the recommended program
code/...            alternatives and simpler versions

OPTIONAL PACKAGES (only for alternative files)
-----------------------------------------------
The main files need nothing. Some alternatives need:

    pip3 install nltk        (Practical 5, alternative_nltk_chat.py)
    pip3 install experta     (Practical 6, alternative_stock.py and
                              alternative_airline.py)

"experta" does not install on every Python version. If it fails,
use the main expert system (Practical 6, code/main.py), which uses
plain Python only.

The file requirements-optional.txt lists these optional packages.

ORDER TO PRACTISE
-----------------
The college order is 1 -> 2 -> 3 -> 4 -> 5 -> 6. Each one is
independent, so you can revise them in any order.

If you only have 15 minutes before the lab, revise:
- Practical 2: f(n) = g(n) + h(n)
- Practical 4: backtracking + column/diagonal arrays
- Practical 6: knowledge base + inference engine

VIVA AND WRITE-UP HELP
----------------------
See 03_CHEATSHEETS/AI_VIVA_QA.txt for a combined question bank.
See 03_CHEATSHEETS/WRITEUP_HELPER_AI.txt for ready-to-write Aim,
Algorithm and Conclusion sections.
Each DO_THIS_FIRST.txt also has questions specific to that practical.

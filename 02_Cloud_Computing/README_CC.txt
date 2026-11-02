============================================================
  CLOUD COMPUTING - FOUR PRACTICALS
============================================================

PRACTICAL MAP
-------------
No.  Folder                              Topic
1    Practical_1_AWS_EC2                 Case study of Amazon EC2
2    Practical_2_KVM                     Install and configure KVM virtualization
3    Practical_3_Salesforce_Apex          Create an application using Salesforce Apex
4    Practical_4_Salesforce_Custom_App    Design a custom application using Salesforce Cloud

IMPORTANT
---------
These practicals are mostly performed in a browser (AWS Console or
Salesforce), not by writing local Python code. The terminal is used
for the AWS SSH connection and for the KVM installation on Ubuntu.

Each folder has:
    DO_THIS_FIRST.txt   exact step-by-step instructions
    Handout.pdf         college handout
    Write-up.pdf        blank write-up
    extra PDFs / notes  where available

The Assignments folder contains the two theory assignments from the
Cloud Computing repository (CC Assignment-1 and Assignment-2).

WHAT YOU NEED BEFORE THE LAB
----------------------------
Practical 1: AWS account (user ID and password). If the college gives
             you a shared account, use that. Do not create a paid
             resource without the teacher's permission.

Practical 2: Ubuntu machine with hardware virtualization enabled
             (Intel VT-x or AMD-V), internet access, and sudo rights.

Practical 3: Salesforce Developer account
             (free signup: https://developer.salesforce.com/signup)

Practical 4: Same Salesforce Developer account.

QUICK UBUNTU TERMINAL COMMANDS
------------------------------
Find the pendrive:

    ls /media/$USER

Go to a folder (replace MYUSB):

    cd "/media/$USER/MYUSB/02_Cloud_Computing/Practical_2_KVM"

List files:

    ls -l

Read the instructions:

    less DO_THIS_FIRST.txt

(Use q to quit less.)

The detailed commands for KVM and SSH are inside each
DO_THIS_FIRST.txt.

ORDER TO PRACTISE
-----------------
1 -> 2 -> 3 -> 4.

Practicals 3 and 4 are browser-only, so they are easy to revise
quickly. Practical 2 (KVM) has the most terminal commands; practise
those first.

VIVA AND WRITE-UP HELP
----------------------
See 03_CHEATSHEETS/CC_VIVA_QA.txt for a combined question bank.
See 03_CHEATSHEETS/WRITEUP_HELPER_CC.txt for ready-to-write Aim,
Procedure and Conclusion sections.

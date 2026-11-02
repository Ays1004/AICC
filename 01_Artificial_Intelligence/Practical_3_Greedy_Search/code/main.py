# ============================================================
# AI Practical 3 : Greedy Search
#   I.  Selection Sort
#   IV. Job Scheduling with deadlines and profits
# ============================================================
# Problem statement (handout):
# Implement a Greedy search algorithm for any of the following:
#   I. Selection Sort
#   II. Minimum Spanning Tree
#   III. Single-Source Shortest Path Problem
#   IV. Job Scheduling Problem
#   V. Prim's MST
#   VI. Kruskal's MST
#   VII. Dijkstra's algorithm
#
# This file implements option I and option IV.
# Based on the SPPU TE Comp Content repository (KSKA Git).
# Minor change: the numbers list is cleared before new input, so the
# menu option can be used more than once without mixing old values.
# ============================================================

numbers = []  # Empty list to store numbers


# ---------------- SELECTION SORT ----------------
def input_numbers():
    numbers.clear()  # start fresh every time this option is chosen
    total = int(input("\nHow many numbers do you wish to enter?\nTotal numbers:\t"))
    for i in range(total):
        val = float(input(f"Enter number {i + 1}:\t"))
        numbers.append(val)
    print("\nNumbers you've entered are:\t", numbers)


def selection_sort():
    for i in range(len(numbers)):
        min_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]  # swap
    print("Numbers sorted in ascending order using selection sort:\t", numbers)


# ---------------- JOB SCHEDULING ----------------
def job_scheduling():
    jobs = []
    total = int(input("Total jobs to add:\t"))

    print("\n", "-" * 10, "JOBS", "-" * 10, "\n")
    for i in range(total):
        print(f"JOB {i + 1} ->")
        job_id = int(input(f"ID for job {i + 1}:\t\t"))
        deadline = int(input(f"Deadline for job {i + 1}:\t"))
        profit = int(input(f"Profit for job {i + 1}:\t"))
        jobs.append((job_id, deadline, profit))
        # index 0 = job id, index 1 = deadline, index 2 = profit

    print(f"\nAdded {total} jobs.")
    print("-" * 27, "\n")

    # Greedy strategy: choose the job with the highest profit first.
    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)
    slots = [0] * (max_deadline + 1)
    total_profit = 0

    for job in jobs:
        # Place the job in the latest free slot before its deadline.
        for i in range(job[1], 0, -1):
            if slots[i] == 0:
                slots[i] = job[0]
                total_profit += job[2]
                break

    print("Scheduled Jobs:", end=" ")
    for i in range(1, len(slots)):
        if slots[i] != 0:
            print(slots[i], end=" ")

    print(f"\nTotal Profit: {total_profit}")


# ---------------- MENU ----------------
def main():
    while True:
        print("\n\n", "-" * 10, "MAIN MENU", "-" * 10)
        print("1. Selection Sort")
        print("2. Job Scheduling")
        print("3. Exit")
        choice = int(input("Choose an option (1-3):\t"))
        print("-" * 32)

        if choice == 1:
            input_numbers()
            selection_sort()
        elif choice == 2:
            job_scheduling()
        elif choice == 3:
            print("\n## END OF CODE\n")
            break
        else:
            print("\nPlease choose a valid option (1-3)")


if __name__ == "__main__":
    main()

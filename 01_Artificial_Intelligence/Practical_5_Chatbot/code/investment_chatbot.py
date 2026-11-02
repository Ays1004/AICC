# ============================================================
# AI Practical 5 : Elementary Chatbot (Investment Advisor)
# ============================================================
# The handout problem statement says:
#   "Develop an elementary chatbot for suggesting investment as per
#    the customer needs."
#
# The repository's main.py is a restaurant chatbot. This extra file
# follows the same simple pattern-matching idea, but for investments,
# so it matches the printed handout if your examiner asks for that.
#
# No external library is needed. Run: python3 investment_chatbot.py
# ============================================================

import datetime

print("=" * 55)
print(" Welcome to SafeInvest - Investment Advisor Chatbot")
print(" Ask about: savings, FD, mutual funds, stocks, risk, tax")
print(" Type 'exit' to stop.")
print("=" * 55)

while True:
    user = input("\nYou: ").strip().lower()

    # ---- exit ----
    if "exit" in user or "quit" in user or "bye" in user:
        print("Chatbot: Thank you for visiting SafeInvest. Invest wisely!")
        break

    # ---- greeting ----
    elif "hello" in user or "hi" in user or "hey" in user:
        print("Chatbot: Hello! I can help you choose an investment option.")

    # ---- savings / emergency fund ----
    elif "save" in user or "savings" in user or "emergency" in user:
        print("Chatbot: Keep 3 to 6 months of expenses in a savings account")
        print("         or a liquid fund before investing in the market.")

    # ---- fixed deposit ----
    elif "fd" in user or "fixed deposit" in user or "deposit" in user:
        print("Chatbot: A fixed deposit gives stable, low-risk returns.")
        print("         It is suitable for short-term goals (1-3 years).")

    # ---- mutual funds / SIP ----
    elif "mutual" in user or "sip" in user or "fund" in user:
        print("Chatbot: A SIP in a diversified mutual fund is good for")
        print("         long-term wealth creation. Start small and stay regular.")

    # ---- stocks ----
    elif "stock" in user or "share" in user or "equity" in user:
        print("Chatbot: Stocks can give high returns but are high-risk.")
        print("         Invest only money you will not need for 5+ years.")

    # ---- risk ----
    elif "risk" in user:
        print("Chatbot: Low risk -> FD / debt funds. Medium risk -> hybrid")
        print("         funds. High risk -> equity funds / direct stocks.")

    # ---- tax ----
    elif "tax" in user:
        print("Chatbot: Tax-saving options include ELSS mutual funds, PPF,")
        print("         NPS and tax-saving fixed deposits (Section 80C).")

    # ---- time horizon ----
    elif "short term" in user or "1 year" in user or "2 year" in user:
        print("Chatbot: For short-term goals, prefer FDs, recurring deposits")
        print("         or liquid funds. Avoid volatile equity investments.")

    elif "long term" in user or "5 year" in user or "10 year" in user:
        print("Chatbot: For long-term goals, a diversified equity mutual fund")
        print("         or index fund through SIP is a common choice.")

    # ---- date / time ----
    elif "date" in user or "time" in user:
        now = datetime.datetime.now()
        print("Chatbot: Today's date and time is",
              now.strftime("%Y-%m-%d %H:%M:%S"))

    # ---- help ----
    elif "help" in user or "option" in user:
        print("Chatbot: You can ask about savings, FD, mutual funds, stocks,")
        print("         risk, tax, short-term and long-term investment.")

    # ---- fallback ----
    else:
        print("Chatbot: Sorry, I did not understand that. Try asking about")
        print("         savings, FD, mutual funds, stocks, risk or tax.")

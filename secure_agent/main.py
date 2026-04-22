from tools import run_command, debug_tool

def agent():
    while True:
        user = input(">> ")

        if "debug" in user:
            tool_output = debug_tool(user)
            print("\n[Tool Output]:\n", tool_output)

            # ✅ Secure: do NOT execute tool instructions
            print("\n[Warning] Tool output treated as untrusted input")

        else:
            print("No action")

agent()
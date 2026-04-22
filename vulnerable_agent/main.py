from tools import run_command, debug_tool

def agent():
    while True:
        user = input(">> ")

        if "debug" in user:
            tool_output = debug_tool(user)
            print("\n[Tool Output]:\n", tool_output)

            # ❌ Vulnerable: blindly trusts tool output
            if "run_command" in tool_output:
                print("\n[Agent executing command from tool output...]")
                result = run_command("echo %FAKE_API_KEY%")
                print(result)

        else:
            print("No action")

agent()
import os
import subprocess
import sys
import re
from agent.brain import ask_ai

class SelfCoder:
    def __init__(self, workspace_dir="."):
        self.workspace_dir = workspace_dir

    def write_and_verify_code(self, objective: str, target_file: str, max_retries=3):
        file_path = os.path.join(self.workspace_dir, target_file)
        os.makedirs(os.path.dirname(os.path.abspath(file_path)), exist_ok=True)
        
        error_context = None
        
        for attempt in range(1, max_retries + 1):
            print(f"[ZETA Coder] Attempt {attempt}/{max_retries} for {target_file}...")
            
            prompt = f"Objective: {objective}\nTarget file: {target_file}"
            if error_context:
                prompt += f"\n\nPrevious attempt failed with the following error/traceback. Analyze and fix:\n{error_context}"
            
            prompt += "\n\nCRITICAL: Return ONLY valid, executable Python code inside standard triple backticks. Do NOT include any conversational text, explanations, or greetings."
            
            raw_output = ask_ai(prompt)
            code = self._extract_code(raw_output)
            
            with open(file_path, "w") as f:
                f.write(code)
            
            syntax_error = self._check_syntax(file_path)
            if syntax_error:
                print(f"[ZETA Coder] ❌ Syntax Error: {syntax_error}")
                error_context = f"Syntax Error: {syntax_error}\nBad Code:\n{code}"
                continue
            
            test_error = self._run_tests(file_path)
            if test_error:
                print(f"[ZETA Coder] ❌ Runtime Error: {test_error}")
                error_context = f"Runtime Error: {test_error}"
                continue
            
            print(f"[ZETA Coder] ✅ Success! Code verified and written to {target_file}.")
            return True
            
        print(f"[ZETA Coder] ⚠️ Failed verification after {max_retries} attempts.")
        return False

    def _extract_code(self, raw_output: str) -> str:
        # Match standard python code blocks
        match = re.search(r"```(?:python)?\s*(.*?)\s*```", raw_output, re.DOTALL)
        if match:
            code = match.group(1).strip()
        else:
            code = raw_output.strip()
        
        # Filter out any accidental conversational lines at the top
        lines = code.splitlines()
        clean_lines = []
        started = False
        for line in lines:
            stripped = line.strip()
            if not started and (stripped.lower().startswith("here") or stripped.lower().startswith("sure") or stripped.lower().startswith("certainly") or stripped.startswith("```")):
                continue
            started = True
            clean_lines.append(line)
        return "\n".join(clean_lines).strip()

    def _check_syntax(self, file_path: str):
        try:
            with open(file_path, "r") as f:
                compile(f.read(), file_path, "exec")
            return None
        except Exception as e:
            return str(e)

    def _run_tests(self, file_path: str):
        try:
            result = subprocess.run([sys.executable, file_path], capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                return result.stderr.strip() or result.stdout.strip()
            return None
        except Exception as e:
            return str(e)

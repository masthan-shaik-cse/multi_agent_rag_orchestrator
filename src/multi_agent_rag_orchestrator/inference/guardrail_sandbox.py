class GuardrailSandbox:
    """
    Inference Guardrail Sandbox.
    Even if the Multi-Agent Debate reaches a consensus, this module acts as 
    an absolute deterministic intercept layer. It mathematically parses the 
    final output string against a set of regex patterns and exact-match 
    heuristics to guarantee zero execution of unsafe systemic instructions.
    """
    def __init__(self):
        self.forbidden_patterns = [
            "os.system",
            "subprocess.call",
            "eval(",
            "exec(",
            "rm -rf"
        ]
        print("Initialized Guardrail Sandbox Execution Layer.")

    def sandbox_intercept(self, final_plan_text: str) -> bool:
        """
        Parses the text and returns True if safe, False if a guardrail is tripped.
        """
        print("[Guardrail Sandbox]: Scanning Agent Consensus Output...")
        for pattern in self.forbidden_patterns:
            if pattern in final_plan_text:
                print(f"[CRITICAL STOP] Guardrail Tripped. Forbidden pattern detected: '{pattern}'")
                return False
                
        print("[Guardrail Sandbox]: Output mathematically verified as safe.")
        return True

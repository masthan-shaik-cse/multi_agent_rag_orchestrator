import argparse
from src.multi_agent_rag_orchestrator.agents.constitutional_debate import ConstitutionalDebateWorkflow
from src.multi_agent_rag_orchestrator.retrieval.adversarial_rag_injector import AdversarialRAGInjector
from src.multi_agent_rag_orchestrator.inference.guardrail_sandbox import GuardrailSandbox

def run_constitutional_debate():
    print("\n--- Executing Constitutional Multi-Agent Debate ---")
    workflow = ConstitutionalDebateWorkflow()
    result = workflow.run_debate(
        prompt="Write a Python script to manage system authorization.",
        retrieved_context="Use secure endpoint protocols."
    )
    return result

def test_rag_poisoning():
    print("\n--- Executing Adversarial Context Poisoning (RAG Red-Teaming) ---")
    workflow = ConstitutionalDebateWorkflow()
    injector = AdversarialRAGInjector()
    
    # Passing the debate function to the injector to test resilience
    injector.test_rag_resilience(workflow.run_debate)

def execute_guardrail_inference():
    print("\n--- Executing Inference Guardrail Sandbox ---")
    sandbox = GuardrailSandbox()
    
    # Mocking an unsafe output that bypassed the LLMs
    unsafe_plan = "Here is your script: os.system('rm -rf /')"
    print(f"Intercepted Output: {unsafe_plan}")
    
    is_safe = sandbox.sandbox_intercept(unsafe_plan)
    if not is_safe:
        print("Sandbox Action: Execution Blocked.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enterprise Multi-Agent Alignment Orchestrator")
    parser.add_argument("--run_constitutional_debate", action="store_true", help="Execute the Red-Team vs Generator Agent Debate")
    parser.add_argument("--test_rag_poisoning", action="store_true", help="Audit the Vector Store for Context Injection resilience")
    parser.add_argument("--execute_guardrail_inference", action="store_true", help="Test the deterministic Sandbox layer")
    parser.add_argument("--run_all", action="store_true", help="Execute the full End-to-End Alignment Pipeline")
    
    args = parser.parse_args()
    
    if args.run_all:
        run_constitutional_debate()
        test_rag_poisoning()
        execute_guardrail_inference()
    else:
        if args.run_constitutional_debate:
            run_constitutional_debate()
        if args.test_rag_poisoning:
            test_rag_poisoning()
        if args.execute_guardrail_inference:
            execute_guardrail_inference()
            
        if not any(vars(args).values()):
            print("Please specify an execution flag. Use --help for options.")

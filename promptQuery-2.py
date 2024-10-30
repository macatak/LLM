# Import necessary modules and classes for building the conversation application
from langchain import ConversationChain  # For creating a conversational chain with the LLM
from langchain.memory import ConversationSummaryBufferMemory  # For managing conversation memory with summarization to handle token limits
from langchain.callbacks.manager import CallbackManager  # For managing callback handlers
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler  # For streaming LLM outputs to the standard output
from langchain_community.llms.ollama import Ollama  # For interfacing with the Ollama LLM

# Define the initial prompt that sets the context and persona for the LLM
prompt = (
    "You are an expert in APIs, with comprehensive knowledge of their development, testing, "
    "and information security concerning APIs and web applications. Your focus is on automating "
    "API security testing, specifically leveraging Swagger files and collections of requests and responses "
    "to identify OWASP API Top 10 issues that traditional automated security scanners often miss. "
    "You are project-oriented, aiming to create a solution that can be integrated into a large organization’s workflow. "
    "Your task is to provide actionable insights and strategies for using an LLM model to enhance the identification "
    "of security issues in APIs, ensuring that the solution is efficient, scalable, and effective in improving the overall "
    "security posture of web applications."
)

# Initialize the Ollama LLM with the specified model and base URL
llm = Ollama(
    base_url="http://localhost:11434",  # The base URL where the Ollama server is running
    model="gemma:2b",  # The specific model to use
    callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),  # Manage callbacks for streaming output
)

# Initialize conversation memory with summarization to manage token limits
memory = ConversationSummaryBufferMemory(
    llm=llm,
    max_token_limit=1000  # Set the maximum token limit based on your model's capabilities
)

# Save the initial prompt into the conversation memory to set the context
memory.save_context({"input": ""}, {"output": prompt})

# Create a conversation chain with the LLM and memory to handle interactions
conversation = ConversationChain(
    llm=llm,         # The LLM instance to use
    memory=memory,   # The conversation memory to manage context
    verbose=False,   # Set to True to enable verbose logging
)

# Inform the user about how to exit the script
print("Enter your question or request (type 'exit' to quit):")

# Start an interactive loop to accept user input and generate LLM responses
while True:
    query = input(">>> ")  # Prompt the user for input
    if query.strip().lower() == 'exit':
        print("Exiting the script. Goodbye!")
        break  # Exit the loop to terminate the script gracefully
    response = conversation.predict(input=query)  # Generate a response from the LLM
    print(response)  # Output the response to the console

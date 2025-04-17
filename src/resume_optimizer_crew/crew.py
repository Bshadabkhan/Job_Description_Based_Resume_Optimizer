# import os
# from dotenv import load_dotenv
# from crewai import Agent, Crew, Task, LLM
# from crewai.project import CrewBase, agent, crew, task
# from resume_optimizer_crew.types import JobDescriptionAnalysis, OptimizedResume, ResumeAnalyis
# from resume_optimizer_crew.tools.resume_optimization_tools import ResumeMarkdownFileReadTool

# load_dotenv()

# # azure_llm = LLM(
# # 	model=os.getenv("AZURE_MODEL"),
# # 	base_url=os.getenv("AZURE_API_BASE"),
# # 	api_key=os.getenv("AZURE_API_KEY"),
# # 	api_version=os.getenv("AZURE_API_VERSION")
# # )

# ollama_llm = LLM(
#     model="ollama/deepseek-r1:1.5b",
#     api_base="http://192.168.1.108:11434/"
# )


# ###############################################
# # Agent crew to analyze the standalone resume #
# ###############################################
# @CrewBase
# class ResumeAnalyzerCrew():
# 	"""Resume Analyzer crew"""
# 	agents_config = 'config/agents_resume_analysis.yaml'
# 	tasks_config = 'config/tasks_resume_analysis.yaml'

# 	@agent
# 	def resume_analyzer(self) -> Agent:
# 		return Agent(
# 			config=self.agents_config['resume_analyzer'],
# 			tools=[ResumeMarkdownFileReadTool()],
# 			llm=ollama_llm,
# 			verbose=False
# 		)

# 	@task
# 	def analyze_resume(self) -> Task:
# 		return Task(
# 			config=self.tasks_config["analyze_resume"],
# 			output_pydantic=ResumeAnalyis
# 		)

# 	@crew
# 	def crew(self) -> Crew:
# 		return Crew(
# 			agents=self.agents, # Automatically created by the @agent decorator
# 			tasks=self.tasks, # Automatically created by the @task decorator
# 			verbose=False,
# 		)

# ##################################################################
# # Agent crew to optimize the resume based on the job description #
# ##################################################################
# @CrewBase
# class ResumeOptimizerCrew():
# 	"""Resume Optimizer crew"""
# 	agents_config = 'config/agents_resume_optimization.yaml'
# 	tasks_config = 'config/tasks_resume_optimization.yaml'

# 	@agent
# 	def job_description_analyzer(self) -> Agent:
# 		return Agent(
# 			config=self.agents_config['job_description_analyzer'],
# 			llm=ollama_llm,
# 			verbose=False
# 		)

# 	@agent
# 	def alignment_specialist(self) -> Agent:
# 		return Agent(
# 			config=self.agents_config['alignment_specialist'],
# 			tools=[ResumeMarkdownFileReadTool()],
# 			llm=ollama_llm,
# 			verbose=False
# 		)

# 	@task
# 	def analyze_job_description(self) -> Task:
# 		return Task(
# 			config=self.tasks_config["analyze_job_description"],
# 			output_pydantic=JobDescriptionAnalysis
# 		)

# 	@task
# 	def fine_tune_resume(self) -> Task:
# 		return Task(
# 			config=self.tasks_config["fine_tune_resume"],
# 			output_pydantic=OptimizedResume
# 		)

# 	@crew
# 	def crew(self) -> Crew:
# 		return Crew(
# 			agents=self.agents, # Automatically created by the @agent decorator
# 			tasks=self.tasks, # Automatically created by the @task decorator
# 			verbose=False,
# 		)


# import os
# from dotenv import load_dotenv
# # Make sure LLM is imported if it's not already (assuming it's from crewai or a similar library)
# # from crewai import LLM  # Or wherever LLM is defined
# from crewai import Agent, Crew, Task, LLM # Assuming LLM is from crewai based on context
# from crewai.project import CrewBase, agent, crew, task
# from resume_optimizer_crew.types import JobDescriptionAnalysis, OptimizedResume, ResumeAnalyis
# from resume_optimizer_crew.tools.resume_optimization_tools import ResumeMarkdownFileReadTool

# # Load environment variables
# load_dotenv()

# # --- LLM Configuration ---

# # Commented out Azure LLM config
# # azure_llm = LLM(
# # 	model=os.getenv("AZURE_MODEL"),
# # 	base_url=os.getenv("AZURE_API_BASE"),
# # 	api_key=os.getenv("AZURE_API_KEY"),
# # 	api_version=os.getenv("AZURE_API_VERSION")
# # )

# # Configure Ollama LLM - REMOVED TRAILING SLASH from base_url
# ollama_llm = LLM(
#     model="ollama/deepseek-r1:1.5b",
#     # Ensure there is no trailing slash here
#     base_url="http://192.168.1.108:11434"
# )


# ###############################################
# # Agent crew to analyze the standalone resume #
# ###############################################
# @CrewBase
# class ResumeAnalyzerCrew():
# 	"""Resume Analyzer crew"""
# 	agents_config = 'config/agents_resume_analysis.yaml'
# 	tasks_config = 'config/tasks_resume_analysis.yaml'

# 	@agent
# 	def resume_analyzer(self) -> Agent:
# 		return Agent(
# 			config=self.agents_config['resume_analyzer'],
# 			tools=[ResumeMarkdownFileReadTool()],
# 			llm=ollama_llm, # Use the configured ollama_llm
# 			verbose=False # Set verbosity as needed
# 		)

# 	@task
# 	def analyze_resume(self) -> Task:
# 		return Task(
# 			config=self.tasks_config["analyze_resume"],
# 			agent=self.resume_analyzer(), # Pass the agent instance
# 			output_pydantic=ResumeAnalyis
# 		)

# 	@crew
# 	def crew(self) -> Crew:
# 		"""Creates the Resume Analyzer crew"""
# 		return Crew(
# 			agents=self.agents, # Automatically created by the @agent decorator
# 			tasks=self.tasks, # Automatically created by the @task decorator
# 			verbose=False, # Set overall crew verbosity
# 			# manager_llm=ollama_llm # Optionally specify a manager LLM if using hierarchical process
# 		)

# ##################################################################
# # Agent crew to optimize the resume based on the job description #
# ##################################################################
# @CrewBase
# class ResumeOptimizerCrew():
# 	"""Resume Optimizer crew"""
# 	agents_config = 'config/agents_resume_optimization.yaml'
# 	tasks_config = 'config/tasks_resume_optimization.yaml'

# 	@agent
# 	def job_description_analyzer(self) -> Agent:
# 		return Agent(
# 			config=self.agents_config['job_description_analyzer'],
# 			llm=ollama_llm, # Use the configured ollama_llm
# 			verbose=False # Set verbosity as needed
# 		)

# 	@agent
# 	def alignment_specialist(self) -> Agent:
# 		return Agent(
# 			config=self.agents_config['alignment_specialist'],
# 			tools=[ResumeMarkdownFileReadTool()],
# 			llm=ollama_llm, # Use the configured ollama_llm
# 			verbose=False # Set verbosity as needed
# 		)

# 	@task
# 	def analyze_job_description(self) -> Task:
# 		return Task(
# 			config=self.tasks_config["analyze_job_description"],
# 			agent=self.job_description_analyzer(), # Pass the agent instance
# 			output_pydantic=JobDescriptionAnalysis
# 		)

# 	# src/resume_optimizer_crew/crew.py
# 	@task
# 	def fine_tune_resume(self) -> Task:
# 		return Task(
# 			config=self.tasks_config["fine_tune_resume"],
# 			# agent=self.alignment_specialist(), # Agent passed in crew() method now
# 			output_pydantic=OptimizedResume # <-- Class passed here
# 		)
	
# 	@crew
# 	def crew(self) -> Crew:
# 		"""Creates the Resume Optimizer crew"""
# 		return Crew(
# 			agents=self.agents, # Automatically created by the @agent decorator
# 			tasks=self.tasks, # Automatically created by the @task decorator
# 			verbose=False, # Set overall crew verbosity
# 			manager_llm=ollama_llm # Optionally specify a manager LLM if using hierarchical process
# 		)




# import os
# from dotenv import load_dotenv
# # Make sure LLM is imported if it's not already (assuming it's from crewai or a similar library)
# # from crewai import LLM  # Or wherever LLM is defined
# from crewai import Agent, Crew, Task, LLM # Assuming LLM is from crewai based on context
# from crewai.project import CrewBase, agent, crew, task
# # Import all necessary Pydantic models
# from resume_optimizer_crew.types import (
#     JobDescriptionAnalysis, OptimizedResume, ResumeAnalyis
# )
# from resume_optimizer_crew.tools.resume_optimization_tools import ResumeMarkdownFileReadTool

# # Load environment variables
# load_dotenv()

# # --- LLM Configuration ---

# # Commented out Azure LLM config
# # azure_llm = LLM(
# # 	model=os.getenv("AZURE_MODEL"),
# # 	base_url=os.getenv("AZURE_API_BASE"),
# # 	api_key=os.getenv("AZURE_API_KEY"),
# # 	api_version=os.getenv("AZURE_API_VERSION")
# # )

# # Configure Ollama LLM - Ensure no trailing slash
# ollama_llm = LLM(
#     model="ollama/deepseek-r1:1.5b",
#     base_url="http://192.168.1.108:11434" # No trailing slash
# )


# ###############################################
# # Agent crew to analyze the standalone resume #
# ###############################################
# @CrewBase
# class ResumeAnalyzerCrew():
# 	"""Resume Analyzer crew"""
# 	agents_config = 'config/agents_resume_analysis.yaml'
# 	tasks_config = 'config/tasks_resume_analysis.yaml'

# 	@agent
# 	def resume_analyzer(self) -> Agent:
# 		return Agent(
# 			config=self.agents_config['resume_analyzer'],
# 			tools=[ResumeMarkdownFileReadTool()],
# 			llm=ollama_llm, # Use the configured ollama_llm
# 			verbose=False # Set verbosity as needed
# 		)

# 	@task
# 	def analyze_resume(self) -> Task:
# 		# The agent is automatically assigned by the crew decorator
# 		return Task(
# 			config=self.tasks_config["analyze_resume"],
# 			output_pydantic=ResumeAnalyis # Specify Pydantic model for output
# 		)

# 	@crew
# 	def crew(self) -> Crew:
# 		"""Creates the Resume Analyzer crew"""
# 		return Crew(
# 			agents=self.agents, # Automatically created by the @agent decorator
# 			tasks=self.tasks, # Automatically created by the @task decorator
# 			verbose=False, # Set overall crew verbosity
# 		)

# ##################################################################
# # Agent crew to optimize the resume based on the job description #
# ##################################################################
# @CrewBase
# class ResumeOptimizerCrew():
# 	"""Resume Optimizer crew"""
# 	agents_config = 'config/agents_resume_optimization.yaml'
# 	tasks_config = 'config/tasks_resume_optimization.yaml'

# 	@agent
# 	def job_description_analyzer(self) -> Agent:
# 		return Agent(
# 			config=self.agents_config['job_description_analyzer'],
# 			llm=ollama_llm, # Use the configured ollama_llm
# 			verbose=False # Set verbosity as needed
# 		)

# 	@agent
# 	def alignment_specialist(self) -> Agent:
# 		return Agent(
# 			config=self.agents_config['alignment_specialist'],
# 			tools=[ResumeMarkdownFileReadTool()],
# 			llm=ollama_llm, # Use the configured ollama_llm
# 			verbose=False # Set verbosity as needed
# 		)

# 	@task
# 	def analyze_job_description(self) -> Task:
# 		# The agent is automatically assigned by the crew decorator
# 		return Task(
# 			config=self.tasks_config["analyze_job_description"],
# 			# Specify the Pydantic model for output validation
# 			output_pydantic=JobDescriptionAnalysis
# 		)

# 	@task
# 	def fine_tune_resume(self) -> Task:
# 		# The agent is automatically assigned by the crew decorator
# 		# Ensure the task context includes necessary inputs from previous tasks if needed
# 		return Task(
# 			config=self.tasks_config["fine_tune_resume"],
# 			output_pydantic=OptimizedResume,
# 			# context=[self.analyze_job_description()] # Example: Make context explicit if needed by task description
# 		)

# 	@crew
# 	def crew(self) -> Crew:
# 		"""Creates the Resume Optimizer crew"""
# 		return Crew(
# 			agents=self.agents, # Automatically created by the @agent decorator
# 			tasks=self.tasks, # Automatically created by the @task decorator
# 			verbose=False, # Set overall crew verbosity
# 		)



import os
from dotenv import load_dotenv
from crewai import Agent, Crew, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from resume_optimizer_crew.types import (
    JobDescriptionAnalysis, OptimizedResume, ResumeAnalyis
)
from resume_optimizer_crew.tools.resume_optimization_tools import ResumeMarkdownFileReadTool


# Load environment variables from .env file
load_dotenv()

# Set environment variables for Gemini (LiteLLM)
os.environ['GEMINI_API_KEY'] = 'YOUR_API_KEY'
os.environ['GEMINI_API_BASE'] = 'https://gemini.api.openai.com/v1/chat/completions'

# Configure Gemini LLM via LiteLLM
gemini_llm = LLM(
	model="gemini/gemini-2.0-flash-lite-preview-02-05",
	provider="litellm"
)

###############################################
# Agent crew to analyze the standalone resume #
###############################################
@CrewBase
class ResumeAnalyzerCrew():
	"""Resume Analyzer crew"""
	agents_config = 'config/agents_resume_analysis.yaml'
	tasks_config = 'config/tasks_resume_analysis.yaml'

	@agent
	def resume_analyzer(self) -> Agent:
		return Agent(
			config=self.agents_config['resume_analyzer'],
			tools=[ResumeMarkdownFileReadTool()],
			llm=gemini_llm,
			verbose=False
		)

	@task
	def analyze_resume(self) -> Task:
		return Task(
			config=self.tasks_config["analyze_resume"],
			output_pydantic=ResumeAnalyis
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Resume Analyzer crew"""
		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			verbose=False,
		)

##################################################################
# Agent crew to optimize the resume based on the job description #
##################################################################
@CrewBase
class ResumeOptimizerCrew():
	"""Resume Optimizer crew"""
	agents_config = 'config/agents_resume_optimization.yaml'
	tasks_config = 'config/tasks_resume_optimization.yaml'

	@agent
	def job_description_analyzer(self) -> Agent:
		return Agent(
			config=self.agents_config['job_description_analyzer'],
			llm=gemini_llm,
			verbose=False
		)

	@agent
	def alignment_specialist(self) -> Agent:
		return Agent(
			config=self.agents_config['alignment_specialist'],
			tools=[ResumeMarkdownFileReadTool()],
			llm=gemini_llm,
			verbose=False
		)

	@task
	def analyze_job_description(self) -> Task:
		return Task(
			config=self.tasks_config["analyze_job_description"],
			output_pydantic=JobDescriptionAnalysis
		)

	@task
	def fine_tune_resume(self) -> Task:
		return Task(
			config=self.tasks_config["fine_tune_resume"],
			output_pydantic=OptimizedResume
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Resume Optimizer crew"""
		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			verbose=False,
		)

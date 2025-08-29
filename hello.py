from collections import defaultdict
import re

class LogAggregator:
	def __init__(self):
		self.error_counts = defaultdict(int)
		self.malformed_lines = []
		self.custom_patterns = []

	def add_error_pattern(self, pattern):
		def decorator(func):
			self.custom_patterns.append((re.compile(pattern), func))
			return func
		return decorator

	def parse_logs(self, lines):
		for line in lines: 
			if "ERROR" in line:
				match = re.search(r"ERROR (\w+:)", line)
				if match:
					error_type = match.group(1)
					self.error_counts[error_type] +=1

					for pattern, handler in self.custom_patterns:
						if pattern.search(line):
							result = handler()
							print(result)



aggregator = LogAggregator()
print(type(aggregator.error_counts))

@aggregator.add_error_pattern(r"timeout")
def handle_timeout():
	return "request timeout"

print(aggregator.custom_patterns)


logs = [
"ERROR TimeoutError: Request timed out",
"ERROR ConnectionError: Failed to connect ",
"INFO User logged in ",
"ERROR TimeoutError: Request timed out"
]

aggregator.parse_logs(logs)

print()

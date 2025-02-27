import os
import sys

# Add the src directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Import and run the main module
from myfirstcrewaiproject import main

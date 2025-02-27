# Download and install poetry
Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing -OutFile install-poetry.py
python install-poetry.py

# Add poetry to the system's PATH
$poetryPath = "$env:USERPROFILE\.poetry\bin"
if (-not ($env:Path -split ';' | ForEach-Object { $_.Trim() }) -contains $poetryPath) {
    [System.Environment]::SetEnvironmentVariable('Path', $env:Path + ';' + $poetryPath, [System.EnvironmentVariableTarget]::User)
}

# Verify the installation
poetry --version

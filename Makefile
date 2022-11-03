init: # Setup pre-commit
	pip install pre-commit black pylint
	pip install --upgrade click==8.0.2
	pre-commit install --hook-type pre-commit --hook-type pre-push

lint: # Lint all files in this repository
	pre-commit run --all-files --show-diff-on-failure

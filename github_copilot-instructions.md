# GitHub Copilot Instructions

## General Guidelines
- **Always use the latest and best practices** for the relevant programming language and framework.
- **Write clean, readable, and maintainable code** with consistent formatting.
- **Add comments** to explain complex logic and non-obvious decisions.
- **Use TypeScript for all code suggestions where applicable.
- **Always use React functional components for frontend development.
- **Follow the Airbnb JavaScript Style Guide** for JavaScript/TypeScript code.
- **Follow the PEP 8 Style Guide** for Python code.

## Writing and Editing
- **Automatically complete code snippets** and functions based on context.
- **Suggest improvements** to existing code, including refactoring and optimization.
- **Generate unit tests** for new and modified code.
- **Ensure all code adheres to the project's coding standards** and best practices.

## Reviewing
- **Automatically review code changes** for potential bugs, security vulnerabilities, and performance issues.
- **Provide detailed feedback** on code quality and suggest improvements.
- **Highlight areas of the code that need further attention** or documentation.

## Auto-Save and Auto-Commit
- **Auto-save changes** to the file every 5 seconds.
- **Auto-add changes** to the staging area when a file is saved.
- **Auto-commit changes** with a descriptive commit message when a file is saved.
- **Commit messages should follow the conventional commit format** (e.g., `feat: add new feature`, `fix: resolve bug`, `refactor: improve code structure`).

## Auto-Push
- **Auto-push changes** to the default branch or the branch you are currently working on when a commit is made.
- **Ensure all changes are pushed to the remote repository** to keep it up-to-date.

## Additional Instructions
- **Handle merge conflicts** by suggesting the best resolution based on context.
- **Automatically create pull requests** for new features or significant changes.
- **Ensure all changes are reviewed and approved** before merging to the main branch.
- **Use GitFlow or Trunk-Based Development** as per the project's workflow.
- **Automatically update dependencies** and run tests before committing.
- **Generate and update documentation** for new and modified code.

## Example Commit Message
```plaintext
feat: add new feature for user authentication

- Implement user authentication using JWT
- Add login and logout endpoints
- Update user model to include authentication fields
- Add unit tests for authentication endpoints
```
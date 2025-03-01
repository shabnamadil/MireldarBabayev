module.exports = {
    extends: ['@commitlint/config-conventional'], // Use standard rules
    rules: {
      'type-enum': [2, 'always', [
        'feat',   // New feature
        'fix',    // Bug fix
        'docs',   // Documentation changes
        'style',  // Formatting (no code changes)
        'refactor', // Code refactoring (no bug fix or feature)
        'test',   // Adding tests
        'chore'   // Other tasks (build, CI/CD, dependencies)
      ]],
      'type-case': [2, 'always', 'lower-case'],  // Ensure type is lowercase
      'subject-case': [2, 'never', ['sentence-case', 'start-case', 'pascal-case']], // Enforce lowercase subject
      'subject-full-stop': [2, 'never', '.'], // No full stop at end of message
      'header-max-length': [2, 'always', 72] // Limit commit message length
    }
  };
  
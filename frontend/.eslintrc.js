module.exports = {
    extends: 'next/core-web-vitals',
    rules: {
      'quotes': ['warn', 'single'],
      'semi': ['error', 'never'],
      'comma-dangle': ['warn', 'always-multiline'],
      'no-console': ['warn', { allow: ['warn', 'error'] }],
      'indent': ['warn', 2],
      'object-curly-spacing': ['warn', 'always'],
      'no-var': 'warn',
      'prefer-const': 'warn',
      'function-paren-newline': ['warn', 'consistent'],
      'no-unused-vars': ['warn', { args: 'none' }],
      'consistent-return': 'warn',
      'space-infix-ops': 'warn',
      'eqeqeq': ['warn', 'always'],
      'no-extra-semi': 'warn',
      'react/jsx-first-prop-new-line': ['warn', 'multiline'],
      'react/react-in-jsx-scope': 'off',
    },
  };
  
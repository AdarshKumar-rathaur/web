module.exports = {
  'extends': ['eslint:recommended'],
  'env': {
    'es6': true,
    'browser': true
  },
  'parserOptions': {
    'sourceType': 'module',
    'ecmaVersion': 8
  },
  'globals': {
    'StripeCheckout': true,
  },
  'rules': {
    'linebreak-style': ['error', 'unix'],
    'quotes': ['error', 'single'],
    'multiline-comment-style': ['error', 'starred-block'],
    'no-var': 'error',
    'semi': ['error', 'never']
  }
}

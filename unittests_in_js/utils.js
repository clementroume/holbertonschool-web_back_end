/**
 * A module containing utility functions.
 */
const Utils = {
  /**
   * Performs an operation (SUM, SUBTRACT, or DIVIDE) on two rounded numbers.
   * @param {string} type - The type of operation.
   * @param {number} a - The first number.
   * @param {number} b - The second number.
   * @returns {number|string} The result of the operation or 'Error' for division by zero.
   */
  calculateNumber: (type, a, b) => {
    switch (type) {
      case 'SUM':
        return Math.round(a) + Math.round(b);
      case 'SUBTRACT':
        return Math.round(a) - Math.round(b);
      case 'DIVIDE':
        return Math.round(b) != 0 ? Math.round(a) / Math.round(b) : 'Error';
      default:
        return 0;
    }
  },
};

module.exports = Utils;

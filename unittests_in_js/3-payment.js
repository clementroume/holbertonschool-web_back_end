const Utils = require('./utils.js');

/**
 * Calls Utils.calculateNumber to sum two numbers and logs the result.
 * @param {number} totalAmount - The total amount.
 * @param {number} totalShipping - The shipping cost.
 */
const sendPaymentRequestToApi = (totalAmount, totalShipping) => {
  const total = Utils.calculateNumber('SUM', totalAmount, totalShipping);
};

module.exports = sendPaymentRequestToApi;

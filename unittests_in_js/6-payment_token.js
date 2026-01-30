/**
 * Returns a resolved promise if success is true.
 * @param {boolean} success - Determines if the promise should resolve.
 * @returns {Promise|undefined} A promise that resolves with a success message, or undefined.
 */
const getPaymentTokenFromAPI = (success) => {
  if (success) {
    return new Promise((resolve) => {
      resolve({ data: 'Successful response from the API' });
    });
  }
};

module.exports = getPaymentTokenFromAPI;

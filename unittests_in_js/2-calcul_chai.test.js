// Import the 'expect' function from the 'chai' library
const { expect } = require('chai');
// Import the function to be tested
const calculateNumber = require('./2-calcul_chai.js');

// Describe the main test suite
describe('calculateNumber', function () {
  // Describe the test suite for the 'SUM' operation
  describe('type SUM', function () {
    it('should return 6 when inputs are 1.4 and 4.5', function () {
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });
    it('should handle negative numbers', function () {
      expect(calculateNumber('SUM', -1.4, -4.5)).to.equal(-5);
    });
  });

  // Describe the test suite for the 'SUBTRACT' operation
  describe('type SUBTRACT', function () {
    it('should return -4 when inputs are 1.4 and 4.5', function () {
      expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    });
    it('should handle subtraction resulting in a positive number', function () {
      expect(calculateNumber('SUBTRACT', 4.5, 1.4)).to.equal(4);
    });
  });

  // Describe the test suite for the 'DIVIDE' operation
  describe('type DIVIDE', function () {
    it('should return 0.2 when inputs are 1.4 and 4.5', function () {
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    });
    it('should return "Error" when dividing by 0', function () {
      expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });
    it('should return "Error" when dividing by a number that rounds to 0', function () {
      expect(calculateNumber('DIVIDE', 1.4, 0.4)).to.equal('Error');
    });
    it('should handle division with negative numbers', function () {
      expect(calculateNumber('DIVIDE', -4.5, 1.5)).to.equal(-2);
    });
  });
});

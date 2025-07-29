const kue = require('kue');
const { expect } = require('chai');
const createPushNotificationsJobs = require('./8-job.js');

// Create a test suite for the createPushNotificationsJobs function
describe('createPushNotificationsJobs', () => {
  let queue;

  // Before each test, create a new queue and enter test mode
  beforeEach(() => {
    queue = kue.createQueue();
    queue.testMode.enter();
  });

  // After each test, clear the queue and exit test mode to ensure isolation
  afterEach(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  // Test case for invalid input: jobs is not an array
  it('should display an error message if jobs is not an array', () => {
    // Expect the function to throw an error when called with various non-array types
    expect(() => createPushNotificationsJobs('not-an-array', queue)).to.throw(
      'Jobs is not an array'
    );
    expect(() => createPushNotificationsJobs({}, queue)).to.throw(
      'Jobs is not an array'
    );
    expect(() => createPushNotificationsJobs(42, queue)).to.throw(
      'Jobs is not an array'
    );
  });

  // Test case for valid input: creating jobs successfully
  it('should create two new jobs to the queue', () => {
    // A sample list of jobs to be created
    const list = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account',
      },
    ];

    // Call the function with the list of jobs
    createPushNotificationsJobs(list, queue);

    // --- Assertions ---

    // Check if the correct number of jobs are in the test mode queue
    expect(queue.testMode.jobs.length).to.equal(2);

    // Check the type of the first job
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');

    // Check that the data of the first job matches the input
    // using deep.equal for object comparison
    expect(queue.testMode.jobs[0].data).to.deep.equal(list[0]);

    // Check the data of the second job
    expect(queue.testMode.jobs[1].data).to.deep.equal(list[1]);
  });
});

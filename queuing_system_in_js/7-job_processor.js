import kue from 'kue';

// Array of blacklisted phone numbers
const blacklisted = ['4153518780', '4153518781'];

/**
 * Sends a notification, tracks progress, and handles blacklisted numbers.
 * @param {string} phoneNumber - The recipient's phone number.
 * @param {string} message - The message to send.
 * @param {object} job - The Kue job object.
 * @param {function} done - The callback to signal completion or failure.
 */
const sendNotification = (phoneNumber, message, job, done) => {
  // Track initial progress
  job.progress(0, 100);

  // Check if the phone number is blacklisted
  if (blacklisted.includes(phoneNumber)) {
    // Fail the job with an error
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // Track progress to 50%
  job.progress(50, 100);

  // Log the notification being sent
  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`
  );

  // Signal that the job is successfully completed
  done();
};

// Create a Kue queue
const queue = kue.createQueue();

// Process jobs in the 'push_notification_code_2' queue, two at a time
queue.process('push_notification_code_2', 2, (job, done) => {
  // Extract data from the job
  const { phoneNumber, message } = job.data;

  // Call the notification function with all required arguments
  sendNotification(phoneNumber, message, job, done);
});

import kue from 'kue';

// Create a Kue queue
const queue = kue.createQueue();

/**
 * Sends a notification to a phone number.
 * @param {string} phoneNumber - The recipient's phone number.
 * @param {string} message - The message to send.
 */
const sendNotification = (phoneNumber, message) => {
  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`
  );
};

// Process jobs in the 'push_notification_code' queue
queue.process('push_notification_code', (job, done) => {
  // Extract data from the job
  const { phoneNumber, message } = job.data;

  // Call the notification function
  sendNotification(phoneNumber, message);

  //Signal that the job is done
  done();
});

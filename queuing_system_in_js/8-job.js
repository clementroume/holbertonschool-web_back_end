/**
 * Creates push notification jobs from an array of job data and adds them to a queue.
 * @param {Array} jobs - An array of objects, where each object contains job data.
 * @param {object} queue - The Kue queue instance.
 * @throws {Error} If jobs is not an array.
 */
const createPushNotificationsJobs = (jobs, queue) => {
  // Validate if 'jobs' is an array
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  // Iterate over the jobs array
  jobs.forEach((jobData) => {
    // Create a new job in the 'push_notification_code_3' queue
    const job = queue.create('push_notification_code_3', jobData);

    // Set up event listeners for the job's lifecycle
    job
      .on('complete', () => {
        console.log(`Notification job ${job.id} completed`);
      })
      .on('failed', (errorMessage) => {
        console.log(`Notification job ${job.id} failed: ${errorMessage}`);
      })
      .on('progress', (progress) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
      });

    // Save the job to the queue
    job.save((err) => {
      if (!err) {
        console.log(`Notification job created: ${job.id}`);
      }
    });
  });
};

module.exports = createPushNotificationsJobs;

import kue from 'kue';

// Create a Kue queue
const queue = kue.createQueue();

// Object containing the job data
const jobData = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',
};

// Create a job in the 'push_notification_code' queue
const job = queue.create('push_notification_code', jobData).save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  }
});

// Event listener for when the job is completed
job.on('complete', () => {
  console.log('Notification job completed');
});

// Event listener for when the job fails
job.on('failed', () => {
  console.log('Notification job failed');
});

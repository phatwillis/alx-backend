export default function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  } else {
    for (const individualjob of jobs) {
      const job = queue.create('push_notification_code_3',
      individualjob)
      job.on('complete', () => {
        console.log(`Notification job ${job.id} completed`);
      }).on('failed', function(error){
        console.log(`Notification job ${job.id} failed: ${error}`);
      }).on('progress', (progress) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
      }).save((err) => {
        if (!err) {
          console.log(`Notification job created: ${job.id}`);
        }
      });
    }
  }
}

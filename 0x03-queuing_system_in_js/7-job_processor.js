import kue from 'kue';
const queue = kue.createQueue()


// create an array that will contain the blacklisted phone numbers.
// these 2 numbers will be blacklisted by our jobs processor.
const blacklisted = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done){
  job.progress(0, 100);
  for (const num of blacklisted) {
    if (phoneNumber === num) {
      return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    }
  }
  job.progress(50, 100)
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
}
// the '2' passed as an argument states that it should run 2 jobs concurrently
queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});

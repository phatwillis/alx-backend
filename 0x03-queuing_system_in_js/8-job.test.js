import { describe, it } from "mocha";
import { createQueue } from "kue";
import { assert, expect } from "chai";
import createPushNotificationsJobs from './8-job.js';
const queue = createQueue()

describe('unittests for creating jobs function', () => {
  before(function() {
    queue.testMode.enter();
  });
  afterEach(function() {
    queue.testMode.clear();
  });
  after(function() {
    queue.testMode.exit()
  });
  it('create two new jobs to the queue', () => {
    const list = [
      {
          phoneNumber: '4153518720',
          message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518710',
        message: 'This is the code 1234 to verify your account'
    }
    ];
    createPushNotificationsJobs(list, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
  });
  it('display a error message if jobs is not an array', () => {
    const list = 'string';
    assert(() => {createPushNotificationsJobs(list, queue)}, Error, 'Jobs is not an array');
  });
});

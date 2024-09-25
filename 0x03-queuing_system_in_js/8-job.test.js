import { createQueue } from 'kue';
import { expect } from 'chai';
import { spy } from 'sinon';
import createPushNotificationsJobs from './8-job';

describe('createPushNotifications unit tests', () => {
  const queue = createQueue();
  before(() => {
    queue.testMode.enter();
  });
  afterEach(() => {
    queue.testMode.clear();
  });
  after(() => {
    queue.testMode.exit();
  });

  it('adds jobs to the queue', () => {
    const consoleSpy = spy(console, 'log');
    const jobs = [{ phoneNumber: '1234567890', message: 'Your one time pin is 1234' },
      { phoneNumber: '12345', message: 'Your one time pin is 0987' },
    ];
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(consoleSpy.calledTwice).to.be.true;
  });
  it('adds jobs with the right data', () => {
    const jobs = [{ phoneNumber: '1234567890', message: 'Your one time pin is 1234' }];
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs[0].data).to.equal(jobs[0]);
  });
  it('adds throws an error when the wrong job data type is passed', () => {
    const jobs = { phoneNumber: '1234567890', message: 'Your one time pin is 1234' };
    expect(() => createPushNotificationsJobs(jobs, queue)).to.throw('Jobs is not an array');
  });
});

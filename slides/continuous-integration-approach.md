##  Continuous Integration Approach

---

### Create xUnit Report Output

To create *xUnit*-compatible output, which is understood by most Continuous Integration systems, install the `jasmine-reporters` package:

```bash
npm install --save-dev jasmine-reporters
```

`protractor.conf.js`:

```javascript
onPrepare: function() {
    require('jasmine-reporters');

    jasmine.getEnv().addReporter(
        new jasmine.JUnitXmlReporter('xunit-reports/',
        true, true));
}
```

Then point your Continuous Integration tool to the `xunit-reports` directory for reading the test results.

---

### Check-in/Nightly build?

Trade-off:

* Running end-to-end tests on every commit will prevent regression issues early on.
* False positives due to incomplete commits.
* Overhead of deploying the application every time.
* Execution time of the end-to-end test suite.

---

### Headless tests: PhantomJS vs. Xvfb

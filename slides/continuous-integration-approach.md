##  Continuous Integration Approach

---

### Create xUnit Report Output

To create *xUnit*-compatible output, which is understood by most Continuous Integration systems, install the `jasmine-reporters` package:

```bash
npm install --save-dev jasmine-reporters
```

<br>

`protractor.conf.js`:

```javascript
onPrepare: function() {
  require('jasmine-reporters');

  jasmine.getEnv().addReporter(
    new jasmine.JUnitXmlReporter('xunit-reports/', true, true));
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

### Headless tests: PhantomJS

* Headless WebKit browser, ideal for testing in headless environments.
* Works well with unit tests.
* Some minor differences to Chrome --> make sure your tests work in all browsers.
* Doesn't play well with Selenium WebDriver, e.g. keyboard events.

---

### Headless tests: Xvfb

* *X Virtual Frame Buffer*, available for all major Linux distributions.
* Simulates an *X* environment.
* Allows you to run standard browsers like Chrome or Firefox without an attached display.

---

### Xvfb Configuration

```bash
npm install --save-dev grunt-env
npm install --save-dev grunt-shell-spawn
```

`Gruntfile.js`:

```javascript
grunt.initConfig({
  // ...
  shell: {
    xvfb: {
      command: 'Xvfb :99 -ac -screen 0 1600x1200x24',
      options: { async: true }
    }
  },
  env: {
    xvfb: { DISPLAY: ':99' }
  }
  // ....
});

grunt.registerTask('protractor-xvfb', [
  'shell:xvfb',
  'env:xvfb',
  'protractor:run',
  'shell:xvfb:kill'
]);
```

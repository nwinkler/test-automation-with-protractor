##  Lessons Learned

---

### Unique ID Values

Use unique ID values on your controls to allow easy identification of the screen elements.

Try to auto-generate the ID values.

Make sure the ID values are consistent and don't change across test invocations.

---

### Test on multiple browsers

Tests can be run in parallel against multiple browsers:

```javascript
multiCapabilities: [{
  'browserName': 'firefox'
}, {
  'browserName': 'chrome'
}]
```

Browser configuration documentation: https://github.com/angular/protractor/blob/master/docs/browser-setup.md

---

### Understand OS-specific behavior

Keyboard Input: Some operating systems (e.g. Mac OS X) handle keyboard input in a non-standard way.

<br>

Animations: Take rendering speed of the OS/browser into account.

```javascript
var webDriver = protractor.getInstance().driver;

webDriver.sleep(500);
```

---

### Reusable test libraries

Since Protractor is written as a Node package, you can (and should!) create your own reusable test libraries.

```javascript
var fooApp = require('foo-app-test');

fooApp.session.login('john.doe', '12345');
```

<br>

Create reusable libraries for

* Framework functionality used in multiple applications
* Application features to be reused across test suites
* Common use cases

---

### Measure Code Coverage

Just like with regular unit tests, get a feeling for how much of your code is covered by your tests.

<br>

**Remember**: 100% code coverage does not mean that your code is error-free!

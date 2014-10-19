##  Writing Protractor Tests

---

##  Install

Use the [grunt-protractor-runner](https://github.com/teerapap/grunt-protractor-runner) plugin:

```
npm install grunt-protractor-runner --save-dev
```


Automatic download of the WebDriver binaries as part of `npm install` (in `package.json`, paths abbreviated):

```json
"scripts": {
  "install": "node n_m/grunt-protractor-runner/.../webdriver-manager update"
}
```

---

## Create a configuration file

```javascript
exports.config = {
    specs: ['test/e2e/**/*.spec'],
    baseUrl:'http://localhost:8080/',
};
```

Point it to your test files.

Define the URL to test.

---

---

##  Implement your test

Use standard Jasmine syntax

```javascript
describe('my app', function() {
  beforeEach(function() {

  });

  it('should do something', function() {
    expect(...);
  });
});
```

---

##  Run Your Tests

Deploy/Start your web application

Run the tests

```
grunt protractor
```

Watch in awe!

---

##  Angular Integration

Select DOM elements by ID, CSS, or by Angular model:

```javascript
var fooForm = element(by.id('foo'));

var barElements = foorForm.all(by.css('.bar'));

var input = fooForm.element(by.model('user.name'));
```

---

Each test step is executed asynchronously, waiting for the Angular digest cycle to finish. You can also use promises:

```javascript
fooForm.evaluate('user.name').then(function (name) {
  expect(name).toBe('Nils');
});
```

The `evaluate` function allows you to take a look at the element's Angular *scope*.

---

##  Testing non-Angular apps

Protractor is primarily used to test Angular apps, since it integrates really well with the Angular lifecycle and scope.

Since it is just a wrapper around Selenium WebDriver, it can also be used to test non-Angular apps. Simply apply this change:

```
TBD
```

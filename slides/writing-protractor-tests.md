##  Writing Protractor Tests

---

##  Install

Use the [grunt-protractor-runner](https://github.com/teerapap/grunt-protractor-runner) plugin:

```bash
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
  specs: ['test/**/*.spec'],
  baseUrl:'http://localhost:9000/',
};
```

Point it to your test files.

Define the URL to test.

---

## Create a Grunt configuration

```javascript
protractor: {
  options: {
    keepAlive: true,
    configFile: "protractor.conf.js"
  },
  run: {}
},
```

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

```bash
grunt protractor:run
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

Since it is just a wrapper around Selenium WebDriver, it can also be used to test non-Angular apps. Simply apply this change before running your test:

```javascript
browser.ignoreSynchronization = true;
```

Protractor will now no longer wait for Angular to load, and you can use it to test any web application.

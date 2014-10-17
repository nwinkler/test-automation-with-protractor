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

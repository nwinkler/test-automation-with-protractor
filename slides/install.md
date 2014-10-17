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

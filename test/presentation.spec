/* global [
    foo: true,
    describe: true,
    browser: true,
    it: true,
    element: true,
    by: true,
    expect: true,
    protractor: true
] */

describe('login', function() {
    'use strict';

    var webDriver = protractor.getInstance().driver;
    browser.ignoreSynchronization = true;
    browser.get('');

    it('should check correct title', function() {
        expect(browser.getTitle()).toBe('Test Automation with Protractor');
    });

    it('should find the H1 in the page', function() {
        var present = element(by.css('.present'));

        var heading = present.element(by.css('h1'));

        expect(heading.getText()).toBe('TEST AUTOMATION WITH PROTRACTOR');
    });

    it('should move to the next slide when pressing the n key', function() {
        webDriver.actions().sendKeys('n').perform();

        webDriver.sleep(500);

        var present = element(by.css('.present'));

        var heading = present.element(by.css('h2'));

        expect(heading.getText()).toBe('WOULD YOU HIRE THIS GUY?');
    });
});
